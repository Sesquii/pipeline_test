import os
import re
import sys
import json
import time
import requests
from pathlib import Path
from typing import Dict, List, Optional, Tuple

class TestGenerator:
    def __init__(self, test_model: str = "qwen2.5-coder-7b-instruct"):
        """Initialize the test generator with the specified model.
        
        Args:
            test_model: The model to use for generating tests (e.g., 'qwen2.5-coder-7b-instruct')
        """
        self.test_model = test_model
        self.lm_studio_url = "http://127.0.0.1:1234/v1/chat/completions"
        self.test_processing_dir = Path("Script_Factory/Preprocessing")
        self.test_output_dir = Path("pytest_scripts")
        self.state_file = "test_generator_state.json"
        self.state = self._load_state()

    def _load_state(self) -> Dict:
        """Load the processing state from the state file."""
        if os.path.exists(self.state_file):
            try:
                with open(self.state_file, 'r') as f:
                    return json.load(f)
            except Exception as e:
                print(f"Warning: Could not load state: {e}")
        return {"processed_files": [], "last_processed": None}

    def _save_state(self):
        """Save the current processing state to the state file."""
        try:
            with open(self.state_file, 'w') as f:
                json.dump(self.state, f, indent=2)
        except Exception as e:
            print(f"Warning: Could not save state: {e}")

    def check_lm_studio_connection(self) -> bool:
        """Check if LM Studio is running and accessible."""
        try:
            response = requests.get("http://127.0.0.1:1234/v1/models", timeout=5)
            return response.status_code == 200
        except:
            return False

    def generate_test_prompt(self, script_content: str) -> str:
        """Generate the prompt for test generation."""
        return f"""You are a professional Python developer specializing in writing comprehensive unit tests using pytest.

Please generate a test suite for the following Python script. Follow these requirements:
1. Keep the original script exactly as is
2. Add comprehensive test cases after the original code
3. Test all public functions and classes
4. Include both positive and negative test cases
5. Use pytest fixtures and parametrization where appropriate
6. Add type hints to test functions
7. Include proper docstrings and comments
8. Follow PEP 8 style guidelines
9. Add a clear separator between the original code and test code

Here's the script to test:

```python
{script_content}
```

Now, add your test cases after this line, following the requirements above."""

    def call_llm(self, prompt: str, max_retries: int = 3) -> Optional[str]:
        """Call the LM Studio API to generate test code."""
        headers = {"Content-Type": "application/json"}
        data = {
            "model": self.test_model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.3,
            "max_tokens": 4000,
            "stream": False
        }

        for attempt in range(max_retries):
            try:
                response = requests.post(
                    self.lm_studio_url,
                    headers=headers,
                    json=data,
                    timeout=300  # 5 minutes timeout
                )
                response.raise_for_status()
                return response.json()["choices"][0]["message"]["content"]
            except Exception as e:
                if attempt == max_retries - 1:
                    print(f"Error calling LLM after {max_retries} attempts: {e}")
                    return None
                print(f"Attempt {attempt + 1} failed, retrying...")
                time.sleep(2 ** attempt)  # Exponential backoff

    def process_script(self, script_path: Path, output_path: Path):
        """Process a single script and generate tests."""
        try:
            # Skip if already processed
            if str(script_path) in self.state.get("processed_files", []):
                print(f"Skipping already processed file: {script_path}")
                return

            # Read the original script
            with open(script_path, 'r', encoding='utf-8') as f:
                script_content = f.read()
            
            # Skip if already contains test code
            if "def test_" in script_content:
                print(f"Skipping {script_path} - already contains tests")
                return
            
            print(f"Generating tests for {script_path.name}...")
            
            # Generate test code
            prompt = self.generate_test_prompt(script_content)
            test_code = self.call_llm(prompt)
            
            if not test_code:
                print(f"Failed to generate tests for {script_path.name}")
                return
            
            # Create output directory if it doesn't exist
            output_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Write original code + tests to output file
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(script_content)
                f.write("\n\n# ===== GENERATED TESTS =====\n")
                f.write(test_code)
            
            # Update state
            self.state.setdefault("processed_files", []).append(str(script_path))
            self.state["last_processed"] = str(script_path)
            self._save_state()
            
            print(f"Generated tests: {output_path}")
            
        except Exception as e:
            print(f"Error processing {script_path}: {e}")

    def get_script_info(self, script_path: Path) -> Tuple[str, str, str]:
        """Extract batch, prompt, and model info from script path.
        
        Example path: Script_Factory/Preprocessing/by_model/devstral-small-2507/BATCH2_PROMPT1.py
        """
        model_name = script_path.parent.name  # devstral-small-2507
        script_stem = script_path.stem  # BATCH2_PROMPT1
        
        # Extract batch and prompt number
        match = re.match(r'(BATCH\d+_PROMPT\d+)', script_stem)
        if not match:
            raise ValueError(f"Could not extract batch and prompt from {script_stem}")
        
        return match.group(1), model_name, script_stem

    def get_batch_number(self, batch_str: str) -> int:
        """Extract batch number from batch string (e.g., 'BATCH1' -> 1)."""
        match = re.search(r'BATCH(\d+)', batch_str)
        return int(match.group(1)) if match else float('inf')

    def process_all_scripts(self):
        """Process all scripts in the preprocessing directory in batch order."""
        if not self.check_lm_studio_connection():
            print("Error: Cannot connect to LM Studio. Please make sure it's running on http://127.0.0.1:1234")
            return

        # Collect all script paths with their batch numbers
        script_paths = []
        for root, _, files in os.walk(self.test_processing_dir):
            for file in files:
                if file.endswith('.py') and not file.startswith('__'):
                    script_path = Path(root) / file
                    try:
                        batch_prompt, source_model, _ = self.get_script_info(script_path)
                        batch_num = self.get_batch_number(batch_prompt)
                        script_paths.append((batch_num, batch_prompt, source_model, script_path))
                    except Exception as e:
                        print(f"Skipping {script_path}: {e}")
        
        # Sort by batch number
        script_paths.sort(key=lambda x: x[0])
        
        # Process scripts in order
        for batch_num, batch_prompt, source_model, script_path in script_paths:
            try:
                # Create output path
                output_dir = self.test_output_dir / self.test_model / source_model
                output_path = output_dir / f"Test_{batch_prompt}.py"
                
                # Skip if output already exists
                if output_path.exists():
                    print(f"Skipping {script_path.name} - test file already exists at {output_path}")
                    continue
                    
                # Process the script
                print(f"\nProcessing batch {batch_num}: {script_path.name}")
                self.process_script(script_path, output_path)
                
            except Exception as e:
                print(f"Error processing {script_path}: {e}")
                continue

def main():
    # Initialize the test generator with the test model
    test_model = "qwen2.5-coder-7b-instruct"  # Model used for generating tests
    generator = TestGenerator(test_model=test_model)
    
    # Process all scripts
    print(f"Starting test generation using {test_model}...")
    generator.process_all_scripts()
    print("Test generation complete!")

if __name__ == "__main__":
    main()
