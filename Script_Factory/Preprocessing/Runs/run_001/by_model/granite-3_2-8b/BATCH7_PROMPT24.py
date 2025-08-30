import random
import ast
import os

def randomize_function_order(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        source_code = file.read()

    tree = ast.parse(source_code)

    # Find all function definitions in the code
    functions = [node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]

    random.shuffle(functions)

    # Reconstruct the source code with randomized function order
    new_functions = []
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    current_index = 0
    for line in lines:
        if isinstance(ast.parse(line).body[0], ast.FunctionDef):
            new_functions.append(line)
            current_index += 1

        if current_index < len(functions):
            new_functions.append(str(functions[current_index]))

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(''.join(new_functions))

def main():
    import sys

    if len(sys.argv) != 2:
        print("Usage: python BATCH7_PROMPT24_{model_name}.py <python_file>")
        sys.exit(1)

    file_path = sys.argv[1]

    if not os.path.isfile(file_path):
        print(f"File '{file_path}' does not exist.")
        sys.exit(1)

    randomize_function_order(file_path)
    print(f"Randomized function order in: {file_path}")

if __name__ == "__main__":
    main()