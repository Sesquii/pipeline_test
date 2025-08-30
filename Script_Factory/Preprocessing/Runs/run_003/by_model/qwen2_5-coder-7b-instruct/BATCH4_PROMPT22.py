import random

# Define the substitution cipher for English to "Fictional Language"
SUBSTITUTION_CYPHER = {
    'a': 'z', 'b': 'x', 'c': 'c', 'd': 'v',
    'e': 'b', 'f': 'n', 'g': 'm', 'h': 'k',
    'i': 'j', 'j': 'i', 'k': 'h', 'l': 'g',
    'm': 'f', 'n': 'd', 'o': 'a', 'p': 's',
    'q': 'r', 'r': 'q', 's': 'p', 't': 'o',
    'u': 'l', 'v': 'n', 'w': 'w', 'x': 't',
    'y': 'y', 'z': 'e'
}

# Define a list of random, nonsensical extra characters
EXTRA_CHARS = ['@', '#', '$', '%', '^', '&', '*', '(', ')']

def encode_text(text):
    """
    Encodes the given English text into a made-up "Fictional Language" using a substitution cipher.
    
    Args:
    text (str): The input English text to be encoded.
    
    Returns:
    str: The encoded text in "Fictional Language".
    """
    encoded_text = []
    for char in text:
        if char.isalpha():
            # Substitute the character and add a random extra character
            substituted_char = SUBSTITUTION_CYPHER[char.lower()]
            extra_char = random.choice(EXTRA_CHARS)
            encoded_char = f"{substituted_char}{extra_char}" if char.islower() else f"{substituted_char.upper()}{extra_char}"
        else:
            # If the character is not a letter, leave it as is
            encoded_char = char
        encoded_text.append(encoded_char)
    return ''.join(encoded_text)

def main():
    """
    Entry point for the program. Prompts the user to enter text and encodes it.
    """
    input_text = input("Enter English text to encode: ")
    encoded_result = encode_text(input_text)
    print(f"Encoded text in Fictional Language: {encoded_result}")

if __name__ == "__main__":
    main()
```

This Python script defines a simple substitution cipher for encoding English text into a made-up "Fictional Language". It also includes a list of random, nonsensical extra characters that are appended to each substituted character. The `encode_text` function handles the encoding process, while the `main` function serves as the entry point and user interface.