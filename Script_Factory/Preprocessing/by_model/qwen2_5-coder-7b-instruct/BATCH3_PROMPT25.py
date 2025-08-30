import os
import random
import re

# Define a list of comment templates that are either entirely unrelated to the code or absurdly detailed for simple lines.
COMMENT_TEMPLATES = [
    "This code is the most important part of the application.",  # Unrelated comment
    "The variable 'x' holds the number of apples in the basket.",  # Absurdly detailed comment
    "If this function returns False, it means everything is okay.",  # Unrelated comment
    "This loop increments the value of i by one each time.",  # Absurdly detailed comment
    "The array 'data' contains all user IDs from the database."  # Unrelated comment
]

def insert_comments(file_path):
    """
    Insert random comments into a Python script.
    
    Args:
    file_path (str): The path to the Python script.
    
    Returns:
    None
    """
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    commented_lines = []
    for line in lines:
        # Randomly decide whether to insert a comment before the current line
        if random.choice([True, False]):
            comment_template = random.choice(COMMENT_TEMPLATES)
            # Ensure the comment does not interfere with Python syntax
            if re.match(r'^\s*#', line):
                commented_lines.append(comment_template + '\n' + line)
            else:
                commented_lines.append(line[:2] + '#' + comment_template + ' ' + line[2:])
        else:
            commented_lines.append(line)
    
    with open(file_path, 'w') as file:
        file.writelines(commented_lines)

if __name__ == "__main__":
    if len(os.sys.argv) != 2:
        print("Usage: python BATCH3_PROMPT25_{{model_name}}.py <path_to_python_script>")
    else:
        script_path = os.sys.argv[1]
        if not os.path.exists(script_path):
            print(f"Error: The file {script_path} does not exist.")
        elif not script_path.endswith('.py'):
            print("Error: The provided file is not a Python script.")
        else:
            insert_comments(script_path)
            print(f"Comments inserted successfully into {script_path}.")