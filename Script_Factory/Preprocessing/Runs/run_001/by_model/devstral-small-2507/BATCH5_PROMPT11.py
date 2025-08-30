import json
import random
import sys

def corrupt_value(value):
    """Randomly corrupt a given value."""
    if isinstance(value, int):
        return str(value)  # Change number to string
    elif isinstance(value, float):
        return bool(value)  # Change float to boolean
    elif isinstance(value, bool):
        return None  # Change boolean to null
    elif isinstance(value, str):
        return value[::-1] if len(value) > 0 else ""  # Reverse string
    elif isinstance(value, dict):
        return {k: corrupt_value(v) for k, v in value.items()}
    elif isinstance(value, list):
        return [corrupt_value(item) for item in value]
    else:
        return value

def glitchy_parse(json_data):
    """Parse JSON and randomly corrupt 10% of key-value pairs."""
    if isinstance(json_data, dict):
        keys = list(json_data.keys())
        for key in keys:
            if random.random() < 0.1:  # 10% chance to corrupt
                json_data[key] = corrupt_value(json_data[key])
    elif isinstance(json_data, list):
        for i in range(len(json_data)):
            if random.random() < 0.1:  # 10% chance to corrupt
                json_data[i] = corrupt_value(json_data[i])
    return json_data

def main(input_file_path, output_file_path):
    """Main function to read JSON, apply glitches, and write output."""
    with open(input_file_path, 'r') as f:
        data = json.load(f)

    corrupted_data = glitchy_parse(data)

    with open(output_file_path, 'w') as f:
        json.dump(corrupted_data, f, indent=2)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python glitchy_json.py <input_file.json> <output_file.json>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    main(input_file, output_file)