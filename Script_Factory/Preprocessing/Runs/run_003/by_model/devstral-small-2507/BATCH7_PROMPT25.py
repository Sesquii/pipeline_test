import json
import random
import sys

# Simple substitution cipher for fictional language encoding
SUBSTITUTION_CIPHER = {
    'a': 'ɛ', 'b': 'ḃ', 'c': 'ḉ', 'd': 'ḋ', 'e': 'ɛ',
    'f': 'ḟ', 'g': 'ġ', 'h': 'ẖ', 'i': 'ɨ', 'j': 'ʝ',
    'k': 'ḳ', 'l': 'ḽ', 'm': 'ḿ', 'n': 'ṁ', 'o': 'ɔ',
    'p': 'ṕ', 'q': 'ꝓ', 'r': 'ŕ', 's': 'ſ', 't': 'ť',
    'u': 'ṳ', 'v': 'ṽ', 'w': 'ẃ', 'x': 'ᵡ', 'y': 'ʸ',
    'z': 'ᶻ'
}

# Punctuation marks to insert after words
PUNCTUATIONS = ['.', ',', '!', '?', ';', ':']

def encode_string(s):
    """Encode a string using substitution cipher and add random punctuation."""
    encoded_chars = []
    for char in s:
        if char.lower() in SUBSTITUTION_CIPHER:
            # Preserve case by checking original character
            if char.isupper():
                encoded_chars.append(SUBSTITUTION_CIPHER[char.lower()].upper())
            else:
                encoded_chars.append(SUBSTITUTION_CIPHER[char.lower()])
        else:
            encoded_chars.append(char)

    # Join characters and add random punctuation after each word
    words = ''.join(encoded_chars).split()
    for i, word in enumerate(words):
        if random.choice([True, False]):
            words[i] += random.choice(PUNCTUATIONS)
    return ' '.join(words)

def encode_json_data(data):
    """Recursively encode string values in JSON data."""
    if isinstance(data, dict):
        return {key: encode_json_data(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [encode_json_data(item) for item in data]
    elif isinstance(data, str):
        return encode_string(data)
    else:
        return data

def main(input_file_path, output_file_path):
    # Read and parse input JSON file
    with open(input_file_path, 'r', encoding='utf-8') as f:
        json_data = json.load(f)

    # Encode the JSON data
    encoded_data = encode_json_data(json_data)

    # Write encoded data to output JSON file
    with open(output_file_path, 'w', encoding='utf-8') as f:
        json.dump(encoded_data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python BATCH7_PROMPT25_<model_name>.py <input.json> <output.json>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    main(input_file, output_file)