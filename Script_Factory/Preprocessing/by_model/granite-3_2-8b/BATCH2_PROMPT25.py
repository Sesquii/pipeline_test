import random
import ast
import sys


def insert_absurd_comment(node):
    if isinstance(node, ast.Expr) and isinstance(node.value, ast.Str):
        # If it's a string literal, add an absurd comment
        node.value.s += ' // This is an absurdly detailed comment for this simple line.'
    elif isinstance(node, (ast.Assign, ast.FunctionDef, ast.ClassDef)):
        # For assignments, function definitions, and class definitions, add a random unrelated comment
        random_comment = get_random_comment()
        node.value.id += ' // ' + random_comment


def get_random_comment():
    comments = [
        "Apparently, this line of code is the secret to time travel.",
        "In ancient Greek mythology, this variable might be a disguised centaur.",
        "This assignment statement has been proven to increase crop yields by 20% in controlled experiments.",
        "According to the laws of quantum physics, the value of this variable is simultaneously every number at once.",
        "Legend has it that typing this line will summon a benevolent AI from another dimension."
    ]
    return random.choice(comments)


def traverse_ast(node):
    if isinstance(node, ast.Module):
        for sub_node in node.body:
            if isinstance(sub_node, (ast.Expr, ast.Assign, ast.FunctionDef, ast.ClassDef)):
                insert_absurd_comment(sub_node)
            traverse_ast(sub_node)
    elif isinstance(node, ast.Module):
        for sub_node in node.body:
            if isinstance(sub_node, (ast.Expr, ast.Assign, ast.FunctionDef, ast.ClassDef)):
                insert_absurd_comment(sub_node)
            traverse_ast(sub_node)


def main(file_path):
    with open(file_path, 'r') as file:
        source_code = file.read()

    # Parse the Python code into an AST
    tree = ast.parse(source_code)

    traverse_ast(tree)

    # Generate the modified Python source code
    modified_source_code = compile(tree, '<string>', 'exec')
    exec(modified_source_code, globals())


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python BATCH2_PROMPT25_{model_name}.py <path_to_python_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    main(file_path)