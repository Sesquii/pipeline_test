import os
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python BATCH2_PROMPT23_{{model_name}}.py <directory>")
        return
    
    dir_path = sys.argv[1]
    
    files = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]
    
    for file_name in files:
        for _ in range(3):
            print(file_name)

if __name__ == "__main__":
    main()

# ===== GENERATED TESTS =====
import os
import sys
from unittest.mock import patch

# Original script
def main():
    if len(sys.argv) != 2:
        print("Usage: python BATCH2_PROMPT23_{{model_name}}.py <directory>")
        return
    
    dir_path = sys.argv[1]
    
    files = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]
    
    for file_name in files:
        for _ in range(3):
            print(file_name)

if __name__ == "__main__":
    main()

# Test suite
import pytest

@pytest.fixture
def mock_sys_argv():
    return ["script.py", "test_directory"]

@patch('os.listdir')
def test_main(mock_listdir, mock_sys_argv):
    """Test the main function with a valid directory."""
    # Setup
    mock_listdir.return_value = ['file1.txt', 'file2.txt']
    
    # Call the function
    with patch.object(sys, 'argv', mock_sys_argv):
        main()
    
    # Assertions
    assert len(mock_listdir.call_args[0]) == 1
    assert mock_listdir.call_args[0][0] == 'test_directory'
    assert print.call_count == 6

@patch('os.listdir')
def test_main_no_files(mock_listdir, mock_sys_argv):
    """Test the main function with an empty directory."""
    # Setup
    mock_listdir.return_value = []
    
    # Call the function
    with patch.object(sys, 'argv', mock_sys_argv):
        main()
    
    # Assertions
    assert len(mock_listdir.call_args[0]) == 1
    assert mock_listdir.call_args[0][0] == 'test_directory'
    assert print.call_count == 0

@patch('os.listdir')
def test_main_invalid_directory(mock_listdir, mock_sys_argv):
    """Test the main function with an invalid directory."""
    # Setup
    mock_listdir.side_effect = FileNotFoundError
    
    # Call the function
    with patch.object(sys, 'argv', mock_sys_argv):
        with pytest.raises(SystemExit) as exc_info:
            main()
    
    # Assertions
    assert len(mock_listdir.call_args[0]) == 1
    assert mock_listdir.call_args[0][0] == 'test_directory'
    assert exc_info.value.code == 2

@patch('os.listdir')
def test_main_missing_argument(mock_listdir):
    """Test the main function with missing argument."""
    # Call the function
    with pytest.raises(SystemExit) as exc_info:
        with patch.object(sys, 'argv', ['script.py']):
            main()
    
    # Assertions
    assert exc_info.value.code == 2

@patch('os.listdir')
def test_main_extra_argument(mock_listdir):
    """Test the main function with extra argument."""
    # Call the function
    with pytest.raises(SystemExit) as exc_info:
        with patch.object(sys, 'argv', ['script.py', 'test_directory', 'extra_arg']):
            main()
    
    # Assertions
    assert exc_info.value.code == 2
