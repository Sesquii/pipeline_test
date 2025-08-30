import os

def echo_filename(filename, repetition_count=3):
    """
    Create an echo effect by repeating the filename multiple times.

    Args:
        filename (str): The name of the file to echo.
        repetition_count (int): Number of repetitions for the echo effect.

    Returns:
        str: The filename repeated with decreasing length at each repetition.
    """
    echoed_filename = ""
    for i in range(repetition_count, 0, -1):
        echoed_filename += filename[:len(filename) // i] + " "
    return echoed_filename.strip()

def find_files_in_directory(directory_path):
    """
    Find all files in a given directory and print them with an echo effect.

    Args:
        directory_path (str): The path to the directory to search.
    """
    try:
        # List all entries in the directory
        entries = os.listdir(directory_path)

        for entry in entries:
            full_path = os.path.join(directory_path, entry)
            if os.path.isfile(full_path):
                echoed_filename = echo_filename(entry)
                print(echoed_filename)

    except FileNotFoundError:
        print(f"Directory '{directory_path}' not found.")
    except PermissionError:
        print(f"No permission to access directory '{directory_path}'.")

if __name__ == "__main__":
    # Example usage
    directory_to_search = input("Enter the directory path: ").strip()
    find_files_in_directory(directory_to_search)