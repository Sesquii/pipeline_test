import sys
from collections import Counter

# List of common words to exaggerate
COMMON_WORDS = {"the", "a", "an", "and", "or", "but", "is", "are", "was", "were"}

def read_file(file_path):
    """Read the content of a file and return it as a string."""
    with open(file_path, 'r') as file:
        return file.read()

def count_words(text):
    """Count occurrences of each word in the text."""
    words = text.split()
    return Counter(words)

def exaggerate_counts(word_counts):
    """Exaggerate counts for common words."""
    exaggerated_counts = {}
    for word, count in word_counts.items():
        if word.lower() in COMMON_WORDS:
            # Exaggerate by multiplying the actual count by 10
            exaggerated_counts[word] = count * 10
        else:
            exaggerated_counts[word] = count
    return exaggerated_counts

def main():
    if len(sys.argv) != 2:
        print("Usage: python exaggerated_word_counter.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    text = read_file(file_path)
    word_counts = count_words(text)
    exaggerated_counts = exaggerate_counts(word_counts)

    print("Exaggerated Word Counts:")
    for word, count in exaggerated_counts.items():
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()

# ===== GENERATED TESTS =====
import pytest
from io import StringIO

# Original code
import sys
from collections import Counter

# List of common words to exaggerate
COMMON_WORDS = {"the", "a", "an", "and", "or", "but", "is", "are", "was", "were"}

def read_file(file_path):
    """Read the content of a file and return it as a string."""
    with open(file_path, 'r') as file:
        return file.read()

def count_words(text):
    """Count occurrences of each word in the text."""
    words = text.split()
    return Counter(words)

def exaggerate_counts(word_counts):
    """Exaggerate counts for common words."""
    exaggerated_counts = {}
    for word, count in word_counts.items():
        if word.lower() in COMMON_WORDS:
            # Exaggerate by multiplying the actual count by 10
            exaggerated_counts[word] = count * 10
        else:
            exaggerated_counts[word] = count
    return exaggerated_counts

def main():
    if len(sys.argv) != 2:
        print("Usage: python exaggerated_word_counter.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    text = read_file(file_path)
    word_counts = count_words(text)
    exaggerated_counts = exaggerate_counts(word_counts)

    print("Exaggerated Word Counts:")
    for word, count in exaggerated_counts.items():
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()

# Test cases
def test_read_file(monkeypatch):
    """Test the read_file function with a mock file."""
    monkeypatch.setattr('builtins.open', lambda x: StringIO("hello world hello"))
    assert read_file('dummy.txt') == "hello world hello"

@pytest.mark.parametrize("input_text, expected_output", [
    ("hello world hello", Counter({'hello': 2, 'world': 1})),
    ("", Counter()),
    ("one two three one", Counter({'one': 2, 'two': 1, 'three': 1}))
])
def test_count_words(input_text, expected_output):
    """Test the count_words function with different input texts."""
    assert count_words(input_text) == expected_output

@pytest.mark.parametrize("word_counts, expected_output", [
    (Counter({'hello': 2, 'world': 1}), {'hello': 20, 'world': 1}),
    (Counter({'the': 3, 'a': 2}), {'the': 30, 'a': 20}),
    (Counter({'and': 4, 'or': 5}), {'and': 40, 'or': 50})
])
def test_exaggerate_counts(word_counts, expected_output):
    """Test the exaggerate_counts function with different word counts."""
    assert exaggerate_counts(word_counts) == expected_output

def test_main(capsys, monkeypatch):
    """Test the main function with a mock file and capture output."""
    monkeypatch.setattr('sys.argv', ['exaggerated_word_counter.py', 'dummy.txt'])
    monkeypatch.setattr('builtins.open', lambda x: StringIO("hello world hello"))
    main()
    captured = capsys.readouterr()
    assert "Exaggerated Word Counts:" in captured.out
    assert "hello: 20" in captured.out
    assert "world: 1" in captured.out

def test_main_no_args(capsys):
    """Test the main function with no arguments."""
    monkeypatch.setattr('sys.argv', ['exaggerated_word_counter.py'])
    main()
    captured = capsys.readouterr()
    assert "Usage: python exaggerated_word_counter.py <file_path>" in captured.out
