#!/usr/bin/env python3

import os

def echo_file_finder(directory):
    """
    Function to print out filenames from a directory with an echo effect.

    Args:
        directory (str): The path to the directory.

    Returns:
        None
    """

    # Check if the given path is valid and accessible
    if not os.path.isdir(directory):
        print(f"The provided path '{directory}' does not exist or is not a directory.")
        return

    try:
        for filename in os.listdir(directory):
            echo_effect = '*' * (len(filename) + 1)  # Add one star to accommodate the star at the start
            print(f"{echo_effect}{filename}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python BATCH3_PROMPT23_Granite.py <directory>")
    else:
        directory = sys.argv[1]
        echo_file_finder(directory)