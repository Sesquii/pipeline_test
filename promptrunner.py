import lmstudio as lms
import os
import argparse
import requests
import json
import time
from openai import OpenAI
# LM Studio API configuration
LM_STUDIO_BASE_URL = "http://127.0.0.1:1234"

def check_lm_studio_connection():
    """Check if LM Studio server is running"""
    try:
        response = requests.get(f"{LM_STUDIO_BASE_URL}/v1/models")
        return response.status_code == 200
    except requests.exceptions.ConnectionError:
        return False

def load_model(model_id):
    """Load a model in LM Studio"""
    try:
        response = requests.post(
            f"{LM_STUDIO_BASE_URL}/v1/models/load",
            json={"model": model_id}
        )
        if response.status_code == 200:
            print(f"Successfully loaded model: {model_id}")
            return True
        else:
            print(f"Failed to load model {model_id}: {response.text}")
            return False
    except Exception as e:
        print(f"Error loading model {model_id}: {e}")
        return False

def unload_current_model():
    """Unload the currently loaded model"""
    try:
        response = requests.post(f"{LM_STUDIO_BASE_URL}/v1/models/unload")
        if response.status_code == 200:
            print("Model unloaded successfully")
            return True
        else:
            print(f"Failed to unload model: {response.text}")
            return False
    except Exception as e:
        print(f"Error unloading model: {e}")
        return False

def send_prompt(prompt, model_id, max_retries=1):
    """Send a prompt to the loaded model"""
    # You can set the timeout here or pass it as an argument to the function
    request_timeout = 600 # Timeout in seconds
    
    for attempt in range(max_retries):
        try:
            response = requests.post(
                f"{LM_STUDIO_BASE_URL}/v1/chat/completions",
                json={
                    "model": model_id,
                    "messages": [{"role": "user", "content": prompt}],
                    "temperature": 0.7,
                    "max_tokens": 100000
                },
                timeout=request_timeout # This is where the timeout is added
            )
            
            if response.status_code == 200:
                data = response.json()
                return data['choices'][0]['message']['content']
            else:
                print(f"API error (attempt {attempt + 1}): {response.status_code} - {response.text}")
                if attempt < max_retries - 1:
                    time.sleep(2)
                    
        except Exception as e:
            print(f"Request error (attempt {attempt + 1}): {e}")
            if attempt < max_retries - 1:
                time.sleep(2)
    
    return None

# Set up the OpenAI client to point to the new URL
client = OpenAI(base_url="http://localhost:1234", api_key="lm-studio", timeout=300)
# --- Function to read prompts from a file ---
def read_prompts_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    # Split by ===== and filter out empty strings (handles leading =====)
    prompts = [p.strip() for p in content.split('=====') if p.strip()]
    return prompts

# --- Function to extract filename from prompt ---
def extract_filename_from_prompt(prompt):
    """Extract the expected filename from the prompt text"""
    import re
    # Look for pattern like "BATCH2_PROMPT1_{{model_name}}.py"
    match = re.search(r'`([^`]*{{model_name}}[^`]*)`', prompt)
    if match:
        return match.group(1)
    return None

