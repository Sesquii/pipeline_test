# BATCH2_PROMPT23_{{model_name}}.py

import os

def echo_based_file_finder(directory, repeat_count):
    """
    This function takes a directory path and an integer repeat_count as input.
    It prints each file in the directory repeated 'repeat_count' times.
    
    Args:
    directory (str): The path to the directory to search for files.
    repeat_count (int): The number of times each filename should be repeated.
    """
    try:
        # Check if the provided directory exists
        if not os.path.exists(directory) or not os.path.isdir(directory):
            print("The provided path is not a valid directory.")
            return
        
        # List all files in the directory
        files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
        
        # Print each file repeated 'repeat_count' times
        for file in files:
            print((file + '\n') * repeat_count)
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    import argparse
    
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Echo-Based File Finder")
    parser.add_argument("directory", type=str, help="The directory to search for files.")
    parser.add_argument("repeat_count", type=int, help="Number of times each filename should be repeated.")
    
    args = parser.parse_args()
    
    # Call the function with provided arguments
    echo_based_file_finder(args.directory, args.repeat_count)