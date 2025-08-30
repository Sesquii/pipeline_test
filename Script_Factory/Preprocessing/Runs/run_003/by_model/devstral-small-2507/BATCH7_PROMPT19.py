import ast
import sys

class CodeStyleSaboteur:
    def __init__(self):
        self.variable_counter = 0
        self.function_counter = 0

    def rename_node(self, node):
        # Rename function and variable names to single-letter names
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            new_name = chr(97 + self.function_counter % 26)  # a-z
            self.function_counter += 1
            node.name = new_name

        elif isinstance(node, ast.Name):
            if isinstance(node.ctx, ast.Store):  # Variable assignment
                new_name = chr(97 + self.variable_counter % 26)  # a-z
                self.variable_counter += 1
                node.id = new_name

        return node

    def transform_code(self, code):
        tree = ast.parse(code)
        for node in ast.walk(tree):
            self.rename_node(node)

        return ast.unparse(tree)

def main():
    if len(sys.argv) != 2:
        print("Usage: python BATCH7_PROMPT19_<model_name>.py <input_file.py>")
        sys.exit(1)

    input_file = sys.argv[1]

    try:
        with open(input_file, 'r') as file:
            original_code = file.read()

        saboteur = CodeStyleSaboteur()
        transformed_code = saboteur.transform_code(original_code)

        print("Transformed code:")
        print(transformed_code)

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()