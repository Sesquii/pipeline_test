import random

def encode_fictional_language(text):
    # Define a simple substitution cipher
    cipher = {
        'a': 'q', 'b': 'w', 'c': 'e', 'd': 'r', 'e': 't',
        'f': 'y', 'g': 'u', 'h': 'i', 'i': 'o', 'j': 'p',
        'k': 'a', 'l': 's', 'm': 'd', 'n': 'f', 'o': 'g',
        'p': 'h', 'q': 'j', 'r': 'k', 's': 'l', 't': 'z',
        'u': 'x', 'v': 'c', 'w': 'v', 'x': 'b', 'y': 'n',
        'z': 'm'
    }
    
    # Add random, nonsensical extra characters
    extra_chars = '1234567890!@#$%^&*()_+'
    for char in text:
        if char.isalpha():
            encoded_char = cipher.get(char.lower(), char)
            if random.choice([True, False]):
                encoded_char += random.choice(extra_chars)
            print(f"Original: {char}, Encoded: {encoded_char}")
        else:
            print(f"Original: {char}, Encoded: {char}")

if __name__ == "__main__":
    # Example usage
    input_text = "Hello, World!"
    encode_fictional_language(input_text)
```

This Python script defines a `encode_fictional_language` function that takes an English string and encodes it using a simple substitution cipher. It also adds random extra characters to some of the encoded letters for added complexity. The `if __name__ == "__main__":` block demonstrates how to use this function with an example input.

# ===== GENERATED TESTS =====
```python
import pytest

# Original script code remains unchanged

def test_encode_fictional_language():
    # Test case 1: Basic substitution cipher without extra characters
    text = "hello"
    expected_output = "qwehr"
    with pytest.raises(SystemExit) as excinfo:
        encode_fictional_language(text)
    assert 'Original: h, Encoded: q' in str(excinfo.value)
    assert 'Original: e, Encoded: w' in str(excinfo.value)
    assert 'Original: l, Encoded: e' in str(excinfo.value)
    assert 'Original: l, Encoded: e' in str(excinfo.value)
    assert 'Original: o, Encoded: r' in str(excinfo.value)

def test_encode_fictional_language_with_extra_chars():
    # Test case 2: Basic substitution cipher with extra characters
    text = "world"
    expected_output = "yuiop"
    with pytest.raises(SystemExit) as excinfo:
        encode_fictional_language(text)
    assert 'Original: w, Encoded: y' in str(excinfo.value)
    assert 'Original: o, Encoded: u' in str(excinfo.value)
    assert 'Original: r, Encoded: i' in str(excinfo.value)
    assert 'Original: l, Encoded: o' in str(excinfo.value)
    assert 'Original: d, Encoded: p' in str(excinfo.value)

def test_encode_fictional_language_with_non_alpha_chars():
    # Test case 3: Handling non-alphabetic characters
    text = "Hello, World!"
    expected_output = "qwehr, yuiop!"
    with pytest.raises(SystemExit) as excinfo:
        encode_fictional_language(text)
    assert 'Original: H, Encoded: q' in str(excinfo.value)
    assert 'Original: e, Encoded: w' in str(excinfo.value)
    assert 'Original: l, Encoded: e' in str(excinfo.value)
    assert 'Original: l, Encoded: e' in str(excinfo.value)
    assert 'Original: o, Encoded: r' in str(excinfo.value)
    assert 'Original: ,, Encoded: ,' in str(excinfo.value)
    assert 'Original: W, Encoded: y' in str(excinfo.value)
    assert 'Original: o, Encoded: u' in str(excinfo.value)
    assert 'Original: r, Encoded: i' in str(excinfo.value)
    assert 'Original: l, Encoded: o' in str(excinfo.value)
    assert 'Original: d, Encoded: p' in str(excinfo.value)
    assert 'Original: !, Encoded: !' in str(excinfo.value)

def test_encode_fictional_language_with_empty_string():
    # Test case 4: Handling empty string
    text = ""
    expected_output = ""
    with pytest.raises(SystemExit) as excinfo:
        encode_fictional_language(text)
    assert 'Original: ,, Encoded: ,' in str(excinfo.value)

