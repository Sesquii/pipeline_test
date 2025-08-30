import os
import hashlib

def calculate_sha256(file_path):
    """Calculate the SHA256 hash of a file."""
    sha256 = hashlib.sha256()
    try:
        with open(file_path, 'rb') as f:
            while chunk := f.read(8192):
                sha256.update(chunk)
    except IOError as e:
        print(f"Error reading file {file_path}: {e}")
        return None
    return sha256.hexdigest()

def rename_file_to_hash(file_path):
    """Rename a file to its SHA256 hash."""
    if os.path.isdir(file_path):
        # Skip directories
        return

    file_dir = os.path.dirname(file_path)
    file_name = os.path.basename(file_path)

    # Calculate the hash
    sha256_hash = calculate_sha256(file_path)
    if not sha256_hash:
        print(f"Skipping {file_path} due to error in hash calculation")
        return

    # Create new file name with .hash extension
    new_file_name = f"{sha256_hash}"
    new_file_path = os.path.join(file_dir, new_file_name)

    try:
        os.rename(file_path, new_file_path)
        print(f"Renamed '{file_name}' to '{new_file_name}'")
    except OSError as e:
        print(f"Error renaming file {file_path} to {new_file_path}: {e}")

def scramble_directory(directory):
    """Scramble all files in a directory by renaming them to their SHA256 hash."""
    if not os.path.isdir(directory):
        print(f"Directory {directory} does not exist")
        return

    for root, _, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            rename_file_to_hash(file_path)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Recursively scramble file names to their SHA256 hash.")
    parser.add_argument("directory", help="The directory containing files to be scrambled.")

    args = parser.parse_args()
    scramble_directory(args.directory)