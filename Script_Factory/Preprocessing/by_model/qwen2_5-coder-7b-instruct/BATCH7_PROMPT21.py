import os
import random

# List of common libraries to choose from
COMMON_LIBRARIES = ['os', 'sys', 'math', 'random']

def insert_useless_imports(file_path):
    """
    Inserts 'import *' statements from a random library at the top of every 10th line in the given Python file.
    
    :param file_path: Path to the input Python file.
    """
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # Insert import statements at the top of every 10th line
    for i in range(9, len(lines), 10):
        library = random.choice(COMMON_LIBRARIES)
        lines.insert(i, f"import {library} as *\n")
    
    with open(file_path, 'w') as file:
        file.writelines(lines)

if __name__ == "__main__":
    input_file_path = 'input.py'  # Replace with the path to your Python file
    insert_useless_imports(input_file_path)
```

This script will take an input Python file and randomly insert `import *` statements from a list of common libraries at the top of every 10th line. The modified file will be saved back to the same location.