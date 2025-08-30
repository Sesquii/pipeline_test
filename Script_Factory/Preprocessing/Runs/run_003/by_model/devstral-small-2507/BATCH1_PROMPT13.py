import random
import ast
import re

def add_unhelpful_comments(code: str) -> str:
    # Parse the code into an AST for safe manipulation
    tree = ast.parse(code)

    # List of unhelpful comments
    comments = [
        "good stuff here",
        "fix maybe",
        "nice work",
        "interesting",
        "something clever",
        "needs improvement",
        "maybe useful",
        "what's this?",
        "random thought",
        "maybe later"
    ]

    # Helper function to insert comment at a node
    def insert_comment(node, comment):
        # Find the line number where this node starts
        lineno = node.lineno - 1  # Convert to 0-based index

        # Split the code into lines
        lines = code.split('\n')

        # Add comment on the line above (if not already a comment)
        if lineno < len(lines) and not lines[lineno].strip().startswith('#'):
            lines.insert(lineno, f'# {comment}')

        return '\n'.join(lines)

    # Randomly select some nodes to add comments to
    selected_nodes = random.sample(
        [node for node in ast.walk(tree) if isinstance(node, (ast.FunctionDef, ast.ClassDef, ast.For, ast.While, ast.If))],
        min(3, len([node for node in ast.walk(tree) if isinstance(node, (ast.FunctionDef, ast.ClassDef, ast.For, ast.While, ast.If))]))
    )

    # Insert comments at selected nodes
    modified_code = code
    for node in selected_nodes:
        comment = random.choice(comments)
        modified_code = insert_comment(node, comment)

    return modified_code

# Demo
if __name__ == "__main__":
    example_code = """
def greet(name):
    if name:
        print(f"Hello, {name}!")
    else:
        print("Hello, world!")

for i in range(5):
    greet(i)
"""

    commented_code = add_unhelpful_comments(example_code)
    print(commented_code)