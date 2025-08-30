import os
import random
import string
import sys

def generate_random_string(length=16):
    """Generate a random string of fixed length"""
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

def scramble_file(file_path):
    """Rename the file to a random string"""
    directory, filename = os.path.split(file_path)
    new_filename = generate_random_string() + os.path.splitext(filename)[1]
    new_path = os.path.join(directory, new_filename)

    try:
        os.rename(file_path, new_path)
        print(f"Renamed: {file_path} -> {new_path}")
    except Exception as e:
        print(f"Error renaming {file_path}: {e}")

def scramble_directory(directory_path):
    """Recursively traverse the directory and scramble all files"""
    for root, _, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.isfile(file_path):  # Double-check it's a file
                scramble_file(file_path)

def main():
    """Main entry point"""
    if len(sys.argv) != 2:
        print("Usage: python scrambler.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]

    if not os.path.isdir(directory_path):
        print(f"Error: {directory_path} is not a valid directory")
        sys.exit(1)

    scramble_directory(directory_path)
    print("File scrambling complete.")

if __name__ == "__main__":
    main()