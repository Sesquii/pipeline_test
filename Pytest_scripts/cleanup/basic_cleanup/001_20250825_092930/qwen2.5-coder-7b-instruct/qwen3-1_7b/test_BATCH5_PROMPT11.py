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

# ===== GENERATED TESTS =====
import pytest
from io import StringIO
import sys
import os

# Original script
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

# Test cases
def test_main_with_valid_json(tmp_path):
    """Test main function with a valid JSON file."""
    input_file = tmp_path / "test.json"
    input_file.write_text('{"a": 1, "b": true}')
    
    output_file = tmp_path / "corrupted_test.json"
    assert not output_file.exists()
    
    # Redirect stdout to capture the output
    with open(output_file, 'w') as f:
        sys.stdout = f
        main(["--input-file", str(input_file)])
    
    assert output_file.exists()
    with open(output_file, 'r') as f:
        corrupted_data = json.load(f)
        assert "a" in corrupted_data and isinstance(corrupted_data["a"], str)
        assert "b" in corrupted_data and corrupted_data["b"] is None

def test_main_with_invalid_json(tmp_path):
    """Test main function with an invalid JSON file."""
    input_file = tmp_path / "test.json"
    input_file.write_text('{"a": 1, "b": true')
    
    output_file = tmp_path / "corrupted_test.json"
    assert not output_file.exists()
    
    # Redirect stdout to capture the output
    with open(output_file, 'w') as f:
        sys.stdout = f
        main(["--input-file", str(input_file)])
    
    assert output_file.exists()
    with open(output_file, 'r') as f:
        corrupted_data = json.load(f)
        assert "a" in corrupted_data and isinstance(corrupted_data["a"], str)
        assert "b" not in corrupted_data

def test_main_with_empty_json(tmp_path):
    """Test main function with an empty JSON file."""
    input_file = tmp_path / "test.json"
    input_file.write_text('{}')
    
    output_file = tmp_path / "corrupted_test.json"
    assert not output_file.exists()
    
    # Redirect stdout to capture the output
    with open(output_file, 'w') as f:
        sys.stdout = f
        main(["--input-file", str(input_file)])
    
    assert output_file.exists()
    with open(output_file, 'r') as f:
        corrupted_data = json.load(f)
        assert not corrupted_data

def test_main_with_nonexistent_file(tmp_path):
    """Test main function with a non-existent JSON file."""
    input_file = tmp_path / "nonexistent.json"
    
    output_file = tmp_path / "corrupted_test.json"
    assert not output_file.exists()
    
    # Redirect stdout to capture the output
    with open(output_file, 'w') as f:
        sys.stdout = f
        main(["--input-file", str(input_file)])
    
    assert not output_file.exists()

def test_main_with_large_json(tmp_path):
    """Test main function with a large JSON file."""
    input_file = tmp_path / "test.json"
    large_data = {f"key{i}": i for i in range(1000)}
    input_file.write_text(json.dumps(large_data))
    
    output_file = tmp_path / "corrupted_test.json"
    assert not output_file.exists()
    
    # Redirect stdout to capture the output
    with open(output_file, 'w') as f:
        sys.stdout = f
        main(["--input-file", str(input_file)])
    
    assert output_file.exists()
    with open(output_file, 'r') as f:
        corrupted_data = json.load(f)
        assert len(corrupted_data) == 1000

def test_main_with_boolean_values(tmp_path):
    """Test main function with boolean values."""
    input_file = tmp_path / "test.json"
    input_file.write_text('{"a": true, "b": false}')
    
    output_file = tmp_path / "corrupted_test.json"
    assert not output_file.exists()
    
    # Redirect stdout to capture the output
    with open(output_file, 'w') as f:
        sys.stdout = f
        main(["--input-file", str(input_file)])
    
    assert output_file.exists()
    with open(output_file, 'r') as f:
        corrupted_data = json.load(f)
        assert "a" in corrupted_data and isinstance(corrupted_data["a"], str)
        assert "b" in corrupted_data and corrupted_data["b"] is None

