```python
import argparse
from pathlib import Path
import random
import string
import os

def generate_random_string(length=8):
    """Generate a random string of specified length using letters and digits."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def main():
    """Main function to handle the recursive file scrambler."""
    parser = argparse.ArgumentParser(description='Recursive File Scrambler')
    parser.add_argument('directory', help='Directory path to process')
    args = parser.parse_args()
    
    current_dir = Path(args.directory)
    
    if not current_dir.exists():
        print(f"Error: Directory {current_dir} does not exist.")
        return
    
    # Traverse all files and subdirectories
    for path in current_dir.glob('**/*'):
        if path.is_file():
            new_name = generate_random_string()
            os.rename(path, path.with_suffix(new_name))
            print(f"Renamed {path} to {new_name}")

if __name__ == '__main__':
    main()

# ===== GENERATED TESTS =====
```python
import pytest
from pathlib import Path
import os
import sys

# Original code
def generate_random_string(length=8):
    """Generate a random string of specified length using letters and digits."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def main():
    """Main function to handle the recursive file scrambler."""
    parser = argparse.ArgumentParser(description='Recursive File Scrambler')
    parser.add_argument('directory', help='Directory path to process')
    args = parser.parse_args()
    
    current_dir = Path(args.directory)
    
    if not current_dir.exists():
        print(f"Error: Directory {current_dir} does not exist.")
        return
    
    # Traverse all files and subdirectories
    for path in current_dir.glob('**/*'):
        if path.is_file():
            new_name = generate_random_string()
            os.rename(path, path.with_suffix(new_name))
            print(f"Renamed {path} to {new_name}")

if __name__ == '__main__':
    main()

# Test cases
def test_generate_random_string():
    """Test the generate_random_string function."""
    assert len(generate_random_string(10)) == 10

def test_main_existing_directory(tmp_path):
    """Test the main function with an existing directory."""
    # Create a temporary directory and some files
    os.mkdir(tmp_path / 'test_dir')
    (tmp_path / 'test_dir' / 'file1.txt').touch()
    (tmp_path / 'test_dir' / 'file2.txt').touch()

    # Run the main function with the temporary directory
    sys.argv = ['main.py', str(tmp_path / 'test_dir')]
    main()

    # Check if files have been renamed
    assert not os.path.exists(tmp_path / 'test_dir' / 'file1.txt')
    assert not os.path.exists(tmp_path / 'test_dir' / 'file2.txt')
    assert os.path.exists(tmp_path / 'test_dir' / f'{generate_random_string()}.txt')
    assert os.path.exists(tmp_path / 'test_dir' / f'{generate_random_string()}.txt')

def test_main_non_existing_directory():
    """Test the main function with a non-existing directory."""
    # Run the main function with a non-existing directory
    sys.argv = ['main.py', '/non/existing/directory']
    main()

    # Check if error message is printed
    captured_output = capsys.readouterr()
    assert "Error: Directory /non/existing/directory does not exist." in captured_output.out

def test_generate_random_string_with_length():
    """Test the generate_random_string function with a specified length."""
    random_string = generate_random_string(15)
    assert len(random_string) == 15
    assert all(c.isalnum() for c in random_string)

def test_main_with_subdirectories(tmp_path):
    """Test the main function with subdirectories."""
    # Create a temporary directory and some files/subdirectories
    os.mkdir(tmp_path / 'test_dir')
    os.mkdir(tmp_path / 'test_dir' / 'subdir1')
    (tmp_path / 'test_dir' / 'file1.txt').touch()
    (tmp_path / 'test_dir' / 'subdir1' / 'file2.txt').touch()

    # Run the main function with the temporary directory
    sys.argv = ['main.py', str(tmp_path / 'test_dir')]
    main()

    # Check if files have been renamed
    assert not os.path.exists(tmp_path / 'test_dir' / 'file1.txt')
    assert not os.path.exists(tmp_path / 'test_dir' / 'subdir1' / 'file2.txt')
    assert os.path.exists(tmp_path / 'test_dir' / f'{generate_random_string()}.txt')
    assert os.path.exists(tmp_path / 'test_dir' / 'subdir1' / f'{generate_random_string()}.txt')

def test_main_with_empty_directory(tmp_path):
    """Test the main function with an empty directory."""
    # Create a temporary directory
    os.mkdir(tmp_path / 'test_dir')

    # Run the main function with the temporary directory
    sys.argv = ['main.py', str(tmp_path / 'test_dir')]
    main()

    # Check if no files have been renamed
    assert not os.listdir(tmp_path / 'test_dir')
```