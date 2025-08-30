```python
import random
import sys

def encode(text):
    # Create substitution cipher: shift each letter by 3 positions forward
    substitution = {chr(ord('A') + i): chr(ord('A') + (i + 3) % 26) for i in range(26)}
    
    encoded = []
    for c in text.upper():
        if c.isalpha():
            # Replace with the substituted character
            encoded.append(substitution[c])
        else:
            # Add random symbols
            symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '-', '+', '=', '(', ')', '_', '?']
            encoded.append(random.choice(symbols))
    return ''.join(encoded)

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python BATCH4_PROMPT22_{{model_name}}.py <input_text>")
        sys.exit(1)
    input_text = sys.argv[1]
    encoded_text = encode(input_text)
    print(encoded_text)