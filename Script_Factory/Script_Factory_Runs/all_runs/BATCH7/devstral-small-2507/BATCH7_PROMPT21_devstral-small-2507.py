import random
import sys

def insert_useless_imports(file_path):
    # List of common libraries to import from
    libraries = ['os', 'sys', 'math']

    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
    
        modified_lines = []
        for i, line in enumerate(lines):
            if i % 10 == 0 and i != 0:  # Every 10th line (starting from the second)
                library = random.choice(libraries)
                useless_import = f"from {library} import *\n"
                modified_lines.append(useless_import)
            
            modified_lines.append(line)
    
        with open(file_path, 'w') as file:
            file.writelines(modified_lines)

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python BATCH7_PROMPT21_Devstral.py <python_file>")
    else:
        file_path = sys.argv[1]
        insert_useless_imports(file_path)