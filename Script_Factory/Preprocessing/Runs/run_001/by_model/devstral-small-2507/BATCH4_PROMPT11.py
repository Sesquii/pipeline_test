import json
import random
import sys

def corrupt_value(value):
    """Randomly corrupt a value based on its type."""
    if isinstance(value, int):
        # Change number to string
        return str(value)
    elif isinstance(value, float):
        # Change number to boolean
        return bool(random.getrandbits(1))
    elif isinstance(value, str):
        # Change string to None
        return None
    elif isinstance(value, bool):
        # Change boolean to number
        return random.randint(0, 100)
    elif value is None:
        # Change None to string
        return "null"
    else:
        # For other types (like lists, dicts), recursively corrupt
        if isinstance(value, list):
            return [corrupt_value(item) for item in value]
        elif isinstance(value, dict):
            return {k: corrupt_value(v) for k, v in value.items()}
    return value

def corrupt_json(data):
    """Randomly corrupt 10% of key-value pairs in JSON data."""
    if not isinstance(data, dict):
        raise ValueError("Input data must be a dictionary")

    corrupted_data = {}
    keys = list(data.keys())

    for key in keys:
        # Decide whether to corrupt this key-value pair
        if random.random() < 0.1:
            # Corrupt the value
            corrupted_value = corrupt_value(data[key])
            corrupted_data[key] = corrupted_value
        else:
            # Keep original value
            corrupted_data[key] = data[key]

    return corrupted_data

def main(input_file, output_file):
    """Main function to read JSON, corrupt it, and write the result."""
    try:
        with open(input_file, 'r') as f:
            json_data = json.load(f)

        if not isinstance(json_data, dict):
            raise ValueError("Input JSON must be an object (dictionary)")

        corrupted_data = corrupt_json(json_data)

        # Write corrupted data to output file
        with open(output_file, 'w') as f:
            json.dump(corrupted_data, f, indent=2)
        
        print(f"Successfully corrupted JSON and saved to {output_file}")
    
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python glitchy_json_parser.py <input.json> <output.json>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    main(input_file, output_file)