import sys
import random

def recursive_art(depth, char='*'):
    if depth == 0:
        return ''
    
    lines = []
    for _ in range(2**depth):
        line = recursive_art(depth-1, char)
        if random.choice([True, False]):
            line += char
        lines.append(line)
    
    return '\n'.join(lines)

def main():
    if len(sys.argv) != 2:
        print("Usage: python art_bot.py <depth>")
        sys.exit(1)

    try:
        depth = int(sys.argv[1])
    except ValueError:
        print("Depth must be an integer.")
        sys.exit(1)

    if depth < 0:
        print("Depth cannot be negative.")
        sys.exit(1)

    char_options = '*#@'
    random.shuffle(char_options)
    art = recursive_art(depth, char_options[0])
    
    print(art)

if __name__ == "__main__":
    main()

# ===== GENERATED TESTS =====
```python
import pytest
from io import StringIO

# Original code
import sys
import random

def recursive_art(depth, char='*'):
    if depth == 0:
        return ''
    
    lines = []
    for _ in range(2**depth):
        line = recursive_art(depth-1, char)
        if random.choice([True, False]):
            line += char
        lines.append(line)
    
    return '\n'.join(lines)

def main():
    if len(sys.argv) != 2:
        print("Usage: python art_bot.py <depth>")
        sys.exit(1)

    try:
        depth = int(sys.argv[1])
    except ValueError:
        print("Depth must be an integer.")
        sys.exit(1)

    if depth < 0:
        print("Depth cannot be negative.")
        sys.exit(1)

    char_options = '*#@'
    random.shuffle(char_options)
    art = recursive_art(depth, char_options[0])
    
    print(art)

if __name__ == "__main__":
    main()

# Test code
def test_recursive_art():
    """Test the recursive_art function with different depths and characters."""
    assert recursive_art(0) == ''
    assert recursive_art(1) in ['*', '']
    assert recursive_art(2).count('\n') == 3

def test_main(capsys):
    """Test the main function with different inputs."""
    # Test with valid depth
    sys.argv = ["art_bot.py", "1"]
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() in ['*', '']

    # Test with invalid non-integer depth
    sys.argv = ["art_bot.py", "abc"]
    main()
    captured = capsys.readouterr()
    assert captured.err.strip() == "Depth must be an integer."

    # Test with negative depth
    sys.argv = ["art_bot.py", "-1"]
    main()
    captured = capsys.readouterr()
    assert captured.err.strip() == "Depth cannot be negative."

def test_main_usage(capsys):
    """Test the usage message of the main function."""
    sys.argv = ["art_bot.py"]
    main()
    captured = capsys.readouterr()
    assert captured.err.strip() == "Usage: python art_bot.py <depth>"
```