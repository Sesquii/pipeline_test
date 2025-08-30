import random
import re
import sys

# List of nonsensical words to use as replacements
NONSENSE_WORDS = [
    "flibber", "gabba", "gibber", "jabber", "mumble", "nonsense",
    "piffle", "poppycock", "prattle", "rambling", "titter", "twaddle"
]

def generate_nonsensical_string(length=10):
    """Generate a random nonsensical string of given length."""
    words = [random.choice(NONSENSE_WORDS) for _ in range(length // 5 + 1)]
    return ' '.join(words)

def replace_comments_and_docstrings(code):
    """Replace all comments and docstrings with nonsense strings."""

    # Replace multi-line docstrings ("""...""")
    def replace_docstring(match):
        return '""' + generate_nonsensical_string() + '""'

    # Pattern for matching triple-quoted docstrings
    docstring_pattern = re.compile(r'(""".*?""")', re.DOTALL)
    code = docstring_pattern.sub(replace_docstring, code)

    # Replace single-line comments (#...)
    def replace_comment(match):
        return '# ' + generate_nonsensical_string()

    comment_pattern = re.compile(r'(#.*)')
    code = comment_pattern.sub(replace_comment, code)

    return code

def main():
    if len(sys.argv) != 2:
        print("Usage: python BATCH7_PROMPT22_<model_name>.py <python_file>")
        sys.exit(1)

    input_file = sys.argv[1]

    try:
        with open(input_file, 'r') as file:
            code = file.read()

        modified_code = replace_comments_and_docstrings(code)

        output_file = f"sabotaged_{input_file}"
        with open(output_file, 'w') as file:
            file.write(modified_code)

        print(f"Sabotaged code saved to {output_file}")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

# ===== GENERATED TESTS =====
import pytest
from io import StringIO
import sys

# Original script code (repeated for clarity)
NONSENSE_WORDS = [
    "flibber", "gabba", "gibber", "jabber", "mumble", "nonsense",
    "piffle", "poppycock", "prattle", "rambling", "titter", "twaddle"
]

def generate_nonsensical_string(length=10):
    """Generate a random nonsensical string of given length."""
    words = [random.choice(NONSENSE_WORDS) for _ in range(length // 5 + 1)]
    return ' '.join(words)

def replace_comments_and_docstrings(code):
    """Replace all comments and docstrings with nonsense strings."""

    # Replace multi-line docstrings ("""...""")
    def replace_docstring(match):
        return '""' + generate_nonsensical_string() + '""'

    # Pattern for matching triple-quoted docstrings
    docstring_pattern = re.compile(r'(""".*?""")', re.DOTALL)
    code = docstring_pattern.sub(replace_docstring, code)

    # Replace single-line comments (#...)
    def replace_comment(match):
        return '# ' + generate_nonsensical_string()

    comment_pattern = re.compile(r'(#.*)')
    code = comment_pattern.sub(replace_comment, code)

    return code

def main():
    if len(sys.argv) != 2:
        print("Usage: python BATCH7_PROMPT22_<model_name>.py <python_file>")
        sys.exit(1)

    input_file = sys.argv[1]

    try:
        with open(input_file, 'r') as file:
            code = file.read()

        modified_code = replace_comments_and_docstrings(code)

        output_file = f"sabotaged_{input_file}"
        with open(output_file, 'w') as file:
            file.write(modified_code)

        print(f"Sabotaged code saved to {output_file}")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

# Test cases
def test_generate_nonsensical_string():
    """Test the generate_nonsensical_string function."""
    result = generate_nonsensical_string(20)
    assert isinstance(result, str)
    assert len(result.split()) > 4

def test_replace_comments_and_docstrings():
    """Test the replace_comments_and_docstrings function."""
    code = """
def example_function():
    \"\"\"
    This is a docstring.
    \"\"\"
    # This is a comment
    print("Hello, World!")
    """
    expected_output = re.sub(r'(""".*?""")', r'""' + generate_nonsensical_string() + '""', code)
    expected_output = re.sub(r'(#.*)', r'# ' + generate_nonsensical_string(), expected_output)
    result = replace_comments_and_docstrings(code)
    assert result == expected_output

def test_main_with_valid_file(monkeypatch, tmp_path):
    """Test the main function with a valid file."""
    input_file = tmp_path / "test.py"
    input_file.write_text("""
def example_function():
    \"\"\"
    This is a docstring.
    \"\"\"
    # This is a comment
    print("Hello, World!")
    """)
    
    monkeypatch.setattr(sys, 'argv', ['main.py', str(input_file)])
    output_file = tmp_path / "sabotaged_test.py"

    main()

    with open(output_file, 'r') as file:
        result_code = file.read()
    
    assert "# " + generate_nonsensical_string() in result_code
    assert '""' + generate_nonsensical_string() + '""' in result_code

def test_main_with_invalid_file(monkeypatch):
    """Test the main function with an invalid file."""
    monkeypatch.setattr(sys, 'argv', ['main.py', 'nonexistent_file.py'])
    
    with pytest.raises(SystemExit) as exc_info:
        main()
    
    assert exc_info.value.code == 1
