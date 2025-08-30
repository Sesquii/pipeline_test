"""
BATCH7_PROMPT24_{{model_name}}.py

This script implements a "Code Style Saboteur" that reorders function definitions within a Python file.
"""

import ast
import random
import sys

def find_function_definitions(file_content):
    """
    Parses the Python code and finds all function definitions.

    :param file_content: The content of the Python file as a string.
    :return: A list of AST nodes representing function definitions.
    """
    tree = ast.parse(file_content)
    return [node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]

def reorder_function_definitions(function_definitions):
    """
    Reorders the given list of function definitions randomly.

    :param function_definitions: A list of AST nodes representing function definitions.
    :return: A new list with the function definitions reordered.
    """
    random.shuffle(function_definitions)
    return function_definitions

def reinsert_function_definitions(file_content, reordered_functions):
    """
    Reinserts the reordered function definitions into the original file content.

    :param file_content: The content of the Python file as a string.
    :param reordered_functions: A list of AST nodes representing reordered function definitions.
    :return: The modified file content with reordered functions.
    """
    tree = ast.parse(file_content)
    function_nodes = find_function_definitions(file_content)
    
    for func_node, new_func_node in zip(function_nodes, reordered_functions):
        idx = tree.body.index(func_node)
        tree.body[idx] = new_func_node
    
    return ast.unparse(tree)

def main():
    if len(sys.argv) != 2:
        print("Usage: python BATCH7_PROMPT24_{{model_name}}.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    
    try:
        with open(input_file, 'r') as file:
            content = file.read()
        
        functions = find_function_definitions(content)
        if not functions:
            print("No function definitions found in the file.")
            return
        
        reordered_functions = reorder_function_definitions(functions)
        new_content = reinsert_function_definitions(content, reordered_functions)
        
        with open(input_file, 'w') as file:
            file.write(new_content)
        
        print(f"Function definitions have been reordered and saved back to {input_file}.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()