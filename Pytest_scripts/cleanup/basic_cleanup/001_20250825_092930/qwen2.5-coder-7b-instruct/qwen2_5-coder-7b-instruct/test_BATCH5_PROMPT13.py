import re
from collections import Counter

# Define a list of common words to exaggerate the count
COMMON_WORDS = {'the', 'a', 'an', 'in', 'on', 'at', 'to', 'of', 'and', 'but'}

def exaggerated_word_counter(file_path):
    """
    Counts occurrences of each word in a text file, with an exaggerated count for common words.
    
    Args:
        file_path (str): The path to the input text file.
        
    Returns:
        dict: A dictionary containing the word counts.
    """
    # Initialize a counter object
    word_counts = Counter()
    
    # Open and read the file
    with open(file_path, 'r') as file:
        for line in file:
            # Use regex to find words and convert them to lower case to normalize counting
            words = re.findall(r'\b\w+\b', line.lower())
            for word in words:
                if word in COMMON_WORDS:
                    # Exaggerate count by multiplying
                    word_counts[word] += 100
                else:
                    word_counts[word] += 1
    
    return word_counts

if __name__ == "__main__":
    # Replace 'example.txt' with the path to your text file
    input_file_path = 'example.txt'
    result = exaggerated_word_counter(input_file_path)
    print(result)

# ===== GENERATED TESTS =====
import pytest
from collections import Counter

# Define a list of common words to exaggerate the count
COMMON_WORDS = {'the', 'a', 'an', 'in', 'on', 'at', 'to', 'of', 'and', 'but'}

def exaggerated_word_counter(file_path):
    """
    Counts occurrences of each word in a text file, with an exaggerated count for common words.
    
    Args:
        file_path (str): The path to the input text file.
        
    Returns:
        dict: A dictionary containing the word counts.
    """
    # Initialize a counter object
    word_counts = Counter()
    
    # Open and read the file
    with open(file_path, 'r') as file:
        for line in file:
            # Use regex to find words and convert them to lower case to normalize counting
            words = re.findall(r'\b\w+\b', line.lower())
            for word in words:
                if word in COMMON_WORDS:
                    # Exaggerate count by multiplying
                    word_counts[word] += 100
                else:
                    word_counts[word] += 1
    
    return word_counts

# Test suite using pytest

@pytest.fixture
def sample_text_file(tmp_path):
    """Create a temporary text file with sample content."""
    content = "The quick brown fox jumps over the lazy dog. The fox is very clever."
    file_path = tmp_path / 'sample.txt'
    with open(file_path, 'w') as file:
        file.write(content)
    return file_path

def test_exaggerated_word_counter(sample_text_file):
    """
    Test the exaggerated_word_counter function with a sample text file.
    
    This test checks if the function correctly counts words, including common words
    with an exaggerated count.
    """
    result = exaggerated_word_counter(sample_text_file)
    expected_result = Counter({'the': 200, 'quick': 1, 'brown': 1, 'fox': 201, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1, 'is': 1, 'very': 1, 'clever': 1})
    assert result == expected_result

def test_exaggerated_word_counter_empty_file(tmp_path):
    """
    Test the exaggerated_word_counter function with an empty text file.
    
    This test checks if the function returns an empty dictionary when given an empty file.
    """
    file_path = tmp_path / 'empty.txt'
    with open(file_path, 'w') as file:
        pass
    result = exaggerated_word_counter(file_path)
    assert result == Counter()

def test_exaggerated_word_counter_nonexistent_file():
    """
    Test the exaggerated_word_counter function with a non-existent file.
    
    This test checks if the function raises a FileNotFoundError when given a non-existent file.
    """
    with pytest.raises(FileNotFoundError):
        exaggerated_word_counter('nonexistent.txt')

# Add more tests as needed

This test suite includes:
- A fixture to create a temporary text file for testing purposes.
- Tests for both positive and negative scenarios, including an empty file and a non-existent file.
- Type hints are not directly applicable to pytest fixtures or functions in the same way they are for Python functions, but type annotations are used where appropriate within the test cases.