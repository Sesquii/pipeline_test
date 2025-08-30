import os

def find_files_in_directory(directory):
    """Find all files in the given directory."""
    try:
        with os.scandir(directory) as entries:
            return [entry.name for entry in entries if entry.is_file()]
    except FileNotFoundError:
        print(f"Directory '{directory}' not found.")
        return []
    except PermissionError:
        print(f"Permission denied to access directory '{directory}'.")
        return []

def echo_filename(filename, repeat_count=3):
    """Repeat the filename to create an echo effect."""
    return ' '.join([filename] * repeat_count)

def main():
    # Get directory from user input
    directory = input("Enter the directory path: ").strip()

    # Find files in the specified directory
    files = find_files_in_directory(directory)

    if not files:
        print("No files found or an error occurred.")
        return

    # Print files with echo effect
    for file in files:
        echoed_file = echo_filename(file)
        print(echoed_file)

if __name__ == "__main__":
    main()