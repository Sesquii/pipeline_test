```python
import sys

def encode(text):
    original = 'abcdefghijklmnopqrstuvwxyz'
    substitution = 'zyxwvutsrqponmlkjihgfedcba'
    result = []
    for c in text.lower():
        if c in original:
            replaced = substitution[original.index(c)]
            result.append(replaced)
        else:
            result.append(c)
    # Add random, nonsensical characters
    result.extend(['-', '_', '*'])
    return ''.join(result)

if __name__ == "__main__":
    text = sys.stdin.read()
    encoded_text = encode(text)
    print(encoded_text)