def test_encode_fictional_language_with_long_string():
    # Test case 5: Handling long string
    text = "abcdefghijklmnopqrstuvwxyz"
    expected_output = "qwehrtyuiopasdfghjklzxcvbnm"
    with pytest.raises(SystemExit) as excinfo:
        encode_fictional_language(text)
    for char in 'abcdefghijklmnopqrstuvwxyz':
        assert f'Original: {char}, Encoded: {chr(ord(char) + 1)}' not in str(excinfo.value)

def test_encode_fictional_language_with_special_chars():
    # Test case 6: Handling special characters
    text = "Hello, World!@#"
    expected_output = "qwehr, yuiop!@#"
    with pytest.raises(SystemExit) as excinfo:
        encode_fictional_language(text)
    assert 'Original: H, Encoded: q' in str(excinfo.value)
    assert 'Original: e, Encoded: w' in str(excinfo.value)
    assert 'Original: l, Encoded: e' in str(excinfo.value)
    assert 'Original: l, Encoded: e' in str(excinfo.value)
    assert 'Original: o, Encoded: r' in str(excinfo.value)
    assert 'Original: ,, Encoded: ,' in str(excinfo.value)
    assert 'Original: W, Encoded: y' in str(excinfo.value)
    assert 'Original: o, Encoded: u' in str(excinfo.value)
    assert 'Original: r, Encoded: i' in str(excinfo.value)
    assert 'Original: l, Encoded: o' in str(excinfo.value)
    assert 'Original: d, Encoded: p' in str(excinfo.value)
    assert 'Original: !, Encoded: !' in str(excinfo.value)
    assert 'Original: @, Encoded: @' in str(excinfo.value)
    assert 'Original: #, Encoded: #' in str(excinfo.value)

def test_encode_fictional_language_with_mixed_case():
    # Test case 7: Handling mixed case
    text = "Hello, World!"
    expected_output = "qwehr, yuiop!"
    with pytest.raises(SystemExit) as excinfo:
        encode_fictional_language(text)
    assert 'Original: H, Encoded: q' in str(excinfo.value)
    assert 'Original: e, Encoded: w' in str(excinfo.value)
    assert 'Original: l, Encoded: e' in str(excinfo.value)
    assert 'Original: l, Encoded: e' in str(excinfo.value)
    assert 'Original: o, Encoded: r' in str(excinfo.value)
    assert 'Original: ,, Encoded: ,' in str(excinfo.value)
    assert 'Original: W, Encoded: y' in str(excinfo.value)
    assert 'Original: o, Encoded: u' in str(excinfo.value)
    assert 'Original: r, Encoded: i' in str(excinfo.value)
    assert 'Original: l, Encoded: o' in str(excinfo.value)
    assert 'Original: d, Encoded: p' in str(excinfo.value)
    assert 'Original: !, Encoded: !' in str(excinfo.value)

def test_encode_fictional_language_with_repeated_chars():
    # Test case 8: Handling repeated characters
    text = "aaa"
    expected_output = "qqq"
    with pytest.raises(SystemExit) as excinfo:
        encode_fictional_language(text)
    assert 'Original: a, Encoded: q' in str(excinfo.value)
    assert 'Original: a, Encoded: q' in str(excinfo.value)
    assert 'Original: a, Encoded: q' in str(excinfo.value)

def test_encode_fictional_language_with_single_char():
    # Test case 9: Handling single character
    text = "a"
    expected_output = "q"
    with pytest.raises(SystemExit) as excinfo:
        encode_fictional_language(text)
    assert 'Original: a, Encoded: q' in str(excinfo.value)

def test_encode_fictional_language_with_uppercase():
    # Test case 10: Handling uppercase
    text = "HELLO"
    expected_output = "QWEHR"
    with pytest.raises(SystemExit) as excinfo:
        encode_fictional_language(text)
    assert 'Original: H, Encoded: q' in str(excinfo.value)
    assert 'Original: E, Encoded: w' in str(excinfo.value)
    assert 'Original: L, Encoded: e' in str(excinfo.value)
    assert 'Original: L, Encoded: e' in str(excinfo.value)
    assert 'Original: O, Encoded: r' in str(excinfo.value)

def test_encode_fictional_language_with_lowercase():
    # Test case 11: Handling lowercase
    text = "hello"
    expected_output = "qwehr"
    with pytest.raises(SystemExit) as excinfo:
        encode_fictional_language(text)
    assert 'Original: h, Encoded: q' in str(excinfo.value)
    assert 'Original: e, Encoded: w' in str(excinfo.value)
    assert 'Original: l, Encoded: e' in str(excinfo.value)
    assert 'Original: l, Encoded: e' in str(excinfo.value)
    assert 'Original: o, Encoded: r' in str(excinfo.value)

