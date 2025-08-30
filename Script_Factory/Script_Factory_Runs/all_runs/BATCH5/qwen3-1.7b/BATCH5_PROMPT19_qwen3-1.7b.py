```python
import os
import random
import argparse

def generate_random_string(length=10):
    """Generate a random string of specified length consisting of letters and digits."""
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join(random.choices(characters, k=length))

def scramble_files(directory):
    """Recursively rename all files in the given directory to random strings."""
    for root, dirs, files in os.walk(directory):
        for filename in files:
            new_name = generate_random_string()
            old_path = os.path.join(root, filename)
            new_path = os.path.join(root, new_name)
            os.rename(old_path, new_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Recursive File Scrambler')
    parser.add_argument('directory', help='Directory to process')
    args = parser.parse_args()
    scramble_files(args.directory)