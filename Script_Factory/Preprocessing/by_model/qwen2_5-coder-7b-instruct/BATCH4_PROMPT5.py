import random

def encode_fictional_language(text):
    # Define a simple substitution cipher
    cipher = {
        'a': 'q', 'b': 'w', 'c': 'e', 'd': 'r', 'e': 't',
        'f': 'y', 'g': 'u', 'h': 'i', 'i': 'o', 'j': 'p',
        'k': 'a', 'l': 's', 'm': 'd', 'n': 'f', 'o': 'g',
        'p': 'h', 'q': 'j', 'r': 'k', 's': 'l', 't': 'z',
        'u': 'x', 'v': 'c', 'w': 'v', 'x': 'b', 'y': 'n',
        'z': 'm'
    }
    
    # Add random, nonsensical extra characters
    extra_chars = '1234567890!@#$%^&*()_+'
    for char in text:
        if char.isalpha():
            encoded_char = cipher.get(char.lower(), char)
            if random.choice([True, False]):
                encoded_char += random.choice(extra_chars)
            print(f"Original: {char}, Encoded: {encoded_char}")
        else:
            print(f"Original: {char}, Encoded: {char}")

if __name__ == "__main__":
    # Example usage
    input_text = "Hello, World!"
    encode_fictional_language(input_text)
```

This Python script defines a `encode_fictional_language` function that takes an English string and encodes it using a simple substitution cipher. It also adds random extra characters to some of the encoded letters for added complexity. The `if __name__ == "__main__":` block demonstrates how to use this function with an example input.