# --- Function to send prompts and save responses ---
def process_prompts(prompts, model_id, batch_name):
    # Create the output directory based on the model ID
    model_name_for_folder = model_id.split('/')[-1]
    output_dir = os.path.join("Script_Factory/Script_Factory_Runs/all_runs", f"{batch_name}/{model_name_for_folder}")
    os.makedirs(output_dir, exist_ok=True)
    
    # Load the model
    if not load_model(model_id):
        print(f"Failed to load model {model_id}, skipping...")
        return
    
    # Wait a moment for model to fully load
    time.sleep(3)
    
    successful_prompts = 0
    
    for i, prompt in enumerate(prompts):
        print(f"Processing prompt {i+1}/{len(prompts)} for model {model_id}...")
        
        response_content = send_prompt(prompt, model_id)
        
        if response_content:
            # Clean up the response content
            lines = response_content.splitlines()
        
            # Remove ```python from first line if present
            if lines and lines[0].strip() == "```python":
                lines = lines[1:]
        
            # Remove ``` from last line if present
            if lines and lines[-1].strip() == "```":
                lines = lines[:-1]
        
            # Join the lines back together
            cleaned_content = '\n'.join(lines).strip()
        
            # Try to extract filename from prompt, otherwise use default naming
            expected_filename = extract_filename_from_prompt(prompt)
            if expected_filename:
                # Replace {{model_name}} with actual model name
                filename = expected_filename.replace('{{model_name}}', model_name_for_folder)
            else:
                # Fallback to default naming
                filename = f"{batch_name}_PROMPT{i+1}_{model_name_for_folder}.py"
        
            output_filename = os.path.join(output_dir, filename)
        
            try:
                with open(output_filename, 'w', encoding='utf-8') as f:
                    f.write(cleaned_content)
        
                print(f"Response saved to {output_filename}")
                successful_prompts += 1
            except Exception as e:
                print(f"Error saving file {output_filename}: {e}")
        else:
            print(f"Failed to get response for prompt {i+1}")
    
    print(f"Completed {successful_prompts}/{len(prompts)} prompts for model {model_id}")
    
    # Unload the model after processing all prompts
    unload_current_model()

# --- Main execution with command-line arguments ---
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process prompts using different LLMs in LM Studio.")
    parser.add_argument('--models', type=str, required=True, help="A pipe-separated list of model IDs to run.")
    parser.add_argument('--batches', type=str, required=True, help="A comma-separated list of batch numbers to run (e.g., 1,2,5 or 1-10).")
    args = parser.parse_args()
    
    # Check LM Studio connection
    if not check_lm_studio_connection():
        print("Error: Cannot connect to LM Studio. Make sure LM Studio is running on http://127.0.0.1:1234")
        exit(1)
    
    # Parse batch numbers
    def parse_batch_numbers(batch_str):
        batches = []
        for part in batch_str.split(','):
            part = part.strip()
            if '-' in part:
                start, end = map(int, part.split('-'))
                batches.extend(range(start, end + 1))
            else:
                batches.append(int(part))
        return sorted(set(batches))
    
    try:
        batch_numbers = parse_batch_numbers(args.batches)
    except ValueError as e:
        print(f"Error parsing batch numbers: {e}")
        exit(1)
    
    print(f"Will process batches: {batch_numbers}")
    
    # Parse the pipe-separated model IDs from the command line
    models_to_run = [model.strip() for model in args.models.split('|') if model.strip()]
    
    if not models_to_run:
        print("No valid models specified")
        exit(1)
        
    print(f"Will process {len(models_to_run)} models: {models_to_run}")
    
    # Process each batch for each model
    for batch_num in batch_numbers:
        batch_file = f"Script_Factory/prompts/BATCH{batch_num}_PROMPTS.md"
        
        if not os.path.exists(batch_file):
            print(f"Warning: Batch file not found: {batch_file}, skipping...")
            continue
            
        print(f"\n=== Processing BATCH{batch_num} ===")
        
        batch_prompts = read_prompts_from_file(batch_file)
        
        if not batch_prompts:
            print(f"No prompts found in BATCH{batch_num}, skipping...")
            continue
        
        print(f"Found {len(batch_prompts)} prompts in BATCH{batch_num}")
        
        for i, model in enumerate(models_to_run):
            print(f"\n--- Processing model {i+1}/{len(models_to_run)}: {model} for BATCH{batch_num} ---")
            process_prompts(batch_prompts, model, f"BATCH{batch_num}")
            
            # Add a pause between models to ensure clean transitions
            if i < len(models_to_run) - 1:
                print("Waiting before next model...")
                time.sleep(2)
    
    print("\n=== All batches and models processed successfully! ===")