# BATCH5_PROMPT5_Granite.py

import string
import random

def encode_text(text):
    """
    Encode given English text into a fictional language using a substitution cipher and nonsensical characters.
    
    Args:
        text (str): The English text to be encoded.
        
    Returns:
        str: Encoded text in the fictional language.
    """
    # Define a simple substitution cipher
    cipher = str.maketrans('abcdefghijklmnopqrstuvwxyz', 'uvwxzhjclmnprtsqkfioeaygbd')
    
    # Add some nonsensical characters for fun
    extra_chars = '!@#$%^&*()'
    
    # Encode the text using the cipher and add random extras
    encoded_text = ""
    for char in text.lower():
        if char in string.ascii_lowercase:
            encoded_text += cipher[string.ascii_lowercase.index(char)]
        elif char.isspace():
            encoded_text += ' '  # Keep spaces intact
        else:
            encoded_text += random.choice(extra_chars)
    
    return encoded_text

def main():
    """
    Main function to test the encoding process with sample text.
    """
    if __name__ == "__main__":
        # Test the encode_text function
        sample_text = "Hello, World!"
        print("Original Text:", sample_text)
        
        encoded = encode_text(sample_text)
        print("Encoded Text:", encoded)

if __name__ == "__main__":
    main()

# ===== GENERATED TESTS =====
# BATCH5_PROMPT5_Granite.py

import string
import random
from typing import List, Tuple

def encode_text(text: str) -> str:
    """
    Encode given English text into a fictional language using a substitution cipher and nonsensical characters.
    
    Args:
        text (str): The English text to be encoded.
        
    Returns:
        str: Encoded text in the fictional language.
    """
    # Define a simple substitution cipher
    cipher = str.maketrans('abcdefghijklmnopqrstuvwxyz', 'uvwxzhjclmnprtsqkfioeaygbd')
    
    # Add some nonsensical characters for fun
    extra_chars = '!@#$%^&*()'
    
    # Encode the text using the cipher and add random extras
    encoded_text = ""
    for char in text.lower():
        if char in string.ascii_lowercase:
            encoded_text += cipher[string.ascii_lowercase.index(char)]
        elif char.isspace():
            encoded_text += ' '  # Keep spaces intact
        else:
            encoded_text += random.choice(extra_chars)
    
    return encoded_text

def main():
    """
    Main function to test the encoding process with sample text.
    """
    if __name__ == "__main__":
        # Test the encode_text function
        sample_text = "Hello, World!"
        print("Original Text:", sample_text)
        
        encoded = encode_text(sample_text)
        print("Encoded Text:", encoded)

# BATCH5_PROMPT5_Granite_test.py

import pytest
from BATCH5_PROMPT5_Granite import encode_text

def test_encode_text():
    """
    Test the encode_text function with various inputs.
    """
    # Positive test cases
    assert "jgppq, yqtnf!" == encode_text("Hello, World!")
    assert "wxyzy" == encode_text("abcde")
    assert "  " == encode_text("  ")
    
    # Negative test cases
    with pytest.raises(TypeError):
        encode_text(12345)
    with pytest.raises(ValueError):
        encode_text("")

# Test with parametrization to check multiple inputs at once
@pytest.mark.parametrize("input_text, expected_output", [
    ("Hello, World!", "jgppq, yqtnf!"),
    ("abcde", "wxyzy"),
    ("  ", "  "),
])
def test_encode_text_parametrized(input_text: str, expected_output: str):
    """
    Test the encode_text function with parametrized inputs.
    """
    assert encode_text(input_text) == expected_output

# Test with fixture to provide a consistent input for multiple tests
@pytest.fixture
def sample_input():
    return "Hello, World!"

def test_encode_text_with_fixture(sample_input: str):
    """
    Test the encode_text function using a pytest fixture.
    """
    encoded = encode_text(sample_input)
    assert isinstance(encoded, str)
    assert len(encoded) == len(sample_input)

# Test with multiple inputs and outputs
@pytest.mark.parametrize("input_text, expected_output", [
    ("Hello, World!", "jgppq, yqtnf!"),
    ("abcde", "wxyzy"),
    ("  ", "  "),
])
def test_encode_text_with_multiple_inputs_outputs(input_text: str, expected_output: str):
    """
    Test the encode_text function with multiple inputs and outputs.
    """
    encoded = encode_text(input_text)
    assert encoded == expected_output

This test suite includes comprehensive test cases for the `encode_text` function in the original script. It covers both positive and negative scenarios, uses pytest fixtures and parametrization where appropriate, adds type hints to test functions, includes proper docstrings and comments, follows PEP 8 style guidelines, and clearly separates the original code from the test code.