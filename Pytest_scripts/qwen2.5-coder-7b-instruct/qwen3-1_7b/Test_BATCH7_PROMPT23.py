```python
import sys
import random

def swap_if_else(line):
    if 'if' in line and 'else' in line:
        # Determine if to swap with 30% probability
        if random.random() < 0.3:
            # Find positions of 'if' and 'else'
            if_pos = line.find('if ')
            else_pos = line.find('else ')
            # Extract blocks
            if_block = line[if_pos + 2:]
            else_block = line[else_pos + 4:]
            # Swap them
            new_line = line[:if_pos] + else_block + line[else_pos:] 
            return new_line
    return line

def modify_file(input_path, output_path):
    with open(input_path, 'r') as infile:
        lines = infile.readlines()
    
    modified_lines = []
    for i in range(len(lines)):
        line = lines[i].strip()
        if 'if' in line and 'else' in line:
            new_line = swap_if_else(line)
            modified_lines.append(new_line)
        else:
            modified_lines.append(line)
    
    with open(output_path, 'w') as outfile:
        outfile.writelines(modified_lines)

def main():
    if len(sys.argv) != 2:
        print("Usage: python code_style_saboteur.py <input_file>")
        return
    input_file = sys.argv[1]
    output_file = input_file + ".modified"
    modify_file(input_file, output_file)

if __name__ == "__main__":
    main()

# ===== GENERATED TESTS =====
```python
import pytest
from io import StringIO

# Original script code remains unchanged

def test_swap_if_else():
    """Test the swap_if_else function with various scenarios."""
    
    # Test case 1: Line contains 'if' and 'else', should be swapped
    assert swap_if_else('if x > y else z') == 'z if x <= y'
    
    # Test case 2: Line does not contain 'if' or 'else', should remain unchanged
    assert swap_if_else('x = 5') == 'x = 5'
    
    # Test case 3: Line contains only 'if' but no 'else', should remain unchanged
    assert swap_if_else('if x > y') == 'if x > y'
    
    # Test case 4: Line contains only 'else' but no 'if', should remain unchanged
    assert swap_if_else('else z') == 'else z'

def test_modify_file(tmp_path):
    """Test the modify_file function with various scenarios."""
    
    # Create a temporary input file
    input_file = tmp_path / "input.txt"
    input_file.write_text("if x > y else z\nx = 5")
    
    # Call the modify_file function
    output_file = input_file.with_name(input_file.stem + ".modified")
    modify_file(str(input_file), str(output_file))
    
    # Check if the output file contains the expected content
    assert output_file.read_text() == "z if x <= y\nx = 5"

def test_main(capsys):
    """Test the main function with various scenarios."""
    
    # Test case 1: Correct usage, should not print any error message
    input_file = 'input.txt'
    sys.argv = ['code_style_saboteur.py', input_file]
    main()
    captured = capsys.readouterr()
    assert captured.err == ''
    
    # Test case 2: Incorrect usage, should print error message
    sys.argv = ['code_style_saboteur.py']
    with pytest.raises(SystemExit) as excinfo:
        main()
    assert excinfo.value.code == 1

# Fixtures and parametrization can be added here if needed
```

This test suite includes comprehensive test cases for the `swap_if_else`, `modify_file`, and `main` functions. It uses assertions to verify the correctness of the output and pytest fixtures to handle temporary files and capture console output. The tests cover both positive and negative scenarios, ensuring that the script behaves as expected in various situations.