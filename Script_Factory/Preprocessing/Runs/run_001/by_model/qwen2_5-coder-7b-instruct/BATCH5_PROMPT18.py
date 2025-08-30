import os

def find_circular_dependencies(directory):
    """
    Analyzes a directory of Python files and detects circular dependencies.
    
    Args:
        directory (str): Path to the directory containing Python files.
        
    Returns:
        list: List of tuples representing circular dependency chains.
    """
    modules = {}
    
    # Load all .py files from the directory
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                module_path = os.path.join(root, file)
                with open(module_path, 'r') as f:
                    content = f.read()
                modules[module_path] = [line.strip().split('from ')[1].split('.')[0] 
                                       for line in content.split('\n') if line.startswith('from')]
    
    # Detect circular dependencies
    def check_dependency(path, current_chain):
        """
        Recursively checks for circular dependencies.
        
        Args:
            path (str): Current module path being checked.
            current_chain (list): List of modules in the current dependency chain.
            
        Returns:
            bool: True if a circular dependency is found, False otherwise.
        """
        for mod in modules[path]:
            if mod == '__main__':
                continue
            if mod in current_chain:
                return True
            if path not in modules[mod]:
                continue
            if check_dependency(modules[mod][0], current_chain + [mod]):
                return True
        return False
    
    circular_dependencies = []
    for module, imports in modules.items():
        for imp in imports:
            if imp in modules and check_dependency(imp, [module.split('/')[-1].split('.')[0]]):
                circular_dependencies.append((module, imp))
    
    # Remove duplicate chains
    unique_circular_dependencies = set(tuple(sorted(chain)) for chain in circular_dependencies)
    
    return list(unique_circular_dependencies)

if __name__ == "__main__":
    directory_path = 'path/to/your/python/directory'
    results = find_circular_dependencies(directory_path)
    if results:
        print("Circular dependencies found:")
        for dep1, dep2 in results:
            print(f"{dep1} -> {dep2}")
    else:
        print("No circular dependencies found.")