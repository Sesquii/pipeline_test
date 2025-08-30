# BATCH2_PROMPT22_Devstral.py

import sys
from importlib.util import spec_from_file_location, module_from_spec
import os

# Create a simple module loader that can handle circular dependencies
class InterdependentModuleLoader:
    def __init__(self):
        self.modules = {}
        self.module_files = {
            'module_a': 'module_a.py',
            'module_b': 'module_b.py',
            'module_c': 'module_c.py'
        }

    def load_module(self, name):
        if name in self.modules:
            return self.modules[name]

        file_path = self.module_files[name]
        spec = spec_from_file_location(name, file_path)
        module = module_from_spec(spec)
        sys.modules[name] = module
        spec.loader.exec_module(module)
        self.modules[name] = module
        return module

    def initialize_modules(self):
        # Load all modules first to handle circular dependencies
        for name in self.module_files:
            self.load_module(name)

# Create the module files with circular dependencies
def create_module_files():
    with open('module_a.py', 'w') as f:
        f.write("""
def func_a():
    from module_b import func_b
    print("func_a called")
    return "A -> B"

if __name__ == "__main__":
    print(func_a())
""")

    with open('module_b.py', 'w') as f:
        f.write("""
def func_b():
    from module_c import func_c
    print("func_b called")
    return "B -> C"

if __name__ == "__main__":
    print(func_b())
""")

    with open('module_c.py', 'w') as f:
        f.write("""
def func_c():
    from module_a import func_a
    print("func_c called")
    return "C -> A"

if __name__ == "__main__":
    print(func_c())
""")

def main():
    # Create the module files
    create_module_files()

    # Initialize the module loader
    loader = InterdependentModuleLoader()
    loader.initialize_modules()

    # Now we can use any of the modules without issues
    module_a = loader.load_module('module_a')
    print("Result from module_a:", module_a.func_a())

if __name__ == "__main__":
    main()