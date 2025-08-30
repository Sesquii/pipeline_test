# BATCH3_PROMPT21_Granite.py

import string
import random
from collections import defaultdict

# Define a simple substitution cipher mapping
CIPHER = str.maketrans(
    'abcdefghijklmnopqrstuvwxyz', 
    'qwertyuiopasdfghjklzxcvbnm'
)

# List of extra nonsensical characters
EXTRA_CHARS = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

def encode(text):
    """Encode the input text into our fictional language."""
    
    # Create a dictionary for random substitution of some letters with extras
    random.shuffle(EXTRA_CHARS)
    subst_dict = {char: extra_char for char, extra_char in zip('bcdfghjklmnpqrstvwxyz', EXTRA_CHARS)}
    
    encoded_text = ""
    for char in text.lower():
        if char in subst_dict:
            # Use random substitution for vowels and some consonants
            encoded_text += random.choice(list(subst_dict.values()))
        elif char in 'aeiou':
            # Keep vowels unchanged for simplicity
            encoded_text += char
        else:
            # Apply standard cipher to other letters
            encoded_text += CHARS[CHAR_MAP[char]]
    
    return encoded_text

# Create a mapping for the cipher
CHARS = 'abcdefghijklmnopqrstuvwxyz'
CHAR_MAP = defaultdict(str)
for i, char in enumerate(CHARS):
    CHAR_MAP[char] = CHARS[(i + CIPHER.make_trans('', '', string.ascii_lowercase).find(char)) % len(CHARS)]

def main():
    """Entry point of the program."""
    
    print("Fictional Language Encoder")
    text = input("Enter your English text: ")
    encoded = encode(text)
    print("Encoded Text:", encoded)

if __name__ == "__main__":
    main()

# ===== GENERATED TESTS =====
# BATCH3_PROMPT21_Granite.py

import string
import random
from collections import defaultdict
import pytest

# Define a simple substitution cipher mapping
CIPHER = str.maketrans(
    'abcdefghijklmnopqrstuvwxyz', 
    'qwertyuiopasdfghjklzxcvbnm'
)

# List of extra nonsensical characters
EXTRA_CHARS = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

def encode(text):
    """Encode the input text into our fictional language."""
    
    # Create a dictionary for random substitution of some letters with extras
    random.shuffle(EXTRA_CHARS)
    subst_dict = {char: extra_char for char, extra_char in zip('bcdfghjklmnpqrstvwxyz', EXTRA_CHARS)}
    
    encoded_text = ""
    for char in text.lower():
        if char in subst_dict:
            # Use random substitution for vowels and some consonants
            encoded_text += random.choice(list(subst_dict.values()))
        elif char in 'aeiou':
            # Keep vowels unchanged for simplicity
            encoded_text += char
        else:
            # Apply standard cipher to other letters
            encoded_text += CHARS[CHAR_MAP[char]]
    
    return encoded_text

# Create a mapping for the cipher
CHARS = 'abcdefghijklmnopqrstuvwxyz'
CHAR_MAP = defaultdict(str)
for i, char in enumerate(CHARS):
    CHAR_MAP[char] = CHARS[(i + CIPHER.make_trans('', '', string.ascii_lowercase).find(char)) % len(CHARS)]

def main():
    """Entry point of the program."""
    
    print("Fictional Language Encoder")
    text = input("Enter your English text: ")
    encoded = encode(text)
    print("Encoded Text:", encoded)

if __name__ == "__main__":
    main()

# Test suite for BATCH3_PROMPT21_Granite.py

def test_encode():
    """Test the encode function with various inputs."""
    
    # Positive test cases
    assert encode("hello") in ['h', 'e', 'l', 'l', 'o']
    assert encode("world") in ['w', 'o', 'r', 'l', 'd']
    assert encode("python") in ['p', 'y', 't', 'h', 'o', 'n']
    
    # Negative test cases
    with pytest.raises(TypeError):
        encode(123)
    with pytest.raises(ValueError):
        encode('')

def test_encode_with_special_chars():
    """Test the encode function with special characters."""
    
    # Positive test cases
    assert encode("hello!") in ['h', 'e', 'l', 'l', 'o!']
    assert encode("world@") in ['w', 'o', 'r', 'l', 'd@']
    assert encode("python$") in ['p', 'y', 't', 'h', 'o', 'n$']
    
    # Negative test cases
    with pytest.raises(TypeError):
        encode(123)
    with pytest.raises(ValueError):
        encode('')

def test_encode_with_uppercase():
    """Test the encode function with uppercase letters."""
    
    # Positive test cases
    assert encode("Hello") in ['h', 'e', 'l', 'l', 'o']
    assert encode("World") in ['w', 'o', 'r', 'l', 'd']
    assert encode("Python") in ['p', 'y', 't', 'h', 'o', 'n']
    
    # Negative test cases
    with pytest.raises(TypeError):
        encode(123)
    with pytest.raises(ValueError):
        encode('')

def test_encode_with_numbers():
    """Test the encode function with numbers."""
    
    # Positive test cases
    assert encode("123") == "123"
    assert encode("456") == "456"
    assert encode("789") == "789"
    
    # Negative test cases
    with pytest.raises(TypeError):
        encode(123)
    with pytest.raises(ValueError):
        encode('')

def test_encode_with_empty_string():
    """Test the encode function with an empty string."""
    
    # Positive test cases
    assert encode("") == ""
    
    # Negative test cases
    with pytest.raises(ValueError):
        encode('')