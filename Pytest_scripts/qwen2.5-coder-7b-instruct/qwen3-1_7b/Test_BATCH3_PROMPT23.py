```python
import os
import sys
import random

def main():
    if len(sys.argv) < 2:
        print("Usage: python echo_finder.py <directory>")
        sys.exit(1)
    
    dir_path = sys.argv[1]
    if not os.path.isdir(dir_path):
        print(f"Directory {dir_path} does not exist.")
        sys.exit(1)
    
    # List all files in the directory, excluding directories
    files = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]
    
    # Print each file repeated multiple times (2-5 times)
    for filename in files:
        count = random.randint(2, 5)
        for _ in range(count):
            print(filename)

if __name__ == "__main__":
    main()

# ===== GENERATED TESTS =====
```python
import pytest
from io import StringIO
import sys

# Original script code
def main():
    if len(sys.argv) < 2:
        print("Usage: python echo_finder.py <directory>")
        sys.exit(1)
    
    dir_path = sys.argv[1]
    if not os.path.isdir(dir_path):
        print(f"Directory {dir_path} does not exist.")
        sys.exit(1)
    
    # List all files in the directory, excluding directories
    files = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]
    
    # Print each file repeated multiple times (2-5 times)
    for filename in files:
        count = random.randint(2, 5)
        for _ in range(count):
            print(filename)

if __name__ == "__main__":
    main()

# Test cases
def test_main_no_args(capsys):
    """Test main function with no arguments"""
    sys.argv = ['echo_finder.py']
    with pytest.raises(SystemExit) as excinfo:
        main()
    assert excinfo.value.code == 1
    captured = capsys.readouterr()
    assert "Usage: python echo_finder.py <directory>" in captured.out

def test_main_nonexistent_dir(capsys):
    """Test main function with a non-existent directory"""
    sys.argv = ['echo_finder.py', 'nonexistent_directory']
    with pytest.raises(SystemExit) as excinfo:
        main()
    assert excinfo.value.code == 1
    captured = capsys.readouterr()
    assert "Directory nonexistent_directory does not exist." in captured.out

def test_main_existing_dir(mocker, capsys):
    """Test main function with an existing directory"""
    mock_files = ['file1.txt', 'file2.txt']
    mocker.patch('os.listdir', return_value=mock_files)
    mocker.patch('os.path.isfile', return_value=True)
    
    sys.argv = ['echo_finder.py', '/tmp']
    main()
    captured = capsys.readouterr()
    assert "file1.txt" in captured.out
    assert "file2.txt" in captured.out
    # Check if each file is printed between 2 and 5 times
    assert len(captured.out.split('\n')) >= 4

def test_main_existing_dir_with_subdir(mocker, capsys):
    """Test main function with an existing directory containing subdirectories"""
    mock_files = ['file1.txt', 'subdir/file2.txt']
    mocker.patch('os.listdir', return_value=mock_files)
    mocker.patch('os.path.isfile', side_effect=[True, False])
    
    sys.argv = ['echo_finder.py', '/tmp']
    main()
    captured = capsys.readouterr()
    assert "file1.txt" in captured.out
    assert "subdir/file2.txt" not in captured.out

def test_main_existing_dir_with_empty_file(mocker, capsys):
    """Test main function with an existing directory containing empty files"""
    mock_files = ['empty_file.txt']
    mocker.patch('os.listdir', return_value=mock_files)
    mocker.patch('os.path.isfile', return_value=True)
    
    sys.argv = ['echo_finder.py', '/tmp']
    main()
    captured = capsys.readouterr()
    assert "empty_file.txt" in captured.out
```