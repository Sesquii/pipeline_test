# BATCH2_PROMPT21_Granite.py

import string
import random

def encode_text(text):
    """Encodes a given English text into a fictional language using a simple substitution cipher."""
    
    # Define the character mappings for encoding and decoding
    ENCODING = str.maketrans(
        'abcdefghijklmnopqrstuvwxyz',
        'vwxyzutsrqponmlkjihgfedcba'
    )

    RANDOM_CHARS = '!@#$%^&*()-_=+[]{}|;:,.<>?/`~'
    
    # Randomly add some nonsensical characters to the encoded text
    nonsense_chars = ''.join(random.choice(RANDOM_CHARS) for _ in range(len(text)))
    
    # Encode the original text
    encoded = text.translate(ENCODING) + nonsense_chars

    return encoded

def decode_text(encoded):
    """Decodes a fictional language text back to English."""
    
    # The reverse mapping of ENCODING for decoding
    DECODING = str.maketrans('vwxyzutsrqponmlkjihgfedcba', 'abcdefghijklmnopqrstuvwxyz')
    
    return encoded.translate(DECODING)

if __name__ == "__main__":
    # Example usage:
    original_text = "hello world"

    print("Original Text:", original_text)
    encoded_text = encode_text(original_text)
    print("Encoded Text:", encoded_text)

    decoded_text = decode_text(encoded_text)
    print("Decoded Text:", decoded_text)