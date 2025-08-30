# BATCH4_PROMPT22_Devstral.py

import random

def encode_text(english_text):
    """
    Encodes English text into a made-up language using a simple substitution cipher
    and adds some random nonsensical extra characters.
    
    Args:
        english_text (str): The input English text to be encoded.
    
    Returns:
        str: The encoded text in the made-up language.
    """
    # Define a simple substitution cipher
    substitution_cipher = {
        'a': 'x', 'b': 'y', 'c': 'z', 'd': 'q', 'e': 'w',
        'f': 'r', 'g': 't', 'h': 'u', 'i': 'v', 'j': 'p',
        'k': 'o', 'l': 's', 'm': 'a', 'n': 'b', 'o': 'c',
        'p': 'd', 'q': 'e', 'r': 'f', 's': 'g', 't': 'h',
        'u': 'i', 'v': 'j', 'w': 'k', 'x': 'l', 'y': 'm',
        'z': 'n'
    }
    
    # Initialize the encoded text
    encoded_text = []
    
    # Process each character in the input text
    for char in english_text:
        if char.lower() in substitution_cipher:
            # Apply substitution cipher (preserve case)
            if char.isupper():
                encoded_char = substitution_cipher[char.lower()].upper()
            else:
                encoded_char = substitution_cipher[char]
        else:
            # Leave non-alphabetic characters unchanged
            encoded_char = char
        
        # Add the encoded character to the result
        encoded_text.append(encoded_char)
        
        # Randomly add nonsensical extra characters
        if random.choice([True, False]):
            nonsensical_chars = ['!', '@', '#', '$', '%', '^', '&', '*']
            encoded_text.append(random.choice(nonsensical_chars))
    
    return ''.join(encoded_text)

if __name__ == "__main__":
    # Example usage
    input_text = "Hello World"
    encoded_output = encode_text(input_text)
    print(f"Original: {input_text}")
    print(f"Encoded: {encoded_output}")