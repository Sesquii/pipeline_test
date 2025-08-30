```python
import os
import random
import argparse

def generate_random_string(length=10):
    """Generate a random string of specified length consisting of letters and digits."""
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join(random.choices(characters, k=length))

def scramble_files(directory):
    """Recursively rename all files in the given directory to random strings."""
    for root, dirs, files in os.walk(directory):
        for filename in files:
            new_name = generate_random_string()
            old_path = os.path.join(root, filename)
            new_path = os.path.join(root, new_name)
            os.rename(old_path, new_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Recursive File Scrambler')
    parser.add_argument('directory', help='Directory to process')
    args = parser.parse_args()
    scramble_files(args.directory)

# ===== GENERATED TESTS =====
```python
import os
import tempfile
import shutil
from typing import List

# Original script remains unchanged

def generate_random_string(length=10):
    """Generate a random string of specified length consisting of letters and digits."""
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join(random.choices(characters, k=length))

def scramble_files(directory):
    """Recursively rename all files in the given directory to random strings."""
    for root, dirs, files in os.walk(directory):
        for filename in files:
            new_name = generate_random_string()
            old_path = os.path.join(root, filename)
            new_path = os.path.join(root, new_name)
            os.rename(old_path, new_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Recursive File Scrambler')
    parser.add_argument('directory', help='Directory to process')
    args = parser.parse_args()
    scramble_files(args.directory)


# Test suite starts here

import pytest

@pytest.fixture
def temp_dir():
    """Create a temporary directory for testing."""
    temp_dir_path = tempfile.mkdtemp()
    yield temp_dir_path
    shutil.rmtree(temp_dir_path)

def test_generate_random_string(temp_dir):
    """Test the generate_random_string function."""
    # Positive case: Check if the generated string has the correct length
    random_str = generate_random_string(10)
    assert len(random_str) == 10

    # Negative case: Check if the generated string contains only allowed characters
    for char in random_str:
        assert char.isalnum()

def test_scramble_files(temp_dir):
    """Test the scramble_files function."""
    # Create a temporary file inside the temp directory
    original_file_path = os.path.join(temp_dir, 'testfile.txt')
    with open(original_file_path, 'w') as f:
        f.write('Hello, World!')

    # Scramble the files in the directory
    scramble_files(temp_dir)

    # Check if the file has been renamed
    assert not os.path.exists(original_file_path)
    new_name = random.choice(os.listdir(temp_dir))
    new_file_path = os.path.join(temp_dir, new_name)
    assert os.path.exists(new_file_path)

def test_scramble_files_empty_directory(temp_dir):
    """Test the scramble_files function with an empty directory."""
    # Scramble files in an empty directory
    scramble_files(temp_dir)

    # Check if no files were renamed
    assert not os.listdir(temp_dir)

def test_scramble_files_non_existent_directory():
    """Test the scramble_files function with a non-existent directory."""
    with pytest.raises(FileNotFoundError):
        scramble_files('/nonexistent/directory')

# Add more tests as needed
```

This test suite includes comprehensive test cases for both `generate_random_string` and `scramble_files` functions. It uses pytest fixtures to create temporary directories for testing, ensuring that the original script remains unchanged. The test cases cover positive scenarios (e.g., generating a random string of the correct length) and negative scenarios (e.g., checking if the generated string contains only allowed characters). Additionally, it tests edge cases such as an empty directory and a non-existent directory.