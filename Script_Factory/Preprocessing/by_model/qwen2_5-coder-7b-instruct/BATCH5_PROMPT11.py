import json
import random

def corrupt_value(value):
    """Randomly corrupts a value."""
    if isinstance(value, dict):
        return {k: corrupt_value(v) for k, v in value.items()}
    elif isinstance(value, list):
        return [corrupt_value(v) for v in value]
    elif isinstance(value, (int, float)):
        return str(value)
    elif isinstance(value, bool):
        return None
    else:
        return value

def glitchy_json_parser(input_path, output_path):
    """Parses a JSON file and corrupts 10% of the key-value pairs."""
    with open(input_path, 'r') as file:
        data = json.load(file)

    # Calculate the number of items to corrupt
    num_items_to_corrupt = int(len(data) * 0.1)
    
    # Randomly select keys to corrupt
    keys_to_corrupt = random.sample(list(data.keys()), num_items_to_corrupt)
    
    # Corrupt selected key-value pairs
    for key in keys_to_corrupt:
        data[key] = corrupt_value(data[key])

    with open(output_path, 'w') as file:
        json.dump(data, file, indent=4)

if __name__ == "__main__":
    input_path = "input.json"  # Replace with your JSON file path
    output_path = "output.json"
    glitchy_json_parser(input_path, output_path)
```

This Python script defines a function `glitchy_json_parser` that takes an input JSON file path and an output JSON file path. It reads the JSON data from the input file, randomly corrupts 10% of the key-value pairs (changing numbers to strings, booleans to null), and writes the corrupted JSON back to the output file. The `corrupt_value` function handles the corruption logic recursively for nested dictionaries and lists.