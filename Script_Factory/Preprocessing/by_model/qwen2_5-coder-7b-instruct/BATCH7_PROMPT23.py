import random

def swap_if_else_blocks(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    modified_lines = []
    in_if_block = False
    if_block_content = []
    else_block_content = []

    for line in lines:
        stripped_line = line.strip()
        if stripped_line.startswith('if'):
            in_if_block = True
            if_block_content.append(line)
        elif stripped_line.startswith('else'):
            in_if_block = False
            else_block_content.append(line)
        elif not stripped_line or stripped_line.isspace():
            if in_if_block:
                if random.random() < 0.3:
                    modified_lines.extend(else_block_content + if_block_content)
                else:
                    modified_lines.extend(if_block_content + else_block_content)
                if_block_content = []
                else_block_content = []
        elif in_if_block:
            if_block_content.append(line)
        else:
            else_block_content.append(line)

    # Handle the last block if file doesn't end with an empty line
    if in_if_block:
        if random.random() < 0.3:
            modified_lines.extend(else_block_content + if_block_content)
        else:
            modified_lines.extend(if_block_content + else_block_content)
    else:
        modified_lines.extend(if_block_content + else_block_content)

    with open(file_path, 'w') as file:
        file.writelines(modified_lines)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python BATCH7_PROMPT23_{{model_name}}.py <python_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    swap_if_else_blocks(input_file)
```

This Python script, `BATCH7_PROMPT23_{{model_name}}.py`, takes a Python file as input and introduces a logical bug by swapping the contents of `if` and `else` blocks with a 30% chance. The program reads the file line by line, identifies `if` and `else` blocks, and randomly decides whether to swap their contents. The modified lines are then written back to the same file.