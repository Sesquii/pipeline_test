import os
import sys

def traverse_and_modify(directory):
    """Traverse through a directory and modify Python files."""

    # Walk through the directory
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)

                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Replace double quotes with single quotes and remove trailing commas
                content = content.replace('"', "'").strip().rstrip(',')

                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)

    print(f"Modified files in {directory}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python BATCH7_PROMPT18_{model_name}.py <path_to_directory>")
        sys.exit(1)

    directory = sys.argv[1]

    if not os.path.isdir(directory):
        print("The provided path is not a valid directory.")
        sys.exit(1)

    traverse_and_modify(directory)