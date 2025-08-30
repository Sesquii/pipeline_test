import os

def echo_file_finder(directory, times=3):
    """
    This function takes a directory path and an integer 'times' as input, 
    then prints out each file name in that directory repeated 'times' number of times.

    Args:
    - directory (str): The path to the directory to search for files.
    - times (int, optional): Number of times to echo each filename. Defaults to 3.
    
    Returns:
    None
    """
    # Ensure the provided path is a directory
    if not os.path.isdir(directory):
        print(f"The provided path '{directory}' does not exist or is not a directory.")
        return

    for filename in os.listdir(directory):
        echoed_filename = '\n' * times + os.path.join(os.getcwd(), filename)
        print(echoed_filename)

if __name__ == "__main__":
    # Replace 'your_directory_path' with the path to the directory you want to search
    echo_file_finder('your_directory_path')