```python
import sys
import random

def swap_if_else(line):
    if 'if' in line and 'else' in line:
        # Determine if to swap with 30% probability
        if random.random() < 0.3:
            # Find positions of 'if' and 'else'
            if_pos = line.find('if ')
            else_pos = line.find('else ')
            # Extract blocks
            if_block = line[if_pos + 2:]
            else_block = line[else_pos + 4:]
            # Swap them
            new_line = line[:if_pos] + else_block + line[else_pos:] 
            return new_line
    return line

def modify_file(input_path, output_path):
    with open(input_path, 'r') as infile:
        lines = infile.readlines()
    
    modified_lines = []
    for i in range(len(lines)):
        line = lines[i].strip()
        if 'if' in line and 'else' in line:
            new_line = swap_if_else(line)
            modified_lines.append(new_line)
        else:
            modified_lines.append(line)
    
    with open(output_path, 'w') as outfile:
        outfile.writelines(modified_lines)

def main():
    if len(sys.argv) != 2:
        print("Usage: python code_style_saboteur.py <input_file>")
        return
    input_file = sys.argv[1]
    output_file = input_file + ".modified"
    modify_file(input_file, output_file)

if __name__ == "__main__":
    main()