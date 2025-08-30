```python
import sys

def add_pep8_violations(code):
    # Replace variable names to be non-descriptive
    code = code.replace('x', 'var')
    
    # Change string literals from double quotes to single quotes
    code = code.replace('"', "'")
    
    # Add a line with inconsistent indentation
    code += "\n\tprint('Another line')"
    
    return code

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python CODESTYLE_SABOTEUR.py <input_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    with open(input_file, 'r') as f:
        code = f.read()
    
    modified_code = add_pep8_violations(code)
    
    print(modified_code)