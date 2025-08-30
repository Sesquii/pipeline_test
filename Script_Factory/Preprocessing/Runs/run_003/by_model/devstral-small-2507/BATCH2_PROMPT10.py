import re
import random
import sys

def add_pep8_violations(code):
    # Change indentation randomly between spaces and tabs
    lines = code.split('\n')
    for i in range(len(lines)):
        if re.match(r'^\s+', lines[i]):
            current_indent = re.match(r'^(\s+)', lines[i]).group(1)
            if random.choice([True, False]):
                # Convert spaces to tabs or vice versa
                if ' ' in current_indent:
                    new_indent = '\t'.join(['']*len(current_indent.strip()))
                else:
                    new_indent = ' '.join(['']*len(current_indent.strip()))
                lines[i] = re.sub(r'^(\s+)', new_indent, lines[i])

    # Change quotes randomly between single and double
    if random.choice([True, False]):
        code = code.replace('"', "'").replace("'", '"')

    # Change variable names to be non-descriptive
    variable_pattern = r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'
    variables = re.findall(variable_pattern, code)
    unique_vars = list(set(variables))
    random.shuffle(unique_vars)

    for var in unique_vars:
        if not re.match(r'^[A-Za-z_][A-Za-z0-9_]{1,3}$', var):  # Skip already short names
            replacement = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz_', k=3))
            code = re.sub(r'\b' + re.escape(var) + r'\b', replacement, code)

    return '\n'.join(lines), code

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python BATCH2_PROMPT10_Devstral.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    try:
        with open(input_file, 'r') as file:
            original_code = file.read()

        modified_indent_code, modified_var_code = add_pep8_violations(original_code)

        output_file = input_file.replace('.py', '_sabotaged.py')
        with open(output_file, 'w') as file:
            file.write(modified_var_code)

        print(f"PEP-8 violations added. Output saved to {output_file}")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)