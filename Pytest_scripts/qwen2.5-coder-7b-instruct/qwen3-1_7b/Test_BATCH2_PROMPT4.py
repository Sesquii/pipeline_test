```python
import sys
import os

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <filename>")
        return
    input_filename = sys.argv[1]
    
    # Read file content and convert to lowercase for case-insensitive checking
    with open(input_filename, 'r') as f:
        content = f.read().lower()
        words = content.split()
        
    # Define a set of positive words for sentiment analysis
    positive_words = {'good', 'great', 'happy', 'positive', 'awesome', 'excellent'}
    
    # Check if any positive word is present in the file
    found_positive = any(word in positive_words for word in words)
    
    if found_positive:
        new_filename = input_filename + "_happy"
    else:
        new_filename = input_filename
    
    # Rename the file
    os.rename(input_filename, new_filename)

if __name__ == "__main__":
    main()

# ===== GENERATED TESTS =====
```python
import pytest
from io import StringIO
import sys

# Original script code
def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <filename>")
        return
    input_filename = sys.argv[1]
    
    # Read file content and convert to lowercase for case-insensitive checking
    with open(input_filename, 'r') as f:
        content = f.read().lower()
        words = content.split()
        
    # Define a set of positive words for sentiment analysis
    positive_words = {'good', 'great', 'happy', 'positive', 'awesome', 'excellent'}
    
    # Check if any positive word is present in the file
    found_positive = any(word in positive_words for word in words)
    
    if found_positive:
        new_filename = input_filename + "_happy"
    else:
        new_filename = input_filename
    
    # Rename the file
    os.rename(input_filename, new_filename)

if __name__ == "__main__":
    main()

# Test cases
def test_main_no_args(capsys):
    """Test main function with no arguments."""
    sys.argv = ['script.py']
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Usage: python script.py <filename>"

def test_main_invalid_file(capsys, tmp_path):
    """Test main function with invalid file."""
    input_filename = str(tmp_path / 'nonexistent.txt')
    sys.argv = ['script.py', input_filename]
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == f"Usage: python script.py <filename>"

def test_main_empty_file(capsys, tmp_path):
    """Test main function with an empty file."""
    input_filename = str(tmp_path / 'empty.txt')
    with open(input_filename, 'w') as f:
        pass
    sys.argv = ['script.py', input_filename]
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Usage: python script.py <filename>"

def test_main_no_positive_words(capsys, tmp_path):
    """Test main function with no positive words."""
    input_filename = str(tmp_path / 'no_positive.txt')
    with open(input_filename, 'w') as f:
        f.write("This is a neutral file.")
    sys.argv = ['script.py', input_filename]
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Usage: python script.py <filename>"

def test_main_with_positive_words(capsys, tmp_path):
    """Test main function with positive words."""
    input_filename = str(tmp_path / 'positive.txt')
    with open(input_filename, 'w') as f:
        f.write("This is a great file.")
    sys.argv = ['script.py', input_filename]
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Usage: python script.py <filename>"
    assert os.path.exists(input_filename + "_happy")

def test_main_with_positive_words_and_existing_new_file(capsys, tmp_path):
    """Test main function with positive words and existing new file."""
    input_filename = str(tmp_path / 'positive.txt')
    new_filename = str(tmp_path / 'positive_happy.txt')
    with open(input_filename, 'w') as f:
        f.write("This is a great file.")
    os.rename(new_filename, input_filename)
    sys.argv = ['script.py', input_filename]
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Usage: python script.py <filename>"
    assert not os.path.exists(input_filename + "_happy")
```