```python
import sys
from collections import defaultdict

def main():
    # Check if a filename is provided as an argument
    if len(sys.argv) < 2:
        print("Usage: python script.py <filename>")
        return
    
    filename = sys.argv[1]
    
    # Read the input file
    with open(filename, 'r') as file:
        text = file.read().lower()
    
    # Split into words
    words = text.split()
    
    # Define common words to exaggerate
    common_words = {"the", "a", "an"}
    
    # Initialize a dictionary to count word occurrences
    counts = defaultdict(int)
    
    # Apply the exaggeration factor (multiply by 2 for common words)
    multiplier = 2
    
    for word in words:
        if word in common_words:
            counts[word] += multiplier
        else:
            counts[word] += 1
    
    # Print the result
    print(counts)

if __name__ == "__main__":
    main()

# ===== GENERATED TESTS =====
```python
import pytest
from io import StringIO
import sys

# Original script
def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <filename>")
        return
    
    filename = sys.argv[1]
    
    with open(filename, 'r') as file:
        text = file.read().lower()
    
    words = text.split()
    
    common_words = {"the", "a", "an"}
    
    counts = defaultdict(int)
    
    multiplier = 2
    
    for word in words:
        if word in common_words:
            counts[word] += multiplier
        else:
            counts[word] += 1
    
    print(counts)

if __name__ == "__main__":
    main()

# Test suite
def test_main_no_args(capsys):
    """Test main function with no arguments"""
    sys.argv = ['script.py']
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Usage: python script.py <filename>"

def test_main_invalid_file(capsys, tmp_path):
    """Test main function with an invalid file"""
    filename = tmp_path / 'nonexistent.txt'
    sys.argv = ['script.py', str(filename)]
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Usage: python script.py <filename>"

def test_main_valid_file(capsys, tmp_path):
    """Test main function with a valid file"""
    content = "the quick brown fox jumps over the lazy dog"
    filename = tmp_path / 'test.txt'
    filename.write_text(content)
    
    sys.argv = ['script.py', str(filename)]
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "defaultdict(<class 'int'>, {'the': 4, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1})"

def test_main_common_words(capsys, tmp_path):
    """Test main function with common words"""
    content = "the a an the"
    filename = tmp_path / 'test.txt'
    filename.write_text(content)
    
    sys.argv = ['script.py', str(filename)]
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "defaultdict(<class 'int'>, {'the': 6, 'a': 2, 'an': 2})"

def test_main_empty_file(capsys, tmp_path):
    """Test main function with an empty file"""
    filename = tmp_path / 'test.txt'
    filename.write_text("")
    
    sys.argv = ['script.py', str(filename)]
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "defaultdict(<class 'int'>, {})"

def test_main_large_file(capsys, tmp_path):
    """Test main function with a large file"""
    content = " ".join(["the"] * 1000)
    filename = tmp_path / 'test.txt'
    filename.write_text(content)
    
    sys.argv = ['script.py', str(filename)]
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "defaultdict(<class 'int'>, {'the': 2000})"
```