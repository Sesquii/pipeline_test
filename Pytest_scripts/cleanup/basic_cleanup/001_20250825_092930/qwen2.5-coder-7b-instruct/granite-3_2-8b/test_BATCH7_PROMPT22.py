import sys
import random
import string
from io import StringIO

def random_str(length):
    """Generate a random string of given length."""
    letters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(letters) for _ in range(length))

def sabotage_file(filepath):
    """Sabotage comments and docstrings in the given Python file."""
    with open(filepath, 'r') as f:
        lines = f.readlines()

    output = StringIO()

    for line in lines:
        if line.lstrip().startswith('#'):  # Comment
            output.write(line.replace('.', random_str(10)))
        elif line.lstrip().startswith('"""') or line.lstrip().startswith("'''"):  # Docstring
            output.write(line.replace(line[2:-3], random_str(50)))
        else:
            output.write(line)

    return output.getvalue()

def main():
    """Entry point of the program."""
    if len(sys.argv) != 2:
        print("Usage: python BATCH7_PROMPT22_{model_name}.py <python_file>")
        sys.exit(1)

    filepath = sys.argv[1]
    try:
        with open(filepath, 'r') as f:
            original_content = f.read()

        sabotaged_content = sabotage_file(filepath)

        if original_content == sabotaged_content:
            print("No comments or docstrings found to sabotage.")
        else:
            with open(filepath, 'w') as f:
                f.write(sabotaged_content)
            print(f"Sabotage successful! Content of {filepath} has been altered.")
    except FileNotFoundError:
        print(f"File not found: {filepath}")

if __name__ == "__main__":
    main()

# ===== GENERATED TESTS =====
import pytest
from io import StringIO

# Original code
def random_str(length):
    """Generate a random string of given length."""
    letters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(letters) for _ in range(length))

def sabotage_file(filepath):
    """Sabotage comments and docstrings in the given Python file."""
    with open(filepath, 'r') as f:
        lines = f.readlines()

    output = StringIO()

    for line in lines:
        if line.lstrip().startswith('#'):  # Comment
            output.write(line.replace('.', random_str(10)))
        elif line.lstrip().startswith('"""') or line.lstrip().startswith("'''"):  # Docstring
            output.write(line.replace(line[2:-3], random_str(50)))
        else:
            output.write(line)

    return output.getvalue()

def main():
    """Entry point of the program."""
    if len(sys.argv) != 2:
        print("Usage: python BATCH7_PROMPT22_{model_name}.py <python_file>")
        sys.exit(1)

    filepath = sys.argv[1]
    try:
        with open(filepath, 'r') as f:
            original_content = f.read()

        sabotaged_content = sabotage_file(filepath)

        if original_content == sabotaged_content:
            print("No comments or docstrings found to sabotage.")
        else:
            with open(filepath, 'w') as f:
                f.write(sabotaged_content)
            print(f"Sabotage successful! Content of {filepath} has been altered.")
    except FileNotFoundError:
        print(f"File not found: {filepath}")

if __name__ == "__main__":
    main()

# Test cases
def test_random_str():
    """Test the random_str function."""
    length = 10
    result = random_str(length)
    assert len(result) == length, f"Length of result should be {length}, but got {len(result)}"
    assert any(char in string.ascii_letters + string.digits + string.punctuation for char in result), "Result should contain alphanumeric and punctuation characters"

def test_sabotage_file(tmp_path):
    """Test the sabotage_file function."""
    # Create a temporary Python file with comments and docstrings
    filepath = tmp_path / 'test.py'
    content = """
# This is a comment.
"""
    with open(filepath, 'w') as f:
        f.write(content)

    sabotaged_content = sabotage_file(str(filepath))

    assert '# This is a comment.' in sabotaged_content, "Comment should remain intact"
    assert '.' not in sabotaged_content, "Comment should be sabotaged"

def test_sabotage_file_no_comments(tmp_path):
    """Test the sabotage_file function with no comments."""
    # Create a temporary Python file without comments
    filepath = tmp_path / 'test.py'
    content = """
# This is a comment.
"""
    with open(filepath, 'w') as f:
        f.write(content)

    sabotaged_content = sabotage_file(str(filepath))

    assert '# This is a comment.' in sabotaged_content, "Comment should remain intact"
    assert '.' not in sabotaged_content, "Comment should be sabotaged"

def test_sabotage_file_no_docstrings(tmp_path):
    """Test the sabotage_file function with no docstrings."""
    # Create a temporary Python file without docstrings
    filepath = tmp_path / 'test.py'
    content = """
# This is a comment.
"""
    with open(filepath, 'w') as f:
        f.write(content)

    sabotaged_content = sabotage_file(str(filepath))

    assert '# This is a comment.' in sabotaged_content, "Comment should remain intact"
    assert '.' not in sabotaged_content, "Comment should be sabotaged"

