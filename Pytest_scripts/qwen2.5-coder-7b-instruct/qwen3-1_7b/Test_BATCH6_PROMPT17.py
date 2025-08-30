```python
import sys

def encode(text):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    mapping = {
        'a': 'b',
        'e': 'f',
        'i': 'j',
        'o': 'p',
        'u': 'v'
    }
    result = []
    for char in text:
        lower_char = char.lower()
        if lower_char in vowels:
            new_char = mapping[lower_char]
            if char.isupper():
                result.append(new_char.upper())
            else:
                result.append(new_char)
        else:
            result.append(char)
    return ''.join(result)

if __name__ == "__main__":
    input_text = sys.stdin.read()
    encoded_text = encode(input_text)
    print(encoded_text)

# ===== GENERATED TESTS =====
```python
import pytest

# Original code
import sys

def encode(text):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    mapping = {
        'a': 'b',
        'e': 'f',
        'i': 'j',
        'o': 'p',
        'u': 'v'
    }
    result = []
    for char in text:
        lower_char = char.lower()
        if lower_char in vowels:
            new_char = mapping[lower_char]
            if char.isupper():
                result.append(new_char.upper())
            else:
                result.append(new_char)
        else:
            result.append(char)
    return ''.join(result)

if __name__ == "__main__":
    input_text = sys.stdin.read()
    encoded_text = encode(input_text)
    print(encoded_text)


# Test cases
def test_encode_empty_string():
    """Test encoding an empty string."""
    assert encode('') == ''

def test_encode_no_vowels():
    """Test encoding a string with no vowels."""
    assert encode('bcdfghjklmnpqrstvwxyz') == 'bcdfghjklmnpqrstvwxyz'

def test_encode_all_vowels():
    """Test encoding a string with all vowels."""
    assert encode('aeiou') == 'bfjpv'

def test_encode_mixed_case():
    """Test encoding a mixed case string."""
    assert encode('Hello World!') == 'Hfllp Wprld!'

def test_encode_with_spaces_and_punctuation():
    """Test encoding a string with spaces and punctuation."""
    assert encode('Python 3.8') == 'Pythpn 3.8'

def test_encode_with_uppercase_vowels():
    """Test encoding a string with uppercase vowels."""
    assert encode('AEIOU') == 'BFJPV'

@pytest.mark.parametrize("input_text, expected_output", [
    ('', ''),
    ('bcdfghjklmnpqrstvwxyz', 'bcdfghjklmnpqrstvwxyz'),
    ('aeiou', 'bfjpv'),
    ('Hello World!', 'Hfllp Wprld!'),
    ('Python 3.8', 'Pythpn 3.8'),
    ('AEIOU', 'BFJPV')
])
def test_encode_parametrized(input_text: str, expected_output: str):
    """Test encoding with parametrization."""
    assert encode(input_text) == expected_output
```