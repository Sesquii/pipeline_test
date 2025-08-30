import sys
import random

def main():
    if len(sys.argv) != 2:
        print("Usage: python BATCH7_PROMPT21_{{model_name}}.py <input_file>")
        return
    
    input_file = sys.argv[1]
    
    # Read the input file into a list of lines
    with open(input_file, 'r') as f:
        original_lines = [line.strip() for line in f.readlines()]
    
    # List of common libraries to choose from
    libraries = ['os', 'sys', 'math', 'random', 'datetime']
    
    # Generate a random import line (always "import *")
    import_line = 'import *'
    selected_library = random.choice(libraries)
    
    # Create new lines list with the inserted import at every 10th position
    new_lines = []
    for i in range(len(original_lines)):
        if i % 10 == 0:
            new_lines.append(import_line)
        new_lines.append(original_lines[i])
    
    # Write the modified content back to the file
    with open(input_file, 'w') as f:
        for line in new_lines:
            f.write(line + '\n')

if __name__ == "__main__":
    main()

# ===== GENERATED TESTS =====
import pytest
from io import StringIO
import sys

# Original code
def main():
    if len(sys.argv) != 2:
        print("Usage: python BATCH7_PROMPT21_{{model_name}}.py <input_file>")
        return
    
    input_file = sys.argv[1]
    
    # Read the input file into a list of lines
    with open(input_file, 'r') as f:
        original_lines = [line.strip() for line in f.readlines()]
    
    # List of common libraries to choose from
    libraries = ['os', 'sys', 'math', 'random', 'datetime']
    
    # Generate a random import line (always "import *")
    import_line = 'import *'
    selected_library = random.choice(libraries)
    
    # Create new lines list with the inserted import at every 10th position
    new_lines = []
    for i in range(len(original_lines)):
        if i % 10 == 0:
            new_lines.append(import_line)
        new_lines.append(original_lines[i])
    
    # Write the modified content back to the file
    with open(input_file, 'w') as f:
        for line in new_lines:
            f.write(line + '\n')

if __name__ == "__main__":
    main()

# Test cases
def test_main_help(capsys):
    """Test that help message is printed when no arguments are provided."""
    sys.argv = ['script.py']
    with pytest.raises(SystemExit) as excinfo:
        main()
    assert excinfo.value.code == 0
    captured = capsys.readouterr()
    assert "Usage: python BATCH7_PROMPT21_{{model_name}}.py <input_file>" in captured.out

def test_main_valid_input(tmp_path):
    """Test that the script processes a valid input file correctly."""
    input_content = ["line1", "line2", "line3", "line4", "line5"]
    input_file = tmp_path / "test.txt"
    with open(input_file, 'w') as f:
        for line in input_content:
            f.write(line + '\n')
    
    sys.argv = ['script.py', str(input_file)]
    main()
    
    with open(input_file, 'r') as f:
        modified_lines = [line.strip() for line in f.readlines()]
    
    assert modified_lines[0] == "import *"
    assert modified_lines[1] == input_content[0]
    assert modified_lines[2] == "import *"
    assert modified_lines[3] == input_content[1]
    assert modified_lines[4] == "import *"
    assert modified_lines[5] == input_content[2]

def test_main_invalid_input(capsys):
    """Test that the script handles invalid input file correctly."""
    sys.argv = ['script.py', 'nonexistent_file.txt']
    with pytest.raises(SystemExit) as excinfo:
        main()
    assert excinfo.value.code != 0
    captured = capsys.readouterr()
    assert "No such file or directory" in captured.err

def test_main_no_input(capsys):
    """Test that the script handles no input arguments correctly."""
    sys.argv = ['script.py']
    with pytest.raises(SystemExit) as excinfo:
        main()
    assert excinfo.value.code != 0
    captured = capsys.readouterr()
    assert "No such file or directory" in captured.err

def test_main_multiple_imports(tmp_path):
    """Test that the script handles multiple imports correctly."""
    input_content = ["line1", "line2", "line3", "line4", "line5"]
    input_file = tmp_path / "test.txt"
    with open(input_file, 'w') as f:
        for line in input_content:
            f.write(line + '\n')
    
    sys.argv = ['script.py', str(input_file)]
    main()
    
    with open(input_file, 'r') as f:
        modified_lines = [line.strip() for line in f.readlines()]
    
    assert modified_lines[0] == "import *"
    assert modified_lines[1] == input_content[0]
    assert modified_lines[2] == "import *"
    assert modified_lines[3] == input_content[1]
    assert modified_lines[4] == "import *"
    assert modified_lines[5] == input_content[2]

def test_main_random_import(tmp_path):
    """Test that the script inserts a random import line correctly."""
    input_content = ["line1", "line2", "line3", "line4", "line5"]
    input_file = tmp_path / "test.txt"
    with open(input_file, 'w') as f:
        for line in input_content:
            f.write(line + '\n')
    
    sys.argv = ['script.py', str(input_file)]
    main()
    
    with open(input_file, 'r') as f:
        modified_lines = [line.strip() for line in f.readlines()]
    
    assert "import *" in modified_lines
    assert len(modified_lines) == 6

def test_main_no_import(tmp_path):
    """Test that the script does not insert an import line if it's already present."""
    input_content = ["import *", "line2", "line3", "line4", "line5"]
    input_file = tmp_path / "test.txt"
    with open(input_file, 'w') as f:
        for line in input_content:
            f.write(line + '\n')
    
    sys.argv = ['script.py', str(input_file)]
    main()
    
    with open(input_file, 'r') as f:
        modified_lines = [line.strip() for line in f.readlines()]
    
    assert modified_lines[0] == "import *"
    assert len(modified_lines) == 5
