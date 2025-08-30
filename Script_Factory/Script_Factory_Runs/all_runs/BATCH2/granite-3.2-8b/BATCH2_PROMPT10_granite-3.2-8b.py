import sys
from random import choice

def sabotage_code(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    modifications = [
        ('add_extra_whitespace', '  '),
        ('change_quotes', ("'", '"')),
        ('swap_var_names', {'old': 'new'}),
    ]

    sabotaged_lines = []
    for line in lines:
        for mod, args in modifications:
            if choice([True, False]):  # Randomly apply each modification
                line = eval(f"modify_{mod}(line, {args})")

        sabotaged_lines.append(line)

    with open(file_path, 'w') as file:
        file.writelines(sabotaged_lines)


def modify_add_extra_whitespace(line, whitespace):
    return line + whitespace


def modify_change_quotes(line, quotes):
    old_quote, new_quote = quotes
    return line.replace('"', old_quote).replace("'", new_quote)


def modify_swap_var_names(line, var_dict):
    for old_name, new_name in var_dict.items():
        line = line.replace(old_name, new_name)
    return line


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python BATCH2_PROMPT10_{model_name}.py <path_to_python_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    sabotage_code(file_path)