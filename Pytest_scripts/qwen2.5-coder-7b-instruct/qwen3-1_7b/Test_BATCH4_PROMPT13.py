```python
import sys
from collections import defaultdict

def main():
    if len(sys.argv) != 2:
        print("Usage: python exaggerate_word_counter.py <filename>")
        return
    filename = sys.argv[1]
    with open(filename, 'r') as f:
        words = f.read().split()
    common_words = {"the", "a", "an", "and", "but", "or", "this", "that", "it", "is", "are", "was", "were", "has", "have", "had", "will", "would", "shall", "should", "do", "does", "did", "doesnt", "not", "no", "nope"}
    counts = defaultdict(int)
    for word in words:
        if word in common_words:
            counts[word] += 10
        else:
            counts[word] += 1
    print(counts)

if __name__ == "__main__":
    main()

# ===== GENERATED TESTS =====
```python
import pytest
from io import StringIO
import sys

# Original code
import sys
from collections import defaultdict

def main():
    if len(sys.argv) != 2:
        print("Usage: python exaggerate_word_counter.py <filename>")
        return
    filename = sys.argv[1]
    with open(filename, 'r') as f:
        words = f.read().split()
    common_words = {"the", "a", "an", "and", "but", "or", "this", "that", "it", "is", "are", "was", "were", "has", "have", "had", "will", "would", "shall", "should", "do", "does", "did", "doesnt", "not", "no", "nope"}
    counts = defaultdict(int)
    for word in words:
        if word in common_words:
            counts[word] += 10
        else:
            counts[word] += 1
    print(counts)

if __name__ == "__main__":
    main()

# Test cases
def test_main_valid_file(capsys):
    """Test with a valid file containing words."""
    input_data = "the cat and the hat\nthis is a test"
    filename = 'test_input.txt'
    with open(filename, 'w') as f:
        f.write(input_data)
    
    sys.argv = ['exaggerate_word_counter.py', filename]
    main()
    
    captured = capsys.readouterr()
    expected_output = "defaultdict(<class 'int'>, {'the': 20, 'cat': 1, 'and': 10, 'hat': 10, 'this': 10, 'is': 1, 'a': 11, 'test': 1})\n"
    assert captured.out == expected_output

def test_main_invalid_file(capsys):
    """Test with an invalid file."""
    filename = 'nonexistent.txt'
    sys.argv = ['exaggerate_word_counter.py', filename]
    main()
    
    captured = capsys.readouterr()
    expected_output = "Usage: python exaggerate_word_counter.py <filename>\n"
    assert captured.out == expected_output

def test_main_no_arguments(capsys):
    """Test with no arguments."""
    sys.argv = ['exaggerate_word_counter.py']
    main()
    
    captured = capsys.readouterr()
    expected_output = "Usage: python exaggerate_word_counter.py <filename>\n"
    assert captured.out == expected_output

def test_main_extra_arguments(capsys):
    """Test with extra arguments."""
    filename = 'test_input.txt'
    sys.argv = ['exaggerate_word_counter.py', filename, 'extra']
    main()
    
    captured = capsys.readouterr()
    expected_output = "Usage: python exaggerate_word_counter.py <filename>\n"
    assert captured.out == expected_output
```