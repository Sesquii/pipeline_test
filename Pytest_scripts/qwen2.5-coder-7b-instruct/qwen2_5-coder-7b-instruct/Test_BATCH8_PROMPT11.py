# BATCH8_PROMPT11_{{model_name}}.py

# Import necessary library
import re

# List of positive words to be exaggerated
positive_words = {'love', 'happy', 'great', 'excited', 'amazing'}

def count_words(file_path):
    """
    Counts the words in a file, exaggerating counts for positive words.
    
    Args:
    file_path (str): Path to the text file to be analyzed.
    
    Returns:
    dict: A dictionary with word counts, where positive words are exaggerated by 100 times.
    """
    # Initialize an empty dictionary to store word counts
    word_counts = {}
    
    # Open the file and read line by line
    with open(file_path, 'r') as file:
        for line in file:
            # Use regular expression to find words
            words = re.findall(r'\b\w+\b', line.lower())
            for word in words:
                if word in positive_words:
                    # Exaggerate the count by 100 times for positive words
                    word_counts[word] = word_counts.get(word, 0) + 100
                else:
                    # Increment the count normally for other words
                    word_counts[word] = word_counts.get(word, 0) + 1
    
    return word_counts

def main():
    """
    Entry point of the program. Prompts user for file path and prints the word counts.
    """
    # Prompt user to enter the file path
    file_path = input("Enter the path to the text file: ")
    
    # Get the word counts from the function
    word_counts = count_words(file_path)
    
    # Print the word counts
    print("Word Counts:")
    for word, count in word_counts.items():
        print(f"{word}: {count}")

# Check if the script is run as the main program
if __name__ == "__main__":
    main()

