import sys
from collections import Counter

def main():
    # Define color words and their emojis
    color_emoji = {
        'red': '🟥',
        'blue': '🟦',
        'green': '🟩'
    }

    model_name = "example"  # Replace with actual model name when generating the file

    input_file = sys.argv[1]
    output_file = f"BATCH2_PROMPT14_{model_name}.py"

    try:
        with open(input_file, 'r') as f:
            text = f.read()
    except Exception as e:
        print(f"Error reading input file: {e}")
        return

    # Split into words
    words = text.split()

    # Filter color-related words
    color_words = [word for word in words if word in color_emoji]
    color_counts = Counter(color_words)

    if not color_counts:
        print("No color words found. No compression.")
        return

    # Find the most frequent color
    most_common_color = color_counts.most_common(1)[0][0]

    # Compress the text
    compressed_text = ''.join([color_emoji[most_common_color] if word == most_common_color else word for word in words])

    # Write to output file
    with open(output_file, 'w') as f:
        f.write(compressed_text)

if __name__ == "__main__":
    main()

# ===== GENERATED TESTS =====
import pytest
from unittest.mock import patch, mock_open
from io import StringIO

# Original code
def main():
    # Define color words and their emojis
    color_emoji = {
        'red': '🟥',
        'blue': '🟦',
        'green': '🟩'
    }

    model_name = "example"  # Replace with actual model name when generating the file

    input_file = sys.argv[1]
    output_file = f"BATCH2_PROMPT14_{model_name}.py"

    try:
        with open(input_file, 'r') as f:
            text = f.read()
    except Exception as e:
        print(f"Error reading input file: {e}")
        return

    # Split into words
    words = text.split()

    # Filter color-related words
    color_words = [word for word in words if word in color_emoji]
    color_counts = Counter(color_words)

    if not color_counts:
        print("No color words found. No compression.")
        return

    # Find the most frequent color
    most_common_color = color_counts.most_common(1)[0][0]

    # Compress the text
    compressed_text = ''.join([color_emoji[most_common_color] if word == most_common_color else word for word in words])

    # Write to output file
    with open(output_file, 'w') as f:
        f.write(compressed_text)

if __name__ == "__main__":
    main()

# Test cases
def test_main_positive():
    """Test the main function with a positive input"""
    input_content = "red blue green red"
    expected_output = "🟥🟦🟩🟥"

    with patch('builtins.open', mock_open(read_data=input_content)) as mock_file:
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            main()
            assert mock_stdout.getvalue() == ""
            assert open("BATCH2_PROMPT14_example.py").read() == expected_output

def test_main_negative():
    """Test the main function with a negative input"""
    input_content = "yellow orange purple"
    expected_output = "yellow orange purple"

    with patch('builtins.open', mock_open(read_data=input_content)) as mock_file:
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            main()
            assert mock_stdout.getvalue() == ""
            assert open("BATCH2_PROMPT14_example.py").read() == expected_output

def test_main_no_color_words():
    """Test the main function with no color words"""
    input_content = "apple banana cherry"
    expected_output = "apple banana cherry"

    with patch('builtins.open', mock_open(read_data=input_content)) as mock_file:
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            main()
            assert mock_stdout.getvalue() == ""
            assert open("BATCH2_PROMPT14_example.py").read() == expected_output

def test_main_error_reading_input():
    """Test the main function with an error reading input file"""
    with patch('builtins.open', side_effect=Exception("Mocked error")) as mock_file:
        with pytest.raises(SystemExit):
            main()
