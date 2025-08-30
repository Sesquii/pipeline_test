# BATCH4_PROMPT5_Granite.py

import string
from random import randint, choice

def create_cipher():
    """Generate a simple substitution cipher."""
    # Define our alphabet (English letters)
    alphabet = list(string.ascii_lowercase)
    
    # Randomly shuffle the alphabet to create our cipher
    for i in range(len(alphabet)):
        j = randint(i, len(alphabet)-1)
        alphabet[i], alphabet[j] = alphabet[j], alphabet[i]
    
    return dict((c, alphabet[i]) for i, c in enumerate(alphabet))

def encode_text(text):
    """Encode the given text using our cipher and random extras."""
    cipher = create_cipher()
    
    # Encode each letter, adding a random extra character after every 5th letter
    encoded_text = ''.join(cipher.get(c.lower(), c) if c in string.ascii_lowercase else c for c in text)
    random_extras = [choice('!@#$%^&*()') for _ in range(len(encoded_text)//5)]
    
    return encoded_text + ''.join(random_extras)

def main():
    """Entry point of the script."""
    print("Fictional Language Encoder")
    while True:
        user_input = input("Enter text to encode (or 'quit' to exit): ")
        
        if user_input.lower() == 'quit':
            break
        
        encoded = encode_text(user_input)
        print(f"Encoded: {encoded}")

if __name__ == "__main__":
    main()