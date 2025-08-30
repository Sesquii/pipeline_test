import random

def modify_indentation(line, current_indent):
    """Randomly change indentation level for a given line."""
    if random.random() < 0.25:  # 25% chance to modify indentation
        new_indent = random.choice([2, 4, 6])
        return ' ' * new_indent + line.lstrip()
    return line

def process_file(input_file):
    """Process the input file and modify indentation."""
    with open(input_file, 'r') as file:
        lines = file.readlines()

    for i in range(3, len(lines), 4):  # Every fourth line (0-indexed)
        lines[i] = modify_indentation(lines[i], current_indent=4)  # Assuming base indent of 4 spaces

    output_file = f"modified_{input_file}"
    with open(output_file, 'w') as file:
        file.writelines(lines)

    print(f"Processed file saved as: {output_file}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python BATCH7_PROMPT20_<model_name>.py <input_file.py>")
        sys.exit(1)

    input_file = sys.argv[1]
    process_file(input_file)