def test_encode_fictional_language_with_numbers():
    # Test case 12: Handling numbers
    text = "123"
    expected_output = "123"
    with pytest.raises(SystemExit) as excinfo:
        encode_fictional_language(text)
    assert 'Original: 1, Encoded: 1' in str(excinfo.value)
    assert 'Original: 2, Encoded: 2' in str(excinfo.value)
    assert 'Original: 3, Encoded: 3' in str(excinfo.value)

def test_encode_fictional_language_with_special_chars_and_numbers():
    # Test case 13: Handling special characters and numbers
    text = "Hello, World!@#123"
    expected_output = "qwehr, yuiop!@#123"
    with pytest.raises(SystemExit) as excinfo:
        encode_fictional_language(text)
    assert 'Original: H, Encoded: q' in str(excinfo.value)
    assert 'Original: e, Encoded: w' in str(excinfo.value)
    assert 'Original: l, Encoded: e' in str(excinfo.value)
    assert 'Original: l, Encoded: e' in str(excinfo.value)
    assert 'Original: o, Encoded: r' in str(excinfo.value)
    assert 'Original: ,, Encoded: ,' in str(excinfo.value)
    assert 'Original: W, Encoded: y' in str(excinfo.value)
    assert 'Original: o, Encoded: u' in str(excinfo.value)
    assert 'Original: r, Encoded: i' in str(excinfo.value)
    assert 'Original: l, Encoded: o' in str(excinfo.value)
    assert 'Original: d, Encoded: p' in str(excinfo.value)
    assert 'Original: !, Encoded: !' in str(excinfo.value)
    assert 'Original: @, Encoded: @' in str(excinfo.value)
    assert 'Original: #, Encoded: #' in str(excinfo.value)
    assert 'Original: 1, Encoded: 1' in str(excinfo.value)
    assert 'Original: 2, Encoded: 2' in str(excinfo.value)
    assert 'Original: 3, Encoded: 3' in str(excinfo.value)

def test_encode_fictional_language_with_long_string_and_special_chars():
    # Test case 14: Handling long string and special characters
    text = "abcdefghijklmnopqrstuvwxyz!@#$%^&*()_+"
    expected_output = "qwehrtyuiopasdfghjklzxcvbnm!@#$%^&*()_+"
    with pytest.raises(SystemExit) as excinfo:
        encode_fictional_language(text)
    for char in 'abcdefghijklmnopqrstuvwxyz':
        assert f'Original: {char}, Encoded: {chr(ord(char) + 1)}' not in str(excinfo.value)

def test_encode_fictional_language_with_long_string_and_numbers():
    # Test case 15: Handling long string and numbers
    text = "abcdefghijklmnopqrstuvwxyz1234567890"
    expected_output = "qwehrtyuiopasdfghjklzxcvbnm1234567890"
    with pytest.raises(SystemExit) as excinfo:
        encode_fictional_language(text)
    for char in 'abcdefghijklmnopqrstuvwxyz':
        assert f'Original: {char}, Encoded: {chr(ord(char) + 1)}' not in str(excinfo.value)

def test_encode_fictional_language_with_long_string_and_special_chars_and_numbers():
    # Test case 16: Handling long string, special characters and numbers
    text = "abcdefghijklmnopqrstuvwxyz!@#$%^&*()_+1234567890"
    expected_output = "qwehrtyuiopasdfghjklzxcvbnm!@#$%^&*()_+1234567890"
    with pytest.raises(SystemExit) as excinfo:
        encode_fictional_language(text)
    for char in 'abcdefghijklmnopqrstuvwxyz':
        assert f'Original: {char}, Encoded: {chr(ord(char) + 1)}' not in str(excinfo.value)

def test_encode_fictional_language_with_long_string_and_repeated_chars():
    # Test case 17: Handling long string and repeated characters
    text = "aaaaaaaaaaaaaaa"
    expected_output = "qqqqqqqqqqqqqqq"
    with pytest.raises(SystemExit) as excinfo:
        encode_fictional_language(text)
    for char in 'aaaaaaaaaaaaaaa':
        assert f'Original: {char}, Encoded: q' not in str(excinfo.value)

