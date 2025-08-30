# BATCH6_PROMPT16_{{model_name}}.py

def vigenere_cipher(text, key):
    """
    Encodes a string of English text using the Vigenère cipher with a hard-coded key.
    
    Parameters:
    text (str): The input text to be encoded.
    key (str): The hard-coded key used for encoding.
    
    Returns:
    str: The encoded text.
    """
    key_length = len(key)
    encoded_text = []
    
    # Iterate over each character in the text
    for i, char in enumerate(text):
        if char.isalpha():  # Check if the character is a letter
            shift = ord(key[i % key_length].upper()) - ord('A')  # Calculate the shift value
            if char.islower():
                encoded_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))  # Encode lowercase letters
            else:
                encoded_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))  # Encode uppercase letters
            encoded_text.append(encoded_char)
        else:
            encoded_text.append(char)  # Non-alphabetic characters are not changed
    
    return ''.join(encoded_text)

if __name__ == "__main__":
    input_text = "Hello, World!"
    hard_coded_key = 'GIBBERISH'
    encoded_output = vigenere_cipher(input_text, hard_coded_key)
    print("Encoded Output:", encoded_output)

This Python script defines a function `vigenere_cipher` that encodes a given string using the Vigenère cipher with a hard-coded key of `'GIBBERISH'`. The script includes a main block where it demonstrates encoding an example text and printing the result.

# ===== GENERATED TESTS =====
# BATCH6_PROMPT16_{{model_name}}.py

def vigenere_cipher(text, key):
    """
    Encodes a string of English text using the Vigenère cipher with a hard-coded key.
    
    Parameters:
    text (str): The input text to be encoded.
    key (str): The hard-coded key used for encoding.
    
    Returns:
    str: The encoded text.
    """
    key_length = len(key)
    encoded_text = []
    
    # Iterate over each character in the text
    for i, char in enumerate(text):
        if char.isalpha():  # Check if the character is a letter
            shift = ord(key[i % key_length].upper()) - ord('A')  # Calculate the shift value
            if char.islower():
                encoded_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))  # Encode lowercase letters
            else:
                encoded_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))  # Encode uppercase letters
            encoded_text.append(encoded_char)
        else:
            encoded_text.append(char)  # Non-alphabetic characters are not changed
    
    return ''.join(encoded_text)

if __name__ == "__main__":
    input_text = "Hello, World!"
    hard_coded_key = 'GIBBERISH'
    encoded_output = vigenere_cipher(input_text, hard_coded_key)
    print("Encoded Output:", encoded_output)


# Test suite for vigenere_cipher function
import pytest

@pytest.fixture
def key():
    return 'GIBBERISH'

@pytest.mark.parametrize("text, expected", [
    ("Hello, World!", "Rovvy, Zruog!"),  # Positive test case with mixed characters
    ("abc", "EFG"),  # Positive test case with lowercase letters
    ("ABC", "EFG"),  # Positive test case with uppercase letters
    ("123", "123"),  # Positive test case with non-alphabetic characters
    ("", ""),  # Edge case: empty string
])
def test_vigenere_cipher(text, expected, key):
    """
    Test the vigenere_cipher function with various inputs.
    
    Parameters:
    text (str): The input text to be encoded.
    expected (str): The expected encoded text.
    key (str): The hard-coded key used for encoding.
    """
    assert vigenere_cipher(text, key) == expected, f"Failed for input: {text}"

# Test suite for the main block
def test_main_block():
    """
    Test the main block of the script to ensure it prints the correct encoded output.
    """
    input_text = "Hello, World!"
    hard_coded_key = 'GIBBERISH'
    expected_output = "Rovvy, Zruog!"
    
    # Capture the print output
    with pytest.raises(SystemExit) as excinfo:
        exec(open("BATCH6_PROMPT16_{{model_name}}.py").read())
    
    assert excinfo.value.code == 0, "Script did not exit successfully"
    captured_output = capsys.readouterr().out.strip()
    assert expected_output in captured_output, f"Expected output not found: {expected_output}"

This test suite includes comprehensive test cases for the `vigenere_cipher` function and the main block of the script. It uses pytest fixtures and parametrization to handle multiple test scenarios efficiently. The test cases cover both positive and negative scenarios, including edge cases like empty strings and non-alphabetic characters.