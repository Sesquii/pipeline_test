import os
import random
import string

def scramble_file_name(file_path):
    """Scrambles the name of a file to a random string."""
    directory, filename = os.path.split(file_path)
    new_filename = ''.join(random.choices(string.ascii_letters + string.digits, k=len(filename)))
    return os.path.join(directory, new_filename)

def recursive_scramble_directory(directory_path):
    """Recursively scrambles all files in the given directory."""
    for root, _, files in os.walk(directory_path):
        for file in files:
            old_file_path = os.path.join(root, file)
            new_file_path = scramble_file_name(old_file_path)
            os.rename(old_file_path, new_file_path)
            print(f"Renamed: {old_file_path} -> {new_file_path}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python recursive_scrambler.py <directory_path>")
        sys.exit(1)
    
    directory_path = sys.argv[1]
    recursive_scramble_directory(directory_path)
```

This Python script defines a function `scramble_file_name` that generates a random string of alphanumeric characters to replace the original file name. The `recursive_scramble_directory` function traverses the specified directory recursively and renames each file using the `scramble_file_name` function. The entry point of the script checks for a command-line argument specifying the directory path to scramble, then calls the recursive scrambling function with that path.