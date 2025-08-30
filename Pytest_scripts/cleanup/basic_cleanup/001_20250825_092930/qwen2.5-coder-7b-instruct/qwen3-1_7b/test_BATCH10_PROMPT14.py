import os
import hashlib
import sys

def compute_sha256(file_path):
    with open(file_path, 'rb') as f:
        data = f.read()
        return hashlib.sha256(data).hexdigest()

def main():
    if len(sys.argv) < 2:
        print("Usage: python scrambler.py <directory>")
        return
    
    dir_path = sys.argv[1]
    
    for filename in os.listdir(dir_path):
        file_path = os.path.join(dir_path, filename)
        
        if not os.path.isfile(file_path):
            continue
        
        sha256_hash = compute_sha256(file_path)
        
        parts = filename.split('.')
        base_part = parts[0] if len(parts) >= 1 else ''
        ext_part = parts[-1] if len(parts) >= 2 else ''
        new_filename = f"{sha256_hash}{base_part}.{ext_part}"
        
        os.rename(file_path, os.path.join(dir_path, new_filename))
    
    print("Renaming completed.")

if __name__ == "__main__":
    main()

# ===== GENERATED TESTS =====
import pytest
from unittest.mock import patch, mock_open

# Original script code remains unchanged

def test_compute_sha256():
    """Test the compute_sha256 function with a sample file."""
    # Create a temporary file with some content
    with open('test_file.txt', 'w') as f:
        f.write('Hello, world!')
    
    expected_hash = hashlib.sha256(b'Hello, world!').hexdigest()
    assert compute_sha256('test_file.txt') == expected_hash
    
    # Clean up the temporary file
    os.remove('test_file.txt')

def test_compute_sha256_empty_file():
    """Test the compute_sha256 function with an empty file."""
    with open('empty_file.txt', 'w'):
        pass  # Create an empty file
    
    expected_hash = hashlib.sha256(b'').hexdigest()
    assert compute_sha256('empty_file.txt') == expected_hash
    
    os.remove('empty_file.txt')

def test_main_no_arguments(capsys):
    """Test the main function with no arguments."""
    with pytest.raises(SystemExit) as exc_info:
        main()
    
    assert exc_info.value.code == 1
    captured = capsys.readouterr()
    assert "Usage: python scrambler.py <directory>" in captured.out

def test_main_nonexistent_directory(capsys):
    """Test the main function with a nonexistent directory."""
    with pytest.raises(SystemExit) as exc_info:
        main(['scrambler.py', 'nonexistent_dir'])
    
    assert exc_info.value.code == 1
    captured = capsys.readouterr()
    assert "No such file or directory" in captured.err

def test_main_empty_directory(capsys):
    """Test the main function with an empty directory."""
    with patch('os.listdir', return_value=[]):
        with pytest.raises(SystemExit) as exc_info:
            main(['scrambler.py', 'empty_dir'])
    
    assert exc_info.value.code == 0
    captured = capsys.readouterr()
    assert "Renaming completed." in captured.out

def test_main_with_files(capsys, tmpdir):
    """Test the main function with files in a directory."""
    # Create some sample files
    file1_path = os.path.join(tmpdir, 'file1.txt')
    file2_path = os.path.join(tmpdir, 'file2.txt')
    
    with open(file1_path, 'w') as f:
        f.write('File 1 content')
    
    with open(file2_path, 'w') as f:
        f.write('File 2 content')
    
    # Mock the rename function
    with patch('os.rename') as mock_rename:
        main(['scrambler.py', str(tmpdir)])
    
    # Check if files were renamed correctly
    assert os.path.exists(os.path.join(tmpdir, hashlib.sha256(b'File 1 content').hexdigest() + 'file1.txt'))
    assert os.path.exists(os.path.join(tmpdir, hashlib.sha256(b'File 2 content').hexdigest() + 'file2.txt'))
    
    captured = capsys.readouterr()
    assert "Renaming completed." in captured.out

# Add more test cases as needed
