import os
import re

def replace_quotes_and_remove_trailing_commas(file_path):
    """
    Replace all double-quotes with single-quotes and remove trailing commas 
    from function calls and list definitions in the given file.
    """
    with open(file_path, 'r') as file:
        content = file.read()

    # Replace double quotes with single quotes
    content = content.replace('"', "'")

    # Remove trailing commas from function calls and list definitions
    # This regex matches trailing commas in various contexts
    content = re.sub(r',\s*([)\]}])', r'\1', content)
    content = re.sub(r',\s*(?=[^\w\s]))', '', content)

    with open(file_path, 'w') as file:
        file.write(content)

def traverse_directory(directory):
    """
    Recursively traverse the given directory and apply style changes to Python files.
    """
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                replace_quotes_and_remove_trailing_commas(file_path)

if __name__ == "__main__":
    # Get the directory to process from command line arguments
    import sys
    if len(sys.argv) != 2:
        print("Usage: python BATCH7_PROMPT18_{{model_name}}.py <directory>")
        sys.exit(1)

    directory = sys.argv[1]
    traverse_directory(directory)