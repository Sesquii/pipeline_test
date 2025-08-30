import os
import random
import string
import sys
from argparse import ArgumentParser


def generate_random_filename(length=10):
    """Generates a random filename of specified length."""
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))


def scramble_files(directory):
    """Recursively scrambles file names within the given directory."""
    for root, _, files in os.walk(directory):
        for filename in files:
            old_filepath = os.path.join(root, filename)
            new_filename = generate_random_filename() + os.path.splitext(filename)[1]
            new_filepath = os.path.join(root, new_filename)

            # Rename the file
            os.rename(old_filepath, new_filepath)
            print(f"Renamed '{old_filepath}' to '{new_filepath}'")


if __name__ == "__main__":
    parser = ArgumentParser(description="Scrambles file names in a directory.")
    parser.add_argument("directory", help="The path of the directory to scramble files in.")

    args = parser.parse_args()
    
    if not os.path.isdir(args.directory):
        print(f"Error: '{args.directory}' is not a valid directory.")
    else:
        scramble_files(args.directory)

# ===== GENERATED TESTS =====
```python
import pytest
from unittest.mock import patch, MagicMock

# Original script code
import os
import random
import string
import sys
from argparse import ArgumentParser


def generate_random_filename(length=10):
    """Generates a random filename of specified length."""
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))


def scramble_files(directory):
    """Recursively scrambles file names within the given directory."""
    for root, _, files in os.walk(directory):
        for filename in files:
            old_filepath = os.path.join(root, filename)
            new_filename = generate_random_filename() + os.path.splitext(filename)[1]
            new_filepath = os.path.join(root, new_filename)

            # Rename the file
            os.rename(old_filepath, new_filepath)
            print(f"Renamed '{old_filepath}' to '{new_filepath}'")


if __name__ == "__main__":
    parser = ArgumentParser(description="Scrambles file names in a directory.")
    parser.add_argument("directory", help="The path of the directory to scramble files in.")

    args = parser.parse_args()
    
    if not os.path.isdir(args.directory):
        print(f"Error: '{args.directory}' is not a valid directory.")
    else:
        scramble_files(args.directory)
```

# Test cases

```python
import pytest
from unittest.mock import patch, MagicMock

def test_generate_random_filename():
    """Test the generate_random_filename function."""
    filename = generate_random_filename()
    assert isinstance(filename, str)
    assert len(filename) == 10
    assert all(c in string.ascii_letters + string.digits for c in filename)

@patch('os.walk')
def test_scramble_files(mock_os_walk):
    """Test the scramble_files function."""
    mock_os_walk.return_value = [
        ('/test/directory', [], ['file1.txt', 'file2.jpg']),
        ('/test/directory/subdir', [], ['file3.png'])
    ]

    with patch('os.rename') as mock_rename:
        scramble_files('/test/directory')

        mock_rename.assert_called_with(
            '/test/directory/file1.txt',
            '/test/directory/' + generate_random_filename() + '.txt'
        )
        mock_rename.assert_called_with(
            '/test/directory/file2.jpg',
            '/test/directory/' + generate_random_filename() + '.jpg'
        )
        mock_rename.assert_called_with(
            '/test/directory/subdir/file3.png',
            '/test/directory/subdir/' + generate_random_filename() + '.png'
        )

def test_scramble_files_invalid_directory():
    """Test the scramble_files function with an invalid directory."""
    with patch('os.path.isdir', return_value=False):
        with pytest.raises(SystemExit) as exc_info:
            scramble_files('/invalid/directory')

        assert exc_info.value.code == 1

def test_scramble_files_empty_directory():
    """Test the scramble_files function with an empty directory."""
    with patch('os.walk', return_value=[('/test/empty', [], [])]):
        with pytest.raises(SystemExit) as exc_info:
            scramble_files('/test/empty')

        assert exc_info.value.code == 0
```