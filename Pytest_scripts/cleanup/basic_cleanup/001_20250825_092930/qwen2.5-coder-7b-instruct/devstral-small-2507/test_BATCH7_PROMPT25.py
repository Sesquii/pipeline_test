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

# ===== GENERATED TESTS =====
import json
import random
from typing import Any, Dict, List, Union

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

def encode_string(s: str) -> str:
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

def encode_json_data(data: Union[Dict[str, Any], List[Any], str]) -> Union[Dict[str, Any], List[Any], str]:
    """Recursively encode string values in JSON data."""
    if isinstance(data, dict):
        return {key: encode_json_data(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [encode_json_data(item) for item in data]
    elif isinstance(data, str):
        return encode_string(data)
    else:
        return data

def main(input_file_path: str, output_file_path: str) -> None:
    # Read and parse input JSON file
    with open(input_file_path, 'r', encoding='utf-8') as f:
        json_data = json.load(f)

    # Encode the JSON data
    encoded_data = encode_json_data(json_data)

    # Write encoded data to output JSON file
    with open(output_file_path, 'w', encoding='utf-8') as f:
        json.dump(encoded_data, f, ensure_ascii=False, indent=2)

# Test cases below this line

import pytest
from io import StringIO
import os

@pytest.fixture
def sample_json():
    return {
        "name": "Alice",
        "age": 30,
        "address": {
            "street": "123 Main St",
            "city": "Anytown"
        },
        "hobbies": ["reading", "cycling"]
    }

@pytest.fixture
def encoded_sample_json():
    return {
        "name": "ɛlɛ",
        "age": 30,
        "address": {
            "street": "123 M>Main St",
            "city": "Anytown"
        },
        "hobbies": ["rɛading", "cycling"]
    }

@pytest.fixture
def sample_input_file(sample_json, tmpdir):
    file_path = os.path.join(tmpdir, 'input.json')
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(sample_json, f)
    return file_path

@pytest.fixture
def sample_output_file(tmpdir):
    return os.path.join(tmpdir, 'output.json')

@pytest.mark.parametrize("data, expected", [
    ("hello world", "hɛllo wórld"),
    ("Python is fun!", "Pythón ɪs fún!"),
    ("12345", "12345")
])
def test_encode_string(data: str, expected: str) -> None:
    assert encode_string(data) == expected

@pytest.mark.parametrize("data, expected", [
    ({"name": "Alice"}, {"name": "ɛlɛ"}),
    ([], []),
    ("not a dict or list", "not a dict or list")
])
def test_encode_json_data(data: Any, expected: Any) -> None:
    assert encode_json_data(data) == expected

def test_main(sample_input_file: str, sample_output_file: str, encoded_sample_json: Dict[str, Any]) -> None:
    main(sample_input_file, sample_output_file)
    with open(sample_output_file, 'r', encoding='utf-8') as f:
        result = json.load(f)
    assert result == encoded_sample_json

def test_main_with_invalid_args(capsys) -> None:
    with pytest.raises(SystemExit):
        main('input.json', 'output.json')
    captured = capsys.readouterr()
    assert captured.out.strip() == "Usage: python BATCH7_PROMPT25_<model_name>.py <input.json> <output.json>"

This test suite includes comprehensive tests for the `encode_string`, `encode_json_data`, and `main` functions. It uses pytest fixtures to create sample data and temporary files, and it includes both positive and negative test cases. The test cases are parameterized where appropriate, and they follow PEP 8 style guidelines.