import os
import random
import string

def scramble_file_name(file_path):
    """
    Generates a random, meaningless file name.
    """
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10))

def rename_files_in_directory(directory):
    """
    Recursively traverses the directory and renames each file to a random, meaningless string of characters.
    """
    for root, _, files in os.walk(directory):
        for file in files:
            old_file_path = os.path.join(root, file)
            new_file_name = scramble_file_name()
            new_file_path = os.path.join(root, new_file_name)
            
            # Check if the new file name already exists to avoid overwriting
            while os.path.exists(new_file_path):
                new_file_name = scramble_file_name()
                new_file_path = os.path.join(root, new_file_name)
            
            os.rename(old_file_path, new_file_path)
            print(f'Renamed: {old_file_path} -> {new_file_path}')

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
        sys.exit(1)
    
    directory_path = sys.argv[1]
    rename_files_in_directory(directory_path)
```

This Python program defines two functions: `scramble_file_name` and `rename_files_in_directory`. The `scramble_file_name` function generates a random, meaningless file name consisting of letters and digits. The `rename_files_in_directory` function recursively traverses the specified directory and renames each file to a new randomly generated file name, ensuring that no two files in the same directory have the same name.

The script checks if it has been given exactly one command-line argument (the directory path) and then calls the `rename_files_in_directory` function with this argument. If the correct number of arguments is not provided, it prints a usage message and exits.