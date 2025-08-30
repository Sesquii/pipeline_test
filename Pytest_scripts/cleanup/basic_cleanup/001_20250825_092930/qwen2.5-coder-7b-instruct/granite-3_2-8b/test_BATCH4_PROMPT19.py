import os
import sys
import random
import string
from argparse import ArgumentParser

def generate_random_name(length=8):
    """Generate a random string of characters."""
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

def scramble_file(path):
    """Recursively rename files to random strings."""
    if os.path.isfile(path):
        # Generate a new random name and replace the old one
        old_name = os.path.basename(path)
        new_name = generate_random_name() + os.path.splitext(old_name)[1]
        new_path = os.path.join(os.path.dirname(path), new_name)
        os.rename(path, new_path)
    elif os.path.isdir(path):
        # Traverse the directory
        for item in os.listdir(path):
            scramble_file(os.path.join(path, item))

def main():
    parser = ArgumentParser(description='Recursive File Scrambler')
    parser.add_argument('directory', type=str, help='The directory to scramble files in')

    args = parser.parse_args()
    
    if not os.path.exists(args.directory) or not os.path.isdir(args.directory):
        print(f"Invalid directory: {args.directory}")
        return

    scramble_file(args.directory)
    print(f'Files in {args.directory} have been scrambled.')

if __name__ == "__main__":
    main()

# ===== GENERATED TESTS =====
import os
import sys
import random
import string
from argparse import ArgumentParser
import pytest

def generate_random_name(length=8):
    """Generate a random string of characters."""
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

def scramble_file(path):
    """Recursively rename files to random strings."""
    if os.path.isfile(path):
        # Generate a new random name and replace the old one
        old_name = os.path.basename(path)
        new_name = generate_random_name() + os.path.splitext(old_name)[1]
        new_path = os.path.join(os.path.dirname(path), new_name)
        os.rename(path, new_path)
    elif os.path.isdir(path):
        # Traverse the directory
        for item in os.listdir(path):
            scramble_file(os.path.join(path, item))

def main():
    parser = ArgumentParser(description='Recursive File Scrambler')
    parser.add_argument('directory', type=str, help='The directory to scramble files in')

    args = parser.parse_args()
    
    if not os.path.exists(args.directory) or not os.path.isdir(args.directory):
        print(f"Invalid directory: {args.directory}")
        return

    scramble_file(args.directory)
    print(f'Files in {args.directory} have been scrambled.')

if __name__ == "__main__":
    main()

# Test cases
def test_generate_random_name():
    """Test the generate_random_name function."""
    name = generate_random_name()
    assert isinstance(name, str)
    assert len(name) == 8

def test_scramble_file(tmpdir):
    """Test the scramble_file function with a temporary directory."""
    # Create a temporary file
    temp_file_path = os.path.join(tmpdir, 'test.txt')
    with open(temp_file_path, 'w') as f:
        f.write('Hello, World!')

    # Scramble the file
    scramble_file(temp_file_path)

    # Check if the file has been renamed
    assert not os.path.exists(temp_file_path)
    new_name = os.listdir(tmpdir)[0]
    assert isinstance(new_name, str)
    assert new_name.startswith(generate_random_name())

def test_scramble_directory(tmpdir):
    """Test the scramble_file function with a temporary directory containing files and subdirectories."""
    # Create a temporary directory structure
    subdir_path = os.path.join(tmpdir, 'subdir')
    os.mkdir(subdir_path)
    temp_file_path1 = os.path.join(tmpdir, 'test.txt')
    temp_file_path2 = os.path.join(subdir_path, 'test2.txt')
    with open(temp_file_path1, 'w') as f:
        f.write('Hello, World!')
    with open(temp_file_path2, 'w') as f:
        f.write('Hello, World!')

    # Scramble the directory
    scramble_file(tmpdir)

    # Check if files have been renamed
    assert not os.path.exists(temp_file_path1)
    assert not os.path.exists(temp_file_path2)
    new_name1 = os.listdir(tmpdir)[0]
    new_name2 = os.listdir(subdir_path)[0]
    assert isinstance(new_name1, str)
    assert isinstance(new_name2, str)
    assert new_name1.startswith(generate_random_name())
    assert new_name2.startswith(generate_random_name())

def test_main_invalid_directory(capsys):
    """Test the main function with an invalid directory."""
    # Create a temporary file
    temp_file_path = os.path.join('nonexistent', 'test.txt')
    with open(temp_file_path, 'w') as f:
        f.write('Hello, World!')

    # Run the main function
    sys.argv = ['script.py', 'nonexistent']
    main()

    # Check if the error message is printed
    captured = capsys.readouterr()
    assert "Invalid directory: nonexistent" in captured.out

def test_main_valid_directory(tmpdir, capsys):
    """Test the main function with a valid directory."""
    # Create a temporary file
    temp_file_path = os.path.join(tmpdir, 'test.txt')
    with open(temp_file_path, 'w') as f:
        f.write('Hello, World!')

    # Run the main function
    sys.argv = ['script.py', tmpdir]
    main()

    # Check if the success message is printed
    captured = capsys.readouterr()
    assert "Files in" in captured.out

def test_scramble_file_with_special_chars(tmpdir):
    """Test the scramble_file function with a file containing special characters."""
    # Create a temporary file with special characters
    temp_file_path = os.path.join(tmpdir, 'test!@#.txt')
    with open(temp_file_path, 'w') as f:
        f.write('Hello, World!')

    # Scramble the file
    scramble_file(temp_file_path)

    # Check if the file has been renamed
    assert not os.path.exists(temp_file_path)
    new_name = os.listdir(tmpdir)[0]
    assert isinstance(new_name, str)
    assert new_name.startswith(generate_random_name())
