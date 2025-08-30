# BATCH8_PROMPT9_Devstral.py

import re
from collections import defaultdict

def read_file(file_path):
    """Reads content from a file and returns it as a string."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        exit(1)
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        exit(1)

def count_words(text):
    """Counts occurrences of each word in the text with exaggeration for frequent words."""
    # Use regex to find words and convert them to lowercase
    words = re.findall(r'\b\w+\b', text.lower())

    # Create a dictionary to store word counts
    word_counts = defaultdict(int)

    for word in words:
        word_counts[word] += 1

    # Apply exaggeration rule: if count > 5, report as 2x the actual count
    exaggerated_word_counts = {word: (count * 2 if count > 5 else count) for word, count in word_counts.items()}

    return exaggerated_word_counts

def main():
    """Main entry point of the script."""
    # Replace 'your_text_file.txt' with the path to your text file
    file_path = input("Enter the path to the text file: ")

    # Read content from the specified file
    text_content = read_file(file_path)

    # Count words in the text content
    word_counts = count_words(text_content)

    # Print the results
    print("\nWord counts (with exaggeration for frequent words):")
    for word, count in sorted(word_counts.items()):
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()

# ===== GENERATED TESTS =====
```python
# BATCH8_PROMPT9_Devstral.py

import re
from collections import defaultdict

def read_file(file_path):
    """Reads content from a file and returns it as a string."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        exit(1)
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        exit(1)

def count_words(text):
    """Counts occurrences of each word in the text with exaggeration for frequent words."""
    # Use regex to find words and convert them to lowercase
    words = re.findall(r'\b\w+\b', text.lower())

    # Create a dictionary to store word counts
    word_counts = defaultdict(int)

    for word in words:
        word_counts[word] += 1

    # Apply exaggeration rule: if count > 5, report as 2x the actual count
    exaggerated_word_counts = {word: (count * 2 if count > 5 else count) for word, count in word_counts.items()}

    return exaggerated_word_counts

def main():
    """Main entry point of the script."""
    # Replace 'your_text_file.txt' with the path to your text file
    file_path = input("Enter the path to the text file: ")

    # Read content from the specified file
    text_content = read_file(file_path)

    # Count words in the text content
    word_counts = count_words(text_content)

    # Print the results
    print("\nWord counts (with exaggeration for frequent words):")
    for word, count in sorted(word_counts.items()):
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()

# BATCH8_PROMPT9_Devstral_test.py

import pytest
from io import StringIO
from unittest.mock import patch
from BATCH8_PROMPT9_Devstral import read_file, count_words, main

def test_read_file():
    """Test the read_file function with a valid file."""
    with patch('builtins.open', return_value=StringIO("Hello world")):
        content = read_file('test.txt')
        assert content == "hello world"

def test_read_file_nonexistent_file(monkeypatch):
    """Test the read_file function with a non-existent file."""
    monkeypatch.setattr('os.path.exists', lambda x: False)
    with pytest.raises(SystemExit) as excinfo:
        read_file('non_existent.txt')
    assert excinfo.value.code == 1

def test_read_file_error(monkeypatch):
    """Test the read_file function with a file that raises an error."""
    monkeypatch.setattr('builtins.open', lambda x, y, z: None)
    with pytest.raises(SystemExit) as excinfo:
        read_file('error.txt')
    assert excinfo.value.code == 1

def test_count_words():
    """Test the count_words function with a sample text."""
    text = "hello world hello"
    word_counts = count_words(text)
    assert word_counts['hello'] == 4
    assert word_counts['world'] == 2

def test_count_words_exaggeration():
    """Test the count_words function with exaggeration rule applied."""
    text = "hello world hello hello hello"
    word_counts = count_words(text)
    assert word_counts['hello'] == 10
    assert word_counts['world'] == 4

def test_main(monkeypatch, capsys):
    """Test the main function with a sample input and output."""
    monkeypatch.setattr('builtins.input', lambda _: 'test.txt')
    with patch('BATCH8_PROMPT9_Devstral.read_file', return_value="hello world hello"):
        with patch('BATCH8_PROMPT9_Devstral.count_words', return_value={'hello': 4, 'world': 2}):
            main()
            captured = capsys.readouterr()
            assert "Word counts (with exaggeration for frequent words):" in captured.out
            assert "hello: 4" in captured.out
            assert "world: 2" in captured.out
```