# BATCH4_PROMPT5_Devstral.py

import random
import string

def fictional_language_encoder(text):
    """
    Encodes English text into a made-up language using a simple substitution cipher
    and adds some random nonsensical extra characters.
    
    Args:
        text (str): The input English text to encode.
    
    Returns:
        str: The encoded fictional language text.
    """
    # Simple hard-coded substitution cipher
    substitution_cipher = {
        'a': 'x', 'b': 'y', 'c': 'z', 'd': 'q', 'e': 'w',
        'f': 'r', 'g': 't', 'h': 'u', 'i': 'v', 'j': 's',
        'k': 'a', 'l': 'b', 'm': 'c', 'n': 'd', 'o': 'e',
        'p': 'f', 'q': 'g', 'r': 'h', 's': 'i', 't': 'j',
        'u': 'k', 'v': 'l', 'w': 'm', 'x': 'n', 'y': 'o',
        'z': 'p'
    }

    # Add some nonsensical extra characters
    nonsensical_chars = ['@', '#', '$', '%', '^', '&', '*', '!']

    encoded_chars = []
    for char in text.lower():
        if char in substitution_cipher:
            encoded_char = substitution_cipher[char]
            # Randomly add a nonsensical character with 20% probability
            if random.random() < 0.2:
                encoded_char += random.choice(nonsensical_chars)
            encoded_chars.append(encoded_char)
        else:
            encoded_chars.append(char)

    return ''.join(encoded_chars)

def main():
    """Main entry point for the script."""
    # Example usage
    input_text = "Hello World"
    encoded_text = fictional_language_encoder(input_text)
    print(f"Original: {input_text}")
    print(f"Encoded: {encoded_text}")

if __name__ == "__main__":
    main()