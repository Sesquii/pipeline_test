import re
from collections import Counter

# Define color mappings to emojis
COLOR_EMOJI_MAP = {
    'red': '🔴',
    'blue': '🔵',
    'green': '🟢',
    'yellow': '🟡',
    'orange': '🟠',
    'purple': '🟣',
    'pink': '🹖',
    'brown': '🤎',
    'gray': '⬛',
    'black': '⬜',
    'white': '☐'
}

def count_color_words(text):
    """Count occurrences of color-related words in the text."""
    # Create a regex pattern to match color words
    pattern = r'\b(?:' + '|'.join(COLOR_EMOJI_MAP.keys()) + r')\b'
    matches = re.findall(pattern, text.lower())
    return Counter(matches)

def compress_text(text):
    """Compress text by replacing most frequent color word with corresponding emoji."""
    color_counts = count_color_words(text)
    
    if not color_counts:
        return text  # No color words found, return original text
    
    # Find the most common color word
    most_common_color = color_counts.most_common(1)[0][0]
    emoji = COLOR_EMOJI_MAP[most_common_color]
    
    # Replace occurrences of the most common color with its emoji
    pattern = r'\b' + re.escape(most_common_color) + r'\b'
    compressed_text = re.sub(pattern, emoji, text, flags=re.IGNORECASE)
    
    return compressed_text

def process_file(input_file_path):
    """Process a file by compressing color-related words."""
    try:
        with open(input_file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        compressed_content = compress_text(content)
        
        # Create output filename by replacing .txt with _compressed.txt
        if input_file_path.endswith('.txt'):
            output_file_path = input_file_path[:-4] + '_compressed.txt'
        else:
            output_file_path = input_file_path + '_compressed.txt'
        
        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.write(compressed_content)
        
        print(f"Compression complete. Output saved to: {output_file_path}")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python BATCH3_PROMPT14_<model_name>.py <input_file.txt>")
        sys.exit(1)

    input_file = sys.argv[1]
    process_file(input_file)

# ===== GENERATED TESTS =====
```python
import pytest
from typing import List, Tuple

# Original code remains unchanged

# Test suite for the script

def test_count_color_words():
    """Test the count_color_words function."""
    text = "The red ball is blue and the green apple."
    expected_result = Counter({'red': 1, 'blue': 1, 'green': 1})
    assert count_color_words(text) == expected_result

    # Test with no color words
    text = "This is a test sentence without any color words."
    expected_result = Counter()
    assert count_color_words(text) == expected_result

def test_compress_text():
    """Test the compress_text function."""
    text = "The red ball is blue and the green apple."
    expected_result = "The 🔴 ball is 🔵 and the 🟢 apple."
    assert compress_text(text) == expected_result

    # Test with no color words
    text = "This is a test sentence without any color words."
    expected_result = "This is a test sentence without any color words."
    assert compress_text(text) == expected_result

def test_process_file(tmp_path):
    """Test the process_file function."""
    input_file_path = tmp_path / 'test_input.txt'
    input_file_path.write_text("The red ball is blue and the green apple.")
    
    process_file(str(input_file_path))
    
    output_file_path = str(input_file_path.with_name('test_input_compressed.txt'))
    assert output_file_path.exists()
    with open(output_file_path, 'r', encoding='utf-8') as file:
        compressed_content = file.read()
    expected_result = "The 🔴 ball is 🔵 and the 🟢 apple."
    assert compressed_content == expected_result

def test_process_file_nonexistent_file(tmp_path):
    """Test the process_file function with a non-existent file."""
    input_file_path = tmp_path / 'nonexistent.txt'
    
    with pytest.raises(FileNotFoundError):
        process_file(str(input_file_path))

# Test cases using fixtures and parametrization
@pytest.fixture(params=[
    ("The red ball is blue and the green apple.", "The 🔴 ball is 🔵 and the 🟢 apple."),
    ("This is a test sentence without any color words.", "This is a test sentence without any color words.")
])
def input_output_pairs(request):
    return request.param

def test_compress_text_with_fixture(input_output_pairs: Tuple[str, str]):
    """Test the compress_text function with fixture."""
    input_text, expected_result = input_output_pairs
    assert compress_text(input_text) == expected_result

# Test cases using parametrization
@pytest.mark.parametrize("input_text, expected_result", [
    ("The red ball is blue and the green apple.", "The 🔴 ball is 🔵 and the 🟢 apple."),
    ("This is a test sentence without any color words.", "This is a test sentence without any color words.")
])
def test_compress_text_with_parametrize(input_text: str, expected_result: str):
    """Test the compress_text function with parametrize."""
    assert compress_text(input_text) == expected_result
```

This comprehensive test suite covers all public functions and classes in the original script. It includes both positive and negative test cases, uses pytest fixtures and parametrization where appropriate, adds type hints to test functions, follows PEP 8 style guidelines, and includes proper docstrings and comments.