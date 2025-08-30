```python
import sys
import random
import string
import re

def generate_random_string(length=10):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

def process_line(line):
    # Remove single-line comments starting with #
    line = re.sub(r'#.*$', '', line)
    # Remove block comments starting with ##
    line = re.sub(r'##.*', '', line)
    return line.strip()

if __name__ == "__main__":
    lines = sys.stdin.read().splitlines()
    processed_lines = []
    for line in lines:
        processed_line = process_line(line)
        processed_lines.append(processed_line)
    print('\n'.join(processed_lines))