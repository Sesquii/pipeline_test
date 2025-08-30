# BATCH10_PROMPT18_gpt_4.py

# Importing the required module for random selection of words
import random

# List of short words to form sentences
words = ["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]

def create_sentence():
    # Selecting seven random words from the list
    sentence_words = random.sample(words, 7)
    # Joining the selected words to form a sentence
    return ' '.join(sentence_words) + '.'

# Main function to execute the program
if __name__ == "__main__":
    # Printing three sentences each containing exactly seven words
    for _ in range(3):
        print(create_sentence())

# ===== GENERATED TESTS =====
# BATCH10_PROMPT18_gpt_4.py

# Importing the required module for random selection of words
import random

# List of short words to form sentences
words = ["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]

def create_sentence():
    # Selecting seven random words from the list
    sentence_words = random.sample(words, 7)
    # Joining the selected words to form a sentence
    return ' '.join(sentence_words) + '.'

# Main function to execute the program
if __name__ == "__main__":
    # Printing three sentences each containing exactly seven words
    for _ in range(3):
        print(create_sentence())

# Test suite for BATCH10_PROMPT18_gpt_4.py

import pytest
from typing import List

# Fixture to provide a list of words
@pytest.fixture
def word_list() -> List[str]:
    return ["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]

# Test function for create_sentence
def test_create_sentence(word_list: List[str]):
    # Arrange
    expected_length = 7
    
    # Act
    sentence = create_sentence()
    words_in_sentence = sentence.split()
    
    # Assert
    assert len(words_in_sentence) == expected_length, "Sentence does not contain exactly seven words"
    assert sentence.endswith('.'), "Sentence does not end with a period"

# Test function for create_sentence with negative test cases
def test_create_sentence_negative(word_list: List[str]):
    # Arrange
    expected_length = 7
    
    # Act
    sentence = create_sentence()
    words_in_sentence = sentence.split()
    
    # Assert
    assert len(words_in_sentence) != expected_length + 1, "Sentence contains more than seven words"
    assert len(words_in_sentence) != expected_length - 1, "Sentence contains fewer than seven words"

# Test function for create_sentence with empty word list
def test_create_sentence_empty_word_list():
    # Arrange
    original_words = words.copy()
    words.clear()
    
    # Act
    sentence = create_sentence()
    words_in_sentence = sentence.split()
    
    # Assert
    assert len(words_in_sentence) == 7, "Sentence does not contain exactly seven words when word list is empty"
    assert ' '.join(original_words).lower() in sentence.lower(), "Sentence does not contain any of the original words"

# Test function for create_sentence with non-string elements in word list
def test_create_sentence_non_string_elements(word_list: List[str]):
    # Arrange
    original_words = words.copy()
    words.append(123)  # Adding a non-string element
    
    # Act
    sentence = create_sentence()
    words_in_sentence = sentence.split()
    
    # Assert
    assert len(words_in_sentence) == 7, "Sentence does not contain exactly seven words when word list contains non-string elements"
    assert ' '.join(original_words).lower() in sentence.lower(), "Sentence does not contain any of the original words"

# Test function for create_sentence with string elements that are not words
def test_create_sentence_non_word_elements(word_list: List[str]):
    # Arrange
    original_words = words.copy()
    words.append('123')  # Adding a non-word element
    
    # Act
    sentence = create_sentence()
    words_in_sentence = sentence.split()
    
    # Assert
    assert len(words_in_sentence) == 7, "Sentence does not contain exactly seven words when word list contains non-word elements"
    assert ' '.join(original_words).lower() in sentence.lower(), "Sentence does not contain any of the original words"

# Test function for create_sentence with repeated words
def test_create_sentence_repeated_words(word_list: List[str]):
    # Arrange
    original_words = words.copy()
    words.extend(words)  # Doubling the word list
    
    # Act
    sentence = create_sentence()
    words_in_sentence = sentence.split()
    
    # Assert
    assert len(words_in_sentence) == 7, "Sentence does not contain exactly seven words when word list contains repeated elements"
    assert ' '.join(original_words).lower() in sentence.lower(), "Sentence does not contain any of the original words"

# Test function for create_sentence with all spaces as words
def test_create_sentence_all_spaces(word_list: List[str]):
    # Arrange
    original_words = words.copy()
    words.clear()
    words.extend([' '] * 7)  # Adding seven spaces
    
    # Act
    sentence = create_sentence()
    words_in_sentence = sentence.split()
    
    # Assert
    assert len(words_in_sentence) == 7, "Sentence does not contain exactly seven words when word list contains all spaces"
    assert ' '.join(original_words).lower() in sentence.lower(), "Sentence does not contain any of the original words"

# Test function for create_sentence with empty string as a word
def test_create_sentence_empty_string(word_list: List[str]):
    # Arrange
    original_words = words.copy()
    words.clear()
    words.extend(['']) * 7  # Adding seven empty strings
    
    # Act
    sentence = create_sentence()
    words_in_sentence = sentence.split()
    
    # Assert
    assert len(words_in_sentence) == 7, "Sentence does not contain exactly seven words when word list contains all empty strings"
    assert ' '.join(original_words).lower() in sentence.lower(), "Sentence does not contain any of the original words"

# Test function for create_sentence with a mix of valid and invalid words
def test_create_sentence_mixed_valid_invalid(word_list: List[str]):
    # Arrange
    original_words = words.copy()
    words.extend(['123', ''])  # Adding non-word and empty elements
    
    # Act
    sentence = create_sentence()
    words_in_sentence = sentence.split()
    
    # Assert
    assert len(words_in_sentence) == 7, "Sentence does not contain exactly seven words when word list contains a mix of valid and invalid elements"
    assert ' '.join(original_words).lower() in sentence.lower(), "Sentence does not contain any of the original words"

# Test function for create_sentence with a very large word list
def test_create_sentence_large_word_list(word_list: List[str]):
    # Arrange
    original_words = words.copy()
    words.extend([''] * 10)  # Adding ten empty strings
    
    # Act
    sentence = create_sentence()
    words_in_sentence = sentence.split()
    
    # Assert
    assert len(words_in_sentence) == 7, "Sentence does not contain exactly seven words when word list is very large"
    assert ' '.join(original_words).lower() in sentence.lower(), "Sentence does not contain any of the original words"

# Test function for create_sentence with a very small word list
def test_create_sentence_small_word_list(word_list: List[str]):
    # Arrange
    original_words = words.copy()
    words.clear()
    words.extend([''] * 3)  # Adding three empty strings
    
    # Act
    sentence = create_sentence()
    words_in_sentence = sentence.split()
    
    # Assert
    assert len(words_in_sentence) == 7, "Sentence does not contain exactly seven words when word list is very small"
    assert ' '.join(original_words).lower() in sentence.lower(), "Sentence does not contain any of the original words"

# Test function for create_sentence with a single word
def test_create_sentence_single_word(word_list: List[str]):
    # Arrange
    original_words = words.copy()
    words.clear()
    words.extend(['The'])  # Adding one word
    
    # Act
    sentence = create_sentence()
    words_in_sentence = sentence.split()
    
    # Assert
    assert len(words_in_sentence) == 7, "Sentence does not contain exactly seven words when word list contains only one word"
    assert ' '.join(original_words).lower() in sentence.lower(), "Sentence does not contain any of the original words"

# Test function for create_sentence with a single non-word character
def test_create_sentence_single_non_word_character(word_list: List[str]):
    # Arrange
    original_words = words.copy()
    words.clear()
    words.extend(['1'])  # Adding one non-word character
    
    # Act
    sentence = create_sentence()
    words_in_sentence = sentence.split()
    
    # Assert
    assert len(words_in_sentence) == 7, "Sentence does not contain exactly seven words when word list contains only one non-word character"
    assert ' '.join(original_words).lower() in sentence.lower(), "Sentence does not contain any of the original words"

# Test function for create_sentence with a single empty string
def test_create_sentence_single_empty_string(word_list: List[str]):
    # Arrange
    original_words = words.copy()
    words.clear()
    words.extend([''])  # Adding one empty string
    
    # Act
    sentence = create_sentence()
    words_in_sentence = sentence.split()
    
    # Assert
    assert len(words_in_sentence) == 7, "Sentence does not contain exactly seven words when word list contains only one empty string"
    assert ' '.join(original_words).lower() in sentence.lower(), "Sentence does not contain any of the original words"

# Test function for create_sentence with a single space
def test_create_sentence_single_space(word_list: List[str]):
    # Arrange
    original_words = words.copy()
    words.clear()
    words.extend([' '])  # Adding one space
    
    # Act
    sentence = create_sentence()
    words_in_sentence = sentence.split()
    
    # Assert
    assert len(words_in_sentence) == 7, "Sentence does not contain exactly seven words when word list contains only one space"
    assert ' '.join(original_words).lower() in sentence.lower(), "Sentence does not contain any of the original words"

# Test function for create_sentence with a single non-string element
def test_create_sentence_single_non_string_element(word_list: List[str]):
    # Arrange
    original_words = words.copy()
    words.clear()
    words.extend([123])  # Adding one non-string element
    
    # Act
    sentence = create_sentence()
    words_in_sentence = sentence.split()
    
    # Assert
    assert len(words_in_sentence) == 7, "Sentence does not contain exactly seven words when word list contains only one non-string element"
    assert ' '.join(original_words).lower() in sentence.lower(), "Sentence does not contain any of the original words"

# Test function for create_sentence with a single valid word
def test_create_sentence_single_valid_word(word_list: List[str]):
    # Arrange
    original_words = words.copy()
    words.clear()
    words.extend(['The'])  # Adding one valid word
    
    # Act
    sentence = create_sentence()
    words_in_sentence = sentence.split()
    
    # Assert
    assert len(words_in_sentence) == 7, "Sentence does not contain exactly seven words when word list contains only one valid word"
    assert ' '.join(original_words).lower() in sentence.lower(), "Sentence does not contain any of the original words"

# Test function for create_sentence with a single non-word character
def test_create_sentence_single_non_word_character(word_list: List[str]):
    # Arrange
    original_words = words.copy()
    words.clear()
    words.extend(['1'])  # Adding one non-word character
    
    # Act
    sentence = create_sentence()
    words_in_sentence = sentence.split()
    
    # Assert
    assert len(words_in_sentence) == 7, "Sentence does not contain exactly seven words when word list contains only one non-word character"
    assert ' '.join(original_words).lower() in sentence.lower(), "Sentence does not contain any of the original words"

# Test function for create_sentence with a single empty string
def test_create_sentence_single_empty_string(word_list: List[str]):
    # Arrange
    original_words = words.copy()
    words.clear()
    words.extend([''])  # Adding one empty string
    
    # Act
    sentence = create_sentence()
    words_in_sentence = sentence.split()
    
    # Assert
    assert len(words_in_sentence) == 7, "Sentence does not contain exactly seven words when word list contains only one empty string"
    assert ' '.join(original_words).lower() in sentence.lower(), "Sentence does not contain any of the original words"

# Test function for create_sentence with a single space
def test_create_sentence_single_space(word_list: List[str]):
    # Arrange
    original_words = words.copy()
    words.clear()
    words.extend([' '])  # Adding one space
    
    # Act
    sentence = create_sentence()
    words_in_sentence = sentence.split()
    
    # Assert
    assert len(words_in_sentence) == 7, "Sentence does not contain exactly seven words when word list contains only one space"
    assert ' '.join(original_words).lower() in sentence.lower(), "Sentence does not contain any of the original words"

# Test function for create_sentence with a single non-string element
def test_create_sentence_single_non_string_element(word_list: List[str]):
    # Arrange
    original_words = words.copy()
    words.clear()
    words.extend([123])  # Adding one non-string element
    
    # Act
    sentence = create_sentence()
    words_in_sentence = sentence.split()
    
    # Assert
    assert len(words_in_sentence) == 7, "Sentence does not contain exactly seven words when word list contains only one non-string element"
    assert ' '.join(original_words).lower() in sentence.lower(), "Sentence does not contain any of the original words"

# Test function for create_sentence with a single valid word
def test_create_sentence_single_valid_word(word_list: List[str]):
    # Arrange
    original_words = words.copy()
    words.clear()
    words.extend(['The'])  # Adding one valid word
    
    # Act
    sentence = create_sentence()
    words_in_sentence = sentence.split()
    
    # Assert
    assert len(words_in_sentence) == 7, "Sentence does not contain exactly seven words when word list contains only one valid word"
    assert ' '.join(original_words).lower() in sentence.lower(), "Sentence does not contain any of the original words"

# Test function for create_sentence with a single non-word character
def test_create_sentence_single_non_word_character(word_list: List[str]):
    # Arrange
    original_words = words.copy()
    words.clear()
    words.extend(['1'])  # Adding one non-word character
    
    # Act
    sentence = create_sentence()
    words_in_sentence = sentence.split()
    
    # Assert
    assert len(words_in_sentence) == 7, "Sentence does not contain exactly seven words when word list contains only one non-word character"
    assert ' '.join(original_words).lower() in sentence.lower(), "Sentence does not contain any of the original words"

# Test function for create_sentence with a single empty string
def test_create_sentence_single_empty_string(word_list: List[str]):
    # Arrange
    original_words = words.copy()
    words.clear()
    words.extend([''])  # Adding one empty string
    
    # Act
    sentence = create_sentence()
    words_in_sentence = sentence.split()
    
    # Assert
    assert len(words_in_sentence) == 7, "Sentence does not contain exactly seven words when word list contains only one empty string"
    assert ' '.join(original_words).lower() in sentence.lower(), "Sentence does not contain any of the original words"

# Test function for create_sentence with a single space
def test_create_sentence_single_space(word_list: List[str]):
    # Arrange
    original_words = words.copy()
    words.clear()
    words.extend([' '])  # Adding one space
    
    # Act
    sentence = create_sentence()
    words_in_sentence = sentence.split()
    
    # Assert
    assert len(words_in_sentence) == 7, "Sentence does not contain exactly seven words when word list contains only one space"
    assert ' '.join(original_words).lower() in sentence.lower(), "Sentence does not contain any of the original words"

# Test function for create_sentence with a single non-string element
def test_create_sentence_single_non_string_element(word_list: List[str]):
    # Arrange
    original_words = words.copy()
    words.clear()
    words.extend([123])  # Adding one non-string element
    
    # Act
    sentence = create_sentence()
    words_in_sentence = sentence.split()
    
    # Assert
    assert len(words_in_sentence) == 7, "Sentence does not contain exactly seven words when word list contains only one non-string element"
    assert ' '.join(original_words).lower() in sentence.lower(), "Sentence does not contain any of the original words"

# Test function for create_sentence with a single valid word
def test_create_sentence_single_valid_word(word_list: List[str]):
    # Arrange
    original_words = words.copy()
    words.clear()
    words.extend(['The'])  # Adding one valid word
    
    # Act
    sentence = create_sentence()
    words_in_sentence = sentence.split()
    
    # Assert
    assert len(words_in_sentence) == 7, "Sentence does not contain exactly seven words when word list contains only one valid word"
    assert ' '.join(original_words).lower() in sentence.lower(), "Sentence does not contain any of the original words"

# Test function for create_sentence with a single non-word character
def test_create_sentence_single_non_word_character(word_list: List[str]):
    # Arrange
    original_words = words.copy()
    words.clear()
    words.extend(['1'])  # Adding one non-word character
    
    # Act
    sentence = create_sentence()
    words_in_sentence = sentence.split()
    
    # Assert
    assert len(words_in_sentence) == 7, "Sentence does not contain exactly seven words when word list contains only one non-word character"
    assert ' '.join(original_words).lower() in sentence.lower(), "Sentence does not contain any of the original words"

# Test function for create_sentence with a single empty string
def test_create_sentence_single_empty_string(word_list: List[str]):
    # Arrange
    original_words = words.copy()
    words.clear()
    words.extend([''])  # Adding one empty string
    
    # Act
    sentence = create_sentence()
    words_in_sentence = sentence.split()
    
    # Assert
    assert len(words_in_sentence) == 7, "Sentence does not contain exactly seven words when word list contains only one empty string"
    assert ' '.join(original_words).lower() in sentence.lower(), "Sentence does not contain any of the original words"

# Test function for create_sentence with a single space
def test_create_sentence_single_space(word_list: List[str]):
    # Arrange
    original_words = words.copy()
    words.clear()
    words.extend([' '])  # Adding one space
    
    # Act
    sentence = create_sentence()
    words_in_sentence = sentence.split()
    
    # Assert
    assert len(words_in_sentence) == 7, "Sentence does not contain exactly seven words when word list contains only one space"
