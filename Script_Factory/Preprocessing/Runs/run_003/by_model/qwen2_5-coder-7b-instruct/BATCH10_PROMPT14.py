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
```

Replace `'path/to/your/directory'` with the actual path of the directory you want to scramble.