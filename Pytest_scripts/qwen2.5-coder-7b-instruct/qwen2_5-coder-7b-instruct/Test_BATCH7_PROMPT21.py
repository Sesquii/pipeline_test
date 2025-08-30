import os
import random

# List of common libraries to choose from
COMMON_LIBRARIES = ['os', 'sys', 'math', 'random']

def insert_useless_imports(file_path):
    """
    Inserts 'import *' statements from a random library at the top of every 10th line in the given Python file.
    
    :param file_path: Path to the input Python file.
    """
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # Insert import statements at the top of every 10th line
    for i in range(9, len(lines), 10):
        library = random.choice(COMMON_LIBRARIES)
        lines.insert(i, f"import {library} as *\n")
    
    with open(file_path, 'w') as file:
        file.writelines(lines)

if __name__ == "__main__":
    input_file_path = 'input.py'  # Replace with the path to your Python file
    insert_useless_imports(input_file_path)
```

This script will take an input Python file and randomly insert `import *` statements from a list of common libraries at the top of every 10th line. The modified file will be saved back to the same location.

# ===== GENERATED TESTS =====
```python
import pytest
from typing import List

# Original script remains unchanged

def test_insert_useless_imports(tmp_path):
    """
    Test the insert_useless_imports function with a temporary file.
    
    :param tmp_path: Temporary directory provided by pytest for testing.
    """
    input_file = tmp_path / 'input.py'
    input_file.write_text("print('Hello, World!')")
    
    insert_useless_imports(input_file)
    
    with open(input_file, 'r') as file:
        lines = file.readlines()
    
    # Check if there are any import statements added
    assert any(line.startswith('import ') for line in lines), "No import statements were added."
    
    # Check if the number of import statements is a multiple of 10
    import_statements = [line for line in lines if line.startswith('import ')]
    assert len(import_statements) % 10 == 0, "The number of import statements is not a multiple of 10."
    
def test_insert_useless_imports_no_lines(tmp_path):
    """
    Test the insert_useless_imports function with an empty file.
    
    :param tmp_path: Temporary directory provided by pytest for testing.
    """
    input_file = tmp_path / 'input.py'
    input_file.write_text("")
    
    insert_useless_imports(input_file)
    
    with open(input_file, 'r') as file:
        lines = file.readlines()
    
    # Check if there are no import statements added
    assert not any(line.startswith('import ') for line in lines), "Import statements were added to an empty file."
    
def test_insert_useless_imports_random_library(tmp_path):
    """
    Test the insert_useless_imports function with a temporary file and check if random libraries are used.
    
    :param tmp_path: Temporary directory provided by pytest for testing.
    """
    input_file = tmp_path / 'input.py'
    input_file.write_text("print('Hello, World!')")
    
    insert_useless_imports(input_file)
    
    with open(input_file, 'r') as file:
        lines = file.readlines()
    
    # Check if the imported libraries are from the list of common libraries
    import_statements = [line.split()[1] for line in lines if line.startswith('import ') and line.endswith('*\n')]
    assert all(library in COMMON_LIBRARIES for library in import_statements), "Imported libraries are not from the list of common libraries."
    
def test_insert_useless_imports_multiple_files(tmp_path):
    """
    Test the insert_useless_imports function with multiple temporary files.
    
    :param tmp_path: Temporary directory provided by pytest for testing.
    """
    input_files = [tmp_path / f'input_{i}.py' for i in range(3)]
    for file in input_files:
        file.write_text("print('Hello, World!')")
    
    for file in input_files:
        insert_useless_imports(file)
    
    for file in input_files:
        with open(file, 'r') as f:
            lines = f.readlines()
        
        # Check if there are any import statements added
        assert any(line.startswith('import ') for line in lines), "No import statements were added to a file."
        
        # Check if the number of import statements is a multiple of 10
        import_statements = [line for line in lines if line.startswith('import ')]
        assert len(import_statements) % 10 == 0, "The number of import statements is not a multiple of 10."
```