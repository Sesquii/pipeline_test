import os
import shutil
import re
import ast
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Set
import json
from datetime import datetime

class ScriptPreprocessor:
    def __init__(self, source_dir: str, dest_dir: str):
        """
        Initialize the ScriptPreprocessor with source and destination directories.
        
        Args:
            source_dir: Path to the all_runs directory containing the original scripts
            dest_dir: Base directory where preprocessed files will be stored
        """
        self.source_dir = Path(source_dir)
        self.dest_dir = Path(dest_dir)
        
        # Create runs directory and find the next run number
        self.runs_dir = self.dest_dir / 'Runs'
        self.runs_dir.mkdir(parents=True, exist_ok=True)
        
        # Get all existing runs
        existing_runs = [d for d in self.runs_dir.iterdir() if d.is_dir() and d.name.startswith('run_')]
        run_numbers = [int(d.name[4:]) for d in existing_runs if d.name[4:].isdigit()]
        next_run = max(run_numbers) + 1 if run_numbers else 1
        
        self.current_run_dir = self.runs_dir / f'run_{next_run:03d}'
        self.current_run_dir.mkdir(exist_ok=True)
        
        self.by_model_dir = self.current_run_dir / 'by_model'
        self.by_model_dir.mkdir(exist_ok=True)
        
        # Track files from previous runs to avoid duplicates
        self.processed_files = self._get_processed_files_from_previous_runs()
        
        self.metadata = {
            'run_number': next_run,
            'run_directory': str(self.current_run_dir),
            'preprocess_timestamp': datetime.utcnow().isoformat(),
            'total_scripts_processed': 0,
            'total_duplicates_skipped': 0,
            'models_processed': {},
            'errors': []
        }
        
    def _get_processed_files_from_previous_runs(self) -> set:
        """Get a set of all files that have been processed in previous runs."""
        processed = set()
        
        # Get all run directories except the current one
        run_dirs = [d for d in self.runs_dir.iterdir() 
                   if d.is_dir() and d.name.startswith('run_') and d != self.current_run_dir]
        
        for run_dir in run_dirs:
            by_model_dir = run_dir / 'by_model'
            if not by_model_dir.exists():
                continue
                
            # Find all Python files in by_model subdirectories
            for py_file in by_model_dir.rglob('*.py'):
                # Get relative path from by_model directory
                rel_path = py_file.relative_to(by_model_dir)
                processed.add(str(rel_path))
                
        return processed
    
    def extract_metadata(self, filename: str) -> Tuple[str, str, str, str]:
        """
        Extract batch number, prompt number, and model from filename.
        Expected format: BATCH{number}_PROMPT{number}_{model}.txt
        
        Returns:
            Tuple of (batch_num, prompt_num, model, original_filename)
        """
        try:
            # Remove extension and get the base name
            base_name = os.path.splitext(filename)[0]
            
            # Extract batch and prompt numbers using regex to be more flexible
            batch_match = re.search(r'BATCH(\d+)', filename, re.IGNORECASE)
            prompt_match = re.search(r'PROMPT(\d+)', filename, re.IGNORECASE)
            
            if not batch_match or not prompt_match:
                raise ValueError(f"Could not extract batch or prompt number from {filename}")
                
            batch_num = batch_match.group(1)
            prompt_num = prompt_match.group(1)
            
            # Get the model name by removing BATCH{num}_PROMPT{num}_ from the start
            model = re.sub(r'^BATCH\d+_PROMPT\d+_?', '', base_name, flags=re.IGNORECASE)
            if not model:  # If no model specified in filename
                model = 'unknown'
                
            # Create the standardized output filename
            output_filename = f"BATCH{batch_num}_PROMPT{prompt_num}.py"
            
            return batch_num, prompt_num, model, output_filename
        except Exception as e:
            self.metadata['errors'].append(f"Error processing {filename}: {str(e)}")
            return None, None, None
    
    def process_file(self, filepath: Path):
        """Process a single script file."""
        try:
            # Skip non-Python files and __init__.py
            if filepath.suffix != '.py' or filepath.name == '__init__.py':
                return
                
            # Extract metadata from filename
            batch_num, prompt_num, model, output_filename = self.extract_metadata(filepath.name)
            
            # Check if this file has already been processed in a previous run
            model_dir = model.replace('.', '_')  # Normalize model name for directory
            rel_path = f"{model_dir}/{output_filename}"
            
            if rel_path in self.processed_files:
                self.metadata['total_duplicates_skipped'] += 1
                if self.metadata['total_duplicates_skipped'] <= 5:  # Don't flood the log
                    print(f"Skipping duplicate: {rel_path}")
                elif self.metadata['total_duplicates_skipped'] == 6:
                    print("Additional duplicates will be skipped silently...")
                return
            
            # Clean the model name for directory use (no periods, special chars)
            model_safe = re.sub(r'[^\w-]', '_', model)
            
            # Read and clean the file content
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Fix any imports in the file that might have version numbers with periods
            content = self.fix_imports(content)
            
            # Save to by_model structure
            model_dir = self.by_model_dir / model_safe
            model_dir.mkdir(exist_ok=True)
            with open(model_dir / output_filename, 'w', encoding='utf-8') as f:
                f.write(content)
            
            # Update metadata
            self.metadata['total_scripts_processed'] += 1
            if model_safe not in self.metadata['models_processed']:
                self.metadata['models_processed'][model_safe] = 0
            self.metadata['models_processed'][model_safe] += 1
            
        except Exception as e:
            self.metadata['errors'].append(f"Error processing {filepath}: {str(e)}")
    
    def run(self):
        """
        Process all script files in the source directory, skipping duplicates from previous runs.
        
        Returns:
            dict: Metadata about the processing results
        """
        print(f"Starting preprocessing run {self.metadata['run_number']}")
        print(f"Source directory: {self.source_dir}")
        print(f"Destination directory: {self.dest_dir}")
        
        # Check for prompts file first
        prompts_file = self.source_dir.parent / 'prompts' / 'promptsforfactory.md'
        if prompts_file.exists():
            print("\nFound prompts file, processing BATCH1 prompts...")
            self.process_prompts_file(prompts_file)
        
        # Get all .txt and .py files in the source directory and subdirectories
        script_files = list(self.source_dir.rglob('*.txt')) + list(self.source_dir.rglob('*.py'))
        
        # Filter out any temporary files we might have created
        script_files = [f for f in script_files if not f.name.startswith('temp_')]
        
        print(f"\nFound {len(script_files)} script files to process")
        
        # Process files
        new_files = 0
        skipped_duplicates = 0
        
        for i, filepath in enumerate(script_files, 1):
            if i % 10 == 0 or i == 1 or i == len(script_files):
                status = f"Processing file {i} of {len(script_files)}: {filepath.name}"
                if skipped_duplicates > 0:
                    status += f" (skipped {skipped_duplicates} duplicates)"
                print(status)
            
            # Process the file and track if it was a duplicate
            before_count = self.metadata['total_duplicates_skipped']
            self.process_file(filepath)
            
            # Update counters based on whether this was a duplicate
            if self.metadata['total_duplicates_skipped'] > before_count:
                skipped_duplicates += 1
            else:
                new_files += 1
        
        # Save metadata
        metadata_path = self.dest_dir / 'preprocess_metadata.json'
        with open(metadata_path, 'w', encoding='utf-8') as f:
            json.dump(self.metadata, f, indent=2)
            
        print(f"\nPreprocessing complete!")
        print(f"New scripts processed: {new_files}")
        print(f"Duplicate scripts skipped: {skipped_duplicates}")
        
        if self.metadata['errors']:
            print(f"\nErrors encountered: {len(self.metadata['errors'])}")
            for error in self.metadata['errors'][:5]:
                print(f"- {error}")
            if len(self.metadata['errors']) > 5:
                print(f"... and {len(self.metadata['errors']) - 5} more errors")
        
        return self.metadata

    def fix_imports(self, content: str) -> str:
        """
        Fix import statements in the content to handle model names with version numbers.
        Replaces periods in model names with underscores in import statements.
        """
        try:
            # This is a simple fix that handles most common import patterns
            # For more complex cases, we might need to use ast to parse and modify the imports
            
            # Handle 'from model.x.y import ...' patterns
            def replace_import(match):
                prefix = match.group(1)  # 'from ' or 'import '
                path = match.group(2)    # The import path
                # Replace periods with underscores in model names (but not in the rest of the path)
                parts = path.split('.')
                if len(parts) > 1 and any(any(c.isdigit() for c in part) for part in parts):
                    # This is likely a model name with version number
                    model_part = parts[0]
                    if any(c.isdigit() for c in model_part):
                        model_part = model_part.replace('.', '_')
                        return f"{prefix}{model_part}.{'.'.join(parts[1:])}"
                return match.group(0)
            
            # Apply the replacement to import statements
            content = re.sub(r'(from\s+|import\s+)([\w.]+)', replace_import, content)
            
            return content
            
        except Exception as e:
            self.metadata['errors'].append(f"Error fixing imports: {str(e)}")
            return content

