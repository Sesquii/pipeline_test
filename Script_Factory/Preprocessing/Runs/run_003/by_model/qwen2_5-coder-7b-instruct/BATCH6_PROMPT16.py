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
```

This Python script defines a function `vigenere_cipher` that encodes a given string using the Vigenère cipher with a hard-coded key of `'GIBBERISH'`. The script includes a main block where it demonstrates encoding an example text and printing the result.