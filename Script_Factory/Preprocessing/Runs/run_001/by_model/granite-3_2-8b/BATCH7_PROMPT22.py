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