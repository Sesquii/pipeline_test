import random

UNHELPFUL_COMMENTS = [
    "good stuff here",
    "fix maybe",
    "nice work",
    "this is a good place",
    "maybe not needed",
    "keep it simple",
    "refactor this",
    "what was I thinking?",
    "why did I write this?",
    "delete me if you don't need me"
]

def add_unhelpful_comments(code: str) -> str:
    tree = ast.parse(code)
    visitor = CommentInsertionVisitor()
    visitor.visit(tree)
    return ast.unparse(tree)

class CommentInsertionVisitor(ast.NodeTransformer):
    def generic_visit(self, node):
        super().generic_visit(node)
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
            self.insert_comment_before_node(node)
        else:
            self.insert_comment_after_node(node)
        return node

    def insert_comment_before_node(self, node):
        comment = f'# {random.choice(UNHELPFUL_COMMENTS)}'
        new_node = ast.Expr(value=ast.Str(s=comment))
        node.body.insert(0, new_node)

    def insert_comment_after_node(self, node):
        if not isinstance(node, (ast.Module, ast.Expr)):
            comment = f'# {random.choice(UNHELPFUL_COMMENTS)}'
            new_node = ast.Expr(value=ast.Str(s=comment))
            node.body.append(new_node)

if __name__ == "__main__":
    example_code = """
def add(a, b):
    return a + b

result = add(3, 5)
print(result)
"""
    commented_code = add_unhelpful_comments(example_code)
    print(commented_code)

# ===== GENERATED TESTS =====
```python
import pytest
from ast import parse, Module
from typing import List

# Original script code remains unchanged

# Test suite for the provided Python script

def test_add_unhelpful_comments():
    """Test the add_unhelpful_comments function with a simple example."""
    example_code = """
def add(a, b):
    return a + b

result = add(3, 5)
print(result)
"""
    commented_code = add_unhelpful_comments(example_code)
    assert isinstance(commented_code, str)

def test_comment_insertion_visitor():
    """Test the CommentInsertionVisitor class with various node types."""
    # Test function definition
    code = """
def my_function():
    pass
"""
    tree = parse(code)
    visitor = CommentInsertionVisitor()
    new_tree = visitor.visit(tree)
    assert isinstance(new_tree, Module)
    assert len(new_tree.body) == 2

    # Test class definition
    code = """
class MyClass:
    pass
"""
    tree = parse(code)
    visitor = CommentInsertionVisitor()
    new_tree = visitor.visit(tree)
    assert isinstance(new_tree, Module)
    assert len(new_tree.body) == 2

def test_insert_comment_before_node():
    """Test the insert_comment_before_node method."""
    code = """
def my_function():
    pass
"""
    tree = parse(code)
    visitor = CommentInsertionVisitor()
    new_tree = visitor.visit(tree)
    assert isinstance(new_tree, Module)
    assert len(new_tree.body) == 2

def test_insert_comment_after_node():
    """Test the insert_comment_after_node method."""
    code = """
def my_function():
    pass
"""
    tree = parse(code)
    visitor = CommentInsertionVisitor()
    new_tree = visitor.visit(tree)
    assert isinstance(new_tree, Module)
    assert len(new_tree.body) == 2

# Test cases for negative scenarios
def test_add_unhelpful_comments_empty_code():
    """Test the add_unhelpful_comments function with an empty string."""
    example_code = ""
    commented_code = add_unhelpful_comments(example_code)
    assert isinstance(commented_code, str)

def test_comment_insertion_visitor_no_nodes():
    """Test the CommentInsertionVisitor class with no nodes."""
    code = ""
    tree = parse(code)
    visitor = CommentInsertionVisitor()
    new_tree = visitor.visit(tree)
    assert isinstance(new_tree, Module)
    assert len(new_tree.body) == 0

# Test cases for edge scenarios
def test_add_unhelpful_comments_single_line_code():
    """Test the add_unhelpful_comments function with a single line of code."""
    example_code = "print('Hello, World!')"
    commented_code = add_unhelpful_comments(example_code)
    assert isinstance(commented_code, str)

# Test cases for parametrization
@pytest.mark.parametrize("input_code, expected_length", [
    ("def my_function():\n    pass", 2),
    ("class MyClass:\n    pass", 2),
    ("print('Hello, World!')", 1)
])
def test_comment_insertion_visitor_parametrized(input_code: str, expected_length: int):
    """Test the CommentInsertionVisitor class with parametrized input."""
    tree = parse(input_code)
    visitor = CommentInsertionVisitor()
    new_tree = visitor.visit(tree)
    assert isinstance(new_tree, Module)
    assert len(new_tree.body) == expected_length

# Test cases for fixtures
@pytest.fixture
def sample_code():
    """Fixture to provide a sample code snippet."""
    return """
def my_function():
    pass
"""

def test_comment_insertion_visitor_with_fixture(sample_code: str):
    """Test the CommentInsertionVisitor class with a fixture."""
    tree = parse(sample_code)
    visitor = CommentInsertionVisitor()
    new_tree = visitor.visit(tree)
    assert isinstance(new_tree, Module)
    assert len(new_tree.body) == 2
```