import os
import hashlib

def scramble_file_name(file_path):
    """
    Renames a file to its SHA256 hash.
    
    Args:
    file_path (str): The path to the file to be renamed.
    
    Returns:
    str: The new path of the renamed file.
    """
    # Calculate SHA256 hash of the file's content
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as f:
        buf = f.read(65536)
        while len(buf) > 0:
            hasher.update(buf)
            buf = f.read(65536)
    
    # Get the directory and filename
    dir_path, file_name = os.path.split(file_path)
    
    # Create new file name with SHA256 hash
    new_file_name = f"{hasher.hexdigest()}{os.path.splitext(file_name)[1]}"
    new_file_path = os.path.join(dir_path, new_file_name)
    
    # Rename the file
    os.rename(file_path, new_file_path)
    return new_file_path

def scramble_directory(directory_path):
    """
    Recursively scrambles (renames) all files in a directory to their SHA256 hash.
    
    Args:
    directory_path (str): The path to the directory containing the files to be renamed.
    """
    for root, _, files in os.walk(directory_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            scramble_file_name(file_path)

if __name__ == "__main__":
    # Specify the directory to be scrambled
    target_directory = 'path/to/your/directory'
    
    # Scramble the directory
    scramble_directory(target_directory)

Replace `'path/to/your/directory'` with the actual path of the directory you want to scramble.

# ===== GENERATED TESTS =====
import os
import hashlib
from pathlib import Path
import pytest

# Original script remains unchanged

def test_scramble_file_name():
    """Test the scramble_file_name function."""
    # Create a temporary file with known content
    temp_dir = Path("temp_tests")
    temp_dir.mkdir(exist_ok=True)
    temp_file_path = temp_dir / "test.txt"
    with open(temp_file_path, 'wb') as f:
        f.write(b"Hello, world!")
    
    # Scramble the file name
    new_file_path = scramble_file_name(str(temp_file_path))
    
    # Check if the file was renamed
    assert os.path.exists(new_file_path)
    assert not os.path.exists(temp_file_path)
    
    # Verify the new file name is a SHA256 hash followed by the original extension
    _, ext = os.path.splitext(new_file_path)
    assert len(ext) > 0
    assert hashlib.sha256(b"Hello, world!").hexdigest().startswith(os.path.splitext(new_file_path)[0])
    
    # Clean up
    os.remove(new_file_path)
    temp_dir.rmdir()

def test_scramble_directory():
    """Test the scramble_directory function."""
    # Create a temporary directory with known files
    temp_dir = Path("temp_tests")
    temp_dir.mkdir(exist_ok=True)
    sub_dir = temp_dir / "subdir"
    sub_dir.mkdir()
    
    file_paths = [
        temp_dir / "test1.txt",
        temp_dir / "test2.txt",
        sub_dir / "test3.txt"
    ]
    for path in file_paths:
        with open(path, 'wb') as f:
            f.write(b"Hello, world!")
    
    # Scramble the directory
    scramble_directory(str(temp_dir))
    
    # Check if all files were renamed
    for path in file_paths:
        assert not os.path.exists(path)
    
    # Verify new file names are SHA256 hashes followed by the original extensions
    for path in file_paths:
        new_path = temp_dir / f"{hashlib.sha256(b'Hello, world!').hexdigest()}{os.path.splitext(path)[1]}"
        assert os.path.exists(new_path)
    
    # Clean up
    for path in file_paths:
        os.remove(path)
    sub_dir.rmdir()
    temp_dir.rmdir()

def test_scramble_file_name_nonexistent():
    """Test the scramble_file_name function with a non-existent file."""
    non_existent_file_path = "non_existent_file.txt"
    with pytest.raises(FileNotFoundError):
        scramble_file_name(non_existent_file_path)

def test_scramble_directory_empty():
    """Test the scramble_directory function with an empty directory."""
    temp_dir = Path("temp_tests")
    temp_dir.mkdir(exist_ok=True)
    
    # Scramble the empty directory
    scramble_directory(str(temp_dir))
    
    # Check if the directory is still empty
    assert not any(temp_dir.iterdir())
    
    # Clean up
    temp_dir.rmdir()

def test_scramble_file_name_large_file():
    """Test the scramble_file_name function with a large file."""
    temp_dir = Path("temp_tests")
    temp_dir.mkdir(exist_ok=True)
    temp_file_path = temp_dir / "large_test.txt"
    
    # Create a large file
    with open(temp_file_path, 'wb') as f:
        f.write(b"X" * (1024 * 1024))  # 1 MB
    
    # Scramble the file name
    new_file_path = scramble_file_name(str(temp_file_path))
    
    # Check if the file was renamed
    assert os.path.exists(new_file_path)
    assert not os.path.exists(temp_file_path)
    
    # Verify the new file name is a SHA256 hash followed by the original extension
    _, ext = os.path.splitext(new_file_path)
    assert len(ext) > 0
    assert hashlib.sha256(b"X" * (1024 * 1024)).hexdigest().startswith(os.path.splitext(new_file_path)[0])
    
    # Clean up
    os.remove(new_file_path)
    temp_dir.rmdir()
