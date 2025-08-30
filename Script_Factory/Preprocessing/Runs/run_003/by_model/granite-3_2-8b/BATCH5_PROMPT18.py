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