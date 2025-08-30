import random
import re

def generate_random_string(length=10):
    """Generate a random nonsensical string of specified length."""
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    return ''.join(random.choice(characters) for _ in range(length))

def remove_comments_and_replace(file_content):
    """Remove all comments from the file content and replace them with random strings."""
    # Remove single-line comments (// ...)
    no_single_line_comments = re.sub(r'//.*', lambda match: f"// {generate_random_string()}", file_content)

    # Remove multi-line comments (/* ... */)
    no_multi_line_comments = re.sub(
        r'/\*.*?\*/',
        lambda match: f"/* {generate_random_string()} */",
        no_single_line_comments,
        flags=re.DOTALL
    )

    return no_multi_line_comments

def process_file(input_filename, output_filename):
    """Process a file by removing comments and replacing them with random strings."""
    try:
        with open(input_filename, 'r') as file:
            content = file.read()

        modified_content = remove_comments_and_replace(content)

        with open(output_filename, 'w') as file:
            file.write(modified_content)

        print(f"Processed {input_filename} and saved to {output_filename}")
    except FileNotFoundError:
        print(f"Error: The file {input_filename} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    input_file = "input.py"
    output_file = "output.py"
    process_file(input_file, output_file)