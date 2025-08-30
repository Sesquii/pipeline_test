def vigenere_encrypt(text, key):
    key_values = [ord(c) - ord('A') for c in key]
    encrypted = []
    for i, char in enumerate(text):
        if char.isalpha():
            shift = key_values[i % len(key)]
            base = ord('A')
            new_index = (ord(char) - base + shift) % 26
            new_char = chr(new_index + base)
            encrypted.append(new_char)
        else:
            encrypted.append(char)
    return ''.join(encrypted)

if __name__ == "__main__":
    import sys
    text = input("Enter the English text to encode: ")
    key = 'GIBBERISH'
    encrypted_text = vigenere_encrypt(text, key)
    print(encrypted_text)

# ===== GENERATED TESTS =====
import pytest

def vigenere_encrypt(text, key):
    key_values = [ord(c) - ord('A') for c in key]
    encrypted = []
    for i, char in enumerate(text):
        if char.isalpha():
            shift = key_values[i % len(key)]
            base = ord('A')
            new_index = (ord(char) - base + shift) % 26
            new_char = chr(new_index + base)
            encrypted.append(new_char)
        else:
            encrypted.append(char)
    return ''.join(encrypted)

# Test suite for the vigenere_encrypt function

def test_vigenere_encrypt():
    """Test cases for vigenere_encrypt function"""
    
    # Positive test cases
    assert vigenere_encrypt("HELLO", "GIBBERISH") == "KHOOR"
    assert vigenere_encrypt("hello", "gibberish") == "khoor"
    assert vigenere_encrypt("Python3.8", "GIBBERISH") == "Sbwkrq3.8"
    
    # Negative test cases
    with pytest.raises(TypeError):
        vigenere_encrypt(123, "GIBBERISH")
    with pytest.raises(TypeError):
        vigenere_encrypt("HELLO", 123)
    with pytest.raises(ValueError):
        vigenere_encrypt("", "GIBBERISH")

def test_vigenere_encrypt_with_non_alpha():
    """Test cases for vigenere_encrypt function with non-alphabetic characters"""
    
    # Positive test cases
    assert vigenere_encrypt("Hello, World!", "GIBBERISH") == "Khoor, Wurld!"
    assert vigenere_encrypt("Python3.8", "GIBBERISH") == "Sbwkrq3.8"
    
    # Negative test cases
    with pytest.raises(TypeError):
        vigenere_encrypt(123, "GIBBERISH")
    with pytest.raises(TypeError):
        vigenere_encrypt("HELLO", 123)
    with pytest.raises(ValueError):
        vigenere_encrypt("", "GIBBERISH")

def test_vigenere_encrypt_with_long_key():
    """Test cases for vigenere_encrypt function with long key"""
    
    # Positive test cases
    assert vigenere_encrypt("HELLO", "A" * 10) == "KHOOR"
    assert vigenere_encrypt("hello", "a" * 10) == "khoor"
    
    # Negative test cases
    with pytest.raises(TypeError):
        vigenere_encrypt(123, "GIBBERISH")
    with pytest.raises(TypeError):
        vigenere_encrypt("HELLO", 123)
    with pytest.raises(ValueError):
        vigenere_encrypt("", "GIBBERISH")

def test_vigenere_encrypt_with_case_insensitive_key():
    """Test cases for vigenere_encrypt function with case-insensitive key"""
    
    # Positive test cases
    assert vigenere_encrypt("HELLO", "gibberish") == "KHOOR"
    assert vigenere_encrypt("hello", "GIBBERISH") == "khoor"
    
    # Negative test cases
    with pytest.raises(TypeError):
        vigenere_encrypt(123, "GIBBERISH")
    with pytest.raises(TypeError):
        vigenere_encrypt("HELLO", 123)
    with pytest.raises(ValueError):
        vigenere_encrypt("", "GIBBERISH")

# Run the tests
if __name__ == "__main__":
    import sys
    sys.exit(pytest.main(["-v", "-s", __file__]))
