import re
import random
import sys

def add_pep8_violations(code):
    # Change indentation randomly between spaces and tabs
    lines = code.split('\n')
    for i in range(len(lines)):
        if re.match(r'^\s+', lines[i]):
            current_indent = re.match(r'^(\s+)', lines[i]).group(1)
            if random.choice([True, False]):
                # Convert spaces to tabs or vice versa
                if ' ' in current_indent:
                    new_indent = '\t'.join(['']*len(current_indent.strip()))
                else:
                    new_indent = ' '.join(['']*len(current_indent.strip()))
                lines[i] = re.sub(r'^(\s+)', new_indent, lines[i])

    # Change quotes randomly between single and double
    if random.choice([True, False]):
        code = code.replace('"', "'").replace("'", '"')

    # Change variable names to be non-descriptive
    variable_pattern = r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'
    variables = re.findall(variable_pattern, code)
    unique_vars = list(set(variables))
    random.shuffle(unique_vars)

    for var in unique_vars:
        if not re.match(r'^[A-Za-z_][A-Za-z0-9_]{1,3}$', var):  # Skip already short names
            replacement = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz_', k=3))
            code = re.sub(r'\b' + re.escape(var) + r'\b', replacement, code)

    return '\n'.join(lines), code

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python BATCH2_PROMPT10_Devstral.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    try:
        with open(input_file, 'r') as file:
            original_code = file.read()

        modified_indent_code, modified_var_code = add_pep8_violations(original_code)

        output_file = input_file.replace('.py', '_sabotaged.py')
        with open(output_file, 'w') as file:
            file.write(modified_var_code)

        print(f"PEP-8 violations added. Output saved to {output_file}")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

# ===== GENERATED TESTS =====
import pytest
from typing import Tuple

# Original code remains unchanged for testing purposes

def test_add_pep8_violations():
    """Test the add_pep8_violations function with various inputs."""
    
    # Test case 1: Basic Python code with indentation and quotes
    input_code = "def hello_world():\n    print('Hello, World!')"
    expected_output = re.sub(r'^(\s+)', '\t'.join(['']*len(input_code.split('\n')[0].strip())), input_code)
    modified_code, _ = add_pep8_violations(input_code)
    
    assert modified_code != input_code
    assert modified_code == expected_output
    
    # Test case 2: Code with non-descriptive variable names
    input_code = "def calculate_sum(a, b):\n    return a + b"
    expected_output = re.sub(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', ''.join(random.choices('abcdefghijklmnopqrstuvwxyz_', k=3)), input_code)
    modified_code, _ = add_pep8_violations(input_code)
    
    assert modified_code != input_code
    assert all(not re.match(r'^[A-Za-z_][A-Za-z0-9_]{1,3}$', var) for var in re.findall(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', modified_code))
    
    # Test case 3: Code with mixed indentation
    input_code = "def test_function():\n\tprint('This is a test')"
    expected_output = re.sub(r'^(\s+)', '\t'.join(['']*len(input_code.split('\n')[0].strip())), input_code)
    modified_code, _ = add_pep8_violations(input_code)
    
    assert modified_code != input_code
    assert modified_code == expected_output
    
    # Test case 4: Code with single quotes
    input_code = "def test_quotes():\n    print('Single quotes')"
    expected_output = re.sub(r"'", '"', input_code)
    modified_code, _ = add_pep8_violations(input_code)
    
    assert modified_code != input_code
    assert modified_code == expected_output
    
    # Test case 5: Code with tabs
    input_code = "def test_tabs():\n\tprint('Tabs')"
    expected_output = re.sub(r'^(\s+)', ' '*len(input_code.split('\n')[0].strip()), input_code)
    modified_code, _ = add_pep8_violations(input_code)
    
    assert modified_code != input_code
    assert modified_code == expected_output

def test_add_pep8_violations_with_empty_input():
    """Test the add_pep8_violations function with an empty string."""
    input_code = ""
    modified_code, _ = add_pep8_violations(input_code)
    
    assert modified_code == input_code
    
def test_add_pep8_violations_with_invalid_input_type():
    """Test the add_pep8_violations function with an invalid input type."""
    with pytest.raises(TypeError):
        add_pep8_violations(123)

# Add more test cases as needed

This test suite includes comprehensive test cases for the `add_pep8_violations` function, covering various scenarios such as indentation, quotes, and variable names. It also tests edge cases like empty input and invalid input type. The test cases are designed to ensure that the function behaves correctly under different conditions.