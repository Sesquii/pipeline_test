import random
import re
import sys

def find_function_definitions(code):
    """Extract all function definitions from the given code."""
    # Regular expression to match Python function definitions
    pattern = r'def\s+[\w_]\w*\s*\([^)]*\)\s*:.*?(?=\n\n|\Z)'  # Matches a single function definition including its body until empty line or end of file
    return re.findall(pattern, code, re.DOTALL)

def insert_functions_back(code, functions):
    """Insert the list of functions back into the original code."""
    
    # Regular expression to match between class/function definitions and other code blocks
    pattern = r'def\s+[\w_]\w*\s*\([^)]*\)\s*:.*?(?=\n\n|\Z)'  # Matches a single function definition including its body until empty line or end of file
    
    # Find the insertion point (usually after imports, before main code execution)
    insert_pos = re.search(pattern, code).start()
    
    # Insert the randomly ordered functions back into the original code
    new_code = code[:insert_pos] + '\n\n'.join(functions) + code[insert_pos:]

    return new_code

def main(input_file):
    """Main function to reorder function definitions in a Python file."""
    with open(input_file, 'r') as f:
        original_code = f.read()

    # Find all function definitions
    functions = find_function_definitions(original_code)

    if not functions:
        print("No function definitions found in the input file.")
        return

    # Randomly reorder the functions
    random.shuffle(functions)

    # Insert the randomly ordered functions back into the code
    modified_code = insert_functions_back(original_code, functions)

    output_file = f'BATCH7_PROMPT24_{input_file}'
    with open(output_file, 'w') as f:
        f.write(modified_code)

    print(f"Modified code saved to {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python BATCH7_PROMPT24.py <input_python_file>")
    else:
        main(sys.argv[1])