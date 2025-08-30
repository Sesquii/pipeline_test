import json
import random
from copy import deepcopy

def corrupt_value(value):
    """ Randomly corrupt a value. """
    if isinstance(value, (int, float)):
        return str(value)
    elif isinstance(value, bool):
        return None if random.random() < 0.1 else value
    elif isinstance(value, list):
        return [corrupt_value(v) for v in value]
    elif isinstance(value, dict):
        return {k: corrupt_value(v) for k, v in value.items()}
    else:
        return value

def glitch_json(input_path, output_path):
    """ Parse JSON and randomly corrupt 10% of key-value pairs. """
    with open(input_path, 'r') as file:
        data = json.load(file)

    corrupted_data = deepcopy(data)
    for key, value in list(corrupted_data.items()):
        if random.random() < 0.1:
            corrupted_data[key] = corrupt_value(value)

    with open(output_path, 'w') as file:
        json.dump(corrupted_data, file, indent=4)

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: python glitchy_json.py <input_json_file> <output_json_file>")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    glitch_json(input_path, output_path)
    print(f"Corrupted JSON written to {output_path}")