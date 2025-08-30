import random

# Define a simple substitution cipher for our fictional language
SUBSTITUTION_CIPHER = {
    'a': 'x', 'b': 'y', 'c': 'z', 'd': 'q',
    'e': 'w', 'f': 'r', 'g': 't', 'h': 'u',
    'i': 'v', 'j': 'p', 'k': 's', 'l': 'd',
    'm': 'f', 'n': 'g', 'o': 'h', 'p': 'j',
    'q': 'k', 'r': 'l', 's': 'm', 't': 'n',
    'u': 'b', 'v': 'c', 'w': 'a', 'x': 'e',
    'y': 'i', 'z': 'o'
}

# Define some extra nonsensical characters to add
EXTRA_CHARACTERS = ['!', '@', '#', '$', '%']

def encode_text(text):
    """Encodes English text into our fictional language."""
    encoded_chars = []
    
    for char in text.lower():
        if char in SUBSTITUTION_CIPHER:
            # Apply substitution cipher
            encoded_chars.append(SUBSTITUTION_CIPHER[char])
        else:
            # Keep non-alphabetic characters as is
            encoded_chars.append(char)
        
        # Randomly add extra nonsensical characters
        if random.choice([True, False]):
            encoded_chars.append(random.choice(EXTRA_CHARACTERS))
    
    return ''.join(encoded_chars)

if __name__ == "__main__":
    # Example usage
    input_text = "Hello World"
    encoded_output = encode_text(input_text)
    print(f"Original: {input_text}")
    print(f"Encoded: {encoded_output}")