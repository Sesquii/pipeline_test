import os
import re
import json
import requests
from pathlib import Path
from typing import List, Dict, Optional
import time
from preprocess_scripts import ScriptPreprocessor

class ScriptCleaner:
    def __init__(self, source_dir: Path, dest_dir: Path):
        """
        Initialize the ScriptCleaner with source and destination directories.
        
        Args:
            source_dir: Path to the directory containing the preprocessed scripts (should be a run_* directory)
            dest_dir: Base directory where cleaned files will be stored (root project directory)
        """
        self.source_dir = Path(source_dir)
        # Create a Cleaned_Scripts directory with the same run_* structure
        run_name = self.source_dir.name
        self.dest_dir = Path(dest_dir) / 'Cleaned_Scripts' / run_name
        self.dest_dir.mkdir(parents=True, exist_ok=True)
        self.llm_url = "http://127.0.0.1:1234/v1/chat/completions"
        self.llm_model = "gpt-oss-20b"
        
        # Load or create metadata
        self.metadata = self._load_metadata()
        
    def _load_metadata(self) -> Dict:
        """Load or initialize metadata for the cleaning process."""
        metadata_file = self.dest_dir / 'cleanup_metadata.json'
        if metadata_file.exists():
            with open(metadata_file, 'r') as f:
                return json.load(f)
        return {
            'last_processed_run': None,
            'processed_files': [],
            'errors': []
        }
        
    def _save_metadata(self):
        """Save the current metadata to disk."""
        metadata_file = self.dest_dir / 'cleanup_metadata.json'
        with open(metadata_file, 'w') as f:
            json.dump(self.metadata, f, indent=2)
            
    def clean_script(self, script_content: str) -> Optional[str]:
        """
        Send script to LLM for cleaning.
        
        Args:
            script_content: The content of the script to clean
            
        Returns:
            Cleaned script content or None if cleaning failed
        """
        prompt = f"""Please process the following Python script. 
        Remove all non-code elements (markdown formatting, explanations, etc.) 
        and return ONLY the valid Python code. 
        Do not include any other text or formatting.
        
        Input script:
        ```python
        {script_content}
        ```
        
        Return ONLY the cleaned Python code with no additional text or formatting."""
        
        headers = {"Content-Type": "application/json"}
        data = {
            "model": self.llm_model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.1,
            "max_tokens": 8000,
            "stream": False
        }
        
        try:
            response = requests.post(
                self.llm_url,
                headers=headers,
                json=data,
                timeout=300
            )
            response.raise_for_status()
            return response.json()["choices"][0]["message"]["content"]
        except Exception as e:
            print(f"Error cleaning script: {e}")
            return None
            
    def process_directory(self, input_dir: Path):
        """Process all scripts in the input directory."""
        for script_file in input_dir.rglob('*.py'):
            # Skip already processed files
            if str(script_file.relative_to(self.source_dir)) in self.metadata['processed_files']:
                continue
                
            try:
                # Read the script content
                with open(script_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                # Clean the script
                cleaned_content = self.clean_script(content)
                if not cleaned_content:
                    raise ValueError("Failed to clean script")
                    
                # Save the cleaned script
                rel_path = script_file.relative_to(self.source_dir)
                output_path = self.dest_dir / rel_path
                output_path.parent.mkdir(parents=True, exist_ok=True)
                
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(cleaned_content)
                    
                # Update metadata
                self.metadata['processed_files'].append(str(rel_path))
                print(f"Processed: {rel_path}")
                
            except Exception as e:
                error_msg = f"Error processing {script_file}: {str(e)}"
                print(error_msg)
                self.metadata['errors'].append(error_msg)
                
        # Save metadata after processing
        self._save_metadata()

def process_test_scripts(cleaner: ScriptCleaner, root_dir: Path):
    """Process test scripts from Pytest_Scripts_Raw directory."""
    raw_scripts_dir = root_dir / "Pytest_Scripts_Raw"
    if not raw_scripts_dir.exists():
        print(f"No Pytest_Scripts_Raw directory found at {raw_scripts_dir}")
        return
    
    # Process each model directory
    for model_dir in raw_scripts_dir.iterdir():
        if not model_dir.is_dir():
            continue
            
        print(f"\nProcessing model: {model_dir.name}")
        
        # Process each test file in the model directory and its subdirectories
        for test_file in model_dir.rglob('Test_*.py'):
            try:
                # Read the test file content
                with open(test_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Clean the script
                cleaned_content = cleaner.clean_script(content)
                if not cleaned_content:
                    raise ValueError("Failed to clean script")
                
                # Create relative path for output
                rel_path = test_file.relative_to(raw_scripts_dir)
                output_path = cleaner.dest_dir / rel_path
                output_path.parent.mkdir(parents=True, exist_ok=True)
                
                # Save the cleaned script
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(cleaned_content)
                
                # Update metadata
                cleaner.metadata['processed_files'].append(str(rel_path))
                print(f"Processed: {rel_path}")
                
            except Exception as e:
                error_msg = f"Error processing {test_file}: {str(e)}"
                print(error_msg)
                cleaner.metadata['errors'].append(error_msg)
    
    # Save metadata after processing
    cleaner._save_metadata()

def main():
    # Define paths relative to the script's location
    root_dir = Path(__file__).parent
    
    # Create Cleaned_Scripts directory in root
    cleaned_scripts_dir = root_dir / 'Cleaned_Scripts'
    cleaned_scripts_dir.mkdir(exist_ok=True)
    
    # Initialize the cleaner
    cleaner = ScriptCleaner(root_dir, root_dir)  # Using root_dir for both source and dest as we'll handle paths manually
    
    # Process test scripts from Pytest_Scripts_Raw
    print("Starting to process test scripts from Pytest_Scripts_Raw...")
    process_test_scripts(cleaner, root_dir)
    
    print(f"\nCleaning complete. Processed files saved to: {cleaned_scripts_dir}")
    if cleaner.metadata['errors']:
        print("\nEncountered some errors:")
        for error in cleaner.metadata['errors']:
            print(f"- {error}")

if __name__ == "__main__":
    main()
