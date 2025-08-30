import os
import random
import string
import sys

def generate_random_string(length=10):
    """Generate a random string of fixed length"""
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

def scramble_files_in_directory(directory_path):
    """Recursively traverse the directory and rename files to random strings"""
    try:
        # Walk through the directory
        for root, _, files in os.walk(directory_path):
            for filename in files:
                file_path = os.path.join(root, filename)
                # Generate a new random name and rename the file
                new_name = generate_random_string() + os.path.splitext(filename)[1]
                new_file_path = os.path.join(root, new_name)
                print(f"Renaming '{file_path}' to '{new_file_path}'")
                os.rename(file_path, new_file_path)
        print("File scrambling complete!")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python scramble_files.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]

    if not os.path.isdir(directory_path):
        print(f"Error: '{directory_path}' is not a valid directory.")
        sys.exit(1)

    scramble_files_in_directory(directory_path)

if __name__ == "__main__":
    main()