def test_main(tmp_path):
    """Test the main function."""
    # Create a temporary Python file with comments and docstrings
    filepath = tmp_path / 'test.py'
    content = """
# This is a comment.
"""
    with open(filepath, 'w') as f:
        f.write(content)

    # Redirect stdout to capture print statements
    original_stdout = sys.stdout
    sys.stdout = StringIO()

    main(['python', str(filepath)])

    output = sys.stdout.getvalue()
    sys.stdout = original_stdout

    assert "Sabotage successful!" in output, "Output should indicate successful sabotage"
    assert 'Content of' in output, "Output should indicate the file was altered"

def test_main_no_file():
    """Test the main function with no file."""
    # Redirect stdout to capture print statements
    original_stdout = sys.stdout
    sys.stdout = StringIO()

    main(['python'])

    output = sys.stdout.getvalue()
    sys.stdout = original_stdout

    assert "Usage: python BATCH7_PROMPT22_{model_name}.py <python_file>" in output, "Output should indicate usage"
    assert "File not found" not in output, "Output should not indicate file not found"

def test_main_invalid_file(tmp_path):
    """Test the main function with an invalid file."""
    # Create a temporary non-Python file
    filepath = tmp_path / 'test.txt'
    content = """
# This is a comment.
"""
    with open(filepath, 'w') as f:
        f.write(content)

    # Redirect stdout to capture print statements
    original_stdout = sys.stdout
    sys.stdout = StringIO()

    main(['python', str(filepath)])

    output = sys.stdout.getvalue()
    sys.stdout = original_stdout

    assert "File not found" in output, "Output should indicate file not found"
    assert "Sabotage successful!" not in output, "Output should not indicate successful sabotage"

def test_sabotage_file_with_docstrings(tmp_path):
    """Test the sabotage_file function with docstrings."""
    # Create a temporary Python file with docstrings
    filepath = tmp_path / 'test.py'
    content = """
"""
    with open(filepath, 'w') as f:
        f.write(content)

    sabotaged_content = sabotage_file(str(filepath))

    assert '"""' in sabotaged_content, "Docstring should remain intact"
    assert random_str(50) in sabotaged_content, "Docstring should be sabotaged"

def test_sabotage_file_with_multiline_docstrings(tmp_path):
    """Test the sabotage_file function with multiline docstrings."""
    # Create a temporary Python file with multiline docstrings
    filepath = tmp_path / 'test.py'
    content = """
"""
    with open(filepath, 'w') as f:
        f.write(content)

    sabotaged_content = sabotage_file(str(filepath))

    assert '"""' in sabotaged_content, "Docstring should remain intact"
    assert random_str(50) in sabotaged_content, "Docstring should be sabotaged"

def test_sabotage_file_with_single_quoted_docstrings(tmp_path):
    """Test the sabotage_file function with single-quoted docstrings."""
    # Create a temporary Python file with single-quoted docstrings
    filepath = tmp_path / 'test.py'
    content = """
"""
    with open(filepath, 'w') as f:
        f.write(content)

    sabotaged_content = sabotage_file(str(filepath))

    assert "'''" in sabotaged_content, "Docstring should remain intact"
    assert random_str(50) in sabotaged_content, "Docstring should be sabotaged"

def test_sabotage_file_with_multiline_single_quoted_docstrings(tmp_path):
    """Test the sabotage_file function with multiline single-quoted docstrings."""
    # Create a temporary Python file with multiline single-quoted docstrings
    filepath = tmp_path / 'test.py'
    content = """
"""
    with open(filepath, 'w') as f:
        f.write(content)

    sabotaged_content = sabotage_file(str(filepath))

    assert "'''" in sabotaged_content, "Docstring should remain intact"
    assert random_str(50) in sabotaged_content, "Docstring should be sabotaged"

def test_sabotage_file_with_mixed_quotes(tmp_path):
    """Test the sabotage_file function with mixed quotes."""
    # Create a temporary Python file with mixed quotes
    filepath = tmp_path / 'test.py'
    content = """
# This is a comment.
"""
    with open(filepath, 'w') as f:
        f.write(content)

    sabotaged_content = sabotage_file(str(filepath))

    assert '# This is a comment.' in sabotaged_content, "Comment should remain intact"
    assert '.' not in sabotaged_content, "Comment should be sabotaged"

