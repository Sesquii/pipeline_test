# BATCH6_PROMPT17_{{model_name}}.py

def encode_fictional_language(text):
    """
    Encodes a given string of English text into a "Fictional Language" by replacing every vowel with the next consonant in the alphabet.
    
    Parameters:
    text (str): The input English text to be encoded.
    
    Returns:
    str: The encoded text using the Fictional Language rules.
    """
    # Define vowels and their corresponding next consonants
    vowel_to_consonant = {
        'a': 'b', 'e': 'f', 'i': 'j', 'o': 'p', 'u': 'v',
        'A': 'B', 'E': 'F', 'I': 'J', 'O': 'P', 'U': 'V'
    }
    
    # Initialize an empty list to store encoded characters
    encoded_text = []
    
    # Iterate over each character in the input text
    for char in text:
        # If the character is a vowel, replace it with the corresponding consonant
        if char in vowel_to_consonant:
            encoded_text.append(vowel_to_consonant[char])
        else:
            # Otherwise, keep the character as is
            encoded_text.append(char)
    
    # Join the list of characters into a single string and return it
    return ''.join(encoded_text)

# Entry point for the script
if __name__ == "__main__":
    # Example usage: Encode the string "Hello World"
    input_text = "Hello World"
    encoded_output = encode_fictional_language(input_text)
    print(f"Original Text: {input_text}")
    print(f"Encoded Text: {encoded_output}")
```

This Python program defines a function `encode_fictional_language` that takes a string of English text and encodes it according to the specified rules. The main part of the script demonstrates how to use this function with an example input.

# ===== GENERATED TESTS =====
```python
# BATCH6_PROMPT17_{{model_name}}.py

def encode_fictional_language(text):
    """
    Encodes a given string of English text into a "Fictional Language" by replacing every vowel with the next consonant in the alphabet.
    
    Parameters:
    text (str): The input English text to be encoded.
    
    Returns:
    str: The encoded text using the Fictional Language rules.
    """
    # Define vowels and their corresponding next consonants
    vowel_to_consonant = {
        'a': 'b', 'e': 'f', 'i': 'j', 'o': 'p', 'u': 'v',
        'A': 'B', 'E': 'F', 'I': 'J', 'O': 'P', 'U': 'V'
    }
    
    # Initialize an empty list to store encoded characters
    encoded_text = []
    
    # Iterate over each character in the input text
    for char in text:
        # If the character is a vowel, replace it with the corresponding consonant
        if char in vowel_to_consonant:
            encoded_text.append(vowel_to_consonant[char])
        else:
            # Otherwise, keep the character as is
            encoded_text.append(char)
    
    # Join the list of characters into a single string and return it
    return ''.join(encoded_text)

# Entry point for the script
if __name__ == "__main__":
    # Example usage: Encode the string "Hello World"
    input_text = "Hello World"
    encoded_output = encode_fictional_language(input_text)
    print(f"Original Text: {input_text}")
    print(f"Encoded Text: {encoded_output}")

# Test suite for the encode_fictional_language function
import pytest

def test_encode_fictional_language():
    """
    Tests the encode_fictional_language function with various inputs to ensure it works correctly.
    """
    
    # Positive test cases
    assert encode_fictional_language("Hello World") == "Hfllp Wprld", "Test case 1 failed"
    assert encode_fictional_language("Programming is fun!") == "Prpgrmmjng ks fvn!", "Test case 2 failed"
    assert encode_fictional_language("AEIOUaeiou") == "BFJPVbfjpv", "Test case 3 failed"
    
    # Negative test cases
    assert encode_fictional_language("") == "", "Test case 4 failed"
    assert encode_fictional_language("12345!@#$%") == "12345!@#$%", "Test case 5 failed"
    assert encode_fictional_language("abcdefghijklmnopqrstuvwxyz") == "bfjpvwxyz", "Test case 6 failed"

# Run the test suite
if __name__ == "__main__":
    pytest.main()
```

This script includes a comprehensive test suite for the `encode_fictional_language` function. It uses pytest to run the tests and includes both positive and negative test cases. The test cases cover various scenarios, including empty strings, non-alphabetic characters, and strings with all vowels.