# BATCH3_PROMPT22_Devstral.py

import importlib.util
import sys

def load_module_from_code(module_name, code):
    """Dynamically load a module from source code."""
    spec = importlib.util.spec_from_loader(module_name, loader=None)
    module = importlib.util.module_from_spec(spec)

    # Execute the code in the module's namespace
    exec(code, module.__dict__)
    return module

# Define the three interdependent modules as strings
module_a_code = """
def function_a():
    print("Function A called")
    function_b()
"""

module_b_code = """
def function_b():
    print("Function B called")
    function_c()
"""

module_c_code = """
def function_c():
    print("Function C called")
    function_a()
"""

# Load the modules
module_a = load_module_from_code('module_a', module_a_code)
module_b = load_module_from_code('module_b', module_b_code)
module_c = load_module_from_code('module_c', module_c_code)

# Create a circular reference resolution
def initialize_modules():
    """Initialize modules with proper circular dependency handling."""
    # Inject functions into each other's namespace
    module_a.function_b = module_b.function_b
    module_b.function_c = module_c.function_c
    module_c.function_a = module_a.function_a

if __name__ == "__main__":
    initialize_modules()
    print("Modules initialized with circular dependencies")
    try:
        # This will demonstrate the circular dependency
        module_a.function_a()
    except RecursionError as e:
        print(f"Circular dependency detected: {e}")