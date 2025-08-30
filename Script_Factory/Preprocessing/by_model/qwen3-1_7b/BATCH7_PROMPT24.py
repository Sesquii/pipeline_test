```python
import sys
from random import shuffle

def main():
    # Read the input Python file and split into lines
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

    # Separate non-function lines from function definitions
    non_func_lines = []
    func_lines = []

    for line in lines:
        stripped_line = line.strip()
        if stripped_line.startswith('def'):
            func_lines.append(line)
        else:
            non_func_lines.append(line)

    # Shuffle the list of function definitions to randomize their order
    shuffle(func_lines)

    # Reconstruct the code with shuffled functions
    new_code = []
    for line in non_func_lines:
        new_code.append(line)
    for line in func_lines:
        new_code.append(line)

    # Write the modified code back to the original file
    with open(sys.argv[1], 'w') as f:
        f.writelines(new_code)

if __name__ == "__main__":
    main()