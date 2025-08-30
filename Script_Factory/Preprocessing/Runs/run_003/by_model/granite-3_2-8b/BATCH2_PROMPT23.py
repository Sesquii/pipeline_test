# BATCH2_PROMPT23_Granite.py

import os
import sys
from random import randint

def echo_find_files(directory):
    """
    This function lists files in a given directory with an 'echo' effect,
    repeating each filename multiple times at random intervals.

    :param directory: The directory to search for files.
    """
    # Get list of all entries in the provided directory
    entries = os.listdir(directory)

    # Filter out directories and only keep files
    files = [f for f in entries if os.path.isfile(os.path.join(directory, f))]
    
    for file_name in files:
        print("\n" + '*'*30)  # Separator line

        # Simulate echo effect by randomly repeating the filename multiple times
        for _ in range(randint(1, 5)):  # Randomly repeat between 1 to 5 times
            print(file_name)
        
        print('\n' + '*'*30)  # Separator line

def main():
    """Entry point of the script."""
    if len(sys.argv) != 2:
        print("Usage: python BATCH2_PROMPT23_Granite.py <directory>")
        sys.exit(1)

    directory = sys.argv[1]

    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory.")
        sys.exit(1)

    echo_find_files(directory)

if __name__ == "__main__":
    main()