def test_main_with_integer_values(tmp_path):
    """Test main function with integer values."""
    input_file = tmp_path / "test.json"
    input_file.write_text('{"a": 1, "b": 2}')
    
    output_file = tmp_path / "corrupted_test.json"
    assert not output_file.exists()
    
    # Redirect stdout to capture the output
    with open(output_file, 'w') as f:
        sys.stdout = f
        main(["--input-file", str(input_file)])
    
    assert output_file.exists()
    with open(output_file, 'r') as f:
        corrupted_data = json.load(f)
        assert "a" in corrupted_data and isinstance(corrupted_data["a"], str)
        assert "b" in corrupted_data and isinstance(corrupted_data["b"], str)

def test_main_with_float_values(tmp_path):
    """Test main function with float values."""
    input_file = tmp_path / "test.json"
    input_file.write_text('{"a": 1.0, "b": 2.5}')
    
    output_file = tmp_path / "corrupted_test.json"
    assert not output_file.exists()
    
    # Redirect stdout to capture the output
    with open(output_file, 'w') as f:
        sys.stdout = f
        main(["--input-file", str(input_file)])
    
    assert output_file.exists()
    with open(output_file, 'r') as f:
        corrupted_data = json.load(f)
        assert "a" in corrupted_data and isinstance(corrupted_data["a"], str)
        assert "b" in corrupted_data and isinstance(corrupted_data["b"], str)

def test_main_with_string_values(tmp_path):
    """Test main function with string values."""
    input_file = tmp_path / "test.json"
    input_file.write_text('{"a": "1", "b": "2.5"}')
    
    output_file = tmp_path / "corrupted_test.json"
    assert not output_file.exists()
    
    # Redirect stdout to capture the output
    with open(output_file, 'w') as f:
        sys.stdout = f
        main(["--input-file", str(input_file)])
    
    assert output_file.exists()
    with open(output_file, 'r') as f:
        corrupted_data = json.load(f)
        assert "a" in corrupted_data and isinstance(corrupted_data["a"], str)
        assert "b" in corrupted_data and isinstance(corrupted_data["b"], str)

def test_main_with_null_values(tmp_path):
    """Test main function with null values."""
    input_file = tmp_path / "test.json"
    input_file.write_text('{"a": null, "b": null}')
    
    output_file = tmp_path / "corrupted_test.json"
    assert not output_file.exists()
    
    # Redirect stdout to capture the output
    with open(output_file, 'w') as f:
        sys.stdout = f
        main(["--input-file", str(input_file)])
    
    assert output_file.exists()
    with open(output_file, 'r') as f:
        corrupted_data = json.load(f)
        assert "a" in corrupted_data and isinstance(corrupted_data["a"], str)
        assert "b" in corrupted_data and isinstance(corrupted_data["b"], str)

def test_main_with_array_values(tmp_path):
    """Test main function with array values."""
    input_file = tmp_path / "test.json"
    input_file.write_text('{"a": [1, 2], "b": [3.5]}')
    
    output_file = tmp_path / "corrupted_test.json"
    assert not output_file.exists()
    
    # Redirect stdout to capture the output
    with open(output_file, 'w') as f:
        sys.stdout = f
        main(["--input-file", str(input_file)])
    
    assert output_file.exists()
    with open(output_file, 'r') as f:
        corrupted_data = json.load(f)
        assert "a" in corrupted_data and isinstance(corrupted_data["a"], str)
        assert "b" in corrupted_data and isinstance(corrupted_data["b"], str)

