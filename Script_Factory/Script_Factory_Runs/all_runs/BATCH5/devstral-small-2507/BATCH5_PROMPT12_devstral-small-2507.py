import os
import random
import string

def generate_random_string(length=10):
    """Generate a random string of fixed length."""
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(length))

def scramble_files_in_directory(directory):
    """Recursively traverse the directory and rename files with random strings."""
    try:
        for root, dirs, files in os.walk(directory):
            for filename in files:
                file_path = os.path.join(root, filename)
                # Generate a new random name for the file
                new_name = generate_random_string() + os.path.splitext(filename)[1]
                new_file_path = os.path.join(root, new_name)
                # Rename the file
                os.rename(file_path, new_file_path)
                print(f'Renamed: {file_path} -> {new_file_path}')
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    """Entry point of the script."""
    import sys

    if len(sys.argv) != 2:
        print("Usage: python scramble_files.py <directory>")
        return

    directory = sys.argv[1]

    # Check if provided argument is a valid directory
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory.")
        return

    scramble_files_in_directory(directory)

if __name__ == "__main__":
    main()