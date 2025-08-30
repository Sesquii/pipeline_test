import os

def process_python_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Replace double-quotes with single-quotes
    content = content.replace('"', "'")
    
    # Remove trailing commas from function calls and list definitions
    lines = content.split('\n')
    for i in range(len(lines)):
        line = lines[i]
        if ',' in line:
            if line.strip().endswith(','):
                line = line.rstrip(',') + '\n'
                lines[i] = line
    
    new_content = ''.join(lines)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_content)

def traverse_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                process_python_file(file_path)

if __name__ == "__main__":
    # Specify the directory containing your Python project
    project_directory = 'path_to_your_project'
    
    traverse_directory(project_directory)
```

This script defines a `process_python_file` function that reads a Python file, replaces double-quotes with single-quotes, and removes trailing commas from function calls and list definitions. It then writes the modified content back to the file. The `traverse_directory` function recursively traverses the specified directory and applies `process_python_file` to each Python file it finds. The entry point checks if the script is being run directly and specifies the project directory to process.

# ===== GENERATED TESTS =====
```python
import os
from pathlib import Path
import pytest

# Original code
def process_python_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Replace double-quotes with single-quotes
    content = content.replace('"', "'")
    
    # Remove trailing commas from function calls and list definitions
    lines = content.split('\n')
    for i in range(len(lines)):
        line = lines[i]
        if ',' in line:
            if line.strip().endswith(','):
                line = line.rstrip(',') + '\n'
                lines[i] = line
    
    new_content = ''.join(lines)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_content)

def traverse_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                process_python_file(file_path)

# Test cases
@pytest.fixture
def test_dir():
    # Create a temporary directory with test files
    temp_dir = Path('test_temp_dir')
    temp_dir.mkdir(exist_ok=True)
    
    # Create some test Python files
    (temp_dir / 'test1.py').write_text('print("Hello, world!")\ndef my_function():\n    return "foo",\n')
    (temp_dir / 'test2.py').write_text('x = [1, 2, 3,]\ny = {"a": 1,}\n')
    
    yield temp_dir
    
    # Clean up the temporary directory
    for file in temp_dir.iterdir():
        file.unlink()
    temp_dir.rmdir()

def test_process_python_file(test_dir):
    """Test process_python_file function"""
    file_path = test_dir / 'test1.py'
    process_python_file(file_path)
    
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    assert "'Hello, world!'" in content
    assert "def my_function():\n    return 'foo'" in content

def test_traverse_directory(test_dir):
    """Test traverse_directory function"""
    process_path = test_dir / 'processed'
    process_path.mkdir(exist_ok=True)
    
    # Move the original files to a separate directory for processing
    (test_dir / 'test1.py').rename(process_path / 'test1.py')
    (test_dir / 'test2.py').rename(process_path / 'test2.py')
    
    traverse_directory(test_dir)
    
    # Check if the processed files are correctly modified
    with open(process_path / 'test1.py', 'r', encoding='utf-8') as file:
        content = file.read()
    
    assert "'Hello, world!'" in content
    assert "def my_function():\n    return 'foo'" in content
    
    with open(process_path / 'test2.py', 'r', encoding='utf-8') as file:
        content = file.read()
    
    assert "x = [1, 2, 3]" in content
    assert "y = {'a': 1}" in content

if __name__ == "__main__":
    pytest.main(['-v'])
```

This test suite includes two test cases: `test_process_python_file` and `test_traverse_directory`. The `test_dir` fixture is used to create a temporary directory with test files, which are cleaned up after the tests. Both test cases use assertions to verify that the functions behave as expected.