# BATCH6_PROMPT17_{model_name}.py

def encode_vowel(c):
    """Replace a vowel with the next consonant in the alphabet."""
    vowels = 'aeiouAEIOU'
    if c in vowels:
        if c == 'a' or c == 'A':
            return 'b'
        elif c == 'e' or c == 'E':
            return 'f'
        elif c == 'i' or c == 'I':
            return 'g'
        elif c == 'o' or c == 'O':
            return 'j'
        else:  # c is 'u' or 'U'
            return 'k'
    return c

def encode_text(text):
    """Encode an English text into the fictional language."""
    encoded_text = ''.join(encode_vowel(char) for char in text if char.isalpha())
    return encoded_text

if __name__ == "__main__":
    user_input = input("Enter a sentence to encode: ")
    result = encode_text(user_input)
    print("Encoded Text:", result)

# ===== GENERATED TESTS =====
# BATCH6_PROMPT17_{model_name}.py

def encode_vowel(c):
    """Replace a vowel with the next consonant in the alphabet."""
    vowels = 'aeiouAEIOU'
    if c in vowels:
        if c == 'a' or c == 'A':
            return 'b'
        elif c == 'e' or c == 'E':
            return 'f'
        elif c == 'i' or c == 'I':
            return 'g'
        elif c == 'o' or c == 'O':
            return 'j'
        else:  # c is 'u' or 'U'
            return 'k'
    return c

def encode_text(text):
    """Encode an English text into the fictional language."""
    encoded_text = ''.join(encode_vowel(char) for char in text if char.isalpha())
    return encoded_text

if __name__ == "__main__":
    user_input = input("Enter a sentence to encode: ")
    result = encode_text(user_input)
    print("Encoded Text:", result)

# Test suite
import pytest

def test_encode_vowel():
    """Test the encode_vowel function."""
    assert encode_vowel('a') == 'b'
    assert encode_vowel('A') == 'B'
    assert encode_vowel('e') == 'f'
    assert encode_vowel('E') == 'F'
    assert encode_vowel('i') == 'g'
    assert encode_vowel('I') == 'G'
    assert encode_vowel('o') == 'j'
    assert encode_vowel('O') == 'J'
    assert encode_vowel('u') == 'k'
    assert encode_vowel('U') == 'K'
    assert encode_vowel('b') == 'b'  # Non-vowel should return unchanged
    assert encode_vowel('B') == 'B'

def test_encode_text():
    """Test the encode_text function."""
    assert encode_text("hello") == "jellf"
    assert encode_text("HELLO") == "JELLO"
    assert encode_text("world") == "wurld"
    assert encode_text("World") == "Wurld"
    assert encode_text("Python") == "Pythpn"
    assert encode_text("12345") == ""
    assert encode_text("") == ""
    assert encode_text("aeiou") == "bfjgk"
    assert encode_text("AEIOU") == "BFJGK"

def test_encode_text_with_spaces():
    """Test the encode_text function with spaces."""
    assert encode_text("hello world") == "jellf wurld"
    assert encode_text("Hello World") == "Jellf Wurld"

def test_encode_text_with_punctuation():
    """Test the encode_text function with punctuation."""
    assert encode_text("hello, world!") == "jellf, wurld!"
    assert encode_text("Hello, World!") == "Jellf, Wurld!"

def test_encode_text_with_numbers():
    """Test the encode_text function with numbers."""
    assert encode_text("12345") == ""
    assert encode_text("hello123") == "jellf"

@pytest.mark.parametrize("input_text, expected_output", [
    ("hello", "jellf"),
    ("HELLO", "JELLO"),
    ("world", "wurld"),
    ("World", "Wurld"),
    ("Python", "Pythpn"),
    ("12345", ""),
    ("", ""),
    ("aeiou", "bfjgk"),
    ("AEIOU", "BFJGK"),
    ("hello, world!", "jellf, wurld!"),
    ("Hello, World!", "Jellf, Wurld!"),
    ("12345", ""),
    ("hello123", "jellf")
])
def test_encode_text_parametrized(input_text: str, expected_output: str):
    """Test the encode_text function with parametrization."""
    assert encode_text(input_text) == expected_output
