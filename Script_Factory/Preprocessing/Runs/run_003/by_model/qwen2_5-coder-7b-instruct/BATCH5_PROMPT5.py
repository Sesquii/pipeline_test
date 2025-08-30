# BATCH5_PROMPT5_{{model_name}}.py

import random
import string

# Define a simple substitution cipher mapping English letters to fictional language characters
SUBSTITUTION_CIPHER = {
    'a': 'q', 'b': 'w', 'c': 'e', 'd': 'r', 'e': 't',
    'f': 'y', 'g': 'u', 'h': 'i', 'i': 'o', 'j': 'p',
    'k': 'a', 'l': 's', 'm': 'd', 'n': 'f', 'o': 'g',
    'p': 'h', 'q': 'j', 'r': 'k', 's': 'l', 't': 'z',
    'u': 'x', 'v': 'c', 'w': 'v', 'x': 'b', 'y': 'n',
    'z': 'm'
}

# Define a list of random, nonsensical extra characters to add to the fictional language
EXTRA_CHARACTERS = ['@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+']

def encode_text(text):
    """
    Encodes a given string of English text into a made-up "language" using a substitution cipher and random extra characters.
    
    Parameters:
    - text (str): The input English text to be encoded.
    
    Returns:
    - str: The encoded text in the fictional language.
    """
    # Shuffle the list of extra characters
    shuffled_extra_chars = random.sample(EXTRA_CHARACTERS, len(EXTRA_CHARACTERS))
    
    # Create a mapping from original letters to shuffled extra characters
    letter_to_extra_char = dict(zip(SUBSTITUTION_CIPHER.keys(), shuffled_extra_chars))
    
    # Encode each character in the input text
    encoded_text = []
    for char in text:
        if char.lower() in SUBSTITUTION_CIPHER:
            # Convert to lower case and replace with extra character
            new_char = letter_to_extra_char[char.lower()]
        else:
            # Keep non-English characters as is
            new_char = char
        
        encoded_text.append(new_char)
    
    return ''.join(encoded_text)

if __name__ == "__main__":
    # Example usage
    input_text = "Hello, world!"
    encoded_text = encode_text(input_text)
    print("Original Text:", input_text)
    print("Encoded Text:", encoded_text)
```

This Python script defines a simple substitution cipher and a list of random extra characters to create a fictional language. The `encode_text` function takes an English string as input and encodes it into the fictional language by replacing each letter according to the substitution cipher and adding a randomly chosen extra character from the predefined list. The script includes a basic entry point for demonstration purposes.