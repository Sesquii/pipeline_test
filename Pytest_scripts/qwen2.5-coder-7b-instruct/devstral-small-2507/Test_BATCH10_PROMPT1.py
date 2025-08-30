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



import json
import sys
from unittest.mock import patch, mock_open
import pytest

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


# Test cases for BATCH10_PROMPT1_Devstral.py

def test_load_json():
    """Test the load_json function."""
    with patch('builtins.open', mock_open(read_data='{"key": "value"}')):
        data = load_json('test.json')
        assert data == {'key': 'value'}

def test_load_json_file_not_found(monkeypatch):
    """Test the load_json function when file is not found."""
    monkeypatch.setattr('builtins.open', mock_open(side_effect=FileNotFoundError))
    with pytest.raises(SystemExit) as excinfo:
        load_json('nonexistent.json')
    assert excinfo.value.code == 1

def test_load_json_decode_error(monkeypatch):
    """Test the load_json function when JSON decode error occurs."""
    monkeypatch.setattr('builtins.open', mock_open(read_data='invalid json'))
    with pytest.raises(SystemExit) as excinfo:
        load_json('invalid.json')
    assert excinfo.value.code == 1

def test_digest_json_dict():
    """Test the digest_json function on a dictionary."""
    data = {'key': 'value'}
    processed_data = digest_json(data)
    assert processed_data == {'KEY': 'VALUE'}

def test_digest_json_list():
    """Test the digest_json function on a list."""
    data = ['item1', 'item2']
    processed_data = digest_json(data)
    assert processed_data == ['ITEM1', 'ITEM2']

def test_digest_json_string():
    """Test the digest_json function on a string."""
    data = 'string'
    processed_data = digest_json(data)
    assert processed_data == 'STRING'

def test_digest_json_other_type():
    """Test the digest_json function on other types."""
    data = 123
    processed_data = digest_json(data)
    assert processed_data == 123

def test_save_json(monkeypatch):
    """Test the save_json function."""
    mock_file = mock_open()
    monkeypatch.setattr('builtins.open', mock_file)
    data = {'key': 'value'}
    save_json('test.json', data)
    mock_file.assert_called_once_with('test.json', 'w')
    handle = mock_file()
    handle.write.assert_called_once()

def test_save_json_io_error(monkeypatch):
    """Test the save_json function when IO error occurs."""
    monkeypatch.setattr('builtins.open', mock_open(side_effect=IOError))
    with pytest.raises(SystemExit) as excinfo:
        save_json('test.json', {'key': 'value'})
    assert excinfo.value.code == 1

def test_main(monkeypatch, capsys):
    """Test the main function."""
    input_data = '{"key": "value"}'
    expected_output = '{"KEY": "VALUE"}\n'

    with patch('builtins.open', mock_open(read_data=input_data)):
        with patch('BATCH10_PROMPT1_Devstral.save_json') as mock_save:
            monkeypatch.setattr(sys, 'argv', ['script.py', 'input.json', 'output.json'])
            main('input.json', 'output.json')
            mock_save.assert_called_once_with('output.json', expected_output)
    captured = capsys.readouterr()
    assert captured.out == f"JSON successfully digested and saved to output.json\n"

def test_main_invalid_args(monkeypatch, capsys):
    """Test the main function with invalid arguments."""
    monkeypatch.setattr(sys, 'argv', ['script.py'])
    with pytest.raises(SystemExit) as excinfo:
        main('input.json', 'output.json')
    assert excinfo.value.code == 1
    captured = capsys.readouterr()
    assert captured.err == "Usage: python BATCH10_PROMPT1_Devstral.py <input.json> <output.json>\n"
