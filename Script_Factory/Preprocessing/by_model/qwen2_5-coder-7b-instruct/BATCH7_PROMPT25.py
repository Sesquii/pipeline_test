import json
import random
import sys

# Define a simple substitution cipher for the fictional language
SUBSTITUTION_CIPHER = {
    'a': 'b', 'b': 'c', 'c': 'd', 'd': 'e', 'e': 'f',
    'f': 'g', 'g': 'h', 'h': 'i', 'i': 'j', 'j': 'k',
    'k': 'l', 'l': 'm', 'm': 'n', 'n': 'o', 'o': 'p',
    'p': 'q', 'q': 'r', 'r': 's', 's': 't', 't': 'u',
    'u': 'v', 'v': 'w', 'w': 'x', 'x': 'y', 'y': 'z'
}

# Define punctuation marks to use
PUNCTUATION = ['.', ',', '!', '?']

def encode_string(s):
    """Encode a string using the substitution cipher and add random punctuation."""
    encoded = ''.join([SUBSTITUTION_CIPHER[c] for c in s if c.isalpha()])
    num_punct = random.randint(1, 3)
    punct_marks = ''.join(random.choices(PUNCTUATION, k=num_punct))
    return encoded + punct_marks

def encode_json(input_file, output_file):
    """Read a JSON file, encode all string values, and write the result to another file."""
    with open(input_file, 'r') as f:
        data = json.load(f)
    
    def recursive_encode(obj):
        if isinstance(obj, dict):
            return {k: recursive_encode(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [recursive_encode(item) for item in obj]
        elif isinstance(obj, str):
            return encode_string(obj)
        else:
            return obj
    
    encoded_data = recursive_encode(data)
    
    with open(output_file, 'w') as f:
        json.dump(encoded_data, f, indent=4)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python BATCH7_PROMPT25_{{model_name}}.py input.json output.json")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    encode_json(input_file, output_file)