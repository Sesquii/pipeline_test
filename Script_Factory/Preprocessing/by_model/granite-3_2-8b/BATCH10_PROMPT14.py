import os
import hashlib
import sys

def hash_file(file_path):
    """Hash a file using SHA256."""
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as f:
        buf = f.read(65536)  # Read in chunks to handle large files
        while len(buf) > 0:
            hasher.update(buf)
            buf = f.read(65536)
    return hasher.hexdigest()

def scramble_files(directory):
    """Recursively rename all files in a directory to their SHA256 hashes."""
    for root, _, files in os.walk(directory):
        for file in files:
            old_path = os.path.join(root, file)
            new_name = hash_file(old_path) + os.path.splitext(file)[1]  # Keep the original extension
            new_path = os.path.join(root, new_name)

            # Rename the file
            os.rename(old_path, new_path)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python BATCH10_PROMPT14_{model_name}.py <directory>")
        sys.exit(1)

    directory = sys.argv[1]

    if not os.path.isdir(directory):
        print(f"The provided path '{directory}' does not exist or is not a directory.")
        sys.exit(1)

    scramble_files(directory)
    print(f"Files in '{directory}' have been scrambled to their SHA256 hashes.")