# BATCH6_PROMPT20_Devstral.py

import sys

def encode_text(text):
    """
    Encodes the input text using a substitution cipher where each letter is replaced by an emoji.

    Args:
        text (str): The text to be encoded.

    Returns:
        str: The encoded text with letters replaced by emojis.
    """
    # Hard-coded dictionary mapping letters to emojis
    emoji_dict = {
        'a': '😀', 'b': '😁', 'c': '😂', 'd': '🤣', 'e': '😃',
        'f': '😄', 'g': '😅', 'h': '😆', 'i': '😉', 'j': '😊',
        'k': '😋', 'l': '😌', 'm': '😍', 'n': '🤩', 'o': '😎',
        'p': '🙂', 'q': '🤥', 'r': '😐', 's': '😑', 't': '😒',
        'u': '😞', 'v': '😔', 'w': '😕', 'x': '😖', 'y': '😗',
        'z': '😙'
    }

    encoded_text = []
    for char in text.lower():
        if char in emoji_dict:
            encoded_text.append(emoji_dict[char])
        else:
            # If the character is not a letter, keep it as is
            encoded_text.append(char)

    return ''.join(encoded_text)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python BATCH6_PROMPT20_Devstral.py <text_to_encode>")
        sys.exit(1)

    text_to_encode = sys.argv[1]
    encoded_output = encode_text(text_to_encode)
    print(f"Encoded Text: {encoded_output}")