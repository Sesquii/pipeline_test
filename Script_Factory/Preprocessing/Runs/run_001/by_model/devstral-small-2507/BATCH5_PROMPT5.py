# BATCH5_PROMPT5_{{model_name}}.py

import random
import string

def encode_text(text):
    """
    Encodes English text into a fictional language using a simple substitution cipher
    and adds some random nonsensical characters.
    
    Args:
        text (str): The input English text to encode
    
    Returns:
        str: The encoded fictional language text
    """
    # Define a hard-coded substitution cipher
    substitution_cipher = {
        'a': 'x', 'b': 'y', 'c': 'z', 'd': 'q', 'e': 'w',
        'f': 'r', 'g': 't', 'h': 'u', 'i': 'p', 'j': 's',
        'k': 'd', 'l': 'f', 'm': 'g', 'n': 'h', 'o': 'j',
        'p': 'k', 'q': 'l', 'r': 'z', 's': 'x', 't': 'c',
        'u': 'v', 'v': 'b', 'w': 'n', 'x': 'm', 'y': 'o',
        'z': 'i'
    }

    # Convert to lowercase for consistent encoding
    text = text.lower()
    encoded_chars = []

    for char in text:
        if char in substitution_cipher:
            encoded_chars.append(substitution_cipher[char])
        elif char in string.whitespace:
            encoded_chars.append(char)  # Preserve whitespace
        else:
            encoded_chars.append(char)  # Leave punctuation/special chars as-is

    # Add some random nonsensical characters
    nonsensical_chars = ['@', '#', '$', '%', '^', '&', '*']
    encoded_text = ''.join(encoded_chars)

    # Randomly insert nonsensical characters
    for _ in range(random.randint(3, 7)):  # Insert 3-7 nonsensical chars
        pos = random.randint(0, len(encoded_text))
        encoded_text = encoded_text[:pos] + random.choice(nonsensical_chars) + encoded_text[pos:]

    return encoded_text

if __name__ == "__main__":
    # Example usage
    input_text = "Hello World! This is a test."
    encoded = encode_text(input_text)
    print(f"Original: {input_text}")
    print(f"Encoded:  {encoded}")