def main():
    import argparse
    
    # Set default paths relative to the script location
    script_dir = Path(__file__).parent
    default_source = script_dir / "Script_Factory" / "Script_Factory_Runs" / "all_runs"
    default_dest = script_dir / "Script_Factory" / "Preprocessing"
    
    parser = argparse.ArgumentParser(description='Preprocess script files from Script Factory output')
    parser.add_argument('--source', 
                      type=str, 
                      default=str(default_source),
                      help=f'Path to the all_runs directory (default: {default_source})')
    parser.add_argument('--dest', 
                      type=str, 
                      default=str(default_dest),
                      help=f'Destination directory for preprocessed files (default: {default_dest})')
    
    args = parser.parse_args()
    
    # Ensure destination directory exists
    dest_path = Path(args.dest)
    dest_path.mkdir(parents=True, exist_ok=True)
    
    print(f"Source directory: {args.source}")
    print(f"Destination directory: {args.dest}")
    
    preprocessor = ScriptPreprocessor(args.source, args.dest)
    results = preprocessor.run()
    
    print(f"Preprocessing complete!")
    print(f"Processed {results['total_scripts_processed']} scripts")
    print(f"Models processed: {', '.join(results['models_processed'].keys())}")
    if results['errors']:
        print(f"\nEncountered {len(results['errors'])} errors:")
        for error in results['errors'][:5]:  # Show first 5 errors
            print(f"- {error}")
        if len(results['errors']) > 5:
            print(f"... and {len(results['errors']) - 5} more errors")

if __name__ == '__main__':
    main()