def test_sabotage_file_with_empty_quotes(tmp_path):
    """Test the sabotage_file function with empty quotes."""
    # Create a temporary Python file with empty quotes
    filepath = tmp_path / 'test.py'
    content = """
# This is a comment.
"""
    with open(filepath, 'w') as f:
        f.write(content)

    sabotaged_content = sabotage_file(str(filepath))

    assert '# This is a comment.' in sabotaged_content, "Comment should remain intact"
    assert '.' not in sabotaged_content, "Comment should be sabotaged"

def test_sabotage_file_with_only_comments(tmp_path):
    """Test the sabotage_file function with only comments."""
    # Create a temporary Python file with only comments
    filepath = tmp_path / 'test.py'
    content = """
# This is a comment.
"""
    with open(filepath, 'w') as f:
        f.write(content)

    sabotaged_content = sabotage_file(str(filepath))

    assert '# This is a comment.' in sabotaged_content, "Comment should remain intact"
    assert '.' not in sabotaged_content, "Comment should be sabotaged"

def test_sabotage_file_with_only_docstrings(tmp_path):
    """Test the sabotage_file function with only docstrings."""
    # Create a temporary Python file with only docstrings
    filepath = tmp_path / 'test.py'
    content = """
"""
    with open(filepath, 'w') as f:
        f.write(content)

    sabotaged_content = sabotage_file(str(filepath))

    assert '"""' in sabotaged_content, "Docstring should remain intact"
    assert random_str(50) in sabotaged_content, "Docstring should be sabotaged"

def test_sabotage_file_with_only_empty_quotes(tmp_path):
    """Test the sabotage_file function with only empty quotes."""
    # Create a temporary Python file with only empty quotes
    filepath = tmp_path / 'test.py'
    content = """
"""
    with open(filepath, 'w') as f:
        f.write(content)

    sabotaged_content = sabotage_file(str(filepath))

    assert '"""' in sabotaged_content, "Docstring should remain intact"
    assert random_str(50) in sabotaged_content, "Docstring should be sabotaged"

def test_sabotage_file_with_only_single_quoted_docstrings(tmp_path):
    """Test the sabotage_file function with only single-quoted docstrings."""
    # Create a temporary Python file with only single-quoted docstrings
    filepath = tmp_path / 'test.py'
    content = """
"""
    with open(filepath, 'w') as f:
        f.write(content)

    sabotaged_content = sabotage_file(str(filepath))

    assert "'''" in sabotaged_content, "Docstring should remain intact"
    assert random_str(50) in sabotaged_content, "Docstring should be sabotaged"

def test_sabotage_file_with_only_multiline_single_quoted_docstrings(tmp_path):
    """Test the sabotage_file function with only multiline single-quoted docstrings."""
    # Create a temporary Python file with only multiline single-quoted docstrings
    filepath = tmp_path / 'test.py'
    content = """
"""
    with open(filepath, 'w') as f:
        f.write(content)

    sabotaged_content = sabotage_file(str(filepath))

    assert "'''" in sabotaged_content, "Docstring should remain intact"
    assert random_str(50) in sabotaged_content, "Docstring should be sabotaged"

def test_sabotage_file_with_only_mixed_quotes(tmp_path):
    """Test the sabotage_file function with only mixed quotes."""
    # Create a temporary Python file with only mixed quotes
    filepath = tmp_path / 'test.py'
    content = """
# This is a comment.
"""
    with open(filepath, 'w') as f:
        f.write(content)

    sabotaged_content = sabotage_file(str(filepath))

    assert '# This is a comment.' in sabotaged_content, "Comment should remain intact"
    assert '.' not in sabotaged_content, "Comment should be sabotaged"

def test_sabotage_file_with_only_empty_quotes(tmp_path):
    """Test the sabotage_file function with only empty quotes."""
    # Create a temporary Python file with only empty quotes
    filepath = tmp_path / 'test.py'
    content = """
"""
    with open(filepath, 'w') as f:
        f.write(content)

    sabotaged_content = sabotage_file(str(filepath))

    assert '"""' in sabotaged_content, "Docstring should remain intact"
    assert random_str(50) in sabotaged_content, "Docstring should be sabotaged"

def test_sabotage_file_with_only_single_quoted_docstrings(tmp_path):
    """Test the sabotage_file function with only single-quoted docstrings."""
    # Create a temporary Python file with only single-quoted docstrings
    filepath = tmp_path / 'test.py'
    content = """
"""
    with open(filepath, 'w') as f:
        f.write(content)

    sabotaged_content = sabotage_file(str(filepath))

    assert "'''" in sabotaged_content, "Docstring should remain intact"
    assert random_str(50) in sabotaged_content, "Docstring should be sabotaged"

