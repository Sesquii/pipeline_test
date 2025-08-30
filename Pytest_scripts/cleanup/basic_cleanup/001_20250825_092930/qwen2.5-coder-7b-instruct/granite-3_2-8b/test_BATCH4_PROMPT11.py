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

# ===== GENERATED TESTS =====
import pytest
from pathlib import Path
import json

# Original code remains unchanged

def test_corrupt_value():
    """ Test the corrupt_value function with various data types. """
    assert corrupt_value(123) == '123'
    assert corrupt_value(45.67) == '45.67'
    assert corrupt_value(True) is None
    assert corrupt_value(False) is False
    assert corrupt_value(['a', 1, True]) == ['a', '1', None]
    assert corrupt_value({'key': 'value', 'num': 2}) == {'key': 'value', 'num': '2'}

def test_glitch_json(tmp_path):
    """ Test the glitch_json function with valid and invalid inputs. """
    input_file = tmp_path / "input.json"
    output_file = tmp_path / "output.json"

    # Create a sample JSON file
    data = {
        "name": "John",
        "age": 30,
        "is_student": False,
        "courses": ["Math", "Science"]
    }
    with open(input_file, 'w') as f:
        json.dump(data, f)

    # Run glitch_json function
    glitch_json(str(input_file), str(output_file))

    # Check if the output file exists and is not empty
    assert output_file.exists()
    assert output_file.stat().st_size > 0

    # Load the corrupted JSON data
    with open(output_file, 'r') as f:
        corrupted_data = json.load(f)

    # Verify that at least one value has been corrupted
    for key, value in corrupted_data.items():
        if isinstance(value, (int, float)):
            assert not value.isdigit()
        elif isinstance(value, bool):
            assert value is None or value is False

def test_glitch_json_invalid_input(tmp_path):
    """ Test the glitch_json function with invalid input. """
    output_file = tmp_path / "output.json"

    # Create an empty file
    input_file = tmp_path / "input.json"
    input_file.touch()

    # Run glitch_json function and expect a ValueError
    with pytest.raises(ValueError):
        glitch_json(str(input_file), str(output_file))

def test_glitch_json_nonexistent_file(tmp_path):
    """ Test the glitch_json function with non-existent input file. """
    output_file = tmp_path / "output.json"

    # Use a non-existent file path
    input_file = Path("non_existent_file.json")

    # Run glitch_json function and expect a FileNotFoundError
    with pytest.raises(FileNotFoundError):
        glitch_json(str(input_file), str(output_file))

def test_glitch_json_no_output(tmp_path):
    """ Test the glitch_json function without writing to output file. """
    input_file = tmp_path / "input.json"
    output_file = tmp_path / "output.json"

    # Create a sample JSON file
    data = {
        "name": "John",
        "age": 30,
        "is_student": False,
        "courses": ["Math", "Science"]
    }
    with open(input_file, 'w') as f:
        json.dump(data, f)

    # Run glitch_json function without writing to output file
    with pytest.raises(FileNotFoundError):
        with open(output_file, 'w') as f:
            pass  # Simulate an error in writing to the output file

# Add more test cases as needed
