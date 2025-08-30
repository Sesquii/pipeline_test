# BATCH2_PROMPT21_Devstral.py

import random
import string

def encode_fictional_language(text):
    """
    Encodes English text into a made-up fictional language using a simple substitution cipher
    and adds some random nonsensical extra characters.

    Args:
        text (str): The English text to be encoded.

    Returns:
        str: The encoded fictional language text.
    """
    # Define a simple hard-coded substitution cipher
    substitution_map = {
        'a': 'x', 'b': 'y', 'c': 'z', 'd': 'q', 'e': 'w',
        'f': 'r', 'g': 't', 'h': 'u', 'i': 'v', 'j': 'p',
        'k': 'o', 'l': 's', 'm': 'a', 'n': 'd', 'o': 'f',
        'p': 'g', 'q': 'h', 'r': 'j', 's': 'k', 't': 'l',
        'u': 'm', 'v': 'n', 'w': 'b', 'x': 'c', 'y': 'e',
        'z': 'i'
    }

    # Initialize the encoded text
    encoded_text = []

    for char in text:
        if char.lower() in substitution_map:
            # Apply substitution (preserve case)
            substituted_char = substitution_map[char.lower()]
            if char.isupper():
                substituted_char = substituted_char.upper()
            encoded_text.append(substituted_char)

            # Randomly add nonsensical extra characters
            if random.choice([True, False]):
                extra_char = random.choice(string.punctuation)
                encoded_text.append(extra_char)
        else:
            # Leave non-alphabetic characters as-is
            encoded_text.append(char)

    return ''.join(encoded_text)

if __name__ == "__main__":
    # Example usage
    input_text = "Hello, World!"
    encoded_text = encode_fictional_language(input_text)
    print(f"Original: {input_text}")
    print(f"Encoded: {encoded_text}")