```python
import random
import string

def encode_text(text):
    # Hardcoded substitution cipher: A→X, B→Y, ..., Z→A
    substitution = {
        'A': 'X', 'B': 'Y', 'C': 'Z', 'D': 'A', 'E': 'B', 'F': 'C',
        'G': 'D', 'H': 'E', 'I': 'F', 'J': 'G', 'K': 'H', 'L': 'I',
        'M': 'J', 'N': 'K', 'O': 'L', 'P': 'M', 'Q': 'N', 'R': 'O',
        'S': 'P', 'T': 'Q', 'U': 'R', 'V': 'S', 'W': 'T', 'X': 'U',
        'Y': 'V', 'Z': 'W'
    }
    
    # Random extra characters (nonsensical and random)
    extra_chars = ['!', '@', '#', '$', '%']
    added_chars = random.choices(extra_chars, k=3)
    
    encoded = []
    for char in text:
        if char.isalpha():
            encoded.append(substitution.get(char.upper(), char))
        else:
            encoded.append(char)
    encoded += added_chars
    
    return ''.join(encoded)

if __name__ == "__main__":
    import sys
    input_text = sys.stdin.read()
    print(encode_text(input_text))