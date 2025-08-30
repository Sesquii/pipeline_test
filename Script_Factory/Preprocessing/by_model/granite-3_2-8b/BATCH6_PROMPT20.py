# BATCH6_PROMPT20_Granite.py

import string
from emoji import emojize


def encode(text: str) -> str:
    """
    Encodes a given text into an emoji-based substitution cipher.

    :param text: The input string to be encoded.
    :return: Encoded string with each letter replaced by an equivalent emoji.
    """
    # Hard-coded dictionary for substituting letters with emojis
    substitution_dict = {
        'a': '🇦', 'b': '🇧', 'c': '🇩', 'd': '🇪', 'e': '🇫', 'f': '🇭', 'g': '🇮', 'h': '🇯',
        'i': '🇰', 'j': '🇱', 'k': '🇲', 'l': '🇳', 'm': '🇴', 'n': '🇵', 'o': '🇶', 'p': '🇷',
        'q': '🇸', 'r': '🇹', 's': '🇺', 't': '🇻', 'u': '🇼', 'v': '🇽', 'w': '🇾', 'x': '🇿',
        'y': '👅', 'z': '👆'
    }

    # Convert the text to lowercase for uniformity
    text = text.lower()

    # Encode the text using the substitution dictionary
    encoded_text = ''.join(substitution_dict.get(char, char) for char in text if char in substitution_dict)

    return emojize(encoded_text)


def main():
    """
    Main function to demonstrate encoding a sample text.
    """
    sample_text = "Hello, World!"
    encoded_text = encode(sample_text)
    print(f'Encoded: {encoded_text}')


if __name__ == "__main__":
    main()