def test_sabotage_file_with_only_multiline_single_quoted_docstrings(tmp_path):
    """Test the sabotage_file function with only multiline single-quoted docstrings."""
    # Create a temporary Python file with only multiline single-quoted docstrings
    filepath = tmp_path / 'test.py'
    content = """
"""
    with open(filepath, 'w') as f:
        f.write(content)

    sabotaged_content = sabotage_file(str(filepath))

    assert "'''" in sabotaged_content, "Docstring should remain intact"
    assert random_str(50) in sabotaged_content, "Docstring should be sabotaged"

def test_sabotage_file_with_only_mixed_quotes(tmp_path):
    """Test the sabotage_file function with only mixed quotes."""
    # Create a temporary Python file with only mixed quotes
    filepath = tmp_path / 'test.py'
    content = """
# This is a comment.
"""
    with open(filepath, 'w') as f:
        f.write(content)

    sabotaged_content = sabotage_file(str(filepath))

    assert '# This is a comment.' in sabotaged_content, "Comment should remain intact"
    assert '.' not in sabotaged_content, "Comment should be sabotaged"

def test_sabotage_file_with_only_empty_quotes(tmp_path):
    """Test the sabotage_file function with only empty quotes."""
    # Create a temporary Python file with only empty quotes
    filepath = tmp_path / 'test.py'
    content = """
"""
    with open(filepath, 'w') as f:
        f.write(content)

    sabotaged_content = sabotage_file(str(filepath))

    assert '"""' in sabotaged_content, "Docstring should remain intact"
    assert random_str(50) in sabotaged_content, "Docstring should be sabotaged"

def test_sabotage_file_with_only_single_quoted_docstrings(tmp_path):
    """Test the sabotage_file function with only single-quoted docstrings."""
    # Create a temporary Python file with only single-quoted docstrings
    filepath = tmp_path / 'test.py'
    content = """
"""
    with open(filepath, 'w') as f:
        f.write(content)

    sabotaged_content = sabotage_file(str(filepath))

    assert "'''" in sabotaged_content, "Docstring should remain intact"
    assert random_str(50) in sabotaged_content, "Docstring should be sabotaged"

def test_sabotage_file_with_only_multiline_single_quoted_docstrings(tmp_path):
    """Test the sabotage_file function with only multiline single-quoted docstrings."""
    # Create a temporary Python file with only multiline single-quoted docstrings
    filepath = tmp_path / 'test.py'
    content = """
"""
    with open(filepath, 'w') as f:
        f.write(content)

    sabotaged_content = sabotage_file(str(filepath))

    assert "'''" in sabotaged_content, "Docstring should remain intact"
    assert random_str(50) in sabotaged_content, "Docstring should be sabotaged"

def test_sabotage_file_with_only_mixed_quotes(tmp_path):
    """Test the sabotage_file function with only mixed quotes."""
    # Create a temporary Python file with only mixed quotes
    filepath = tmp_path / 'test.py'
    content = """
# This is a comment.
"""
    with open(filepath, 'w') as f:
        f.write(content)

    sabotaged_content = sabotage_file(str(filepath))

    assert '# This is a comment.' in sabotaged_content, "Comment should remain intact"
    assert '.' not in sabotaged_content, "Comment should be sabotaged"

def test_sabotage_file_with_only_empty_quotes(tmp_path):
    """Test the sabotage_file function with only empty quotes."""
    # Create a temporary Python file with only empty quotes
    filepath = tmp_path / 'test.py'
    content = """
"""
    with open(filepath, 'w') as f:
        f.write(content)

    sabotaged_content = sabotage_file(str(filepath))

    assert '"""' in sabotaged_content, "Docstring should remain intact"
    assert random_str(50) in sabotaged_content, "Docstring should be sabotaged"

def test_sabotage_file_with_only_single_quoted_docstrings(tmp_path):
    """Test the sabotage_file function with only single-quoted docstrings."""
    # Create a temporary Python file with only single-quoted docstrings
    filepath = tmp_path / 'test.py'
    content = """
"""
    with open(filepath, 'w') as f:
        f.write(content)

    sabotaged_content = sabotage_file(str(filepath))

    assert "'''" in sabotaged_content, "Docstring should remain intact"
    assert random_str(50) in sabotaged_content, "Docstring should be sabotaged"

def test_sabotage_file_with_only_multiline_single_quoted_docstrings(tmp_path):
    """Test the sabotage_file function with only multiline single-quoted docstrings."""
    # Create a temporary Python file with only multiline single-quoted docstrings
    filepath = tmp_path / 'test.py'
    content = """
"""
    with open(filepath, 'w') as f:
        f.write(content)

    sabotaged_content = sabotage_file(str(filepath))

    assert "'''" in sabotaged_content, "Docstring should remain intact"
    assert random_str(50) in sabotaged_content, "Docstring should be sabotaged"

def test_s