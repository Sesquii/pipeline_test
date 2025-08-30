# BATCH8_PROMPT11_Granite.py

import re
from collections import Counter


def read_file(filepath):
    """Reads content from a given file path."""
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()


def word_counter(text, positive_words):
    """Counts words in the text and exaggerates counts for positive words."""
    # Convert all to lower case for uniformity
    text = text.lower()

    # Find all words using regex, ignore punctuation
    words = re.findall(r'\b\w+\b', text)

    word_counts = Counter(words)

    # Exaggerate count for positive words
    exaggerated_counts = {}
    for word in positive_words:
        if word in word_counts:
            exaggerated_counts[word] = 100 * word_counts[word]
        else:
            exaggerated_counts[word] = word_counts.get(word, 0)

    return exaggerated_counts


def print_results(counter):
    """Prints the dictionary of word counts."""
    for word, count in counter.items():
        print(f"{word}: {count}")


def main():
    # Define positive words list
    POSITIVE_WORDS = ['love', 'happy', 'great']

    # Read file content
    text = read_file('input.txt')

    # Count words and exaggerate for positive ones
    word_counts = word_counter(text, POSITIVE_WORDS)

    # Print the results
    print_results(word_counts)


if __name__ == "__main__":
    main()

# ===== GENERATED TESTS =====
# BATCH8_PROMPT11_Granite.py

import re
from collections import Counter


def read_file(filepath):
    """Reads content from a given file path."""
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()


def word_counter(text: str, positive_words: list) -> dict:
    """Counts words in the text and exaggerates counts for positive words."""
    # Convert all to lower case for uniformity
    text = text.lower()

    # Find all words using regex, ignore punctuation
    words = re.findall(r'\b\w+\b', text)

    word_counts = Counter(words)

    # Exaggerate count for positive words
    exaggerated_counts = {}
    for word in positive_words:
        if word in word_counts:
            exaggerated_counts[word] = 100 * word_counts[word]
        else:
            exaggerated_counts[word] = word_counts.get(word, 0)

    return exaggerated_counts


def print_results(counter: dict):
    """Prints the dictionary of word counts."""
    for word, count in counter.items():
        print(f"{word}: {count}")


def main():
    # Define positive words list
    POSITIVE_WORDS = ['love', 'happy', 'great']

    # Read file content
    text = read_file('input.txt')

    # Count words and exaggerate for positive ones
    word_counts = word_counter(text, POSITIVE_WORDS)

    # Print the results
    print_results(word_counts)


if __name__ == "__main__":
    main()

# Test suite for BATCH8_PROMPT11_Granite.py

import pytest
from io import StringIO
from unittest.mock import patch


def test_read_file():
    """Test read_file function."""
    with patch('builtins.open', mock_open(read_data='test content')):
        assert read_file('test.txt') == 'test content'


@pytest.mark.parametrize("text, positive_words, expected", [
    ("I love programming. It is happy and great.", ['love', 'happy', 'great'], {'love': 100, 'happy': 100, 'great': 100}),
    ("No positive words here.", [], {}),
    ("Mixed case with punctuation!", ['case'], {'case': 200})
])
def test_word_counter(text: str, positive_words: list, expected: dict):
    """Test word_counter function."""
    assert word_counter(text, positive_words) == expected


@pytest.mark.parametrize("counter", [
    {'love': 100, 'happy': 100, 'great': 100},
    {},
    {'no': 50}
])
def test_print_results(counter: dict):
    """Test print_results function."""
    with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        print_results(counter)
        assert mock_stdout.getvalue() == '\n'.join([f"{word}: {count}" for word, count in counter.items()]) + '\n'


def test_main():
    """Test main function."""
    with patch('builtins.open', mock_open(read_data='I love programming. It is happy and great.')):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            main()
            assert 'love: 100' in mock_stdout.getvalue()
            assert 'happy: 100' in mock_stdout.getvalue()
            assert 'great: 100' in mock_stdout.getvalue()
