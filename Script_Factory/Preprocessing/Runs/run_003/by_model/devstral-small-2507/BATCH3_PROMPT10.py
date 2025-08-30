import random
import re

def add_pep8_violations(content):
    # Randomly change indentation between 2 and 4 spaces
    lines = content.split('\n')
    new_lines = []
    for line in lines:
        if re.match(r'^\s*', line):
            spaces = random.choice([2, 4])
            new_line = re.sub(r'^(\s*)', lambda m: m.group(1) + (' ' * (spaces - len(m.group(1)))), line)
            new_lines.append(new_line)
        else:
            new_lines.append(line)

    # Randomly change quotes
    content = '\n'.join(new_lines)
    if random.choice([True, False]):
        content = re.sub(r'"', "'", content)

    # Change variable names to be non-descriptive (simple example)
    var_pattern = re.compile(r'\b(a|b|c|x|y|z)\b')
    def replace_var(match):
        return random.choice(['var1', 'tmp', 'val', 'item'])

    content = var_pattern.sub(replace_var, content)

    # Add extra spaces around operators
    operators = ['+', '-', '*', '/', '=', '<', '>', '==']
    for op in operators:
        content = re.sub(r'(\s)' + re.escape(op) + r'(\s)', r' ' + op + r' ', content)

    return content

def main():
    import sys
    if len(sys.argv) != 2:
        print("Usage: python BATCH3_PROMPT10_Devstral.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    try:
        with open(input_file, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)

    modified_content = add_pep8_violations(content)

    output_file = input_file.replace('.py', '_sabotaged.py')
    with open(output_file, 'w') as f:
        f.write(modified_content)

    print(f"PEP-8 violations added. Output saved to '{output_file}'")

if __name__ == "__main__":
    main()