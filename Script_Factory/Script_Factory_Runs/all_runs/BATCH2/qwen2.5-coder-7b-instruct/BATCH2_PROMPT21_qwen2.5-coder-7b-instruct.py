import random

# Define the substitution cipher and extra characters for the fictional language
substitution_cipher = {
    'a': 'q', 'b': 'w', 'c': 'e', 'd': 'r', 'e': 't',
    'f': 'y', 'g': 'u', 'h': 'i', 'i': 'o', 'j': 'p',
    'k': 'a', 'l': 's', 'm': 'd', 'n': 'f', 'o': 'g',
    'p': 'h', 'q': 'j', 'r': 'k', 's': 'l', 't': 'z',
    'u': 'x', 'v': 'c', 'w': 'v', 'x': 'b', 'y': 'n',
    'z': 'm'
}

extra_characters = ['@', '#', '$', '%', '^', '&', '*', '_', '+', '=']

def encode_text(text):
    """
    Encodes a given string of English text into a fictional language using a substitution cipher
    and random, nonsensical extra characters.
    
    :param text: The input string to be encoded.
    :return: The encoded string in the fictional language.
    """
    encoded_text = []
    for char in text:
        if char.lower() in substitution_cipher:
            # Substitute character with its counterpart
            encoded_char = substitution_cipher[char.lower()]
            # Randomly decide whether to add an extra character before or after
            if random.choice([True, False]):
                encoded_text.append(random.choice(extra_characters))
            encoded_text.append(encoded_char.upper() if char.isupper() else encoded_char)
        else:
            encoded_text.append(char)
    return ''.join(encoded_text)

def main():
    """
    Entry point of the program. Prompts the user for input text and encodes it.
    """
    print("Welcome to the Fictional Language Encoder!")
    input_text = input("Enter the English text you want to encode: ")
    encoded_result = encode_text(input_text)
    print(f"Encoded Text: {encoded_result}")

# Check if this script is run as the main program and execute the main function
if __name__ == "__main__":
    main()
```

This Python script defines a "Fictional Language Encoder" that takes an English text string as input, encodes it using a simple substitution cipher, and optionally adds random, nonsensical extra characters to simulate a fictional language. The code is well-commented and includes a clear entry point `if __name__ == "__main__":`.