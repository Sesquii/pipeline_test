```python
import argparse
import json
import random
import os

def main():
    parser = argparse.ArgumentParser(description='Glitchy JSON Parser')
    parser.add_argument('input_file', help='Path to the JSON file')
    args = parser.parse_args()

    with open(args.input_file, 'r') as f:
        json_data = json.load(f)

    corrupted_data = {}

    for key, value in json_data.items():
        if random.random() < 0.1:
            # Apply corruption
            if isinstance(value, (int, float)):
                corrupted_value = str(value)
            elif isinstance(value, bool):
                corrupted_value = None
            else:
                corrupted_value = value
            corrupted_data[key] = corrupted_value
        else:
            corrupted_data[key] = value

    output_filename = f'corrupted_{os.path.basename(args.input_file)}'
    with open(output_filename, 'w') as f:
        json.dump(corrupted_data, f, indent=2)

if __name__ == "__main__":
    main()