def test_encode_fictional_language_with_long_string_and_single_char():
    # Test case 18: Handling long string and single character
    text = "a"
    expected_output = "q"
    with pytest.raises(SystemExit) as excinfo:
        encode_fictional_language(text)
    assert 'Original: a, Encoded: q' in str(excinfo.value)

def test_encode_fictional_language_with_long_string_and_uppercase():
    # Test case 19: Handling long string and uppercase
    text = "HELLO"
    expected_output = "QWEHR"
    with pytest.raises(SystemExit) as excinfo:
        encode_fictional_language(text)
    for char in 'HELLO':
        assert f'Original: {char}, Encoded: {chr(ord(char) + 1)}' not in str(excinfo.value)

def test_encode_fictional_language_with_long_string_and_lowercase():
    # Test case 20: Handling long string and lowercase
    text = "hello"
    expected_output = "qwehr"
    with pytest.raises(SystemExit) as excinfo:
        encode_fictional_language(text)
    for char in 'hello':
        assert f'Original: {char}, Encoded: {chr(ord(char) + 1)}' not in str(excinfo.value)

def test_encode_fictional_language_with_long_string_and_numbers():
    # Test case 21: Handling long string and numbers
    text = "1234567890"
    expected_output = "1234567890"
    with pytest.raises(SystemExit) as excinfo:
        encode_fictional_language(text)
    for char in '1234567890':
        assert f'Original: {char}, Encoded: {chr(ord(char) + 1)}' not in str(excinfo.value)

def test_encode_fictional_language_with_long_string_and_special_chars():
    # Test case 22: Handling long string and special characters
    text = "!@#$%^&*()_+"
    expected_output = "!@#$%^&*()_+"
    with pytest.raises(SystemExit) as excinfo:
        encode_fictional_language(text)
    for char in '!@#$%^&*()_+':
        assert f'Original: {char}, Encoded: {chr(ord(char) + 1)}' not in str(excinfo.value)

def test_encode_fictional_language_with_long_string_and_special_chars_and_numbers():
    # Test case 23: Handling long string, special characters and numbers
    text = "!@#$%^&*()_+1234567890"
    expected_output = "!@#$%^&*()_+1234567890"
    with pytest.raises(SystemExit) as excinfo:
        encode_fictional_language(text)
    for char in '!@#$%^&*()_+':
        assert f'Original: {char}, Encoded: {chr(ord(char) + 1)}' not in str(excinfo.value)

def test_encode_fictional_language_with_long_string_and_repeated_chars():
    # Test case 24: Handling long string and repeated characters
    text = "aaaaaaaaaaaaaaa"
    expected_output = "qqqqqqqqqqqqqqq"
    with pytest.raises(SystemExit) as excinfo:
        encode_fictional_language(text)
    for char in 'aaaaaaaaaaaaaaa':
        assert f'Original: {char}, Encoded: q' not in str(excinfo.value)

def test_encode_fictional_language_with_long_string_and_single_char():
    # Test case 25: Handling long string and single character
    text = "a"
    expected_output = "q"
    with pytest.raises(SystemExit) as excinfo:
        encode_fictional_language(text)
    assert 'Original: a, Encoded: q' in str(excinfo.value)

def test_encode_fictional_language_with_long_string_and_uppercase():
    # Test case 26: Handling long string and uppercase
    text = "HELLO"
    expected_output = "QWEHR"
    with pytest.raises(SystemExit) as excinfo:
        encode_fictional_language(text)
    for char in 'HELLO':
        assert f'Original: {char}, Encoded: {chr(ord(char) + 1)}' not in str(excinfo.value)

def test_encode_fictional_language_with_long_string_and_lowercase():
    # Test case 27: Handling long string and lowercase
    text = "hello"
    expected_output = "qwehr"
    with pytest.raises(SystemExit) as excinfo:
        encode_fictional_language(text)
    for char in 'hello':
        assert f'Original: {char}, Encoded: {chr(ord(char) + 1)}' not in str(excinfo.value)

def test_encode_fictional_language_with_long_string_and_numbers():
    # Test case 28: Handling long string and numbers
    text = "1234567890"
    expected_output = "1234567890"
    with pytest.raises(SystemExit) as excinfo:
        encode_fictional_language(text)
    for char in '1234567890':
        assert f'Original: {char}, Encoded: {chr(ord(char) + 1)}' not