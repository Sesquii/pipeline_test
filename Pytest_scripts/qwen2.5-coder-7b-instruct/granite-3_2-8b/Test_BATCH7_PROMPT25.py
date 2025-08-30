import sys
import json
import random
from string import punctuation

# Fictional language dictionary for substitution cipher
FICTIONAL_LANG = {
    "A": "Α", "B": "Β", "C": "Γ", "D": "Δ", "E": "Ε", "F": "Φ", "G": "Γ", "H": "Η",
    "I": "Ι", "J": "Χ", "K": "Κ", "L": "Λ", "M": "Μ", "N": "Ν", "O": "Ο", "P": "Π",
    "Q": "Ρ", "R": "Σ", "S": "Τ", "T": "Υ", "U": "Ω", "V": "Α", "W": "Β", "X": "Γ",
    "Y": "Δ", "Z": "Ε", "a-z": "α-ω", "0-9": "₀-₉"
}

def encode_string(s):
    """Encode string using fictional language and random punctuation."""
    encoded = ""
    words = s.split()

    for word in words:
        encoded_word = "".join([FICTIONAL_LANG[char] for char in word])
        # Randomly insert a punctuation mark after each word
        if random.choice([True, False]):
            encoded_word += random.choice(punctuation)
        encoded += encoded_word + " "

    return encoded.strip()

def process_json(input_file, output_file):
    """Read JSON file, encode string values and write to new JSON file."""
    with open(input_file, 'r') as infile:
        data = json.load(infile)

    encoded_data = {}
    for key, value in data.items():
        if isinstance(value, str):
            encoded_value = encode_string(value)
        else:
            encoded_value = value  # Non-strings remain unchanged

        encoded_data[key] = encoded_value

    with open(output_file, 'w') as outfile:
        json.dump(encoded_data, outfile, indent=4)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python BATCH7_PROMPT25_{model_name}.py <input_json> <output_json>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    process_json(input_file, output_file)

# ===== GENERATED TESTS =====
```python
import pytest
from pathlib import Path

# Original code
import sys
import json
import random
from string import punctuation

FICTIONAL_LANG = {
    "A": "Α", "B": "Β", "C": "Γ", "D": "Δ", "E": "Ε", "F": "Φ", "G": "Γ", "H": "Η",
    "I": "Ι", "J": "Χ", "K": "Κ", "L": "Λ", "M": "Μ", "N": "Ν", "O": "Ο", "P": "Π",
    "Q": "Ρ", "R": "Σ", "S": "Τ", "T": "Υ", "U": "Ω", "V": "Α", "W": "Β", "X": "Γ",
    "Y": "Δ", "Z": "Ε", "a-z": "α-ω", "0-9": "₀-₉"
}

def encode_string(s):
    """Encode string using fictional language and random punctuation."""
    encoded = ""
    words = s.split()

    for word in words:
        encoded_word = "".join([FICTIONAL_LANG[char] for char in word])
        if random.choice([True, False]):
            encoded_word += random.choice(punctuation)
        encoded += encoded_word + " "

    return encoded.strip()

def process_json(input_file, output_file):
    """Read JSON file, encode string values and write to new JSON file."""
    with open(input_file, 'r') as infile:
        data = json.load(infile)

    encoded_data = {}
    for key, value in data.items():
        if isinstance(value, str):
            encoded_value = encode_string(value)
        else:
            encoded_value = value

        encoded_data[key] = encoded_value

    with open(output_file, 'w') as outfile:
        json.dump(encoded_data, outfile, indent=4)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python BATCH7_PROMPT25_{model_name}.py <input_json> <output_json>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    process_json(input_file, output_file)


# Test cases
def test_encode_string():
    """Test the encode_string function with various inputs."""
    assert encode_string("Hello World") == "Ελληνικά! Ωραίο!"
    assert encode_string("12345") == "₁₂₃₄₅"
    assert encode_string("") == ""
    assert encode_string("NoPunctuation") == "ΝόΠουντεχσιμ!"

def test_process_json(tmp_path):
    """Test the process_json function with various inputs."""
    input_data = {
        "name": "Alice",
        "age": 30,
        "city": "Wonderland"
    }
    
    input_file = tmp_path / "input.json"
    output_file = tmp_path / "output.json"
    
    with open(input_file, 'w') as f:
        json.dump(input_data, f)
    
    process_json(str(input_file), str(output_file))
    
    with open(output_file, 'r') as f:
        encoded_data = json.load(f)
    
    assert encoded_data["name"] == "Αλική!"
    assert encoded_data["age"] == 30
    assert encoded_data["city"] == "Ωνδερλανδ!"

def test_process_json_no_strings(tmp_path):
    """Test the process_json function with non-string values."""
    input_data = {
        "name": "Alice",
        "age": 30,
        "scores": [95, 88, 76]
    }
    
    input_file = tmp_path / "input.json"
    output_file = tmp_path / "output.json"
    
    with open(input_file, 'w') as f:
        json.dump(input_data, f)
    
    process_json(str(input_file), str(output_file))
    
    with open(output_file, 'r') as f:
        encoded_data = json.load(f)
    
    assert encoded_data["name"] == "Αλική!"
    assert encoded_data["age"] == 30
    assert encoded_data["scores"] == [95, 88, 76]

def test_process_json_empty_input(tmp_path):
    """Test the process_json function with an empty input file."""
    input_file = tmp_path / "input.json"
    output_file = tmp_path / "output.json"
    
    with open(input_file, 'w') as f:
        pass
    
    process_json(str(input_file), str(output_file))
    
    assert not output_file.exists()
```