def test_main_with_object_values(tmp_path):
    """Test main function with object values."""
    input_file = tmp_path / "test.json"
    input_file.write_text('{"a": {"x": 1}, "b": {"y": 2.5}}')
    
    output_file = tmp_path / "corrupted_test.json"
    assert not output_file.exists()
    
    # Redirect stdout to capture the output
    with open(output_file, 'w') as f:
        sys.stdout = f
        main(["--input-file", str(input_file)])
    
    assert output_file.exists()
    with open(output_file, 'r') as f:
        corrupted_data = json.load(f)
        assert "a" in corrupted_data and isinstance(corrupted_data["a"], str)
        assert "b" in corrupted_data and isinstance(corrupted_data["b"], str)

def test_main_with_mixed_values(tmp_path):
    """Test main function with mixed values."""
    input_file = tmp_path / "test.json"
    input_file.write_text('{"a": 1, "b": true, "c": null, "d": [1, 2], "e": {"x": 3}}')
    
    output_file = tmp_path / "corrupted_test.json"
    assert not output_file.exists()
    
    # Redirect stdout to capture the output
    with open(output_file, 'w') as f:
        sys.stdout = f
        main(["--input-file", str(input_file)])
    
    assert output_file.exists()
    with open(output_file, 'r') as f:
        corrupted_data = json.load(f)
        assert "a" in corrupted_data and isinstance(corrupted_data["a"], str)
        assert "b" in corrupted_data and isinstance(corrupted_data["b"], str)
        assert "c" in corrupted_data and isinstance(corrupted_data["c"], str)
        assert "d" in corrupted_data and isinstance(corrupted_data["d"], str)
        assert "e" in corrupted_data and isinstance(corrupted_data["e"], str)

def test_main_with_large_input_size(tmp_path):
    """Test main function with a large input size."""
    input_file = tmp_path / "test.json"
    large_data = {f"key{i}": i for i in range(10000)}
    input_file.write_text(json.dumps(large_data))
    
    output_file = tmp_path / "corrupted_test.json"
    assert not output_file.exists()
    
    # Redirect stdout to capture the output
    with open(output_file, 'w') as f:
        sys.stdout = f
        main(["--input-file", str(input_file)])
    
    assert output_file.exists()
    with open(output_file, 'r') as f:
        corrupted_data = json.load(f)
        assert len(corrupted_data) == 10000

def test_main_with_empty_string(tmp_path):
    """Test main function with an empty string."""
    input_file = tmp_path / "test.json"
    input_file.write_text('')
    
    output_file = tmp_path / "corrupted_test.json"
    assert not output_file.exists()
    
    # Redirect stdout to capture the output
    with open(output_file, 'w') as f:
        sys.stdout = f
        main(["--input-file", str(input_file)])
    
    assert not output_file.exists()

def test_main_with_whitespace(tmp_path):
    """Test main function with whitespace."""
    input_file = tmp_path / "test.json"
    input_file.write_text('   ')
    
    output_file = tmp_path / "corrupted_test.json"
    assert not output_file.exists()
    
    # Redirect stdout to capture the output
    with open(output_file, 'w') as f:
        sys.stdout = f
        main(["--input-file", str(input_file)])
    
    assert not output_file.exists()

def test_main_with_comment(tmp_path):
    """Test main function with a comment."""
    input_file = tmp_path / "test.json"
    input_file.write_text('// This is a comment\n{"a": 1}')
    
    output_file = tmp_path / "corrupted_test.json"
    assert not output_file.exists()
    
    # Redirect stdout to capture the output
    with open(output_file, 'w') as f:
        sys.stdout = f
        main(["--input-file", str(input_file)])
    
    assert output_file.exists()
    with open(output_file, 'r') as f:
        corrupted_data = json.load(f)
        assert "a" in corrupted_data and isinstance(corrupted_data["a"], str)

