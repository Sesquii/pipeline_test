import random

def add_random_comments(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    new_lines = []
    for line in lines:
        if "def" in line or "for" in line or "while" in line or "if" in line:
            # Insert a comment before the code line
            comment = generate_random_comment()
            new_lines.append(comment + "\n")
        new_lines.append(line)

    with open(file_path, 'w') as file:
        file.writelines(new_lines)

def generate_random_comment():
    unrelated_comments = [
        "This is a completely unrelated comment.",
        "The sky is blue, the grass is green, and everything is awesome!",
        "Why are you reading this comment? It's not important at all.",
        "I have no idea what I'm doing, but it works!",
        "Look at this code, it's so beautiful."
    ]

    absurdly_detailed_comments = [
        "# This loop iterates 10 times and prints numbers from 1 to 10",
        "# The function takes a list of integers and returns the sum",
        "# This if statement checks if the variable is greater than zero"
    ]

    comment_type = random.choice([unrelated_comments, absurdly_detailed_comments])
    return random.choice(comment_type)

if __name__ == "__main__":
    input_file_path = "input_script.py"  # Replace with your Python script file path
    add_random_comments(input_file_path)

# ===== GENERATED TESTS =====
import pytest
from io import StringIO
import sys

# Original code remains unchanged

def test_add_random_comments(tmpdir):
    # Create a temporary file with some Python code
    input_file_path = tmpdir.join("input_script.py")
    input_file_path.write(
        """
def add_numbers(a, b):
    return a + b

for i in range(5):
    print(i)
"""
    )

    # Call the function to add random comments
    add_random_comments(input_file_path)

    # Read the modified file and check for comments
    with open(input_file_path, 'r') as file:
        lines = file.readlines()

    assert any("This is a completely unrelated comment." in line or "The sky is blue" in line for line in lines)
    assert any("# This loop iterates 10 times and prints numbers from 1 to 10" in line for line in lines)

def test_generate_random_comment():
    # Test the generate_random_comment function
    comments = generate_random_comment()
    assert isinstance(comments, str)
    assert "def" not in comments
    assert "for" not in comments
    assert "while" not in comments
    assert "if" not in comments

def test_add_random_comments_no_code(tmpdir):
    # Create a temporary file with no Python code
    input_file_path = tmpdir.join("input_script.py")
    input_file_path.write(
        """
This is just some plain text.
"""
    )

    # Call the function to add random comments
    add_random_comments(input_file_path)

    # Read the modified file and check for comments
    with open(input_file_path, 'r') as file:
        lines = file.readlines()

    assert any("This is a completely unrelated comment." in line or "The sky is blue" in line for line in lines)
    assert not any("# This loop iterates 10 times and prints numbers from 1 to 10" in line for line in lines)

def test_add_random_comments_empty_file(tmpdir):
    # Create a temporary empty file
    input_file_path = tmpdir.join("input_script.py")
    input_file_path.write("")

    # Call the function to add random comments
    add_random_comments(input_file_path)

    # Read the modified file and check for comments
    with open(input_file_path, 'r') as file:
        lines = file.readlines()

    assert not any(line.strip() for line in lines)
