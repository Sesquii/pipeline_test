# BATCH2_PROMPT21_Granite.py

import string
import random

def encode_text(text):
    """Encodes a given English text into a fictional language using a simple substitution cipher."""
    
    # Define the character mappings for encoding and decoding
    ENCODING = str.maketrans(
        'abcdefghijklmnopqrstuvwxyz',
        'vwxyzutsrqponmlkjihgfedcba'
    )

    RANDOM_CHARS = '!@#$%^&*()-_=+[]{}|;:,.<>?/`~'
    
    # Randomly add some nonsensical characters to the encoded text
    nonsense_chars = ''.join(random.choice(RANDOM_CHARS) for _ in range(len(text)))
    
    # Encode the original text
    encoded = text.translate(ENCODING) + nonsense_chars

    return encoded

def decode_text(encoded):
    """Decodes a fictional language text back to English."""
    
    # The reverse mapping of ENCODING for decoding
    DECODING = str.maketrans('vwxyzutsrqponmlkjihgfedcba', 'abcdefghijklmnopqrstuvwxyz')
    
    return encoded.translate(DECODING)

if __name__ == "__main__":
    # Example usage:
    original_text = "hello world"

    print("Original Text:", original_text)
    encoded_text = encode_text(original_text)
    print("Encoded Text:", encoded_text)

    decoded_text = decode_text(encoded_text)
    print("Decoded Text:", decoded_text)

# ===== GENERATED TESTS =====
```python
# BATCH2_PROMPT21_Granite.py

import string
import random
from typing import List, Tuple

def encode_text(text: str) -> str:
    """Encodes a given English text into a fictional language using a simple substitution cipher."""
    
    # Define the character mappings for encoding and decoding
    ENCODING = str.maketrans(
        'abcdefghijklmnopqrstuvwxyz',
        'vwxyzutsrqponmlkjihgfedcba'
    )

    RANDOM_CHARS = '!@#$%^&*()-_=+[]{}|;:,.<>?/`~'
    
    # Randomly add some nonsensical characters to the encoded text
    nonsense_chars = ''.join(random.choice(RANDOM_CHARS) for _ in range(len(text)))
    
    # Encode the original text
    encoded = text.translate(ENCODING) + nonsense_chars

    return encoded

def decode_text(encoded: str) -> str:
    """Decodes a fictional language text back to English."""
    
    # The reverse mapping of ENCODING for decoding
    DECODING = str.maketrans('vwxyzutsrqponmlkjihgfedcba', 'abcdefghijklmnopqrstuvwxyz')
    
    return encoded.translate(DECODING)

if __name__ == "__main__":
    # Example usage:
    original_text = "hello world"

    print("Original Text:", original_text)
    encoded_text = encode_text(original_text)
    print("Encoded Text:", encoded_text)

    decoded_text = decode_text(encoded_text)
    print("Decoded Text:", decoded_text)


# Test suite for BATCH2_PROMPT21_Granite.py

import pytest

def test_encode_text():
    """Test the encode_text function with various inputs."""
    
    # Positive test cases
    assert encode_text('hello') == 'dssol'
    assert encode_text('world') == 'vqjir'
    assert encode_text('python') == 'nvmxmf'
    assert encode_text('test123') == 'sdrw123'
    
    # Negative test cases
    with pytest.raises(TypeError):
        encode_text(123)
    with pytest.raises(TypeError):
        encode_text(None)

def test_decode_text():
    """Test the decode_text function with various inputs."""
    
    # Positive test cases
    assert decode_text('dssol') == 'hello'
    assert decode_text('vqjir') == 'world'
    assert decode_text('nvmxmf') == 'python'
    assert decode_text('sdrw123') == 'test123'
    
    # Negative test cases
    with pytest.raises(TypeError):
        decode_text(123)
    with pytest.raises(TypeError):
        decode_text(None)

def test_encode_decode_cycle():
    """Test the encode and decode functions in a cycle to ensure they are inverses of each other."""
    
    test_cases = [
        ('hello', 'dssol'),
        ('world', 'vqjir'),
        ('python', 'nvmxmf'),
        ('test123', 'sdrw123')
    ]
    
    for original, expected_encoded in test_cases:
        encoded = encode_text(original)
        decoded = decode_text(encoded)
        assert decoded == original, f"Decoding {encoded} did not return the original text: {original}"
        assert encoded.startswith(expected_encoded), f"Encoded {original} does not match expected prefix: {expected_encoded}"

def test_random_input():
    """Test the encode and decode functions with random input to ensure they handle unexpected characters correctly."""
    
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    encoded = encode_text(random_string)
    decoded = decode_text(encoded)
    assert decoded == random_string, f"Decoding {encoded} did not return the original text: {random_string}"
```