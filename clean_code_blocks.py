#!/usr/bin/env python3
"""
Post-processing script to remove code block markers (```python and ```) from Python test files.
"""
import os
import re
from pathlib import Path

def clean_code_blocks(file_path):
    """Remove code block markers from a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remove ```python and ``` markers
        cleaned_content = re.sub(r'```python\n|```\n?', '', content)
        
        # Only write if changes were made
        if cleaned_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(cleaned_content)
            return True
        return False
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def process_directory(input_dir, output_dir):
    """Process all Python files from input_dir and save to output_dir."""
    input_dir = Path(input_dir)
    output_dir = Path(output_dir)
    processed = 0
    
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.endswith('.py'):
                input_path = Path(root) / file
                # Create corresponding output path
                rel_path = input_path.relative_to(input_dir)
                output_path = output_dir / rel_path
                
                # Ensure output directory exists
                output_path.parent.mkdir(parents=True, exist_ok=True)
                
                # Process file
                with open(input_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Remove ```python and ``` markers
                cleaned_content = re.sub(r'```python\n|```\n?', '', content)
                
                # Remove any lines that start with ===== or ----- (test result separators)
                cleaned_content = re.sub(r'^[=-]+\n?', '', cleaned_content, flags=re.MULTILINE)
                
                # Remove any docstring-like content at the beginning of the file
                cleaned_content = re.sub(r'^\s*("""|\'\'\').*?\1\s*', '', cleaned_content, flags=re.DOTALL)
                
                # Ensure the file ends with a newline
                cleaned_content = cleaned_content.strip() + '\n'
                
                # Write to output location
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(cleaned_content)
                
                print(f"Processed: {input_path} -> {output_path}")
                processed += 1
    
    print(f"\nProcessing complete. Processed {processed} files.")
    return output_dir

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) != 3:
        print("Usage: python clean_code_blocks.py <input_dir> <output_dir>")
        print("Example: python clean_code_blocks.py Cleaned_Scripts PostProcessed_Scripts")
        sys.exit(1)
    
    input_dir = sys.argv[1]
    output_dir = sys.argv[2]
    
    if not os.path.isdir(input_dir):
        print(f"Error: Input directory not found: {input_dir}")
        sys.exit(1)
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    process_directory(input_dir, output_dir)
