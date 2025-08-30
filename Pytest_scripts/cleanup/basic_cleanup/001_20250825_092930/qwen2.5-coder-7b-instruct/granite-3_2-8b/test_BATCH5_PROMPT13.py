import sys
from collections import Counter

# List of common words to exaggerate
COMMON_WORDS = ['the', 'a', 'an']
EXAGGERATION_FACTOR = 100


def count_words(file_path):
    """Count words in a text file, exaggerating common ones."""
    with open(file_path, 'r') as file:
        text = file.read().lower()

    # Split text into words and count occurrences
    word_counts = Counter(text.split())

    # Exaggerate counts for common words
    for word in COMMON_WORDS:
        if word in word_counts:
            word_counts[word] *= EXAGGERATION_FACTOR

    return word_counts


def print_word_counts(word_counts):
    """Print the word count dictionary."""
    for word, count in sorted(word_counts.items()):
        print(f'{word}: {count}')


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python exaggerated_word_counter.py <path_to_text_file>")
    else:
        file_path = sys.argv[1]
        word_counts = count_words(file_path)
        print_word_counts(word_counts)

# ===== GENERATED TESTS =====
import pytest
from io import StringIO
from contextlib import redirect_stdout

# Original script code
import sys
from collections import Counter

# List of common words to exaggerate
COMMON_WORDS = ['the', 'a', 'an']
EXAGGERATION_FACTOR = 100


def count_words(file_path):
    """Count words in a text file, exaggerating common ones."""
    with open(file_path, 'r') as file:
        text = file.read().lower()

    # Split text into words and count occurrences
    word_counts = Counter(text.split())

    # Exaggerate counts for common words
    for word in COMMON_WORDS:
        if word in word_counts:
            word_counts[word] *= EXAGGERATION_FACTOR

    return word_counts


def print_word_counts(word_counts):
    """Print the word count dictionary."""
    for word, count in sorted(word_counts.items()):
        print(f'{word}: {count}')


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python exaggerated_word_counter.py <path_to_text_file>")
    else:
        file_path = sys.argv[1]
        word_counts = count_words(file_path)
        print_word_counts(word_counts)

# Test cases
def test_count_words():
    """Test the count_words function."""
    # Create a temporary text file with some content
    with open('test.txt', 'w') as file:
        file.write("The quick brown fox jumps over the lazy dog. The dog barked.")

    # Call the function and capture the output
    with StringIO() as buffer, redirect_stdout(buffer):
        word_counts = count_words('test.txt')
        print_word_counts(word_counts)

    # Check if the output is correct
    expected_output = (
        "a: 100\n"
        "an: 100\n"
        "barked: 1\n"
        "brown: 1\n"
        "dog: 200\n"
        "fox: 1\n"
        "jumps: 1\n"
        "lazy: 1\n"
        "over: 1\n"
        "quick: 1\n"
        "the: 200\n"
    )
    assert buffer.getvalue() == expected_output

    # Clean up the temporary file
    import os
    os.remove('test.txt')


def test_count_words_with_no_file():
    """Test the count_words function with a non-existent file."""
    with pytest.raises(FileNotFoundError):
        count_words('non_existent_file.txt')


def test_print_word_counts():
    """Test the print_word_counts function."""
    word_counts = {'apple': 3, 'banana': 2, 'cherry': 5}
    expected_output = (
        "apple: 3\n"
        "banana: 2\n"
        "cherry: 5\n"
    )

    # Capture the output
    with StringIO() as buffer, redirect_stdout(buffer):
        print_word_counts(word_counts)

    assert buffer.getvalue() == expected_output


def test_print_word_counts_with_empty_dict():
    """Test the print_word_counts function with an empty dictionary."""
    word_counts = {}
    expected_output = ""

    # Capture the output
    with StringIO() as buffer, redirect_stdout(buffer):
        print_word_counts(word_counts)

    assert buffer.getvalue() == expected_output


# Run tests if this script is executed directly
if __name__ == "__main__":
    pytest.main()
