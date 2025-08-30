# BATCH2_PROMPT14_Qwen.py

def count_color_words(file_path):
    """
    Count the frequency of color-related words in a given text file.
    
    Args:
    file_path (str): Path to the input text file.
    
    Returns:
    dict: A dictionary with color words as keys and their frequencies as values.
    """
    color_words = {
        'red': 0,
        'blue': 0,
        'green': 0,
        # Add more color words as needed
    }
    
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                if word.lower() in color_words:
                    color_words[word.lower()] += 1
    
    return color_words

def compress_file(file_path):
    """
    Compress the input text file by replacing a portion of the text with an emoji
    corresponding to the most frequent color.
    
    Args:
    file_path (str): Path to the input text file.
    """
    # Get the color word frequencies
    color_frequencies = count_color_words(file_path)
    
    # Find the most frequent color
    if not color_frequencies:
        print("No color words found in the file.")
        return
    
    most_frequent_color = max(color_frequencies, key=color_frequencies.get)
    emoji_mapping = {
        'red': '🔴',
        'blue': '🔵',
        'green': '🟢',
        # Add more mappings as needed
    }
    
    if most_frequent_color in emoji_mapping:
        replacement_emoji = emoji_mapping[most_frequent_color]
        
        # Replace the most frequent color word with its corresponding emoji
        with open(file_path, 'r') as file:
            content = file.read()
        
        compressed_content = content.replace(most_frequent_color, replacement_emoji)
        
        with open(file_path, 'w') as file:
            file.write(compressed_content)
        
        print(f"File compressed. Replaced '{most_frequent_color}' with {replacement_emoji}.")
    else:
        print(f"No emoji mapping available for the most frequent color: {most_frequent_color}")

if __name__ == "__main__":
    input_file_path = 'input.txt'  # Replace with your input file path
    compress_file(input_file_path)

This script counts the frequency of color-related words in a text file and replaces them with corresponding emojis. It uses basic Python features and does not require any external libraries. The code is designed to be self-contained, clear, and easy to modify for different sets of color words and their corresponding emojis.

# ===== GENERATED TESTS =====
# BATCH2_PROMPT14_Qwen.py

def count_color_words(file_path):
    """
    Count the frequency of color-related words in a given text file.
    
    Args:
    file_path (str): Path to the input text file.
    
    Returns:
    dict: A dictionary with color words as keys and their frequencies as values.
    """
    color_words = {
        'red': 0,
        'blue': 0,
        'green': 0,
        # Add more color words as needed
    }
    
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                if word.lower() in color_words:
                    color_words[word.lower()] += 1
    
    return color_words

def compress_file(file_path):
    """
    Compress the input text file by replacing a portion of the text with an emoji
    corresponding to the most frequent color.
    
    Args:
    file_path (str): Path to the input text file.
    """
    # Get the color word frequencies
    color_frequencies = count_color_words(file_path)
    
    # Find the most frequent color
    if not color_frequencies:
        print("No color words found in the file.")
        return
    
    most_frequent_color = max(color_frequencies, key=color_frequencies.get)
    emoji_mapping = {
        'red': '🔴',
        'blue': '🔵',
        'green': '🟢',
        # Add more mappings as needed
    }
    
    if most_frequent_color in emoji_mapping:
        replacement_emoji = emoji_mapping[most_frequent_color]
        
        # Replace the most frequent color word with its corresponding emoji
        with open(file_path, 'r') as file:
            content = file.read()
        
        compressed_content = content.replace(most_frequent_color, replacement_emoji)
        
        with open(file_path, 'w') as file:
            file.write(compressed_content)
        
        print(f"File compressed. Replaced '{most_frequent_color}' with {replacement_emoji}.")
    else:
        print(f"No emoji mapping available for the most frequent color: {most_frequent_color}")

if __name__ == "__main__":
    input_file_path = 'input.txt'  # Replace with your input file path
    compress_file(input_file_path)

# BATCH2_PROMPT14_Qwen_test.py

import pytest
from pathlib import Path
from io import StringIO
import os

def test_count_color_words():
    """Test the count_color_words function."""
    # Create a temporary file for testing
    with NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_path = temp_file.name
        temp_file.write("red blue green red Blue")
    
    result = count_color_words(temp_path)
    assert result == {'red': 2, 'blue': 2, 'green': 1}
    
    # Clean up the temporary file
    os.remove(temp_path)

def test_compress_file():
    """Test the compress_file function."""
    # Create a temporary file for testing
    with NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_path = temp_file.name
        temp_file.write("red blue green red Blue")
    
    # Call the compress_file function
    compress_file(temp_path)
    
    # Read the content of the compressed file
    with open(temp_path, 'r') as file:
        content = file.read()
    
    assert "🔴🔵🟢🔴🔵" in content
    
    # Clean up the temporary file
    os.remove(temp_path)

def test_compress_file_no_color_words():
    """Test the compress_file function when no color words are present."""
    # Create a temporary file for testing
    with NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_path = temp_file.name
        temp_file.write("This is a test file without any color words.")
    
    # Call the compress_file function
    compress_file(temp_path)
    
    # Read the content of the compressed file
    with open(temp_path, 'r') as file:
        content = file.read()
    
    assert "No color words found in the file." in content
    
    # Clean up the temporary file
    os.remove(temp_path)

def test_compress_file_no_emoji_mapping():
    """Test the compress_file function when no emoji mapping is available."""
    # Create a temporary file for testing
    with NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_path = temp_file.name
        temp_file.write("red blue green red Blue")
    
    # Modify the emoji_mapping to remove 'blue'
    original_emoji_mapping = compress_file.emoji_mapping.copy()
    del compress_file.emoji_mapping['blue']
    
    # Call the compress_file function
    compress_file(temp_path)
    
    # Read the content of the compressed file
    with open(temp_path, 'r') as file:
        content = file.read()
    
    assert "No emoji mapping available for the most frequent color: blue" in content
    
    # Restore the original emoji_mapping
    compress_file.emoji_mapping = original_emoji_mapping
    
    # Clean up the temporary file
    os.remove(temp_path)
