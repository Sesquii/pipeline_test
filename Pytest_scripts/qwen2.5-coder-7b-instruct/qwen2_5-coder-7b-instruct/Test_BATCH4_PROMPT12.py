import os
import random
import string

def scramble_file_name(file_path):
    """
    Generates a random, meaningless file name.
    """
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10))

def rename_files_in_directory(directory):
    """
    Recursively traverses the directory and renames each file to a random, meaningless string of characters.
    """
    for root, _, files in os.walk(directory):
        for file in files:
            old_file_path = os.path.join(root, file)
            new_file_name = scramble_file_name()
            new_file_path = os.path.join(root, new_file_name)
            
            # Check if the new file name already exists to avoid overwriting
            while os.path.exists(new_file_path):
                new_file_name = scramble_file_name()
                new_file_path = os.path.join(root, new_file_name)
            
            os.rename(old_file_path, new_file_path)
            print(f'Renamed: {old_file_path} -> {new_file_path}')

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
        sys.exit(1)
    
    directory_path = sys.argv[1]
    rename_files_in_directory(directory_path)
```

This Python program defines two functions: `scramble_file_name` and `rename_files_in_directory`. The `scramble_file_name` function generates a random, meaningless file name consisting of letters and digits. The `rename_files_in_directory` function recursively traverses the specified directory and renames each file to a new randomly generated file name, ensuring that no two files in the same directory have the same name.

The script checks if it has been given exactly one command-line argument (the directory path) and then calls the `rename_files_in_directory` function with this argument. If the correct number of arguments is not provided, it prints a usage message and exits.

# ===== GENERATED TESTS =====
```python
import os
import tempfile
from pathlib import Path
from typing import List

# Original script code
import os
import random
import string

def scramble_file_name(file_path):
    """
    Generates a random, meaningless file name.
    """
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10))

def rename_files_in_directory(directory):
    """
    Recursively traverses the directory and renames each file to a random, meaningless string of characters.
    """
    for root, _, files in os.walk(directory):
        for file in files:
            old_file_path = os.path.join(root, file)
            new_file_name = scramble_file_name()
            new_file_path = os.path.join(root, new_file_name)
            
            # Check if the new file name already exists to avoid overwriting
            while os.path.exists(new_file_path):
                new_file_name = scramble_file_name()
                new_file_path = os.path.join(root, new_file_name)
            
            os.rename(old_file_path, new_file_path)
            print(f'Renamed: {old_file_path} -> {new_file_path}')

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
        sys.exit(1)
    
    directory_path = sys.argv[1]
    rename_files_in_directory(directory_path)

# Test cases
import pytest

def create_test_file(directory: Path, file_name: str):
    """Create a test file in the specified directory."""
    with open(os.path.join(directory, file_name), 'w') as f:
        f.write("Test content")

@pytest.fixture(scope="module")
def temp_directory() -> Path:
    """Create a temporary directory for testing."""
    temp_dir = tempfile.mkdtemp()
    yield Path(temp_dir)
    os.rmdir(temp_dir)

def test_scramble_file_name():
    """Test the scramble_file_name function."""
    result = scramble_file_name("test.txt")
    assert len(result) == 10
    assert all(c in string.ascii_letters + string.digits for c in result)

@pytest.mark.parametrize("file_names", [
    ["file1.txt", "file2.txt"],
    ["a.txt", "b.txt", "c.txt"],
    [f"file{i}.txt" for i in range(5)],
])
def test_rename_files_in_directory(temp_directory: Path, file_names: List[str]):
    """Test the rename_files_in_directory function."""
    # Create test files
    for file_name in file_names:
        create_test_file(temp_directory, file_name)
    
    # Call the function to rename files
    rename_files_in_directory(temp_directory)
    
    # Check if all files have been renamed and no two files have the same name
    new_file_names = set()
    for root, _, files in os.walk(temp_directory):
        for file in files:
            assert len(file) == 10
            assert all(c in string.ascii_letters + string.digits for c in file)
            new_file_names.add(file)
    
    assert len(new_file_names) == len(file_names)

def test_rename_files_in_directory_with_existing_name(temp_directory: Path):
    """Test the rename_files_in_directory function with existing names."""
    # Create a test file
    create_test_file(temp_directory, "file1.txt")
    
    # Call the function to rename files
    rename_files_in_directory(temp_directory)
    
    # Check if the file has been renamed and no two files have the same name
    new_file_names = set()
    for root, _, files in os.walk(temp_directory):
        for file in files:
            assert len(file) == 10
            assert all(c in string.ascii_letters + string.digits for c in file)
            new_file_names.add(file)
    
    assert len(new_file_names) == 1

def test_rename_files_in_directory_with_empty_directory(temp_directory: Path):
    """Test the rename_files_in_directory function with an empty directory."""
    # Call the function to rename files
    rename_files_in_directory(temp_directory)

def test_rename_files_in_directory_with_nonexistent_directory():
    """Test the rename_files_in_directory function with a nonexistent directory."""
    with pytest.raises(FileNotFoundError):
        rename_files_in_directory("/nonexistent/directory")
```

This test suite includes comprehensive test cases for both public functions and classes in the original script. It uses pytest fixtures and parametrization where appropriate, adds type hints to test functions, follows PEP 8 style guidelines, and includes proper docstrings and comments.