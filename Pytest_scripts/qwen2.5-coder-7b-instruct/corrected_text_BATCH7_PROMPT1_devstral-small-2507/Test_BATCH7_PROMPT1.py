import random
import re

def transpose_two_letters(word):
    """Transpose two random adjacent letters in a word."""
    word_list = list(word)
    if len(word_list) < 2:
        return word

    # Choose two random adjacent positions
    i = random.randint(0, len(word_list) - 2)
    word_list[i], word_list[i + 1] = word_list[i + 1], word_list[i]

    return ''.join(word_list)

def find_and_correct_misspellings(text, target_words):
    """Find and correct misspelled words in the text."""
    corrected_text = text
    for word in target_words:
        # Create a pattern to match the word with transposed letters
        pattern = re.compile(r'\b' + re.escape(word) + r'\b')
        for misspelling in set(get_all_misspellings(word)):
            if misspelling != word:  # Skip the original word
                corrected_text = re.sub(re.escape(misspelling), word, corrected_text)
    return corrected_text

def get_all_misspellings(word):
    """Generate all possible misspellings by transposing adjacent letters."""
    misspellings = set()
    for i in range(len(word) - 1):
        # Create a misspelling by transposing two adjacent letters
        word_list = list(word)
        word_list[i], word_list[i + 1] = word_list[i + 1], word_list[i]
        misspelling = ''.join(word_list)
        if misspelling != word:
            misspellings.add(misspelling)
    return misspellings

def main():
    # Target words to be corrected
    target_words = ["necessary", "accommodate", "rhythm", "committee", "address",
                    "occur", "separate", "consensus", "hierarchy", "parallel"]

    # Read the input text file
    with open("input_text.txt", "r") as file:
        text = file.read()

    # Introduce misspellings in the target words
    for word in target_words:
        pattern = re.compile(r'\b' + re.escape(word) + r'\b')
        misspelling = transpose_two_letters(word)
        text = pattern.sub(misspelling, text)

    # Correct all misspellings in the text
    corrected_text = find_and_correct_misspellings(text, target_words)

    # Write the corrected text to a new file
    output_filename = "corrected_text_BATCH7_PROMPT1_Devstral.txt"
    with open(output_filename, "w") as file:
        file.write(corrected_text)

    print(f"Corrected text has been written to {output_filename}")

if __name__ == "__main__":
    main()

# ===== GENERATED TESTS =====
```python
import pytest
from typing import List

# Original code remains unchanged

# Test suite for the script

def test_transpose_two_letters():
    """Test the transpose_two_letters function."""
    assert transpose_two_letters("hello") in ["helo", "heol"]
    assert transpose_two_letters("a") == "a"
    assert transpose_two_letters("") == ""

def test_find_and_correct_misspellings():
    """Test the find_and_correct_misspellings function."""
    text = "I need to accomodate the rhythm of the committee."
    target_words = ["accommodate", "rhythm", "committee"]
    corrected_text = find_and_correct_misspellings(text, target_words)
    assert "I need to accommodate the rhythm of the committee." in corrected_text

def test_get_all_misspellings():
    """Test the get_all_misspellings function."""
    word = "accommodate"
    misspellings = get_all_misspellings(word)
    assert len(misspellings) == 9
    for misspelling in misspellings:
        assert transpose_two_letters(word) in [misspelling, word]

# Test cases using pytest fixtures and parametrization

@pytest.fixture(params=["hello", "world", "python"])
def sample_word(request):
    """Fixture to provide sample words for testing."""
    return request.param

def test_transpose_two_letters_with_fixture(sample_word: str):
    """Test the transpose_two_letters function with a fixture."""
    result = transpose_two_letters(sample_word)
    assert isinstance(result, str)
    assert len(result) == len(sample_word)

@pytest.fixture(params=["accommodate", "rhythm", "committee"])
def sample_target_word(request):
    """Fixture to provide sample target words for testing."""
    return request.param

def test_find_and_correct_misspellings_with_fixture(sample_target_word: str):
    """Test the find_and_correct_misspellings function with a fixture."""
    text = f"I need to {sample_target_word} the rhythm of the committee."
    corrected_text = find_and_correct_misspellings(text, [sample_target_word])
    assert sample_target_word in corrected_text

def test_get_all_misspellings_with_fixture(sample_target_word: str):
    """Test the get_all_misspellings function with a fixture."""
    misspellings = get_all_misspellings(sample_target_word)
    assert isinstance(misspellings, set)
    for misspelling in misspellings:
        assert transpose_two_letters(sample_target_word) in [misspelling, sample_target_word]
```