import os
import random
import string

def scramble_filename(path):
    """Generate a random filename."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10)) + os.path.splitext(path)[1]

def rename_files_recursively(directory):
    """
    Recursively traverse the directory and rename every file to a random, meaningless string.
    
    :param directory: The root directory to start renaming files in.
    """
    for root, _, files in os.walk(directory):
        for file in files:
            old_file_path = os.path.join(root, file)
            new_file_name = scramble_filename(old_file_path)
            new_file_path = os.path.join(root, new_file_name)
            
            # Rename the file
            try:
                os.rename(old_file_path, new_file_path)
                print(f'Renamed: {old_file_path} -> {new_file_path}')
            except Exception as e:
                print(f'Failed to rename {old_file_path}: {e}')

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python scramble_files.py <directory_path>")
        sys.exit(1)
    
    directory_path = sys.argv[1]
    
    # Check if the provided path is a valid directory
    if not os.path.isdir(directory_path):
        print(f"Error: {directory_path} is not a valid directory.")
        sys.exit(1)
    
    rename_files_recursively(directory_path)