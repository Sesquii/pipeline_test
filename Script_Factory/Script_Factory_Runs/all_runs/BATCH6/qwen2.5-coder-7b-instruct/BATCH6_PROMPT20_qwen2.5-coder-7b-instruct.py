# BATCH6_PROMPT20_gpt3.py

# Dictionary mapping letters to emojis
EMOJI_SUBSTITUTION = {
    'a': '😀', 'b': '.BLL', 'c': '©️', 'd': '♦️', 'e': '€',
    'f': '₣', 'g': '₲', 'h': 'HeaderView', 'i': 'ì', 'j': 'ĵ',
    'k': 'ķ', 'l': 'ĺ', 'm': '₥', 'n': '₦', 'o': 'õ',
    'p': '₧', 'q': '™', 'r': '®', 's': 'ß', 't': 'ţ',
    'u': 'ü', 'v': '𝑣', 'w': 'ŵ', 'x': '𝕏', 'y': 'ŷ',
    'z': 'ź', ' ': ' ',
}

def encode_to_emojis(text):
    """
    Encodes a given text to a string of emojis using a hard-coded substitution dictionary.
    
    Parameters:
        text (str): The input text to be encoded.
        
    Returns:
        str: The encoded text as a string of emojis.
    """
    return ''.join(EMOJI_SUBSTITUTION.get(char, char) for char in text)

def main():
    """
    Main entry point of the program. Prompts user for input and prints the encoded text.
    """
    print("Fictional Language Encoder")
    user_input = input("Enter text to encode: ")
    encoded_text = encode_to_emojis(user_input)
    print(f"Encoded Text: {encoded_text}")

if __name__ == "__main__":
    main()
```

This Python script implements a simple substitution cipher where each letter is replaced by an emoji from a predefined dictionary. The `encode_to_emojis` function takes a string and returns its encoded form. The `main` function provides a simple user interface to input text and see the encoded output.