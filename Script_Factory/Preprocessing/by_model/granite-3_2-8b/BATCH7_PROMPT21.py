import os
import random
import sys


def add_useless_imports(file_path):
    """
    Adds a useless 'import *' statement to the specified Python file.

    Args:
        file_path (str): Path to the Python file.
    """
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # List of common libraries from which to import randomly
    libs = ['os', 'sys', 'math']

    # Modify the file content
    for i in range(0, len(lines), 10):
        if i + 1 < len(lines):
            lib_index = random.randint(0, len(libs) - 1)
            lines[i] = f"# {libs[lib_index]} import\n"

    # Write the modified content back to the file
    with open(file_path, 'w') as file:
        file.writelines(lines)


def main():
    """
    Entry point of the program. Expects a Python file path as command line argument.
    """
    if len(sys.argv) != 2:
        print("Usage: python BATCH7_PROMPT21_{model_name}.py <python_file_path>")
        return

    file_path = sys.argv[1]

    try:
        add_useless_imports(file_path)
        print(f"Useless imports added to {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()