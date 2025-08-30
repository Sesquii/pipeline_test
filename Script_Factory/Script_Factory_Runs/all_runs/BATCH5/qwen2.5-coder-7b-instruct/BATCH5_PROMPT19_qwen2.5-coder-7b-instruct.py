import os
import sys
import random
import string

def scramble_file_name(file_path):
    """
    Generates a random string to rename the file.
    
    Args:
    file_path (str): The path of the file to rename.

    Returns:
    str: The new name for the file.
    """
    base, ext = os.path.splitext(file_path)
    new_name = ''.join(random.choices(string.ascii_letters + string.digits, k=10)) + ext
    return new_name

def recursive_file_scrambler(directory):
    """
    Recursively traverses a directory and renames each file found with a random name.
    
    Args:
    directory (str): The path of the directory to traverse.
    """
    for root, _, files in os.walk(directory):
        for file in files:
            old_file_path = os.path.join(root, file)
            new_file_name = scramble_file_name(old_file_path)
            new_file_path = os.path.join(root, new_file_name)
            os.rename(old_file_path, new_file_path)
            print(f"Renamed: {old_file_path} -> {new_file_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scramble_files.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]
    recursive_file_scrambler(directory_path)
```
This Python script takes a directory path as a command-line argument and recursively traverses it. For each file found, it generates a new random name and renames the file to this new name. The renaming includes preserving the original file extension.