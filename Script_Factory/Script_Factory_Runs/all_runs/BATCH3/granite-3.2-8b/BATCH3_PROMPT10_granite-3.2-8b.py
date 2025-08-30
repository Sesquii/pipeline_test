#!/usr/bin/env python3
import os
import sys
import random
from pathlib import Path

def sabotage_file(file_path: str) -> None:
    """
    This function takes a Python file as input and adds PEP-8 violations.

    The violations include:
    - Randomly changing single quotes to double quotes or vice versa
    - Introducing inconsistent indentation (spaces/tabs, 2/4 spaces)
    - Renaming variables to non-descriptive names

    :param file_path: Path to the Python file to sabotage.
    """

    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Randomly change quotes
    for i in range(len(lines)):
        if "''" in lines[i] or ''' in lines[i]:
            lines[i] = lines[i].replace('"', "'").replace("'''", "'''")
            lines[i] = lines[i].replace("'''", "'''")

    # Randomly introduce inconsistent indentation
    for i in range(len(lines)):
        if lines[i].strip():  # Don't touch empty lines
            line_indent = len(lines[i]) - len(lines[i].lstrip())
            if random.choice([True, False]):
                if not lines[i].startswith('    '):
                    lines[i] = '    ' + lines[i]
            else:
                if lines[i].startswith('    '):
                    lines[i] = lines[i][4:]

    # Randomly rename variables
    with open(file_path, 'r', encoding='utf-8') as f:
        file_content = f.read()
    
    import ast
    tree = ast.parse(file_content)

    for node in ast.walk(tree):
        if isinstance(node, (ast.Name, ast.Attribute)):
            new_name = ''.join(random.choices('a-zA-Z0-9', k=random.randint(1, 20)))
            while any(new_name == old_name for old_name in [n.id for n in ast.walk(tree) if isinstance(n, (ast.Name, ast.Attribute))]):
                new_name = ''.join(random.choices('a-zA-Z0-9', k=random.randint(1, 20)))
            node.id = new_name

    sabotaged_content = ast.unparse(tree)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(sabotaged_content)

def main():
    if len(sys.argv) != 2:
        print("Usage: python BATCH3_PROMPT10_{model_name}.py <path_to_python_file>")
        sys.exit(1)

    file_path = Path(sys.argv[1])
    
    if not file_path.is_file() or not str(file_path).lower().endswith('.py'):
        print("Invalid file path or not a Python file.")
        sys.exit(1)

    sabotage_file(str(file_path))
    print(f"Sabotaged: {file_path}")

if __name__ == "__main__":
    main()