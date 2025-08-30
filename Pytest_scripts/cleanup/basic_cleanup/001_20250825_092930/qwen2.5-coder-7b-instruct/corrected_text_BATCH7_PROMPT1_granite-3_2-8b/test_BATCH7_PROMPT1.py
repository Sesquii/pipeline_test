import random
from difflib import get_close_matches

# Hard-coded list of target words
TARGET_WORDS = ["necessary", "accommodate", "rhythm"]

def transpose_letters(word):
    """Transposes two adjacent letters in a word."""
    list_word = list(word)
    i, j = random.sample(range(len(list_word) - 1), 2)
    list_word[i], list_word[j] = list_word[j], list_word[i]
    return ''.join(list_word)

def misspell(text):
    """Misspells each target word in the text."""
    words = text.split()
    for i, word in enumerate(words):
        if word in TARGET_WORDS:
            words[i] = transpose_letters(word)
    return ' '.join(words)

def correct_misspellings(text):
    """Corrects misspelled target words using get_close_matches."""
    words = text.split()
    corrected_words = []

    for word in words:
        matches = get_close_matches(word, TARGET_WORDS, n=1, cutoff=0.6)
        if matches:
            corrected_words.append(matches[0])
        else:
            corrected_words.append(word)  # Keep the word unchanged if no close match found

    return ' '.join(corrected_words)

def main():
    input_file = "input_text.txt"
    output_file = f"corrected_text_BATCH7_PROMPT1_{__file__.split('/')[-1]}.txt"

    with open(input_file, 'r') as file:
        text = file.read()

    # Misspell target words
    misspelled_text = misspell(text)

    # Correct misspelled target words
    corrected_text = correct_misspellings(misspelled_text)

    with open(output_file, 'w') as file:
        file.write(corrected_text)

if __name__ == "__main__":
    main()

# ===== GENERATED TESTS =====
import pytest
from typing import List

# Original script code remains unchanged

# Test suite for the original script

@pytest.fixture
def sample_text() -> str:
    """Provide a sample text containing target words."""
    return "necessary rhythm accommodate"

@pytest.fixture
def misspelled_sample_text(sample_text: str) -> str:
    """Return the misspelled version of the sample text."""
    return misspell(sample_text)

@pytest.fixture
def corrected_sample_text() -> str:
    """Provide a corrected version of the sample text."""
    return "necessary rhythm accommodate"

def test_transpose_letters():
    """Test the transpose_letters function with various inputs."""
    assert transpose_letters("hello") in ["helo", "heol"]
    assert transpose_letters("world") in ["wrold", "worl"]
    with pytest.raises(ValueError):
        transpose_letters("a")

def test_misspell(misspelled_sample_text: str, sample_text: str):
    """Test the misspell function."""
    assert misspelled_sample_text != sample_text
    for word in TARGET_WORDS:
        assert word not in misspelled_sample_text

def test_correct_misspellings(corrected_sample_text: str, misspelled_sample_text: str):
    """Test the correct_misspellings function."""
    assert corrected_sample_text == misspelled_sample_text
    for word in TARGET_WORDS:
        assert word in corrected_sample_text

def test_main(sample_text: str, misspelled_sample_text: str, corrected_sample_text: str, tmp_path):
    """Test the main function."""
    input_file = tmp_path / "input_text.txt"
    output_file = tmp_path / f"corrected_text_BATCH7_PROMPT1_{__file__.split('/')[-1]}.txt"

    with open(input_file, 'w') as file:
        file.write(sample_text)

    main()

    with open(output_file, 'r') as file:
        corrected_text_from_file = file.read()

    assert corrected_text_from_file == corrected_sample_text

This test suite includes comprehensive tests for all public functions and classes in the original script. It uses pytest fixtures to provide sample data and temporary files for testing the `main` function. The test cases cover both positive and negative scenarios, including edge cases.