# ===== GENERATED TESTS =====
```python
import pytest
from pathlib import Path

# BATCH8_PROMPT11_{{model_name}}.py

# Import necessary library
import re

# List of positive words to be exaggerated
positive_words = {'love', 'happy', 'great', 'excited', 'amazing'}

def count_words(file_path):
    """
    Counts the words in a file, exaggerating counts for positive words.
    
    Args:
    file_path (str): Path to the text file to be analyzed.
    
    Returns:
    dict: A dictionary with word counts, where positive words are exaggerated by 100 times.
    """
    # Initialize an empty dictionary to store word counts
    word_counts = {}
    
    # Open the file and read line by line
    with open(file_path, 'r') as file:
        for line in file:
            # Use regular expression to find words
            words = re.findall(r'\b\w+\b', line.lower())
            for word in words:
                if word in positive_words:
                    # Exaggerate the count by 100 times for positive words
                    word_counts[word] = word_counts.get(word, 0) + 100
                else:
                    # Increment the count normally for other words
                    word_counts[word] = word_counts.get(word, 0) + 1
    
    return word_counts

def main():
    """
    Entry point of the program. Prompts user for file path and prints the word counts.
    """
    # Prompt user to enter the file path
    file_path = input("Enter the path to the text file: ")
    
    # Get the word counts from the function
    word_counts = count_words(file_path)
    
    # Print the word counts
    print("Word Counts:")
    for word, count in word_counts.items():
        print(f"{word}: {count}")

# Check if the script is run as the main program
if __name__ == "__main__":
    main()

# Test suite for BATCH8_PROMPT11_{{model_name}}.py

@pytest.fixture
def test_file_path(tmpdir):
    """Create a temporary file with some text and return its path."""
    test_file = tmpdir.join("test.txt")
    test_file.write(
        "I love programming. It is happy to see great things happening.\n"
        "Excited about the amazing journey of learning."
    )
    return str(test_file)

def test_count_words_positive_words(test_file_path):
    """Test count_words function with a file containing positive words."""
    word_counts = count_words(test_file_path)
    assert 'love' in word_counts and word_counts['love'] == 101
    assert 'happy' in word_counts and word_counts['happy'] == 101
    assert 'great' in word_counts and word_counts['great'] == 101
    assert 'excited' in word_counts and word_counts['excited'] == 101
    assert 'amazing' in word_counts and word_counts['amazing'] == 101

def test_count_words_negative_words(test_file_path):
    """Test count_words function with a file containing negative words."""
    word_counts = count_words(test_file_path)
    assert 'i' in word_counts and word_counts['i'] == 2
    assert 'it' in word_counts and word_counts['it'] == 1
    assert 'is' in word_counts and word_counts['is'] == 1

def test_count_words_empty_file(tmpdir):
    """Test count_words function with an empty file."""
    test_file = tmpdir.join("empty.txt")
    test_file.write("")
    word_counts = count_words(str(test_file))
    assert not word_counts

def test_count_words_non_existent_file():
    """Test count_words function with a non-existent file."""
    with pytest.raises(FileNotFoundError):
        count_words("/path/to/nonexistent/file.txt")

def test_count_words_with_special_characters(tmpdir):
    """Test count_words function with a file containing special characters."""
    test_file = tmpdir.join("special_chars.txt")
    test_file.write(
        "I love programming! It's happy to see great things happening.\n"
        "Excited about the amazing journey of learning."
    )
    word_counts = count_words(str(test_file))
    assert 'love' in word_counts and word_counts['love'] == 101
    assert 'happy' in word_counts and word_counts['happy'] == 101
    assert 'great' in word_counts and word_counts['great'] == 101
    assert 'excited' in word_counts and word_counts['excited'] == 101
    assert 'amazing' in word_counts and word_counts['amazing'] == 101

def test_count_words_with_numbers(tmpdir):
    """Test count_words function with a file containing numbers."""
    test_file = tmpdir.join("numbers.txt")
    test_file.write(
        "I love programming. It is happy to see great things happening.\n"
        "Excited about the amazing journey of learning 12345."
    )
    word_counts = count_words(str(test_file))
    assert 'love' in word_counts and word_counts['love'] == 101
    assert 'happy' in word_counts and word_counts['happy'] == 101
    assert 'great' in word_counts and word_counts['great'] == 101
    assert 'excited' in word_counts and word_counts['excited'] == 101
    assert 'amazing' in word_counts and word_counts['amazing'] == 101

def test_count_words_with_uppercase(tmpdir):
    """Test count_words function with a file containing uppercase words."""
    test_file = tmpdir.join("uppercase.txt")
    test_file.write(
        "I love Programming. It is happy to see Great things happening.\n"
        "Excited about the Amazing journey of learning."
    )
    word_counts = count_words(str(test_file))
    assert 'love' in word_counts and word_counts['love'] == 101
    assert 'happy' in word_counts and word_counts['happy'] == 101
    assert 'great' in word_counts and word_counts['great'] == 101
    assert 'excited' in word_counts and word_counts['excited'] == 101
    assert 'amazing' in word_counts and word_counts['amazing'] == 101

def test_count_words_with_punctuation(tmpdir):
    """Test count_words function with a file containing punctuation."""
    test_file = tmpdir.join("punctuation.txt")
    test_file.write(
        "I love programming. It is happy to see great things happening.\n"
        "Excited about the amazing journey of learning."
    )
    word_counts = count_words(str(test_file))
    assert 'love' in word_counts and word_counts['love'] == 101
    assert 'happy' in word_counts and word_counts['happy'] == 101
    assert 'great' in word_counts and word_counts['great'] == 101
    assert 'excited' in word_counts and word_counts['excited'] == 101
    assert 'amazing' in word_counts and word_counts['amazing'] == 101

def test_count_words_with_multiple_spaces(tmpdir):
    """Test count_words function with a file containing multiple spaces."""
    test_file = tmpdir.join("multiple_spaces.txt")
    test_file.write(
        "I love programming. It is happy to see great things happening.\n"
        "Excited about the amazing journey of learning."
    )
    word_counts = count_words(str(test_file))
    assert 'love' in word_counts and word_counts['love'] == 101
    assert 'happy' in word_counts and word_counts['happy'] == 101
    assert 'great' in word_counts and word_counts['great'] == 101
    assert 'excited' in word_counts and word_counts['excited'] == 101
    assert 'amazing' in word_counts and word_counts['amazing'] == 101

def test_count_words_with_unicode(tmpdir):
    """Test count_words function with a file containing unicode characters."""
    test_file = tmpdir.join("unicode.txt")
    test_file.write(
        "I love programming. It is happy to see great things happening.\n"
        "Excited about the amazing journey of learning."
    )
    word_counts = count_words(str(test_file))
    assert 'love' in word_counts and word_counts['love'] == 101
    assert 'happy' in word_counts and word_counts['happy'] == 101
    assert 'great' in word_counts and word_counts['great'] == 101
    assert 'excited' in word_counts and word_counts['excited'] == 101
    assert 'amazing' in word_counts and word_counts['amazing'] == 101

def test_count_words_with_empty_lines(tmpdir):
    """Test count_words function with a file containing empty lines."""
    test_file = tmpdir.join("empty_lines.txt")
    test_file.write(
        "I love programming. It is happy to see great things happening.\n"
        "\n\nExcited about the amazing journey of learning."
    )
    word_counts = count_words(str(test_file))
    assert 'love' in word_counts and word_counts['love'] == 101
    assert 'happy' in word_counts and word_counts['happy'] == 101
    assert 'great' in word_counts and word_counts['great'] == 101
    assert 'excited' in word_counts and word_counts['excited'] == 101
    assert 'amazing' in word_counts and word_counts['amazing'] == 101

def test_count_words_with_mixed_case(tmpdir):
    """Test count_words function with a file containing mixed case words."""
    test_file = tmpdir.join("mixed_case.txt")
    test_file.write(
        "I love Programming. It is happy to see great things happening.\n"
        "Excited about the Amazing journey of learning."
    )
    word_counts = count_words(str(test_file))
    assert 'love' in word_counts and word_counts['love'] == 101
    assert 'happy' in word_counts and word_counts['happy'] == 101
    assert 'great' in word_counts and word_counts['great'] == 101
    assert 'excited' in word_counts and word_counts['excited'] == 101
    assert 'amazing' in word_counts and word_counts['amazing'] == 101

def test_count_words_with_single_word(tmpdir):
    """Test count_words function with a file containing a single word."""
    test_file = tmpdir.join("single_word.txt")
    test_file.write(
        "love"
    )
    word_counts = count_words(str(test_file))
    assert 'love' in word_counts and word_counts['love'] == 101

def test_count_words_with_multiple_words(tmpdir):
    """Test count_words function with a file containing multiple words."""
    test_file = tmpdir.join("multiple_words.txt")
    test_file.write(
        "I love programming. It is happy to see great things happening.\n"
        "Excited about the amazing journey of learning."
    )
    word_counts = count_words(str(test_file))
    assert 'love' in word_counts and word_counts['love'] == 101
    assert 'happy' in word_counts and word_counts['happy'] == 101
    assert 'great' in word_counts and word_counts['great'] == 101
    assert 'excited' in word_counts and word_counts['excited'] == 101
    assert 'amazing' in word_counts and word_counts['amazing'] == 101

def test_count_words_with_large_file(tmpdir):
    """Test count_words function with a large file."""
    test_file = tmpdir.join("large_file.txt")
    test_file.write(
        "I love programming. It is happy to see great things happening.\n"
        * 1000
    )
    word_counts = count_words(str(test_file))
    assert 'love' in word_counts and word_counts['love'] == 101

def test_count_words_with_empty_string(tmpdir):
    """Test count_words function with an empty string."""
    test_file = tmpdir.join("empty_string.txt")
    test_file.write("")
    word_counts = count_words(str(test_file))
    assert not word_counts
```