import sys
import re


def replace_names(filename):
    with open(filename, 'r') as file:
        content = file.read()

    # Find all function names (including decorators)
    func_pattern = r'\b[A-Z][a-zA-Z0-9]*\b'
    func_matches = re.findall(func_pattern, content)

    # Replace each function name with a single letter
    for match in func_matches:
        new_name = 'f_' + str(len(set([m for m in func_matches if m != match])))
        content = re.sub(r'\b' + re.escape(match) + r'\b', new_name, content)

    # Find all variable names
    var_pattern = r'[a-zA-Z_][a-zA-Z0-9_]*'
    var_matches = re.findall(var_pattern, content)

    for match in var_matches:
        new_name = 'v_' + str(len(set([m for m in var_matches if m != match])))
        content = re.sub(r'\b' + re.escape(match) + r'\b', new_name, content)

    return content


def main():
    if len(sys.argv) != 2:
        print("Usage: python BATCH7_PROMPT19_{model_name}.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        new_content = replace_names(filename)

        with open(filename, 'w') as file:
            file.write(new_content)

        print(f"Names in '{filename}' have been sabotaged successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()