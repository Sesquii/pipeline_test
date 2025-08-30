import os

def find_circular_dependencies(directory):
    # Dictionary to store module imports
    import_dict = {}

    # Walk through the directory and its subdirectories
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    content = f.read()
                    # Find all import statements
                    imports = [line.strip() for line in content.split('\n') if line.startswith('import') or line.startswith('from')]
                    import_dict[file] = imports

    # Check for circular dependencies
    checked_modules = set()
    def check_circular(module, path):
        if module in checked_modules:
            return True
        checked_modules.add(module)
        for imp in import_dict.get(module, []):
            imp_module = imp.split()[1].rstrip(',') if imp.startswith('import') else imp.split('.')[0]
            if imp_module == module or check_circular(imp_module, path + [module]):
                return True
        return False

    circular_dependencies = []
    for module in import_dict:
        if not module.endswith('__init__.py'):
            if check_circular(module, []):
                circular_dependencies.append(module)

    return circular_dependencies

if __name__ == "__main__":
    directory_to_check = 'path/to/your/python/directory'  # Replace with the path to your Python directory
    result = find_circular_dependencies(directory_to_check)
    for module in result:
        print(f"Circular dependency detected: {module}")

# ===== GENERATED TESTS =====
import os
from typing import List

def find_circular_dependencies(directory):
    # Dictionary to store module imports
    import_dict = {}

    # Walk through the directory and its subdirectories
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    content = f.read()
                    # Find all import statements
                    imports = [line.strip() for line in content.split('\n') if line.startswith('import') or line.startswith('from')]
                    import_dict[file] = imports

    # Check for circular dependencies
    checked_modules = set()
    def check_circular(module, path):
        if module in checked_modules:
            return True
        checked_modules.add(module)
        for imp in import_dict.get(module, []):
            imp_module = imp.split()[1].rstrip(',') if imp.startswith('import') else imp.split('.')[0]
            if imp_module == module or check_circular(imp_module, path + [module]):
                return True
        return False

    circular_dependencies = []
    for module in import_dict:
        if not module.endswith('__init__.py'):
            if check_circular(module, []):
                circular_dependencies.append(module)

    return circular_dependencies

# Test cases
import pytest

@pytest.fixture
def test_directory(tmpdir):
    # Create a temporary directory with some Python files
    os.makedirs(os.path.join(tmpdir, 'module1'))
    with open(os.path.join(tmpdir, 'module1', '__init__.py'), 'w') as f:
        pass
    with open(os.path.join(tmpdir, 'module1', 'file1.py'), 'w') as f:
        f.write("import module2\n")
    
    os.makedirs(os.path.join(tmpdir, 'module2'))
    with open(os.path.join(tmpdir, 'module2', '__init__.py'), 'w') as f:
        pass
    with open(os.path.join(tmpdir, 'module2', 'file2.py'), 'w') as f:
        f.write("import module1\n")
    
    return tmpdir

def test_find_circular_dependencies(test_directory):
    result = find_circular_dependencies(str(test_directory))
    assert len(result) == 2
    assert 'module1' in result
    assert 'module2' in result

def test_find_circular_dependencies_no_circular(test_directory):
    # Create a temporary directory with some Python files that do not have circular dependencies
    os.makedirs(os.path.join(test_directory, 'module3'))
    with open(os.path.join(test_directory, 'module3', '__init__.py'), 'w') as f:
        pass
    with open(os.path.join(test_directory, 'module3', 'file3.py'), 'w') as f:
        f.write("import module4\n")
    
    os.makedirs(os.path.join(test_directory, 'module4'))
    with open(os.path.join(test_directory, 'module4', '__init__.py'), 'w') as f:
        pass
    with open(os.path.join(test_directory, 'module4', 'file4.py'), 'w') as f:
        f.write("import module5\n")
    
    result = find_circular_dependencies(str(test_directory))
    assert len(result) == 0

def test_find_circular_dependencies_empty_directory(tmpdir):
    result = find_circular_dependencies(str(tmpdir))
    assert len(result) == 0
