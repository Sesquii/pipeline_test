import os
import ast
from typing import Dict, List, Set

class CircularDependencyDetector:
    def __init__(self, directory: str):
        self.directory = directory
        self.modules: Dict[str, Set[str]] = {}
        self.dependencies: Dict[str, Set[str]] = {}

    def analyze_directory(self) -> None:
        """Analyze all Python files in the specified directory."""
        for filename in os.listdir(self.directory):
            if filename.endswith('.py'):
                filepath = os.path.join(self.directory, filename)
                with open(filepath, 'r') as file:
                    tree = ast.parse(file.read(), filename=filename)
                    self.analyze_imports(tree)

    def analyze_imports(self, tree: ast.AST) -> None:
        """Analyze imports in the AST and build dependency graph."""
        module_name = os.path.splitext(os.path.basename(tree.filename))[0]
        for node in ast.walk(tree):
            if isinstance(node, (ast.Import, ast.ImportFrom)):
                for alias in node.names:
                    imported_module = alias.name
                    self.add_dependency(module_name, imported_module)

    def add_dependency(self, module: str, dependency: str) -> None:
        """Add a dependency relationship between modules."""
        if module not in self.modules:
            self.modules[module] = set()
        if dependency not in self.dependencies:
            self.dependencies[dependency] = set()
        
        self.modules[module].add(dependency)
        self.dependencies[dependency].add(module)

    def detect_circular_dependencies(self) -> List[str]:
        """Detect circular dependencies using a graph traversal algorithm."""
        visited = set()
        rec_stack = set()

        def is_cyclic(v: str) -> bool:
            if v in rec_stack:
                return True
            if v in visited:
                return False

            visited.add(v)
            rec_stack.add(v)

            for neighbor in self.modules.get(v, []):
                if is_cyclic(neighbor):
                    return True

            rec_stack.remove(v)
            return False

        circular_dependencies = []
        for node in self.modules:
            if is_cyclic(node):
                circular_dependencies.append(node)

        return circular_dependencies

    def report_circular_dependencies(self) -> None:
        """Report any detected circular dependencies."""
        circular_deps = self.detect_circular_dependencies()
        if not circular_deps:
            print("No circular dependencies found.")
        else:
            print("Circular dependencies found:")
            for dep in circular_deps:
                print(f" - {dep}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Detect circular dependencies in Python modules.")
    parser.add_argument("directory", help="Directory containing Python files to analyze")
    args = parser.parse_args()

    detector = CircularDependencyDetector(args.directory)
    detector.analyze_directory()
    detector.report_circular_dependencies()