import os
import random
import string
import sys
from argparse import ArgumentParser


def generate_random_filename(length=10):
    """Generates a random filename of specified length."""
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))


def scramble_files(directory):
    """Recursively scrambles file names within the given directory."""
    for root, _, files in os.walk(directory):
        for filename in files:
            old_filepath = os.path.join(root, filename)
            new_filename = generate_random_filename() + os.path.splitext(filename)[1]
            new_filepath = os.path.join(root, new_filename)

            # Rename the file
            os.rename(old_filepath, new_filepath)
            print(f"Renamed '{old_filepath}' to '{new_filepath}'")


if __name__ == "__main__":
    parser = ArgumentParser(description="Scrambles file names in a directory.")
    parser.add_argument("directory", help="The path of the directory to scramble files in.")

    args = parser.parse_args()
    
    if not os.path.isdir(args.directory):
        print(f"Error: '{args.directory}' is not a valid directory.")
    else:
        scramble_files(args.directory)