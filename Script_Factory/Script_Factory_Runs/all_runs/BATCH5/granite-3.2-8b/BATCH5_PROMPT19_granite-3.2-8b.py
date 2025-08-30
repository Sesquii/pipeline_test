import os
import random
import string
import sys
from argparse import ArgumentParser

def generate_random_filename(length=10):
    """Generate a random string of specified length."""
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(length))

def scramble_files(directory, length=10):
    """Recursively rename all files within the given directory to a random string."""
    for foldername, subfolders, filenames in os.walk(directory):
        for filename in filenames:
            old_file_path = os.path.join(foldername, filename)
            new_filename = generate_random_filename(length) + os.path.splitext(filename)[1]
            new_file_path = os.path.join(foldername, new_filename)
            
            # Rename the file
            os.rename(old_file_path, new_file_path)
            print(f"Renamed: {old_file_path} -> {new_file_path}")

def main():
    parser = ArgumentParser(description="Recursive File Scrambler")
    parser.add_argument("directory", help="Path to the directory to scramble files in.")
    parser.add_argument("-l", "--length", type=int, default=10, help="Length of the random filename (default 10)")

    args = parser.parse_args()
    
    if not os.path.isdir(args.directory):
        print(f"Error: {args.directory} is not a valid directory.")
        sys.exit(1)
    
    scramble_files(args.directory, args.length)

if __name__ == "__main__":
    main()