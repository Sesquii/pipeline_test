import re
from collections import defaultdict


def misspell_word(word):
    """Misspell a word by randomly swapping two letters."""
    if len(word) < 2:
        return word
    
    # Randomly choose two indices to swap
    indices = sorted(random.sample(range(len(word)), 2))
    list_word = list(word)
    list_word[indices[0]], list_word[indices[1]] = list_word[indices[1]], list_word[indices[0]]
    
    return ''.join(list_word)


def correct_spelling(misspelled, words):
    """Correct a misspelled word by finding the closest match in a dictionary."""
    min_distance = float('inf')
    corrected = None

    for w in words:
        distance = sum([1 for a, b in zip(misspelled, w) if a != b])  # Levenshtein distance
        if distance < min_distance:
            min_distance = distance
            corrected = w
    
    return corrected


def main():
    # Read the text file
    with open('input.txt', 'r') as f:
        text = f.read()

    words = re.findall(r'\b\w+\b', text)  # Extract all words

    misspelled_words = defaultdict(list)

    # Misspell every tenth word and keep track of them
    for i, word in enumerate(words):
        if (i + 1) % 10 == 0:
            misspelled_words[word].append(misspell_word(word))

    corrected_text = text

    # Correct each misspelled word
    for word, misspellings in misspelled_words.items():
        for misspelling in misspellings:
            corrected_word = correct_spelling(misspelling, words)
            corrected_text = re.sub(r'\b' + re.escape(misspelling) + r'\b', corrected_word, corrected_text, flags=re.IGNORECASE)

    print(corrected_text)


if __name__ == "__main__":
    main()

# ===== GENERATED TESTS =====
```python
import pytest
from io import StringIO
import random

# Original script code remains unchanged

def test_misspell_word():
    """Test the misspell_word function."""
    assert misspell_word("hello") == "helo" or misspell_word("hello") == "helol"
    assert misspell_word("a") == "a"
    assert misspell_word("") == ""

def test_correct_spelling():
    """Test the correct_spelling function."""
    words = ["apple", "banana", "cherry"]
    assert correct_spelling("aple", words) == "apple"
    assert correct_spelling("bnana", words) == "banana"
    assert correct_spelling("cherries", words) == "cherry"

def test_main():
    """Test the main function."""
    # Create a temporary input file
    with open('input.txt', 'w') as f:
        f.write("This is a test. This is only a test.")

    # Redirect stdout to capture output
    original_stdout = sys.stdout
    sys.stdout = captured_output = StringIO()

    # Run the main function
    main()

    # Restore stdout
    sys.stdout = original_stdout

    # Check if the output contains the corrected text
    assert "This is a test. This is only a test." in captured_output.getvalue()
```

Note: The `misspell_word` and `correct_spelling` functions are tested with simple assertions to check if they produce expected outputs. The `main` function is tested by creating a temporary input file, redirecting stdout to capture the output, running the main function, and then checking if the output contains the corrected text.