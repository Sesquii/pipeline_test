import os
import sys
import random
import string

def scramble_file_name(file_path):
    """
    Generates a random string to rename the file.
    
    Args:
    file_path (str): The path of the file to rename.

    Returns:
    str: The new name for the file.
    """
    base, ext = os.path.splitext(file_path)
    new_name = ''.join(random.choices(string.ascii_letters + string.digits, k=10)) + ext
    return new_name

def recursive_file_scrambler(directory):
    """
    Recursively traverses a directory and renames each file found with a random name.
    
    Args:
    directory (str): The path of the directory to traverse.
    """
    for root, _, files in os.walk(directory):
        for file in files:
            old_file_path = os.path.join(root, file)
            new_file_name = scramble_file_name(old_file_path)
            new_file_path = os.path.join(root, new_file_name)
            os.rename(old_file_path, new_file_path)
            print(f"Renamed: {old_file_path} -> {new_file_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scramble_files.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]
    recursive_file_scrambler(directory_path)
```
This Python script takes a directory path as a command-line argument and recursively traverses it. For each file found, it generates a new random name and renames the file to this new name. The renaming includes preserving the original file extension.

# ===== GENERATED TESTS =====
```python
import os
import sys
import tempfile
from unittest.mock import patch
import pytest

# Original script code remains here as per requirement 1.

def test_scramble_file_name():
    """
    Test the scramble_file_name function with various inputs.
    """
    # Positive test cases
    assert scramble_file_name("test.txt") != "test.txt"
    assert len(scramble_file_name("test.txt")) == 11

    # Negative test cases
    with pytest.raises(TypeError):
        scramble_file_name(123)

def test_recursive_file_scrambler():
    """
    Test the recursive_file_scrambler function.
    """
    # Create a temporary directory and some files for testing
    with tempfile.TemporaryDirectory() as temp_dir:
        file_paths = [os.path.join(temp_dir, f"test{i}.txt") for i in range(5)]
        for path in file_paths:
            open(path, 'a').close()

        # Mock the os.walk function to return predefined paths and files
        with patch('os.walk') as mock_walk:
            mock_walk.return_value = [
                (temp_dir, [], ['test0.txt', 'test1.txt']),
                (os.path.join(temp_dir, 'subdir'), [], ['test2.txt'])
            ]
            
            # Mock the os.rename function to check if it's called correctly
            with patch('os.rename') as mock_rename:
                recursive_file_scrambler(temp_dir)
                
                # Check if os.walk was called with the correct arguments
                mock_walk.assert_called_once_with(temp_dir)

                # Check if os.rename was called for each file
                assert mock_rename.call_count == 3

                # Check if the new file names are valid and have the same extension
                for call_args in mock_rename.call_args_list:
                    old_path, new_path = call_args.args
                    assert os.path.splitext(old_path)[1] == os.path.splitext(new_path)[1]
                    assert len(os.path.basename(new_path)) == 11

# Add more tests as needed following the same pattern.
```