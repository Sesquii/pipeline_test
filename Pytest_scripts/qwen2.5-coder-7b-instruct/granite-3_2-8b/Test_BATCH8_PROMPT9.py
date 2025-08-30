# BATCH8_PROMPT9_Granite.py

def count_words(file_path):
    """
    This function reads a file, counts word occurrences, and applies an exaggeration factor for words appearing more than 5 times.

    Args:
        file_path (str): The path to the input text file.

    Returns:
        dict: A dictionary with words as keys and their respective counts as values.
    """
    # Initialize an empty dictionary to store word counts
    word_counts = {}

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                # Split the line into words
                words = line.lower().split()

                for word in words:
                    # Remove punctuation from the ends of words
                    word = word.strip('.,!?":;()-_[]{}<>')

                    if word:  # Ignore empty strings
                        if word in word_counts:
                            # If word already exists, increment its count
                            word_counts[word] += 1

                            # Exaggerate the count for words appearing more than 5 times
                            if word_counts[word] > 5:
                                word_counts[word] *= 2
                        else:
                            # Add new word to dictionary with initial count of 1
                            word_counts[word] = 1

    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return word_counts


def main():
    """Entry point for the program."""
    # Replace 'your_text_file.txt' with the path to your actual text file
    file_path = 'your_text_file.txt'

    word_counts = count_words(file_path)

    if word_counts:
        print("Word Counts:")
        for word, count in word_counts.items():
            print(f"{word}: {count}")
    else:
        print("No words found or an error occurred during processing.")


if __name__ == "__main__":
    main()

# ===== GENERATED TESTS =====
```python
# BATCH8_PROMPT9_Granite.py

def count_words(file_path):
    """
    This function reads a file, counts word occurrences, and applies an exaggeration factor for words appearing more than 5 times.

    Args:
        file_path (str): The path to the input text file.

    Returns:
        dict: A dictionary with words as keys and their respective counts as values.
    """
    # Initialize an empty dictionary to store word counts
    word_counts = {}

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                # Split the line into words
                words = line.lower().split()

                for word in words:
                    # Remove punctuation from the ends of words
                    word = word.strip('.,!?":;()-_[]{}<>')

                    if word:  # Ignore empty strings
                        if word in word_counts:
                            # If word already exists, increment its count
                            word_counts[word] += 1

                            # Exaggerate the count for words appearing more than 5 times
                            if word_counts[word] > 5:
                                word_counts[word] *= 2
                        else:
                            # Add new word to dictionary with initial count of 1
                            word_counts[word] = 1

    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return word_counts


def main():
    """Entry point for the program."""
    # Replace 'your_text_file.txt' with the path to your actual text file
    file_path = 'your_text_file.txt'

    word_counts = count_words(file_path)

    if word_counts:
        print("Word Counts:")
        for word, count in word_counts.items():
            print(f"{word}: {count}")
    else:
        print("No words found or an error occurred during processing.")


if __name__ == "__main__":
    main()

# BATCH8_PROMPT9_Granite_test.py

import pytest
from pathlib import Path
from io import StringIO
import sys

def test_count_words():
    """Test the count_words function with various inputs."""
    # Test case 1: Normal file with words
    input_text = "Hello world. Hello everyone! This is a test."
    expected_output = {'hello': 3, 'world': 2, 'everyone': 1, 'this': 1, 'is': 1, 'a': 1, 'test': 1}
    with pytest.raises(FileNotFoundError):
        count_words('nonexistent_file.txt')
    
    # Test case 2: Empty file
    input_text = ""
    expected_output = {}
    with open('empty_file.txt', 'w') as f:
        pass
    assert count_words('empty_file.txt') == expected_output
    
    # Test case 3: File with punctuation and mixed case
    input_text = "Hello, world! Hello everyone. This is a test."
    expected_output = {'hello': 3, 'world': 2, 'everyone': 1, 'this': 1, 'is': 1, 'a': 1, 'test': 1}
    with open('punctuation_file.txt', 'w') as f:
        f.write(input_text)
    assert count_words('punctuation_file.txt') == expected_output
    
    # Test case 4: File with words appearing more than 5 times
    input_text = "Hello world. Hello everyone! This is a test. Hello, hello, hello!"
    expected_output = {'hello': 7, 'world': 2, 'everyone': 1, 'this': 1, 'is': 1, 'a': 1, 'test': 1}
    with open('exaggerate_file.txt', 'w') as f:
        f.write(input_text)
    assert count_words('exaggerate_file.txt') == expected_output
    
    # Test case 5: File with non-ASCII characters
    input_text = "Привет мир! Привет всем!"
    expected_output = {'привет': 3, 'мир': 1, 'всем': 1}
    with open('non_ascii_file.txt', 'w', encoding='utf-8') as f:
        f.write(input_text)
    assert count_words('non_ascii_file.txt') == expected_output

def test_main(capsys):
    """Test the main function."""
    # Test case 1: Normal file
    input_text = "Hello world. Hello everyone! This is a test."
    with open('main_test_file.txt', 'w') as f:
        f.write(input_text)
    
    sys.argv[1:] = ['main_test_file.txt']
    main()
    captured = capsys.readouterr()
    assert "Word Counts:" in captured.out
    assert "hello: 3" in captured.out
    assert "world: 2" in captured.out

# Cleanup after tests
Path('empty_file.txt').unlink(missing_ok=True)
Path('punctuation_file.txt').unlink(missing_ok=True)
Path('exaggerate_file.txt').unlink(missing_ok=True)
Path('non_ascii_file.txt').unlink(missing_ok=True)
Path('main_test_file.txt').unlink(missing_ok=True)
```