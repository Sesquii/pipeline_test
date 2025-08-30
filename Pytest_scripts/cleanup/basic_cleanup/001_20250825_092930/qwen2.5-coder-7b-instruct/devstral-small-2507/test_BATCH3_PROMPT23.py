import os

def find_files_in_directory(directory):
    """Find all files in the given directory."""
    try:
        with os.scandir(directory) as entries:
            return [entry.name for entry in entries if entry.is_file()]
    except FileNotFoundError:
        print(f"Directory '{directory}' not found.")
        return []
    except PermissionError:
        print(f"Permission denied to access directory '{directory}'.")
        return []

def echo_filename(filename, repeat_count=3):
    """Repeat the filename to create an echo effect."""
    return ' '.join([filename] * repeat_count)

def main():
    # Get directory from user input
    directory = input("Enter the directory path: ").strip()

    # Find files in the specified directory
    files = find_files_in_directory(directory)

    if not files:
        print("No files found or an error occurred.")
        return

    # Print files with echo effect
    for file in files:
        echoed_file = echo_filename(file)
        print(echoed_file)

if __name__ == "__main__":
    main()

# ===== GENERATED TESTS =====
import os
from typing import List

def find_files_in_directory(directory):
    """Find all files in the given directory."""
    try:
        with os.scandir(directory) as entries:
            return [entry.name for entry in entries if entry.is_file()]
    except FileNotFoundError:
        print(f"Directory '{directory}' not found.")
        return []
    except PermissionError:
        print(f"Permission denied to access directory '{directory}'.")
        return []

def echo_filename(filename, repeat_count=3):
    """Repeat the filename to create an echo effect."""
    return ' '.join([filename] * repeat_count)

def main():
    # Get directory from user input
    directory = input("Enter the directory path: ").strip()

    # Find files in the specified directory
    files = find_files_in_directory(directory)

    if not files:
        print("No files found or an error occurred.")
        return

    # Print files with echo effect
    for file in files:
        echoed_file = echo_filename(file)
        print(echoed_file)

if __name__ == "__main__":
    main()

# Test suite starts here

import pytest
from unittest.mock import patch, MagicMock

# Fixtures to simulate directory contents and user input
@pytest.fixture
def mock_directory():
    return "/path/to/directory"

@pytest.fixture
def mock_files():
    return ["file1.txt", "file2.txt"]

@pytest.fixture
def mock_user_input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: mock_directory)

# Test cases for find_files_in_directory function
def test_find_files_in_directory_success(mock_directory, mock_files):
    """Test successful directory traversal."""
    with patch('os.scandir') as mock_scandir:
        mock_scandir.return_value = MagicMock(__iter__=MagicMock(return_value=[MagicMock(name=file) for file in mock_files]))
        result = find_files_in_directory(mock_directory)
        assert result == mock_files

def test_find_files_in_directory_no_files(mock_directory):
    """Test directory with no files."""
    with patch('os.scandir') as mock_scandir:
        mock_scandir.return_value = MagicMock(__iter__=MagicMock(return_value=[]))
        result = find_files_in_directory(mock_directory)
        assert result == []

def test_find_files_in_directory_file_not_found():
    """Test directory that does not exist."""
    with patch('os.scandir') as mock_scandir:
        mock_scandir.side_effect = FileNotFoundError
        result = find_files_in_directory("/nonexistent/directory")
        assert result == []

def test_find_files_in_directory_permission_denied():
    """Test directory access permission denied."""
    with patch('os.scandir') as mock_scandir:
        mock_scandir.side_effect = PermissionError
        result = find_files_in_directory("/protected/directory")
        assert result == []

# Test cases for echo_filename function
def test_echo_filename_default_repeat():
    """Test default repeat count."""
    result = echo_filename("testfile")
    assert result == "testfile testfile testfile"

def test_echo_filename_custom_repeat():
    """Test custom repeat count."""
    result = echo_filename("testfile", 5)
    assert result == "testfile testfile testfile testfile testfile"

# Test cases for main function
def test_main_success(mock_user_input, mock_files):
    """Test successful execution with files found."""
    with patch('find_files_in_directory', return_value=mock_files) as mock_find_files:
        with patch('echo_filename') as mock_echo:
            main()
            mock_find_files.assert_called_once_with(mock_directory)
            for file in mock_files:
                mock_echo.assert_any_call(file)

def test_main_no_files_found(mock_user_input):
    """Test execution when no files are found."""
    with patch('find_files_in_directory', return_value=[]) as mock_find_files:
        main()
        mock_find_files.assert_called_once_with(mock_directory)
