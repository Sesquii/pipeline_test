#!/usr/bin/env python3
"""
Basic script cleanup utility.

This script performs the following operations on Python files:
1. Removes triple backticks with optional language specifiers (```python, ```bash, etc.)
2. If triple backticks are found within the last 5 lines, removes them and everything after
"""

import re
import sys
from pathlib import Path

def clean_file(file_path: Path) -> None:
    """Clean up a single file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Remove triple backticks with optional language specifier
    cleaned_lines = []
    for line in lines:
        line = re.sub(r'```(python|bash)?\n?', '', line)
        line = line.replace('```', '')
        cleaned_lines.append(line)
    
    # Check last 5 lines for triple backticks
    last_lines = ''.join(cleaned_lines[-5:])
    last_backtick_pos = last_lines.rfind('```')
    
    if last_backtick_pos != -1:
        # Find which line in the last 5 contains the backticks
        last_lines_list = cleaned_lines[-5:]
        for i, line in enumerate(last_lines_list):
            if '```' in line:
                # Keep only the lines before the first occurrence in these last lines
                cleaned_lines = cleaned_lines[:-5 + i]
                break
    
    # Write cleaned content back to file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(cleaned_lines)

def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <file_or_directory>")
        sys.exit(1)
    
    path = Path(sys.argv[1])
    
    if path.is_file() and path.suffix == '.py':
        print(f"Cleaning {path}")
        clean_file(path)
    elif path.is_dir():
        for py_file in path.rglob('*.py'):
            print(f"Cleaning {py_file}")
            clean_file(py_file)
    else:
        print(f"Error: {path} is not a Python file or directory")
        sys.exit(1)

if __name__ == "__main__":
    main()
