import os
import sys
import random
import string
from argparse import ArgumentParser

def generate_random_string(length=10):
    """Generate a random string of specified length."""
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

def scramble_files(directory):
    """Recursively rename files in the given directory to random strings."""
    for root, dirs, files in os.walk(directory):
        for file in files:
            old_path = os.path.join(root, file)
            new_name = generate_random_string() + os.path.splitext(file)[1]
            new_path = os.path.join(root, new_name)
            
            # Rename the file
            os.rename(old_path, new_path)

            print(f"Renamed: {old_path} -> {new_path}")

def main():
    parser = ArgumentParser(description='Recursive File Scrambler')
    parser.add_argument('directory', type=str, help='The directory to scramble files in')
    
    args = parser.parse_args()

    if not os.path.isdir(args.directory):
        print(f"The path '{args.directory}' does not exist or is not a directory.")
        return

    scramble_files(args.directory)

if __name__ == "__main__":
    main()

# ===== GENERATED TESTS =====
```python
import os
from unittest.mock import patch, MagicMock
from io import StringIO
import pytest

# Original script code remains unchanged

# Test suite for the original script

def test_generate_random_string():
    """Test the generate_random_string function."""
    result = generate_random_string(5)
    assert isinstance(result, str)
    assert len(result) == 5
    assert all(c in string.ascii_letters + string.digits for c in result)

@patch('os.walk')
def test_scramble_files(mock_os_walk):
    """Test the scramble_files function."""
    mock_os_walk.return_value = [
        ('/path/to/dir', [], ['file1.txt', 'file2.jpg']),
        ('/path/to/dir/subdir', [], ['file3.png'])
    ]
    
    with patch('os.rename') as mock_rename:
        scramble_files('/path/to/dir')
        
        assert mock_rename.call_count == 3
        mock_rename.assert_any_call('/path/to/dir/file1.txt', '/path/to/dir/xxxxxxxxxx.txt')
        mock_rename.assert_any_call('/path/to/dir/subdir/file3.png', '/path/to/dir/subdir/yyyyyyyyyy.png')

def test_main_valid_directory():
    """Test the main function with a valid directory."""
    with patch('sys.argv', ['script.py', '/path/to/dir']), \
         patch('os.path.isdir', return_value=True), \
         patch('os.walk') as mock_os_walk, \
         patch('os.rename') as mock_rename:
        mock_os_walk.return_value = [
            ('/path/to/dir', [], ['file1.txt']),
        ]
        
        main()
        
        assert mock_rename.call_count == 1
        mock_rename.assert_called_once_with('/path/to/dir/file1.txt', '/path/to/dir/xxxxxxxxxx.txt')

def test_main_invalid_directory():
    """Test the main function with an invalid directory."""
    with patch('sys.argv', ['script.py', '/path/to/nonexistent']), \
         patch('os.path.isdir', return_value=False):
        with pytest.raises(SystemExit) as exc_info:
            main()
        
        assert exc_info.value.code == 1

# Test cases for the original script end here
```