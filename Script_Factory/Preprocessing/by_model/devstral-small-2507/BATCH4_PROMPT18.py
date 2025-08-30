import os
import ast
import sys
from collections import defaultdict

def find_python_files(directory):
    """Recursively find all Python files in a directory."""
    python_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                python_files.append(os.path.join(root, file))
    return python_files

def parse_imports(file_path):
    """Parse import statements from a Python file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        tree = ast.parse(file.read(), filename=file_path)

    imports = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.add(alias.name.split('.')[0])
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imports.add(node.module.split('.')[0])

    return imports

def build_dependency_graph(files):
    """Build a dependency graph from Python files."""
    graph = defaultdict(set)
    for file_path in files:
        module_name = os.path.splitext(os.path.basename(file_path))[0]
        imports = parse_imports(file_path)
        for imported_module in imports:
            if imported_module != module_name:  # Avoid self-imports
                graph[module_name].add(imported_module)
    return graph

def detect_circular_dependencies(graph):
    """Detect circular dependencies in a directed graph."""
    visited = set()
    rec_stack = set()

    def is_cyclic(v):
        if v in rec_stack:
            return True
        if v in visited:
            return False

        visited.add(v)
        rec_stack.add(v)

        for neighbour in graph[v]:
            if is_cyclic(neighbour):
                return True

        rec_stack.remove(v)
        return False

    for node in graph:
        if is_cyclic(node):
            return True
    return False

def find_circular_pairs(graph):
    """Find all circular dependency pairs in a directed graph."""
    visited = set()
    rec_stack = set()
    pairs = set()

    def dfs(v, path):
        if v in rec_stack:
            # Find the index where the cycle starts
            cycle_start_index = path.index(v)
            cycle_modules = path[cycle_start_index:]
            for i in range(len(cycle_modules) - 1):
                pairs.add((cycle_modules[i], cycle_modules[i + 1]))
            return

        if v in visited:
            return

        visited.add(v)
        rec_stack.add(v)
        path.append(v)

        for neighbour in graph[v]:
            dfs(neighbour, path)

        path.pop()
        rec_stack.remove(v)

    for node in graph:
        if node not in visited:
            dfs(node, [])

    return pairs

def main(directory):
    """Main function to detect circular dependencies."""
    python_files = find_python_files(directory)
    if not python_files:
        print("No Python files found in the directory.")
        return

    graph = build_dependency_graph(python_files)

    # Check for any circular dependencies
    has_circular_deps = detect_circular_dependencies(graph)
    if not has_circular_deps:
        print("No circular dependencies found.")
        return

    # Find and report specific circular pairs
    circular_pairs = find_circular_pairs(graph)
    if circular_pairs:
        print("Circular dependencies detected:")
        for pair in circular_pairs:
            print(f"  {pair[0]} -> {pair[1]}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python circular_dependency_detector.py <directory>")
        sys.exit(1)

    directory = sys.argv[1]
    main(directory)