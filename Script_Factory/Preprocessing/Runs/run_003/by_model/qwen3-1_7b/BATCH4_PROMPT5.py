```python
import random

def encode_text(input_str):
    # Simple substitution cipher mapping each letter to the next one in the alphabet
    substitution = {chr(ord('a') + i): chr(ord('a') + (i+1)) for i in range(26)}
    symbols = ['@', '!', '$', '%', '&']
    encoded = []
    
    for char in input_str:
        if char.isalpha():
            original = char.lower()
            replaced_char = substitution[original]
            # Preserve case of the original character
            if char.isupper():
                encoded.append(replaced_char.upper())
            else:
                encoded.append(replaced_char)
        else:
            # Add a random nonsensical symbol
            encoded.append(random.choice(symbols))
    
    return ''.join(encoded)

if __name__ == "__main__":
    import sys
    input_str = sys.stdin.read()
    print(encode_text(input_str))