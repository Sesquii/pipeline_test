```python
import json
import random
import sys

def corrupt_json(data):
    """Corrupts 10% of key-value pairs in the input JSON data."""
    corrupted = {}
    for key, value in data.items():
        if random.random() < 0.1:
            # Randomly choose to corrupt a value
            if isinstance(value, (int, float)):
                # Change number to string
                corrupted[key] = str(value)
            elif isinstance(value, bool):
                # Change boolean to None
                corrupted[key] = None
            else:
                # Leave other types as is
                corrupted[key] = value
        else:
            # No corruption
            corrupted[key] = value
    return corrupted

def main():
    """Main entry point for the glitchy JSON parser."""
    if len(sys.argv) != 2:
        print("Usage: python glitchy_parser.py <input_file>")
        sys.exit(1)
    
    input_path = sys.argv[1]
    with open(input_path, 'r') as f:
        data = json.load(f)
    
    corrupted_data = corrupt_json(data)
    
    output_path = "corrupted_" + input_path
    with open(output_path, 'w') as f:
        json.dump(corrupted_data, f, indent=2)

if __name__ == "__main__":
    main()