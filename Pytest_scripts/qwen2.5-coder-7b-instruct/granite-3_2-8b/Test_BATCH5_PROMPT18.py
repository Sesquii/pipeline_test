import os
import sys
from importlib import import_module
from collections import defaultdict

def get_dependencies(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        source = file.read()
    dependencies = set()
    for line in source.splitlines():
        if 'import' in line or 'from' in line:
            module_name = line.strip().split()[1]
            dependencies.add(module_name)
    return dependencies

def find_circular_dependencies(directory):
    modules_dict = defaultdict(set)
    visited = set()

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                dependencies = get_dependencies(file_path)

                for dep in dependencies:
                    modules_dict[dep].add(file_path)

    circular_deps = set()
    for module, depends_on in modules_dict.items():
        if module in depends_on:
            circular_deps.update({module})

            stack = [module]
            while stack:
                current = stack.pop()
                if current in depends_on:
                    circular_deps.add(current)
                    for dep in modules_dict[current]:
                        if dep not in visited:
                            stack.append(dep)
                            visited.add(dep)

    return list(circular_deps)

def main():
    if len(sys.argv) != 2:
        print("Usage: python circular_dependency_detector.py <directory>")
        sys.exit(1)

    directory = sys.argv[1]

    circular_deps = find_circular_dependencies(directory)

    if circular_deps:
        print("Circular Dependencies Found:")
        for dep in circular_deps:
            print(f"- {dep}")
    else:
        print("No circular dependencies found.")

if __name__ == "__main__":
    main()

# ===== GENERATED TESTS =====
```python
import pytest
from pathlib import Path

# Original code
def get_dependencies(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        source = file.read()
    dependencies = set()
    for line in source.splitlines():
        if 'import' in line or 'from' in line:
            module_name = line.strip().split()[1]
            dependencies.add(module_name)
    return dependencies

def find_circular_dependencies(directory):
    modules_dict = defaultdict(set)
    visited = set()

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                dependencies = get_dependencies(file_path)

                for dep in dependencies:
                    modules_dict[dep].add(file_path)

    circular_deps = set()
    for module, depends_on in modules_dict.items():
        if module in depends_on:
            circular_deps.update({module})

            stack = [module]
            while stack:
                current = stack.pop()
                if current in depends_on:
                    circular_deps.add(current)
                    for dep in modules_dict[current]:
                        if dep not in visited:
                            stack.append(dep)
                            visited.add(dep)

    return list(circular_deps)

def main():
    if len(sys.argv) != 2:
        print("Usage: python circular_dependency_detector.py <directory>")
        sys.exit(1)

    directory = sys.argv[1]

    circular_deps = find_circular_dependencies(directory)

    if circular_deps:
        print("Circular Dependencies Found:")
        for dep in circular_deps:
            print(f"- {dep}")
    else:
        print("No circular dependencies found.")

if __name__ == "__main__":
    main()

# Test cases
@pytest.fixture(scope="module")
def test_directory(tmpdir):
    # Create a temporary directory with some Python files
    os.makedirs(os.path.join(tmpdir, 'package1'))
    with open(os.path.join(tmpdir, 'package1', '__init__.py'), 'w') as f:
        pass
    with open(os.path.join(tmpdir, 'package1', 'module1.py'), 'w') as f:
        f.write("import package2.module2")
    
    os.makedirs(os.path.join(tmpdir, 'package2'))
    with open(os.path.join(tmpdir, 'package2', '__init__.py'), 'w') as f:
        pass
    with open(os.path.join(tmpdir, 'package2', 'module2.py'), 'w') as f:
        f.write("import package1.module1")
    
    return tmpdir

def test_get_dependencies(test_directory):
    file_path = os.path.join(test_directory, 'package1', 'module1.py')
    assert get_dependencies(file_path) == {'package2.module2'}

def test_find_circular_dependencies_no_circular(test_directory):
    circular_deps = find_circular_dependencies(str(test_directory))
    assert not circular_deps

def test_find_circular_dependencies_with_circular(test_directory):
    os.makedirs(os.path.join(test_directory, 'package3'))
    with open(os.path.join(test_directory, 'package3', '__init__.py'), 'w') as f:
        pass
    with open(os.path.join(test_directory, 'package3', 'module3.py'), 'w') as f:
        f.write("import package1.module1")
    
    circular_deps = find_circular_dependencies(str(test_directory))
    assert 'package1' in circular_deps

def test_find_circular_dependencies_with_multiple_circulars(test_directory):
    os.makedirs(os.path.join(test_directory, 'package4'))
    with open(os.path.join(test_directory, 'package4', '__init__.py'), 'w') as f:
        pass
    with open(os.path.join(test_directory, 'package4', 'module4.py'), 'w') as f:
        f.write("import package1.module1")
    
    os.makedirs(os.path.join(test_directory, 'package5'))
    with open(os.path.join(test_directory, 'package5', '__init__.py'), 'w') as f:
        pass
    with open(os.path.join(test_directory, 'package5', 'module5.py'), 'w') as f:
        f.write("import package2.module2")
    
    circular_deps = find_circular_dependencies(str(test_directory))
    assert 'package1' in circular_deps and 'package2' in circular_deps

def test_find_circular_dependencies_with_self_dependency(test_directory):
    with open(os.path.join(test_directory, 'module6.py'), 'w') as f:
        f.write("import module6")
    
    circular_deps = find_circular_dependencies(str(test_directory))
    assert 'module6' in circular_deps
```