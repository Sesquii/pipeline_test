# BATCH10_PROMPT1_Devstral.py

import json
import sys

def load_json(file_path):
    """Load JSON data from a file."""
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading JSON: {e}", file=sys.stderr)
        sys.exit(1)

def digest_json(data):
    """Process and 'digest' the JSON data."""
    # Example digestion: Convert all string values to uppercase
    if isinstance(data, dict):
        return {k: digest_json(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [digest_json(item) for item in data]
    elif isinstance(data, str):
        return data.upper()
    else:
        return data

def save_json(file_path, data):
    """Save processed JSON data to a file."""
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=2)
    except IOError as e:
        print(f"Error saving JSON: {e}", file=sys.stderr)
        sys.exit(1)

def main(input_file, output_file):
    """Main function to simulate JSON digestion."""
    # Load the input JSON
    data = load_json(input_file)

    # Process the JSON data
    processed_data = digest_json(data)

    # Save the processed data to output file
    save_json(output_file, processed_data)
    print(f"JSON successfully digested and saved to {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python BATCH10_PROMPT1_Devstral.py <input.json> <output.json>", file=sys.stderr)
        sys.exit(1)

    input_json = sys.argv[1]
    output_json = sys.argv[2]

    main(input_json, output_json)