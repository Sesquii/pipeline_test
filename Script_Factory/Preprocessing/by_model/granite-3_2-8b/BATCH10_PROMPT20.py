import re
import random
import string

def replace_comments(code):
    """Replace comments with random nonsensical strings."""
    comment_pattern = r'(#.*)$|^(\s*)//'  # Matches both line comments and block comments
    non_comment_lines = re.split(comment_pattern, code)[::2]  # Keep only non-comment lines

    # Generate a random string for each comment
    nonsensical_strings = [''.join(random.choices(string.ascii_letters + string.digits, k=10)) for _ in range(len(re.findall(comment_pattern, code))))

    result = ''
    line_num = 0
    for line in non_comment_lines:
        if comment_pattern.match(line):
            result += nonsensical_strings[line_num] + '\n'
        else:
            result += line + '\n'
        line_num += 1

    return result

def main():
    """Read a Python file, replace comments with random strings, and print the modified code."""
    import sys

    if len(sys.argv) != 2:
        print("Usage: python BATCH10_PROMPT20_{model_name}.py <file_path>")
        return

    file_path = sys.argv[1]

    try:
        with open(file_path, 'r') as file:
            code = file.read()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return

    modified_code = replace_comments(code)
    print(modified_code)

if __name__ == "__main__":
    main()