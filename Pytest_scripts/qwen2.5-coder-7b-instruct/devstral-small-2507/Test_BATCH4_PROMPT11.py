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

# ===== GENERATED TESTS =====
```python
import pytest
from typing import Any, Dict, List, Union

# Original script code remains unchanged as per requirement 1.

def test_corrupt_value_int():
    """Test corrupt_value function with an integer."""
    value = 42
    result = corrupt_value(value)
    assert isinstance(result, str), "Result should be a string"

def test_corrupt_value_float():
    """Test corrupt_value function with a float."""
    value = 3.14
    result = corrupt_value(value)
    assert isinstance(result, bool), "Result should be a boolean"

def test_corrupt_value_str():
    """Test corrupt_value function with a string."""
    value = "hello"
    result = corrupt_value(value)
    assert result is None, "Result should be None"

def test_corrupt_value_bool():
    """Test corrupt_value function with a boolean."""
    value = True
    result = corrupt_value(value)
    assert isinstance(result, int), "Result should be an integer"

def test_corrupt_value_none():
    """Test corrupt_value function with None."""
    value = None
    result = corrupt_value(value)
    assert result == "null", "Result should be 'null'"

def test_corrupt_value_list():
    """Test corrupt_value function with a list."""
    value = [1, 2.0, "three", True, None]
    result = corrupt_value(value)
    assert isinstance(result, list), "Result should be a list"
    for item in result:
        if isinstance(item, str):
            assert isinstance(item, str), "String items should remain strings"
        elif isinstance(item, bool):
            assert isinstance(item, bool), "Boolean items should remain booleans"
        elif item is None:
            assert item == "null", "None items should be 'null'"
        else:
            assert isinstance(item, int), "Other items should be integers"

def test_corrupt_value_dict():
    """Test corrupt_value function with a dictionary."""
    value = {"a": 1, "b": 2.0, "c": "three", "d": True, "e": None}
    result = corrupt_value(value)
    assert isinstance(result, dict), "Result should be a dictionary"
    for key, item in result.items():
        if isinstance(item, str):
            assert isinstance(item, str), f"String items under {key} should remain strings"
        elif isinstance(item, bool):
            assert isinstance(item, bool), f"Boolean items under {key} should remain booleans"
        elif item is None:
            assert item == "null", f"None items under {key} should be 'null'"
        else:
            assert isinstance(item, int), f"Other items under {key} should be integers"

def test_corrupt_json():
    """Test corrupt_json function."""
    data = {
        "a": 1,
        "b": 2.0,
        "c": "three",
        "d": True,
        "e": None
    }
    corrupted_data = corrupt_json(data)
    assert isinstance(corrupted_data, dict), "Result should be a dictionary"
    for key in data:
        if random.random() < 0.1:
            if isinstance(data[key], int):
                assert isinstance(corrupted_data[key], str), f"Integer {key} should be a string"
            elif isinstance(data[key], float):
                assert isinstance(corrupted_data[key], bool), f"Float {key} should be a boolean"
            elif data[key] is None:
                assert corrupted_data[key] == "null", f"None {key} should be 'null'"
            else:
                assert isinstance(corrupted_data[key], int), f"Other {key} should be an integer"
        else:
            assert corrupted_data[key] == data[key], f"{key} should remain unchanged"

def test_main_valid_input_output(tmp_path):
    """Test main function with valid input and output."""
    input_json = tmp_path / "input.json"
    output_json = tmp_path / "output.json"
    
    input_data = {
        "a": 1,
        "b": 2.0,
        "c": "three",
        "d": True,
        "e": None
    }
    
    with open(input_json, 'w') as f:
        json.dump(input_data, f)
    
    main(str(input_json), str(output_json))
    
    assert output_json.exists(), "Output file should exist"
    with open(output_json, 'r') as f:
        corrupted_data = json.load(f)
        for key in input_data:
            if random.random() < 0.1:
                if isinstance(input_data[key], int):
                    assert isinstance(corrupted_data[key], str), f"Integer {key} should be a string"
                elif isinstance(input_data[key], float):
                    assert isinstance(corrupted_data[key], bool), f"Float {key} should be a boolean"
                elif input_data[key] is None:
                    assert corrupted_data[key] == "null", f"None {key} should be 'null'"
                else:
                    assert isinstance(corrupted_data[key], int), f"Other {key} should be an integer"
            else:
                assert corrupted_data[key] == input_data[key], f"{key} should remain unchanged"

def test_main_invalid_input():
    """Test main function with invalid input."""
    with pytest.raises(ValueError) as excinfo:
        main("nonexistent.json", "output.json")
    assert str(excinfo.value) == "Error: [Errno 2] No such file or directory: 'nonexistent.json'", "Exception message should match"

def test_main_invalid_json_input():
    """Test main function with invalid JSON input."""
    input_json = "invalid.json"
    
    with open(input_json, 'w') as f:
        f.write("not a json")
    
    with pytest.raises(ValueError) as excinfo:
        main(input_json, "output.json")
    assert str(excinfo.value) == "Error: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)", "Exception message should match"

def test_main_invalid_output():
    """Test main function with invalid output."""
    input_json = "input.json"
    
    with open(input_json, 'w') as f:
        json.dump({"a": 1}, f)
    
    with pytest.raises(ValueError) as excinfo:
        main(str(input_json), "/invalid/output/path")
    assert str(excinfo.value).startswith("Error: [Errno 2]"), "Exception message should start with '[Errno 2]'"
```