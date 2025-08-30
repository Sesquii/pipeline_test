# BATCH3_PROMPT21_Granite.py

import string
import random
from collections import defaultdict

# Define a simple substitution cipher mapping
CIPHER = str.maketrans(
    'abcdefghijklmnopqrstuvwxyz', 
    'qwertyuiopasdfghjklzxcvbnm'
)

# List of extra nonsensical characters
EXTRA_CHARS = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

def encode(text):
    """Encode the input text into our fictional language."""
    
    # Create a dictionary for random substitution of some letters with extras
    random.shuffle(EXTRA_CHARS)
    subst_dict = {char: extra_char for char, extra_char in zip('bcdfghjklmnpqrstvwxyz', EXTRA_CHARS)}
    
    encoded_text = ""
    for char in text.lower():
        if char in subst_dict:
            # Use random substitution for vowels and some consonants
            encoded_text += random.choice(list(subst_dict.values()))
        elif char in 'aeiou':
            # Keep vowels unchanged for simplicity
            encoded_text += char
        else:
            # Apply standard cipher to other letters
            encoded_text += CHARS[CHAR_MAP[char]]
    
    return encoded_text

# Create a mapping for the cipher
CHARS = 'abcdefghijklmnopqrstuvwxyz'
CHAR_MAP = defaultdict(str)
for i, char in enumerate(CHARS):
    CHAR_MAP[char] = CHARS[(i + CIPHER.make_trans('', '', string.ascii_lowercase).find(char)) % len(CHARS)]

def main():
    """Entry point of the program."""
    
    print("Fictional Language Encoder")
    text = input("Enter your English text: ")
    encoded = encode(text)
    print("Encoded Text:", encoded)

if __name__ == "__main__":
    main()