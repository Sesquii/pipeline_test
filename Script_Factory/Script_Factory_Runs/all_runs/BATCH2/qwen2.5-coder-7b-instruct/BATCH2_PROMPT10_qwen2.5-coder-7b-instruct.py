import argparse
import os
import random

def add_indentation_violations(code):
    lines = code.split('\n')
    new_lines = []
    for line in lines:
        indent_level = len(line) - len(line.lstrip())
        if indent_level > 0 and random.choice([True, False]):
            new_line = ' ' * (indent_level + random.randint(1, 4)) + line.strip()
        else:
            new_line = line
        new_lines.append(new_line)
    return '\n'.join(new_lines)

def replace_quotes(code):
    code = code.replace("'", '"')
    code = code.replace('"', "'")
    return code

def change_variable_names(code):
    variable_names = [name for name in dir() if not name.startswith('__')]
    new_code = code
    for old_name, old_value in zip(variable_names[:-1], variable_names[1:]):
        new_code = new_code.replace(old_name, old_value)
    return new_code

def main():
    parser = argparse.ArgumentParser(description='Code Style Saboteur')
    parser.add_argument('input_file', type=str, help='Path to the input Python file')
    args = parser.parse_args()

    if not os.path.isfile(args.input_file):
        print(f"Error: {args.input_file} is not a valid file.")
        return

    with open(args.input_file, 'r') as file:
        code = file.read()

    modified_code = add_indentation_violations(code)
    modified_code = replace_quotes(modified_code)
    modified_code = change_variable_names(modified_code)

    with open(f"{args.input_file}_sabotaged.py", 'w') as file:
        file.write(modified_code)

if __name__ == "__main__":
    main()