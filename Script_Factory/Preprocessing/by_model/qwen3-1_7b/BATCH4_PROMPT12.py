```python
import os
import random
import sys

def generate_random_name():
    """Generate a random, meaningless string of 8 characters."""
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+{}[];:,.<>?'
    return ''.join(random.choices(chars, k=8))

def main():
    # Check if the user provided a directory
    if len(sys.argv) != 2:
        print("Usage: python scrambler.py <directory>")
        sys.exit(1)
    
    # Get the directory path from command line argument
    directory = sys.argv[1]
    
    # Check if the provided path is a valid directory
    if not os.path.isdir(directory):
        print(f"Directory {directory} does not exist.")
        sys.exit(1)
    
    # Traverse the directory and its subdirectories
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Construct the full path to the file
            file_path = os.path.join(root, file)
            # Generate a random name
            new_name = generate_random_name()
            # Rename the file
            os.rename(file_path, os.path.join(root, new_name))

if __name__ == "__main__":
    main()