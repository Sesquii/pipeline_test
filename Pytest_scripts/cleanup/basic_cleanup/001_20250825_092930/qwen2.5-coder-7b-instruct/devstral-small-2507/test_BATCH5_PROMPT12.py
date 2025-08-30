import os
import random
import string

def generate_random_string(length=10):
    """Generate a random string of fixed length."""
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(length))

def scramble_files_in_directory(directory):
    """Recursively traverse the directory and rename files with random strings."""
    try:
        for root, dirs, files in os.walk(directory):
            for filename in files:
                file_path = os.path.join(root, filename)
                # Generate a new random name for the file
                new_name = generate_random_string() + os.path.splitext(filename)[1]
                new_file_path = os.path.join(root, new_name)
                # Rename the file
                os.rename(file_path, new_file_path)
                print(f'Renamed: {file_path} -> {new_file_path}')
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    """Entry point of the script."""
    import sys

    if len(sys.argv) != 2:
        print("Usage: python scramble_files.py <directory>")
        return

    directory = sys.argv[1]

    # Check if provided argument is a valid directory
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory.")
        return

    scramble_files_in_directory(directory)

if __name__ == "__main__":
    main()

# ===== GENERATED TESTS =====
import pytest
from unittest.mock import patch, MagicMock
import os
import random
import string

# Original script code remains unchanged

def test_generate_random_string():
    """Test the generate_random_string function."""
    length = 10
    result = generate_random_string(length)
    assert len(result) == length
    assert all(c in string.ascii_letters + string.digits for c in result)

@patch('os.walk')
@patch('os.path.join')
@patch('os.rename')
def test_scramble_files_in_directory(mock_rename, mock_join, mock_walk):
    """Test the scramble_files_in_directory function."""
    # Mocking os.walk to return a list of directories and files
    mock_walk.return_value = [
        ('/test_dir', [], ['file1.txt', 'file2.txt']),
        ('/test_dir/subdir', [], ['file3.txt'])
    ]
    
    # Mocking os.path.join to return the correct path
    mock_join.side_effect = lambda *args: '/'.join(args)
    
    # Mocking os.rename to simulate renaming files
    mock_rename.return_value = None
    
    scramble_files_in_directory('/test_dir')
    
    # Check if os.walk was called with the correct arguments
    mock_walk.assert_called_once_with('/test_dir')
    
    # Check if os.path.join was called with the correct arguments
    assert mock_join.call_args_list == [
        call('/test_dir', 'file1.txt'),
        call('/test_dir', 'file2.txt'),
        call('/test_dir/subdir', 'file3.txt')
    ]
    
    # Check if os.rename was called with the correct arguments
    assert mock_rename.call_args_list == [
        call('/test_dir/file1.txt', '/test_dir/xxxxxxxxxx.txt'),
        call('/test_dir/file2.txt', '/test_dir/yyyyyyyyyy.txt'),
        call('/test_dir/subdir/file3.txt', '/test_dir/subdir/zzzzzzzzzz.txt')
    ]

def test_main_valid_directory():
    """Test the main function with a valid directory."""
    # Mocking sys.argv to pass a valid directory
    with patch('sys.argv', ['script.py', '/valid/directory']):
        with patch('os.path.isdir', return_value=True):
            with patch('scramble_files_in_directory') as mock_scramble:
                main()
                
                # Check if scramble_files_in_directory was called with the correct argument
                mock_scramble.assert_called_once_with('/valid/directory')

def test_main_invalid_directory():
    """Test the main function with an invalid directory."""
    # Mocking sys.argv to pass an invalid directory
    with patch('sys.argv', ['script.py', '/invalid/directory']):
        with patch('os.path.isdir', return_value=False):
            with pytest.raises(SystemExit) as exc_info:
                main()
                
                # Check if the script exits with a non-zero status code
                assert exc_info.value.code != 0

# Test cases for the original script end here
