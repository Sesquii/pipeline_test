import random
import sys
import ast


def swap_if_else(tree):
    """Swap if and else branches of an If node."""
    if isinstance(tree, ast.If):
        tree.orelse, tree.body = tree.body, tree.orelse
        return tree
    return None


def traverse(node):
    """Traverse AST nodes and swap if-else blocks."""
    if hasattr(node, 'body') and isinstance(node.body, list) and len(node.body) > 1:
        for i in range(len(node.body)):
            if isinstance(node.body[i], ast.If):
                node.body[i] = swap_if_else(node.body[i])
    for child in node.body:
        if child:
            traverse(child)


def modify_file(file_path):
    """Read file, parse into AST, modify, and write back."""
    with open(file_path, 'r') as f:
        tree = ast.parse(f.read())

    traverse(tree)

    modified_code = compile(tree, file_path, 'exec')
    exec(modified_code, {'__builtins__': None}, {})  # Prevent accessing builtins directly

    with open(file_path, 'w') as f:
        f.write(modified_code)


def main():
    """Entry point."""
    if len(sys.argv) != 2:
        print("Usage: python BATCH7_PROMPT23_{model_name}.py <python_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    modify_file(file_path)


if __name__ == "__main__":
    main()