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

# ===== GENERATED TESTS =====
```python
import pytest

# Original code
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

# Test cases
@pytest.fixture
def example_code():
    return """
def greet(name):
    if name:
        print(f"Hello, {name}!")
    else:
        print("Hello, world!")

for i in range(5):
    greet(i)
"""

@pytest.fixture
def comments():
    return [
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

def test_add_unhelpful_comments(example_code, comments):
    """Test the add_unhelpful_comments function with a sample code."""
    modified_code = add_unhelpful_comments(example_code)
    
    # Check if the modified code contains at least one comment
    assert any(line.startswith('#') for line in modified_code.split('\n'))
    
    # Check if all comments are from the list of unhelpful comments
    found_comments = [line.strip().lstrip('#').strip() for line in modified_code.split('\n') if line.startswith('#')]
    assert all(comment in comments for comment in found_comments)

def test_add_unhelpful_comments_no_nodes(example_code):
    """Test the add_unhelpful_comments function with a code that has no nodes to add comments to."""
    empty_code = """
def empty():
    pass
"""
    modified_code = add_unhelpful_comments(empty_code)
    
    # Check if the modified code is the same as the original code
    assert modified_code == empty_code

def test_add_unhelpful_comments_random_selection(example_code, comments):
    """Test the random selection of nodes to add comments to."""
    modified_code = add_unhelpful_comments(example_code)
    
    # Check if exactly 3 nodes are selected (or less if there are fewer than 3 nodes)
    selected_nodes_count = sum(1 for line in modified_code.split('\n') if line.startswith('#'))
    assert 0 <= selected_nodes_count <= 3

def test_add_unhelpful_comments_no_comments(example_code):
    """Test the add_unhelpful_comments function with a code that already has comments."""
    commented_code = """
# This is a comment
def greet(name):
    if name:
        print(f"Hello, {name}!")
    else:
        print("Hello, world!")

for i in range(5):
    greet(i)
"""
    modified_code = add_unhelpful_comments(commented_code)
    
    # Check if the modified code is the same as the original code
    assert modified_code == commented_code

def test_add_unhelpful_comments_empty_string():
    """Test the add_unhelpful_comments function with an empty string."""
    empty_string = ""
    modified_code = add_unhelpful_comments(empty_string)
    
    # Check if the modified code is the same as the original code
    assert modified_code == empty_string

def test_add_unhelpful_comments_none():
    """Test the add_unhelpful_comments function with None."""
    none_value = None
    with pytest.raises(TypeError):
        add_unhelpful_comments(none_value)
```