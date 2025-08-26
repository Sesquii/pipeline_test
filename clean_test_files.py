# clean_test_files.py
import os
import re
from pathlib import Path

def clean_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Process the file line by line
    lines = content.splitlines(keepends=True)
    cleaned_lines = []
    in_code_block = False
    in_triple_quote = False
    
    # Keywords that indicate valid code lines
    valid_starters = {
        'import ', 'from ', 'def ', 'class ', 'if ', 'for ', 'while ', 'try:', 
        'except', 'with ', 'async ', 'return ', 'yield ', 'raise ', 'assert ',
        'elif ', 'else:', 'except ', 'finally:', 'pass', 'break', 'continue',
        'global ', 'nonlocal ', 'del ', 'print(', 'print (', '#',
        'MEANINGLESS_WORDS =', 'DICTIONARY =', 'LIST =', 'SET =', 'TUPLE =',
        'TEST_', 'test_', 'def test_'
    }
    
    in_collection = False
    collection_indent = 0
    
    for i, line in enumerate(lines):
        # Remove code block markers
        line = re.sub(r'```(python|bash)?\n?', '', line)
        line = line.replace('```', '')
        
        # Skip empty lines
        if not line.strip():
            cleaned_lines.append(line)
            continue
            
        # Check if line is part of a collection
        if not in_collection and re.match(r'^\s*[A-Za-z_][A-Za-z0-9_]*\s*=\s*[[{]', line) and '...' not in line:
            # Start of a collection
            in_collection = True
            collection_indent = len(re.match(r'^\s*', line).group())
            cleaned_lines.append(line)
            continue
            
        if in_collection:
            # Inside a collection, preserve all lines
            cleaned_lines.append(line)
            # Check for end of collection
            current_indent = len(re.match(r'^\s*', line).group())
            if (line.strip() in (']', '}') and current_indent == collection_indent):
                in_collection = False
            continue
        
        # Rest of the cleaning logic for non-collection lines
        line_starts_with_valid = any(line.lstrip().startswith(keyword) for keyword in valid_starters)
        is_indented = line.startswith((' ', '\t')) and not line.strip().startswith('#')
        
        if not (line_starts_with_valid or is_indented):
            if not line.strip().startswith('#'):
                line = f'# {line}'
                
        cleaned_lines.append(line)
        
        if should_comment or (has_indented_quote and not in_code_block):
            # Comment out the line if it's not a valid code line or is a bullet point
            if not line.strip().startswith('#'):
                line = f'# {line}'
        
        cleaned_lines.append(line)
    
    # Write cleaned content back to file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(cleaned_lines)

def clean_test_files(path):
    """Clean either a single file or all .py files in a directory."""
    path = Path(path)
    if path.is_file() and path.suffix == '.py':
        print(f"Cleaning {path}")
        clean_file(path)
    elif path.is_dir():
        for root, _, files in os.walk(path):
            for file in files:
                if file.endswith('.py'):
                    file_path = Path(root) / file
                    print(f"Cleaning {file_path}")
                    clean_file(file_path)
    else:
        print(f"Error: {path} is not a valid Python file or directory")
        return False
    return True

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Clean Python test files by removing code blocks and invalid syntax')
    parser.add_argument('path', nargs='?', default='Pytest_scripts',
                      help='Path to a Python file or directory containing Python files (default: Pytest_scripts)')
    
    args = parser.parse_args()
    
    if clean_test_files(args.path):
        print("Done cleaning files!")
    else:
        exit(1)