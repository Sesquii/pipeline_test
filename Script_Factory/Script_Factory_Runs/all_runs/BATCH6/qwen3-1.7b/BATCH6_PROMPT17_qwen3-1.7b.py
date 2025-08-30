```python
import sys

def encode(text):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    mapping = {
        'a': 'b',
        'e': 'f',
        'i': 'j',
        'o': 'p',
        'u': 'v'
    }
    result = []
    for char in text:
        lower_char = char.lower()
        if lower_char in vowels:
            new_char = mapping[lower_char]
            if char.isupper():
                result.append(new_char.upper())
            else:
                result.append(new_char)
        else:
            result.append(char)
    return ''.join(result)

if __name__ == "__main__":
    input_text = sys.stdin.read()
    encoded_text = encode(input_text)
    print(encoded_text)