import random
import re
import ast

def add_unhelpful_comments(code: str) -> str:
    # Define a list of unhelpful comment templates
    comments = [
        "good stuff here",
        "fix maybe",
        "nice work",
        "check this out",
        "do your thing",
        "leave as is",
        "don't touch"
    ]

    # Parse the code into an abstract syntax tree (AST)
    tree = ast.parse(code)

    # Define a function to add comments at random positions in the AST
    def add_comment(node):
        if isinstance(node, ast.FunctionDef):
            comment_node = ast.Expr(value=ast.Str(s=random.choice(comments)))
            node.body.insert(0, comment_node)  # Insert before first statement
        elif isinstance(node, (ast.For, ast.While)):
            comment_node = ast.Expr(value=ast.Str(s=random.choice(comments)))
            node.body.insert(0, comment_node)  # Insert at the start of loop body
        elif isinstance(node, ast.If):
            comment_node = ast.Expr(value=ast.Str(s=random.choice(comments)))
            node.body.insert(0, comment_node)  # Insert before first statement in if-clause
        elif isinstance(node, ast.With):
            comment_node = ast.Expr(value=ast.Str(s=random.choice(comments)))
            node.body.insert(0, comment_node)  # Insert at the start of with-block

    # Traverse the AST and add comments
    ast.walk(tree, add_comment)

    # Convert the modified AST back to code
    modified_code = compile(tree, '<string>', 'exec')
    return re.sub(r'(\n\s*)+', '\g<1>', str(modified_code))

if __name__ == "__main__":
    example_code = """
def greet(name: str) -> None:
    print(f"Hello, {name}!")

    for i in range(5):
        if i % 2 == 0:
            continue

        print(i)

    with open('file.txt', 'w') as file:
        file.write("Some text.")
    """

    modified_code = add_unhelpful_comments(example_code)
    print(modified_code)