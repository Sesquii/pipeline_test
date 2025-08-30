# BATCH2_PROMPT23_Granite.py

import os
import sys
from random import randint

def echo_find_files(directory):
    """
    This function lists files in a given directory with an 'echo' effect,
    repeating each filename multiple times at random intervals.

    :param directory: The directory to search for files.
    """
    # Get list of all entries in the provided directory
    entries = os.listdir(directory)

    # Filter out directories and only keep files
    files = [f for f in entries if os.path.isfile(os.path.join(directory, f))]
    
    for file_name in files:
        print("\n" + '*'*30)  # Separator line

        # Simulate echo effect by randomly repeating the filename multiple times
        for _ in range(randint(1, 5)):  # Randomly repeat between 1 to 5 times
            print(file_name)
        
        print('\n' + '*'*30)  # Separator line

def main():
    """Entry point of the script."""
    if len(sys.argv) != 2:
        print("Usage: python BATCH2_PROMPT23_Granite.py <directory>")
        sys.exit(1)

    directory = sys.argv[1]

    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory.")
        sys.exit(1)

    echo_find_files(directory)

if __name__ == "__main__":
    main()

# ===== GENERATED TESTS =====
```python
# BATCH2_PROMPT23_Granite.py

import os
import sys
from random import randint
from unittest.mock import patch, mock_open
import pytest

def echo_find_files(directory):
    """
    This function lists files in a given directory with an 'echo' effect,
    repeating each filename multiple times at random intervals.

    :param directory: The directory to search for files.
    """
    # Get list of all entries in the provided directory
    entries = os.listdir(directory)

    # Filter out directories and only keep files
    files = [f for f in entries if os.path.isfile(os.path.join(directory, f))]
    
    for file_name in files:
        print("\n" + '*'*30)  # Separator line

        # Simulate echo effect by randomly repeating the filename multiple times
        for _ in range(randint(1, 5)):  # Randomly repeat between 1 to 5 times
            print(file_name)
        
        print('\n' + '*'*30)  # Separator line

def main():
    """Entry point of the script."""
    if len(sys.argv) != 2:
        print("Usage: python BATCH2_PROMPT23_Granite.py <directory>")
        sys.exit(1)

    directory = sys.argv[1]

    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory.")
        sys.exit(1)

    echo_find_files(directory)

if __name__ == "__main__":
    main()

# Test suite for BATCH2_PROMPT23_Granite.py

def test_echo_find_files(mocker):
    """
    Test the echo_find_files function with mock to simulate file listing.
    """
    # Mock os.listdir to return a list of files
    mocker.patch('os.listdir', return_value=['file1.txt', 'file2.txt'])
    
    # Mock print to capture output
    with patch('builtins.print') as mock_print:
        echo_find_files('/test_directory')
        
        # Check if the correct number of prints were made for each file
        assert len(mock_print.call_args_list) == 6  # 3 files * 2 separator lines

def test_main_valid_directory(mocker, capsys):
    """
    Test the main function with a valid directory.
    """
    # Mock sys.argv to pass a valid directory argument
    mocker.patch.object(sys, 'argv', ['script.py', '/valid_directory'])
    
    # Mock os.path.isdir to return True for a valid directory
    mocker.patch('os.path.isdir', return_value=True)
    
    # Mock echo_find_files to avoid actual execution
    mocker.patch('BATCH2_PROMPT23_Granite.echo_find_files')
    
    main()
    
    captured = capsys.readouterr()
    assert "Usage: python BATCH2_PROMPT23_Granite.py <directory>" not in captured.out

def test_main_invalid_directory(mocker, capsys):
    """
    Test the main function with an invalid directory.
    """
    # Mock sys.argv to pass an invalid directory argument
    mocker.patch.object(sys, 'argv', ['script.py', '/invalid_directory'])
    
    # Mock os.path.isdir to return False for an invalid directory
    mocker.patch('os.path.isdir', return_value=False)
    
    main()
    
    captured = capsys.readouterr()
    assert "Error: /invalid_directory is not a valid directory." in captured.out

def test_main_missing_argument(mocker, capsys):
    """
    Test the main function with missing argument.
    """
    # Mock sys.argv to pass no arguments
    mocker.patch.object(sys, 'argv', ['script.py'])
    
    main()
    
    captured = capsys.readouterr()
    assert "Usage: python BATCH2_PROMPT23_Granite.py <directory>" in captured.out

# Test cases using parametrization for different scenarios
@pytest.mark.parametrize("files, expected_prints", [
    (['file1.txt'], 4),  # 1 file * 2 separator lines + 2 echo prints
    (['file1.txt', 'file2.txt'], 8)  # 2 files * 2 separator lines + 4 echo prints
])
def test_echo_find_files_with_param(mocker, capsys, files, expected_prints):
    """
    Test the echo_find_files function with different number of files.
    """
    mocker.patch('os.listdir', return_value=files)
    
    with patch('builtins.print') as mock_print:
        echo_find_files('/test_directory')
        
        assert len(mock_print.call_args_list) == expected_prints
```

This test suite includes comprehensive tests for the `echo_find_files` and `main` functions. It uses pytest fixtures and parametrization to handle different scenarios, including valid and invalid directories, missing arguments, and different numbers of files in the directory. The tests use mocking to simulate file listing and capture output for verification.