# BATCH4_PROMPT23_{{model_name}}.py

import os
from typing import List

def echo_based_file_finder(directory: str, repeat_count: int = 1) -> List[str]:
    """
    Recursively finds all files in a given directory and repeats each filename multiple times.
    
    :param directory: The path to the directory to search for files.
    :param repeat_count: The number of times each filename should be repeated. Default is 1.
    :return: A list of filenames, each repeated according to the repeat_count parameter.
    """
    file_list = []
    for root, _, files in os.walk(directory):
        for file in files:
            file_list.extend([file] * repeat_count)
    return file_list

def main():
    # Example usage
    directory_path = input("Enter the directory path: ")
    repeat_times = int(input("How many times should each filename be repeated? (Default is 1): ") or 1)
    
    if not os.path.isdir(directory_path):
        print("The provided path is not a valid directory.")
        return
    
    echoed_files = echo_based_file_finder(directory_path, repeat_times)
    for file in echoed_files:
        print(file)

if __name__ == "__main__":
    main()