# BATCH5_PROMPT5_{{model_name}}.py

import random
import string

# Define a simple substitution cipher mapping English letters to fictional language characters
SUBSTITUTION_CIPHER = {
    'a': 'q', 'b': 'w', 'c': 'e', 'd': 'r', 'e': 't',
    'f': 'y', 'g': 'u', 'h': 'i', 'i': 'o', 'j': 'p',
    'k': 'a', 'l': 's', 'm': 'd', 'n': 'f', 'o': 'g',
    'p': 'h', 'q': 'j', 'r': 'k', 's': 'l', 't': 'z',
    'u': 'x', 'v': 'c', 'w': 'v', 'x': 'b', 'y': 'n',
    'z': 'm'
}

# Define a list of random, nonsensical extra characters to add to the fictional language
EXTRA_CHARACTERS = ['@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+']

def encode_text(text):
    """
    Encodes a given string of English text into a made-up "language" using a substitution cipher and random extra characters.
    
    Parameters:
    - text (str): The input English text to be encoded.
    
    Returns:
    - str: The encoded text in the fictional language.
    """
    # Shuffle the list of extra characters
    shuffled_extra_chars = random.sample(EXTRA_CHARACTERS, len(EXTRA_CHARACTERS))
    
    # Create a mapping from original letters to shuffled extra characters
    letter_to_extra_char = dict(zip(SUBSTITUTION_CIPHER.keys(), shuffled_extra_chars))
    
    # Encode each character in the input text
    encoded_text = []
    for char in text:
        if char.lower() in SUBSTITUTION_CIPHER:
            # Convert to lower case and replace with extra character
            new_char = letter_to_extra_char[char.lower()]
        else:
            # Keep non-English characters as is
            new_char = char
        
        encoded_text.append(new_char)
    
    return ''.join(encoded_text)

if __name__ == "__main__":
    # Example usage
    input_text = "Hello, world!"
    encoded_text = encode_text(input_text)
    print("Original Text:", input_text)
    print("Encoded Text:", encoded_text)

This Python script defines a simple substitution cipher and a list of random extra characters to create a fictional language. The `encode_text` function takes an English string as input and encodes it into the fictional language by replacing each letter according to the substitution cipher and adding a randomly chosen extra character from the predefined list. The script includes a basic entry point for demonstration purposes.

# ===== GENERATED TESTS =====
# BATCH5_PROMPT5_{{model_name}}.py

import random
import string
from typing import List

# Define a simple substitution cipher mapping English letters to fictional language characters
SUBSTITUTION_CIPHER = {
    'a': 'q', 'b': 'w', 'c': 'e', 'd': 'r', 'e': 't',
    'f': 'y', 'g': 'u', 'h': 'i', 'i': 'o', 'j': 'p',
    'k': 'a', 'l': 's', 'm': 'd', 'n': 'f', 'o': 'g',
    'p': 'h', 'q': 'j', 'r': 'k', 's': 'l', 't': 'z',
    'u': 'x', 'v': 'c', 'w': 'v', 'x': 'b', 'y': 'n',
    'z': 'm'
}

# Define a list of random, nonsensical extra characters to add to the fictional language
EXTRA_CHARACTERS = ['@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+']

def encode_text(text: str) -> str:
    """
    Encodes a given string of English text into a made-up "language" using a substitution cipher and random extra characters.
    
    Parameters:
    - text (str): The input English text to be encoded.
    
    Returns:
    - str: The encoded text in the fictional language.
    """
    # Shuffle the list of extra characters
    shuffled_extra_chars = random.sample(EXTRA_CHARACTERS, len(EXTRA_CHARACTERS))
    
    # Create a mapping from original letters to shuffled extra characters
    letter_to_extra_char = dict(zip(SUBSTITUTION_CIPHER.keys(), shuffled_extra_chars))
    
    # Encode each character in the input text
    encoded_text = []
    for char in text:
        if char.lower() in SUBSTITUTION_CIPHER:
            # Convert to lower case and replace with extra character
            new_char = letter_to_extra_char[char.lower()]
        else:
            # Keep non-English characters as is
            new_char = char
        
        encoded_text.append(new_char)
    
    return ''.join(encoded_text)

if __name__ == "__main__":
    # Example usage
    input_text = "Hello, world!"
    encoded_text = encode_text(input_text)
    print("Original Text:", input_text)
    print("Encoded Text:", encoded_text)


# Test cases for the encode_text function

import pytest

@pytest.fixture
def substitution_cipher():
    return SUBSTITUTION_CIPHER

@pytest.fixture
def extra_characters():
    return EXTRA_CHARACTERS

def test_encode_text_with_lowercase(substitution_cipher, extra_characters):
    """
    Test encoding with lowercase input text.
    """
    input_text = "hello"
    encoded_text = encode_text(input_text)
    assert all(char in substitution_cipher.values() for char in encoded_text)

def test_encode_text_with_uppercase(substitution_cipher, extra_characters):
    """
    Test encoding with uppercase input text.
    """
    input_text = "HELLO"
    encoded_text = encode_text(input_text)
    assert all(char in substitution_cipher.values() for char in encoded_text)

def test_encode_text_with_mixed_case(substitution_cipher, extra_characters):
    """
    Test encoding with mixed case input text.
    """
    input_text = "HeLlO"
    encoded_text = encode_text(input_text)
    assert all(char in substitution_cipher.values() for char in encoded_text)

def test_encode_text_with_non_english_chars(substitution_cipher, extra_characters):
    """
    Test encoding with non-English characters.
    """
    input_text = "!@#$%^&*()"
    encoded_text = encode_text(input_text)
    assert all(char in input_text for char in encoded_text)

def test_encode_text_with_empty_string(substitution_cipher, extra_characters):
    """
    Test encoding with an empty string.
    """
    input_text = ""
    encoded_text = encode_text(input_text)
    assert encoded_text == ""

def test_encode_text_with_spaces(substitution_cipher, extra_characters):
    """
    Test encoding with spaces in the input text.
    """
    input_text = "Hello World"
    encoded_text = encode_text(input_text)
    assert ' ' not in encoded_text

def test_encode_text_with_repeated_chars(substitution_cipher, extra_characters):
    """
    Test encoding with repeated characters in the input text.
    """
    input_text = "aaa"
    encoded_text = encode_text(input_text)
    assert all(encoded_text[i] == encoded_text[0] for i in range(1, len(encoded_text)))

def test_encode_text_with_long_string(substitution_cipher, extra_characters):
    """
    Test encoding with a long string.
    """
    input_text = "abcdefghijklmnopqrstuvwxyz"
    encoded_text = encode_text(input_text)
    assert all(char in substitution_cipher.values() for char in encoded_text)

def test_encode_text_with_special_chars(substitution_cipher, extra_characters):
    """
    Test encoding with special characters.
    """
    input_text = "!@#$%^&*()"
    encoded_text = encode_text(input_text)
    assert all(char in input_text for char in encoded_text)

def test_encode_text_with_numbers(substitution_cipher, extra_characters):
    """
    Test encoding with numbers.
    """
    input_text = "1234567890"
    encoded_text = encode_text(input_text)
    assert all(char in input_text for char in encoded_text)

def test_encode_text_with_unicode_chars(substitution_cipher, extra_characters):
    """
    Test encoding with Unicode characters.
    """
    input_text = "你好，世界！"
    encoded_text = encode_text(input_text)
    assert all(char == input_text[i] for i, char in enumerate(encoded_text))

