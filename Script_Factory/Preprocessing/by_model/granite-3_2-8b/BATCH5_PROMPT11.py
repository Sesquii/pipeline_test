import json
import random
from typing import Any

def corrupt_json(data: dict) -> dict:
    """Corrupts 10% of key-value pairs in a dictionary."""
    corrupted_data = {}

    for key, value in data.items():
        if random.random() < 0.1:  # 10% chance to corrupt
            if isinstance(value, bool):
                corrupted_value = None
            elif isinstance(value, (int, float)):
                corrupted_value = str(value)
            else:
                corrupted_value = value

            corrupted_data[key] = corrupted_value
        else:
            corrupted_data[key] = value

    return corrupted_data

def parse_and_corrupt(file_path: str, output_path: str):
    """Parses JSON from file_path and writes corrupted JSON to output_path."""
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)

    corrupted_data = corrupt_json(data)

    with open(output_path, 'w') as new_json_file:
        json.dump(corrupted_data, new_json_file, indent=4)

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: python glitchy_parser.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    parse_and_corrupt(input_file, output_file)