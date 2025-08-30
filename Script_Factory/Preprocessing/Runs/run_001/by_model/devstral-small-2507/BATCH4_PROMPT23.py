import os

def echo_filename(filename, repeat_count=3):
    """
    Repeat a filename to create an echo effect.

    Args:
        filename (str): The name of the file to echo.
        repeat_count (int): Number of times to repeat the filename.

    Returns:
        str: The echoed filename string.
    """
    return ' '.join([filename] * repeat_count)

def find_files_in_directory(directory):
    """
    Find all files in a given directory and print them with an echo effect.

    Args:
        directory (str): The path of the directory to search.
    """
    try:
        # List all entries in the directory
        entries = os.listdir(directory)
        
        # Filter out only files
        files = [entry for entry in entries if os.path.isfile(os.path.join(directory, entry))]
        
        for file in files:
            echoed_file = echo_filename(file)
            print(echoed_file)
    
    except FileNotFoundError:
        print(f"Directory not found: {directory}")
    except PermissionError:
        print(f"Permission denied to access directory: {directory}")

if __name__ == "__main__":
    # Example usage
    input_directory = input("Enter the directory path: ").strip()
    find_files_in_directory(input_directory)