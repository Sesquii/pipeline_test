import sys

def encode(text):
    original = 'abcdefghijklmnopqrstuvwxyz'
    substitution = 'zyxwvutsrqponmlkjihgfedcba'
    result = []
    for c in text.lower():
        if c in original:
            replaced = substitution[original.index(c)]
            result.append(replaced)
        else:
            result.append(c)
    # Add random, nonsensical characters
    result.extend(['-', '_', '*'])
    return ''.join(result)

if __name__ == "__main__":
    text = sys.stdin.read()
    encoded_text = encode(text)
    print(encoded_text)

# ===== GENERATED TESTS =====
import pytest

# Original script
def encode(text):
    original = 'abcdefghijklmnopqrstuvwxyz'
    substitution = 'zyxwvutsrqponmlkjihgfedcba'
    result = []
    for c in text.lower():
        if c in original:
            replaced = substitution[original.index(c)]
            result.append(replaced)
        else:
            result.append(c)
    # Add random, nonsensical characters
    result.extend(['-', '_', '*'])
    return ''.join(result)

if __name__ == "__main__":
    text = sys.stdin.read()
    encoded_text = encode(text)
    print(encoded_text)

# Test cases
def test_encode():
    """Test the encode function with various inputs."""
    assert encode('hello') == 'svool-*'
    assert encode('world') == 'dlrow-*'
    assert encode('Python') == '*nohtyP-*'
    assert encode('12345') == '12345-*'
    assert encode('!@#$%') == '!@#$%-*'

def test_encode_with_uppercase():
    """Test the encode function with uppercase inputs."""
    assert encode('Hello') == 'svool-*'
    assert encode('World') == 'dlrow-*'
    assert encode('Python') == '*nohtyP-*'

def test_encode_with_special_characters():
    """Test the encode function with special characters."""
    assert encode('@#$$%') == '@#$$%-*'
    assert encode('!@#$%^&*()_+') == '!@#$%^&*()_+-*'

def test_encode_with_empty_string():
    """Test the encode function with an empty string."""
    assert encode('') == '*-*'

def test_encode_with_whitespace():
    """Test the encode function with whitespace."""
    assert encode('   ') == '---*-'

This test suite includes comprehensive test cases for the `encode` function, covering various scenarios including lowercase letters, uppercase letters, special characters, empty strings, and whitespace. The tests are designed to ensure that the function behaves as expected under different conditions.