# BATCH3_PROMPT21_pytorch.py

import random

# Define a simple substitution cipher mapping for English to a made-up "language"
ENGLISH_TO_FICTIONAL = {
    'a': 'x', 'b': 'y', 'c': 'z',
    'd': 'm', 'e': 'n', 'f': 'o',
    'g': 'p', 'h': 'q', 'i': 'r',
    'j': 's', 'k': 't', 'l': 'u',
    'm': 'v', 'n': 'w', 'o': 'a',
    'p': 'b', 'q': 'c', 'r': 'd',
    's': 'e', 't': 'f', 'u': 'g',
    'v': 'h', 'w': 'i', 'x': 'j',
    'y': 'k', 'z': 'l'
}

# Define a list of random, nonsensical extra characters to add to the fictional language
EXTRA_CHARS = ['@', '#', '$', '%', '^', '&', '*', '_', '+', '=']

def encode_to_fictional(text):
    """
    Encodes an English text string into a made-up "fictional" language using a substitution cipher and random extras.

    :param text: str - The input English text to encode
    :return: str - The encoded fictional language text
    """
    # Encode the text using the substitution cipher
    encoded_text = ''.join(ENGLISH_TO_FICTIONAL.get(char.lower(), char) for char in text)
    
    # Add random extra characters at random positions
    for _ in range(random.randint(0, 5)):  # Randomly add between 0 and 5 extra characters
        insert_index = random.randint(0, len(encoded_text))
        encoded_text = encoded_text[:insert_index] + random.choice(EXTRA_CHARS) + encoded_text[insert_index:]
    
    return encoded_text

if __name__ == "__main__":
    input_text = "Hello, World!"
    output_text = encode_to_fictional(input_text)
    print(f"Original: {input_text}")
    print(f"Fictional Encoded: {output_text}")
```

This Python program defines a simple substitution cipher to map English letters to fictional characters and includes random extra characters to simulate a made-up language. The `encode_to_fictional` function takes an input string, encodes it using the cipher, and adds random extras. The script is self-contained, uses only Python's standard library, and demonstrates how to use the encoding function with a simple entry point in the `if __name__ == "__main__":` block.