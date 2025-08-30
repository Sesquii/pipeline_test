# organize_tests.py
import os
import re
import shutil
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Set
import json
from datetime import datetime, timezone

class TestOrganizer:
    def __init__(self, test_output_dir: str, source_base_dir: str, processed_dir: str):
        """
        Initialize the TestOrganizer.
        
        Args:
            test_output_dir: Directory containing the generated test files
            source_base_dir: Base directory containing the source script files (will search recursively)
            processed_dir: Directory where organized test files will be saved
        """
        self.test_output_dir = Path(test_output_dir)
        self.source_base_dir = Path(source_base_dir)
        self.processed_dir = Path(processed_dir)
        self.metadata = {
            'start_time': datetime.now(timezone.utc).isoformat(),
            'files_processed': 0,
            'files_created': 0,
            'errors': [],
            'source_scripts_found': 0
        }
        
        # Create processed directory if it doesn't exist
        self.processed_dir.mkdir(parents=True, exist_ok=True)
        
        # Cache for source scripts
        self._source_scripts_cache = None
    
    def normalize_model_name(self, model_name: str, for_filename: bool = True) -> str:
        """
        Normalize model name for use in filenames or imports.
        
        Args:
            model_name: Original model name (e.g., 'qwen3-1.7b')
            for_filename: If True, converts dots to underscores for filenames
            
        Returns:
            Normalized model name
        """
        if for_filename:
            return model_name.replace('.', '_')
        return model_name
    
    def find_all_source_scripts(self) -> Dict[str, Path]:
        """Find all source scripts and cache them for faster lookup."""
        if self._source_scripts_cache is not None:
            return self._source_scripts_cache
            
        source_scripts = {}
        for py_file in self.source_base_dir.rglob('BATCH*/*/*.py'):
            # Extract batch, prompt, and model from path
            parts = py_file.parts
            if len(parts) < 3:
                continue
                
            model_name = parts[-2]  # e.g., 'qwen3-1.7b'
            file_stem = py_file.stem  # e.g., 'BATCH1_PROMPT1_qwen3-1.7b'
            
            # Try to extract BATCH and PROMPT numbers
            match = re.match(r'(BATCH\d+_PROMPT\d+)', file_stem)
            if match:
                base_name = match.group(1)  # e.g., 'BATCH1_PROMPT1'
                key = f"{base_name}_{model_name}"
                source_scripts[key] = py_file
        
        self._source_scripts_cache = source_scripts
        self.metadata['source_scripts_found'] = len(source_scripts)
        return source_scripts
    
    def get_script_info(self, test_file: Path) -> Optional[Tuple[str, str, str]]:
        """
        Extract batch, prompt, and model from test file path.
        Returns (batch_prompt, model_name, test_file_name) or None if no match.
        """
        # Get model name from parent directory (e.g., 'qwen3-1_7b')
        # Convert back to standard format for lookup
        dir_name = test_file.parent.name
        model_name = dir_name.replace('_', '.')  # Convert back to 'qwen3-1.7b' format
        
        # Try to extract BATCH and PROMPT from filename
        match = re.match(r'test_(BATCH\d+_PROMPT\d+)', test_file.stem)
        if not match:
            return None
            
        base_name = match.group(1)  # e.g., 'BATCH1_PROMPT1'
        return base_name, model_name, test_file.name
    
    def process_test_file(self, test_file: Path, counter: int) -> Optional[Path]:
        """Process a single test file and return the path to the processed file."""
        script_info = self.get_script_info(test_file)
        if not script_info:
            self.metadata['errors'].append(f"Could not parse test file name: {test_file.name}")
            return None
            
        base_name, model_name, original_name = script_info
        source_scripts = self.find_all_source_scripts()
        source_key = f"{base_name}_{model_name}"
        
        if source_key not in source_scripts:
            self.metadata['errors'].append(
                f"Could not find source script for: {original_name} (model: {model_name})"
            )
            return None
            
        source_script = source_scripts[source_key]
        
        # Create new test file name with normalized model name
        normalized_model = self.normalize_model_name(model_name, for_filename=True)
        new_name = f"test_{base_name}_{normalized_model}_{counter:03d}.py"
        dest_path = self.processed_dir / new_name
        
        try:
            # Read test file content
            with open(test_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Fix imports to point to the source script (using original model name with dots)
            module_name = source_script.stem
            content = self.fix_imports(content, module_name)
            
            # Write to new location
            with open(dest_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            self.metadata['files_created'] += 1
            return dest_path
            
        except Exception as e:
            self.metadata['errors'].append(f"Error processing {test_file}: {str(e)}")
            return None
    
    def fix_imports(self, content: str, module_name: str) -> str:
        """Fix imports in the test file to point to the correct source file."""
        # Replace any import statements that reference the original script
        content = re.sub(
            r'from\s+[\w\.]+\s+import',
            f'from {module_name} import',
            content
        )
        return content
    
    def run(self):
        """Process all test files in the test output directory."""
        counter = 1
        processed_files = set()
        
        # Process all Python files in test output directory
        for test_file in self.test_output_dir.rglob('*.py'):
            if test_file.is_file() and test_file.parent.name != self.processed_dir.name:
                self.metadata['files_processed'] += 1
                processed_path = self.process_test_file(test_file, counter)
                if processed_path:
                    processed_files.add(processed_path)
                    counter += 1
        
        # Save metadata
        self.metadata['end_time'] = datetime.now(timezone.utc).isoformat()
        self.metadata['processed_files'] = [str(p) for p in processed_files]
        
        with open(self.processed_dir / 'test_organization_metadata.json', 'w', encoding='utf-8') as f:
            json.dump(self.metadata, f, indent=2)
        
        return self.metadata

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Organize test files and fix imports.')
    parser.add_argument('--test-dir', default='test_output', 
                       help='Directory containing test files')
    parser.add_argument('--source-dir', default='Script_Factory/Script_Factory_Runs/all_runs', 
                       help='Base directory containing source script files (will search recursively)')
    parser.add_argument('--output-dir', default='test_organized', 
                       help='Directory to save organized test files')
    
    args = parser.parse_args()
    
    organizer = TestOrganizer(
        test_output_dir=args.test_dir,
        source_base_dir=args.source_dir,
        processed_dir=args.output_dir
    )
    
    results = organizer.run()
    print(f"Processed {results['files_processed']} files")
    print(f"Found {results['source_scripts_found']} source scripts")
    print(f"Created {results['files_created']} organized test files")
    
    if results['errors']:
        print(f"\nEncountered {len(results['errors'])} errors:")
        for error in results['errors']:
            print(f"  - {error}")