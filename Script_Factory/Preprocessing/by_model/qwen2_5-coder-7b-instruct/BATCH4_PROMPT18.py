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