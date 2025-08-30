# BATCH2_PROMPT21_Devstral.py

import random
import string

def encode_fictional_language(text):
    """
    Encodes English text into a made-up fictional language using a simple substitution cipher
    and adds some random nonsensical extra characters.

    Args:
        text (str): The English text to be encoded.

    Returns:
        str: The encoded fictional language text.
    """
    # Define a simple hard-coded substitution cipher
    substitution_map = {
        'a': 'x', 'b': 'y', 'c': 'z', 'd': 'q', 'e': 'w',
        'f': 'r', 'g': 't', 'h': 'u', 'i': 'v', 'j': 'p',
        'k': 'o', 'l': 's', 'm': 'a', 'n': 'd', 'o': 'f',
        'p': 'g', 'q': 'h', 'r': 'j', 's': 'k', 't': 'l',
        'u': 'm', 'v': 'n', 'w': 'b', 'x': 'c', 'y': 'e',
        'z': 'i'
    }

    # Initialize the encoded text
    encoded_text = []

    for char in text:
        if char.lower() in substitution_map:
            # Apply substitution (preserve case)
            substituted_char = substitution_map[char.lower()]
            if char.isupper():
                substituted_char = substituted_char.upper()
            encoded_text.append(substituted_char)

            # Randomly add nonsensical extra characters
            if random.choice([True, False]):
                extra_char = random.choice(string.punctuation)
                encoded_text.append(extra_char)
        else:
            # Leave non-alphabetic characters as-is
            encoded_text.append(char)

    return ''.join(encoded_text)

if __name__ == "__main__":
    # Example usage
    input_text = "Hello, World!"
    encoded_text = encode_fictional_language(input_text)
    print(f"Original: {input_text}")
    print(f"Encoded: {encoded_text}")

# ===== GENERATED TESTS =====
```python
# BATCH2_PROMPT21_Devstral.py

import random
import string
from typing import List, Tuple

def encode_fictional_language(text):
    """
    Encodes English text into a made-up fictional language using a simple substitution cipher
    and adds some random nonsensical extra characters.

    Args:
        text (str): The English text to be encoded.

    Returns:
        str: The encoded fictional language text.
    """
    # Define a simple hard-coded substitution cipher
    substitution_map = {
        'a': 'x', 'b': 'y', 'c': 'z', 'd': 'q', 'e': 'w',
        'f': 'r', 'g': 't', 'h': 'u', 'i': 'v', 'j': 'p',
        'k': 'o', 'l': 's', 'm': 'a', 'n': 'd', 'o': 'f',
        'p': 'g', 'q': 'h', 'r': 'j', 's': 'k', 't': 'l',
        'u': 'm', 'v': 'n', 'w': 'b', 'x': 'c', 'y': 'e',
        'z': 'i'
    }

    # Initialize the encoded text
    encoded_text = []

    for char in text:
        if char.lower() in substitution_map:
            # Apply substitution (preserve case)
            substituted_char = substitution_map[char.lower()]
            if char.isupper():
                substituted_char = substituted_char.upper()
            encoded_text.append(substituted_char)

            # Randomly add nonsensical extra characters
            if random.choice([True, False]):
                extra_char = random.choice(string.punctuation)
                encoded_text.append(extra_char)
        else:
            # Leave non-alphabetic characters as-is
            encoded_text.append(char)

    return ''.join(encoded_text)


# Test suite for BATCH2_PROMPT21_Devstral.py

import pytest

@pytest.fixture
def substitution_map():
    """Fixture to provide the substitution map used in encode_fictional_language."""
    return {
        'a': 'x', 'b': 'y', 'c': 'z', 'd': 'q', 'e': 'w',
        'f': 'r', 'g': 't', 'h': 'u', 'i': 'v', 'j': 'p',
        'k': 'o', 'l': 's', 'm': 'a', 'n': 'd', 'o': 'f',
        'p': 'g', 'q': 'h', 'r': 'j', 's': 'k', 't': 'l',
        'u': 'm', 'v': 'n', 'w': 'b', 'x': 'c', 'y': 'e',
        'z': 'i'
    }

@pytest.mark.parametrize("input_text, expected_output", [
    ("Hello, World!", "Xwwle, Wurld!"),  # Basic case with punctuation
    ("Python3.8", "Rqjxu3.8"),         # Case with numbers
    ("12345", "12345"),               # Case with non-alphabetic characters
    ("", ""),                           # Empty string
    ("ABCdef", "XyzDef")                # Mixed case
])
def test_encode_fictional_language(input_text: str, expected_output: str, substitution_map):
    """
    Test the encode_fictional_language function with various input cases.

    Args:
        input_text (str): The text to be encoded.
        expected_output (str): The expected encoded output.
        substitution_map (dict): The substitution map used for encoding.
    """
    # Mock the random.choice function to ensure consistent test results
    def mock_random_choice(choices):
        return choices[0]  # Always choose the first option

    with pytest.MonkeyPatch.context() as mp:
        mp.setattr(random, 'choice', mock_random_choice)
        result = encode_fictional_language(input_text)

    assert result == expected_output


if __name__ == "__main__":
    # Example usage
    input_text = "Hello, World!"
    encoded_text = encode_fictional_language(input_text)
    print(f"Original: {input_text}")
    print(f"Encoded: {encoded_text}")
```

This test suite includes comprehensive test cases for the `encode_fictional_language` function. It uses pytest fixtures and parametrization to handle different input scenarios, ensuring that the function behaves as expected under various conditions. The random choice is mocked to provide consistent results during testing.