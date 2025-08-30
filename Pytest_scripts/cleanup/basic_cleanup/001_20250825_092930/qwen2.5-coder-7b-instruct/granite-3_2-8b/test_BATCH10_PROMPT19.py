import random
from collections import Counter

# Predefined list of less common but correctly spelled words
LESS_COMMON_WORDS = [
    "color", "favorite", "beautiful", "neighborhood", "occasionally", "unnecessary", 
    "mischievous", "independent", "restaurant", "government"
]

# Function to correct word by replacing it with a less common one
def self_correcting_spelling(word):
    # Check if the word is in LESS_COMMON_WORDS list
    corrected_word = random.choice([w for w in LESS_COMMON_WORDS if w != word])

    return corrected_word

# Function to check if a word exists in the less common words list
def is_less_common(word):
    return word in LESS_COMMON_WORDS

if __name__ == "__main__":
    # Example usage:
    input_word = input("Enter a word: ")
    
    corrected = self_correcting_spelling(input_word)
    print(f"Corrected Word: {corrected}")

    # Confirm if the corrected word is less common
    if is_less_common(corrected):
        print("The corrected word is indeed less common.")
    else:
        print("The corrected word might not be sufficiently less common.")

# ===== GENERATED TESTS =====
import pytest
from typing import List

# Predefined list of less common but correctly spelled words
LESS_COMMON_WORDS = [
    "color", "favorite", "beautiful", "neighborhood", "occasionally", "unnecessary", 
    "mischievous", "independent", "restaurant", "government"
]

# Function to correct word by replacing it with a less common one
def self_correcting_spelling(word: str) -> str:
    # Check if the word is in LESS_COMMON_WORDS list
    corrected_word = random.choice([w for w in LESS_COMMON_WORDS if w != word])

    return corrected_word

# Function to check if a word exists in the less common words list
def is_less_common(word: str) -> bool:
    return word in LESS_COMMON_WORDS

# Test suite for the self_correcting_spelling function
@pytest.fixture(params=["color", "favorite", "beautiful"])
def test_word(request):
    return request.param

def test_self_correcting_spelling(test_word: str):
    """
    Test that the self_correcting_spelling function returns a word from the LESS_COMMON_WORDS list.
    """
    corrected_word = self_correcting_spelling(test_word)
    assert corrected_word in LESS_COMMON_WORDS, "The corrected word is not in the less common words list."

def test_self_correcting_spelling_not_in_list():
    """
    Test that the self_correcting_spelling function returns a different word when the input word is in the list.
    """
    for word in LESS_COMMON_WORDS:
        corrected_word = self_correcting_spelling(word)
        assert corrected_word != word, "The corrected word should be different from the input word."

# Test suite for the is_less_common function
def test_is_less_common():
    """
    Test that the is_less_common function returns True for words in the LESS_COMMON_WORDS list.
    """
    for word in LESS_COMMON_WORDS:
        assert is_less_common(word), f"{word} should be considered less common."

def test_is_less_common_not_in_list():
    """
    Test that the is_less_common function returns False for words not in the LESS_COMMON_WORDS list.
    """
    non_less_common_words = ["apple", "banana", "carrot", "date"]
    for word in non_less_common_words:
        assert not is_less_common(word), f"{word} should not be considered less common."

# Test suite for the main functionality
def test_main(monkeypatch, capsys):
    """
    Test that the main functionality of the script works as expected.
    """
    # Mock user input and capture output
    monkeypatch.setattr('builtins.input', lambda _: 'color')
    
    # Run the main function
    import script  # Assuming the script is named 'script.py'
    
    # Capture the printed output
    captured = capsys.readouterr()
    
    # Check if the corrected word is in the output
    assert "Corrected Word: color" not in captured.out, "The original word should not be printed."
    assert "The corrected word is indeed less common." in captured.out, "The script should confirm that the corrected word is less common."

# Run the tests
if __name__ == "__main__":
    pytest.main()

This test suite covers all public functions and classes in the original script. It includes both positive and negative test cases, uses pytest fixtures and parametrization where appropriate, adds type hints to test functions, includes proper docstrings and comments, follows PEP 8 style guidelines, and adds a clear separator between the original code and test code.