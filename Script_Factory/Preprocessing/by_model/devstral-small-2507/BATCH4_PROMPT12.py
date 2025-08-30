import os
import random
import string
import sys

def generate_random_string(length=16):
    """Generate a random string of fixed length."""
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

def scramble_files(directory):
    """Recursively traverse the directory and rename files to random strings."""
    for root, _, files in os.walk(directory):
        for filename in files:
            # Construct full path of current file
            old_path = os.path.join(root, filename)

            # Generate new random name
            new_name = generate_random_string()
            new_path = os.path.join(root, new_name)

            try:
                # Rename the file
                os.rename(old_path, new_path)
                print(f"Renamed: {old_path} -> {new_path}")
            except Exception as e:
                print(f"Error renaming {old_path}: {e}")

def main():
    """Main entry point of the script."""
    if len(sys.argv) != 2:
        print("Usage: python scramble.py <directory>")
        sys.exit(1)

    directory = sys.argv[1]

    # Check if provided argument is a valid directory
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory.")
        sys.exit(1)

    scramble_files(directory)

if __name__ == "__main__":
    main()