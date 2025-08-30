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