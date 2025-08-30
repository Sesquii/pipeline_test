import os
import sys
from collections import defaultdict
from ast import parse

def get_imports(node):
    imports = set()
    if hasattr(node, 'body') and isinstance(node.body, ast.Module):
        for sub_node in node.body.body:
            if isinstance(sub_node, (ast.Import, ast.ImportFrom)):
                for alias in sub_node.names:
                    imports.add(alias.name)
    return imports

def parse_file(file_path):
    with open(file_path, 'r') as f:
        return parse(f.read(), filename=file_path)

def detect_circular_dependencies(directory):
    module_imports = defaultdict(set)
    visited = set()

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                full_path = os.path.join(root, file)
                tree = parse_file(full_path)
                imports = get_imports(tree)

                for import_name in imports:
                    module_name = '.'.join(import_name.split('.')[:-1])

                    if module_name not in visited:
                        visited.add(module_name)
                    else:
                        print(f"Circular dependency detected:\n{full_path}\ndepends on\n{os.path.relpath(visited[module_name], directory)}")

    return

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python circular_dependency_detector.py [directory]")
        sys.exit(1)
    
    directory = sys.argv[1]
    detect_circular_dependencies(directory)