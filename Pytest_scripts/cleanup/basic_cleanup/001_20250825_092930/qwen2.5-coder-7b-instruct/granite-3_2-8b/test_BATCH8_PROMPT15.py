# BATCH8_PROMPT15_Granite.py

def count_words(file_path):
    """
    Counts words from a file and exaggerates counts for words with 'e' appearing more than 3 times.

    Args:
    - file_path (str): Path to the text file to be read.

    Returns:
    - dict: A dictionary where keys are words and values are their exaggerated/actual counts.
    """
    
    # Initialize an empty dictionary for word counts
    word_counts = {}
    
    # Open and read the file
    with open(file_path, 'r') as file:
        for line in file:
            # Split the line into words
            words = line.split()
            
            # Process each word
            for word in words:
                # Remove punctuation and convert to lowercase for case-insensitive comparison
                cleaned_word = ''.join(e for e in word if e.isalnum()).lower()
                
                # Count the 'e' occurrences in the word
                e_count = sum(1 for letter in cleaned_word if letter == 'e')
                
                # If the word has more than 3 'e's, exaggerate its count
                if e_count > 3:
                    word_counts[cleaned_word] = word_counts.get(cleaned_word, 0) * 3
                else:
                    word_counts[cleaned_word] = word_counts.get(cleaned_word, 0) + 1
    
    return word_counts


def main():
    """
    Entry point of the program - reads a file and prints exaggerated word counts.
    """
    # Replace 'your_text_file.txt' with the path to your text file
    file_path = 'your_text_file.txt'
    
    try:
        # Get word counts
        word_counts = count_words(file_path)
        
        # Print results
        for word, count in sorted(word_counts.items()):
            print(f"{word}: {count}")
    except FileNotFoundError:
        print("File not found. Please check the file path.")


if __name__ == "__main__":
    main()

# ===== GENERATED TESTS =====
# BATCH8_PROMPT15_Granite.py

def count_words(file_path):
    """
    Counts words from a file and exaggerates counts for words with 'e' appearing more than 3 times.

    Args:
    - file_path (str): Path to the text file to be read.

    Returns:
    - dict: A dictionary where keys are words and values are their exaggerated/actual counts.
    """
    
    # Initialize an empty dictionary for word counts
    word_counts = {}
    
    # Open and read the file
    with open(file_path, 'r') as file:
        for line in file:
            # Split the line into words
            words = line.split()
            
            # Process each word
            for word in words:
                # Remove punctuation and convert to lowercase for case-insensitive comparison
                cleaned_word = ''.join(e for e in word if e.isalnum()).lower()
                
                # Count the 'e' occurrences in the word
                e_count = sum(1 for letter in cleaned_word if letter == 'e')
                
                # If the word has more than 3 'e's, exaggerate its count
                if e_count > 3:
                    word_counts[cleaned_word] = word_counts.get(cleaned_word, 0) * 3
                else:
                    word_counts[cleaned_word] = word_counts.get(cleaned_word, 0) + 1
    
    return word_counts


def main():
    """
    Entry point of the program - reads a file and prints exaggerated word counts.
    """
    # Replace 'your_text_file.txt' with the path to your text file
    file_path = 'your_text_file.txt'
    
    try:
        # Get word counts
        word_counts = count_words(file_path)
        
        # Print results
        for word, count in sorted(word_counts.items()):
            print(f"{word}: {count}")
    except FileNotFoundError:
        print("File not found. Please check the file path.")


if __name__ == "__main__":
    main()


# BATCH8_PROMPT15_Granite_test.py

import pytest
from pathlib import Path
from io import StringIO
import sys

def test_count_words():
    """
    Test cases for count_words function.
    """
    
    # Create a temporary file with some content
    temp_file = Path("temp.txt")
    temp_file.write_text("hello world\nthis is a test\neeeeee eeeee")
    
    # Call the function and capture output
    result = count_words(str(temp_file))
    
    # Check if the results are as expected
    assert 'hello' in result and result['hello'] == 1
    assert 'world' in result and result['world'] == 1
    assert 'this' in result and result['this'] == 1
    assert 'is' in result and result['is'] == 1
    assert 'a' in result and result['a'] == 1
    assert 'test' in result and result['test'] == 1
    assert 'eeeeee' in result and result['eeeeee'] == 9
    
    # Clean up the temporary file
    temp_file.unlink()

def test_count_words_no_file():
    """
    Test case for count_words function when the file does not exist.
    """
    
    with pytest.raises(FileNotFoundError):
        count_words("nonexistent.txt")

def test_count_words_empty_file():
    """
    Test case for count_words function when the file is empty.
    """
    
    temp_file = Path("empty_temp.txt")
    temp_file.write_text("")
    
    result = count_words(str(temp_file))
    
    assert not result
    
    # Clean up the temporary file
    temp_file.unlink()

def test_count_words_with_punctuation():
    """
    Test case for count_words function with punctuation.
    """
    
    temp_file = Path("punctuation_temp.txt")
    temp_file.write_text("hello, world! This is a test. eeeeee, eeeee.")
    
    result = count_words(str(temp_file))
    
    assert 'hello' in result and result['hello'] == 1
    assert 'world' in result and result['world'] == 1
    assert 'this' in result and result['this'] == 1
    assert 'is' in result and result['is'] == 1
    assert 'a' in result and result['a'] == 1
    assert 'test' in result and result['test'] == 1
    assert 'eeeeee' in result and result['eeeeee'] == 9
    
    # Clean up the temporary file
    temp_file.unlink()

def test_count_words_case_insensitive():
    """
    Test case for count_words function with case-insensitivity.
    """
    
    temp_file = Path("case_temp.txt")
    temp_file.write_text("Hello, hello! This is a test. Eeeeee, eeeee.")
    
    result = count_words(str(temp_file))
    
    assert 'hello' in result and result['hello'] == 2
    assert 'this' in result and result['this'] == 1
    assert 'is' in result and result['is'] == 1
    assert 'a' in result and result['a'] == 1
    assert 'test' in result and result['test'] == 1
    assert 'eeeeee' in result and result['eeeeee'] == 9
    
    # Clean up the temporary file
    temp_file.unlink()
