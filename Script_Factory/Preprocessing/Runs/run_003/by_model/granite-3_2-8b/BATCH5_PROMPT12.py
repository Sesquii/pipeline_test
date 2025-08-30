import os
import sys
import random
import string
from argparse import ArgumentParser

def generate_random_string(length=10):
    """Generate a random string of specified length."""
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

def scramble_files(directory):
    """Recursively rename files in the given directory to random strings."""
    for root, dirs, files in os.walk(directory):
        for file in files:
            old_path = os.path.join(root, file)
            new_name = generate_random_string() + os.path.splitext(file)[1]
            new_path = os.path.join(root, new_name)
            
            # Rename the file
            os.rename(old_path, new_path)

            print(f"Renamed: {old_path} -> {new_path}")

def main():
    parser = ArgumentParser(description='Recursive File Scrambler')
    parser.add_argument('directory', type=str, help='The directory to scramble files in')
    
    args = parser.parse_args()

    if not os.path.isdir(args.directory):
        print(f"The path '{args.directory}' does not exist or is not a directory.")
        return

    scramble_files(args.directory)

if __name__ == "__main__":
    main()