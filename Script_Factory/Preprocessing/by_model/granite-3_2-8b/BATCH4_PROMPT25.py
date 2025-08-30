import random
import ast
from io import StringIO

def add_random_comment(code):
    lines = code.splitlines()
    comments = [
        "# This is an unrelated comment about a penguin's ability to tap dance!",
        "# In this line, we're carefully initializing the variable 'x' with the value 10",
        "# It's crucial that the variable 'y' is increased by 5 in every single iteration of our loop.",
        "# A profound observation: the color blue might evoke feelings of tranquility in some cultures."
    ]
    
    for i, line in enumerate(lines):
        if random.random() > 0.8:  # Randomly decide whether to add a comment
            lines[i] = f"{line}\n{random.choice(comments)}"
    
    return "\n".join(lines)

def process_python_file(filepath):
    with open(filepath, 'r') as file:
        code = file.read()
    
    new_code = add_random_comment(code)

    # Parse the modified code back into an AST to ensure formatting is preserved
    tree = ast.parse(new_code)
    source = StringIO()
    ast.unparse(tree, source)
    new_code = source.getvalue().strip()  # Remove trailing newline
    
    return new_code

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python BATCH4_PROMPT25_{model_name}.py <path_to_python_file>")
        sys.exit(1)

    filepath = sys.argv[1]
    new_code = process_python_file(filepath)
    
    with open('output.py', 'w') as file:
        file.write(new_code)
    
    print(f"Comments added to {filepath}. Results saved in 'output.py'")