```python
import json
import random
from typing import Dict, Any

# Define the fictional substitution cipher mapping
FICTIOINAL_CIPHER = {
    'a': 'x', 'b': 'y', 'c': 'z', 'd': 'j', 'e': 'k', 'f': 'l',
    'g': 'm', 'h': 'n', 'i': 'o', 'j': 'p', 'k': 'q', 'l': 'r',
    'm': 's', 'n': 't', 'o': 'u', 'p': 'v', 'q': 'w', 'r': 'x',
    's': 'y', 't': 'z', 'u': 'a', 'v': 'b', 'w': 'c', 'x': 'd',
    'y': 'e', 'z': 'f'
}

# Define the punctuation marks to insert after each word
PUNCTUATION = ['-', '.', ',', '!', '?', ';', ':', "'", '"']

def encode_string_key(key: str) -> str:
    """Encode a string key using the fictional cipher."""
    return FICTIOINAL_CIPHER.get(key, key)

def add_punctuation(word: str) -> str:
    """Add random punctuation marks to the end of a word."""
    if not word:
        return word
    return word + ''.join(random.choices(PUNCTUATION, k=random.randint(1, 3)))

def encode_value(value: Any) -> Any:
    """Encode a value (including nested structures)."""
    if isinstance(value, dict):
        encoded = {}
        for k, v in value.items():
            encoded[encode_string_key(k)] = encode_value(v)
        return encoded
    elif isinstance(value, list):
        encoded = []
        for item in value:
            encoded.append(encode_value(item))
        return encoded
    else:
        # For non-string values, leave as is (but ensure they are not strings)
        if isinstance(value, str):
            return add_punctuation(value)
        return value

def main():
    import sys
    if len(sys.argv) != 2:
        print("Usage: python BATCH7_PROMPT25_{{model_name}}.py <input_json_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = "encoded_" + input_file

    with open(input_file, 'r') as infile:
        data = json.load(infile)

    encoded_data = encode_value(data)

    with open(output_file, 'w') as outfile:
        json.dump(encoded_data, outfile, indent=2)

if __name__ == "__main__":
    main()