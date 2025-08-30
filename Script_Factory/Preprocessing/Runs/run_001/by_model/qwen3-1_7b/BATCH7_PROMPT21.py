```python
import sys
import random

def main():
    if len(sys.argv) != 2:
        print("Usage: python BATCH7_PROMPT21_{{model_name}}.py <input_file>")
        return
    
    input_file = sys.argv[1]
    
    # Read the input file into a list of lines
    with open(input_file, 'r') as f:
        original_lines = [line.strip() for line in f.readlines()]
    
    # List of common libraries to choose from
    libraries = ['os', 'sys', 'math', 'random', 'datetime']
    
    # Generate a random import line (always "import *")
    import_line = 'import *'
    selected_library = random.choice(libraries)
    
    # Create new lines list with the inserted import at every 10th position
    new_lines = []
    for i in range(len(original_lines)):
        if i % 10 == 0:
            new_lines.append(import_line)
        new_lines.append(original_lines[i])
    
    # Write the modified content back to the file
    with open(input_file, 'w') as f:
        for line in new_lines:
            f.write(line + '\n')

if __name__ == "__main__":
    main()