def test_main_with_unicode(tmp_path):
    """Test main function with unicode characters."""
    input_file = tmp_path / "test.json"
    input_file.write_text('{"a": "你好", "b": "世界"}')
    
    output_file = tmp_path / "corrupted_test.json"
    assert not output_file.exists()
    
    # Redirect stdout to capture the output
    with open(output_file, 'w') as f:
        sys.stdout = f
        main(["--input-file", str(input_file)])
    
    assert output_file.exists()
    with open(output_file, 'r') as f:
        corrupted_data = json.load(f)
        assert "a" in corrupted_data and isinstance(corrupted_data["a"], str)
        assert "b" in corrupted_data and isinstance(corrupted_data["b"], str)

def test_main_with_special_characters(tmp_path):
    """Test main function with special characters."""
    input_file = tmp_path / "test.json"
    input_file.write_text('{"a": "@#$', "b": "*&^%"}')
    
    output_file = tmp_path / "corrupted_test.json"
    assert not output_file.exists()
    
    # Redirect stdout to capture the output
    with open(output_file, 'w') as f:
        sys.stdout = f
        main(["--input-file", str(input_file)])
    
    assert output_file.exists()
    with open(output_file, 'r') as f:
        corrupted_data = json.load(f)
        assert "a" in corrupted_data and isinstance(corrupted_data["a"], str)
        assert "b" in corrupted_data and isinstance(corrupted_data["b"], str)

def test_main_with_large_numbers(tmp_path):
    """Test main function with large numbers."""
    input_file = tmp_path / "test.json"
    input_file.write_text('{"a": 1234567890, "b": -1234567890}')
    
    output_file = tmp_path / "corrupted_test.json"
    assert not output_file.exists()
    
    # Redirect stdout to capture the output
    with open(output_file, 'w') as f:
        sys.stdout = f
        main(["--input-file", str(input_file)])
    
    assert output_file.exists()
    with open(output_file, 'r') as f:
        corrupted_data = json.load(f)
        assert "a" in corrupted_data and isinstance(corrupted_data["a"], str)
        assert "b" in corrupted_data and isinstance(corrupted_data["b"], str)

def test_main_with_large_floats(tmp_path):
    """Test main function with large floats."""
    input_file = tmp_path / "test.json"
    input_file.write_text('{"a": 1.234567890e+10, "b": -1.234567890e+10}')
    
    output_file = tmp_path / "corrupted_test.json"
    assert not output_file.exists()
    
    # Redirect stdout to capture the output
    with open(output_file, 'w') as f:
        sys.stdout = f
        main(["--input-file", str(input_file)])
    
    assert output_file.exists()
    with open(output_file, 'r') as f:
        corrupted_data = json.load(f)
        assert "a" in corrupted_data and isinstance(corrupted_data["a"], str)
        assert "b" in corrupted_data and isinstance(corrupted_data["b"], str)

def test_main_with_large_strings(tmp_path):
    """Test main function with large strings."""
    input_file = tmp_path / "test.json"
    large_string = 'a' * 10000
    input_file.write_text(f'{{"a": "{large_string}"}}')
    
    output_file = tmp_path / "corrupted_test.json"
    assert not output_file.exists()
    
    # Redirect stdout to capture the output
    with open(output_file, 'w') as f:
        sys.stdout = f
        main(["--input-file", str(input_file)])
    
    assert output_file.exists()
    with open(output_file, 'r') as f:
        corrupted_data = json.load(f)
        assert "a" in corrupted_data and isinstance(corrupted_data["a"], str)

def test_main_with_large_arrays(tmp_path):
    """Test main function with large arrays."""
    input_file = tmp_path / "test.json"
    large_array = [1] * 10000
    input_file.write_text(f'{{"a": {json.dumps(large_array)}}}')
    
    output_file = tmp_path / "corrupted_test.json"
    assert not output_file.exists()
    
    # Redirect stdout to capture the output
    with open(output_file, 'w') as f:
        sys.stdout = f
        main(["--input-file", str(input_file)])
    
    assert output_file.exists()
    with open(output_file, 'r') as f:
        corrupted_data = json.load(f)
        assert "a" in corrupted_data and isinstance(corrupted_data["