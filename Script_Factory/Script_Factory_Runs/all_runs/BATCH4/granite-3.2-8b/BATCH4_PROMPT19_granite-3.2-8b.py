import os
import sys
import random
import string
from argparse import ArgumentParser

def generate_random_name(length=8):
    """Generate a random string of characters."""
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

def scramble_file(path):
    """Recursively rename files to random strings."""
    if os.path.isfile(path):
        # Generate a new random name and replace the old one
        old_name = os.path.basename(path)
        new_name = generate_random_name() + os.path.splitext(old_name)[1]
        new_path = os.path.join(os.path.dirname(path), new_name)
        os.rename(path, new_path)
    elif os.path.isdir(path):
        # Traverse the directory
        for item in os.listdir(path):
            scramble_file(os.path.join(path, item))

def main():
    parser = ArgumentParser(description='Recursive File Scrambler')
    parser.add_argument('directory', type=str, help='The directory to scramble files in')

    args = parser.parse_args()
    
    if not os.path.exists(args.directory) or not os.path.isdir(args.directory):
        print(f"Invalid directory: {args.directory}")
        return

    scramble_file(args.directory)
    print(f'Files in {args.directory} have been scrambled.')

if __name__ == "__main__":
    main()