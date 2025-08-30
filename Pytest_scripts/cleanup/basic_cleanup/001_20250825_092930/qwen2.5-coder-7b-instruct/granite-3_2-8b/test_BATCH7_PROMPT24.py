import random
import ast
import os

def randomize_function_order(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        source_code = file.read()

    tree = ast.parse(source_code)

    # Find all function definitions in the code
    functions = [node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]

    random.shuffle(functions)

    # Reconstruct the source code with randomized function order
    new_functions = []
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    current_index = 0
    for line in lines:
        if isinstance(ast.parse(line).body[0], ast.FunctionDef):
            new_functions.append(line)
            current_index += 1

        if current_index < len(functions):
            new_functions.append(str(functions[current_index]))

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(''.join(new_functions))

def main():
    import sys

    if len(sys.argv) != 2:
        print("Usage: python BATCH7_PROMPT24_{model_name}.py <python_file>")
        sys.exit(1)

    file_path = sys.argv[1]

    if not os.path.isfile(file_path):
        print(f"File '{file_path}' does not exist.")
        sys.exit(1)

    randomize_function_order(file_path)
    print(f"Randomized function order in: {file_path}")

if __name__ == "__main__":
    main()

# ===== GENERATED TESTS =====
import pytest
from pathlib import Path

# Original code remains unchanged

def test_randomize_function_order(tmp_path):
    """Test the randomize_function_order function."""
    # Create a temporary Python file with some functions
    temp_file = tmp_path / "temp.py"
    temp_file.write_text(
        """
def function1():
    print("Function 1")

def function2():
    print("Function 2")

def function3():
    print("Function 3")
"""
    )

    # Call the function to randomize the order of functions
    randomize_function_order(str(temp_file))

    # Read the content of the file after shuffling
    with open(str(temp_file), 'r', encoding='utf-8') as file:
        shuffled_code = file.read()

    # Check if all original functions are present in the shuffled code
    assert "def function1" in shuffled_code
    assert "def function2" in shuffled_code
    assert "def function3" in shuffled_code

    # Check if the order of functions has changed
    lines = shuffled_code.split('\n')
    first_function = None
    second_function = None
    third_function = None
    for line in lines:
        if "def function1" in line:
            first_function = True
        elif "def function2" in line:
            second_function = True
        elif "def function3" in line:
            third_function = True

    assert not (first_function and second_function and third_function)

def test_randomize_function_order_nonexistent_file(tmp_path):
    """Test the randomize_function_order function with a non-existent file."""
    temp_file = tmp_path / "nonexistent.py"

    with pytest.raises(SystemExit) as exc_info:
        randomize_function_order(str(temp_file))

    assert exc_info.value.code == 1

def test_randomize_function_order_no_arguments():
    """Test the main function without arguments."""
    with pytest.raises(SystemExit) as exc_info:
        main()

    assert exc_info.value.code == 1

def test_randomize_function_order_invalid_argument(tmp_path):
    """Test the main function with an invalid argument."""
    temp_file = tmp_path / "temp.py"
    temp_file.write_text("")

    with pytest.raises(SystemExit) as exc_info:
        main(["python", str(temp_file)])

    assert exc_info.value.code == 1

def test_randomize_function_order_valid_argument(tmp_path):
    """Test the main function with a valid argument."""
    temp_file = tmp_path / "temp.py"
    temp_file.write_text(
        """
def function1():
    print("Function 1")

def function2():
    print("Function 2")
"""
    )

    main(["python", str(temp_file)])

    # Check if the file has been modified
    with open(str(temp_file), 'r', encoding='utf-8') as file:
        shuffled_code = file.read()

    assert "function1" in shuffled_code
    assert "function2" in shuffled_code

# Add more test cases as needed
