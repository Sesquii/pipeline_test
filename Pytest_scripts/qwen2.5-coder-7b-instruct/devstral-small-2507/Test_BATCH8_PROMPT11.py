#!/usr/bin/env python3

def count_words_with_sentiment(text_file_path):
    """
    Counts words in a text file with exaggerated counts for positive sentiment words.

    Args:
        text_file_path (str): Path to the input text file.

    Returns:
        dict: Dictionary of word counts, with positive words exaggerated.
    """
    # Hard-coded list of positive words
    POSITIVE_WORDS = {'love', 'happy', 'great'}

    # Initialize word count dictionary
    word_counts = {}

    try:
        with open(text_file_path, 'r') as file:
            for line in file:
                words = line.strip().split()
                for word in words:
                    # Convert to lowercase and remove punctuation
                    clean_word = ''.join(char.lower() for char in word if char.isalnum())
                    if clean_word:  # Only count non-empty words
                        if clean_word in POSITIVE_WORDS:
                            # Exaggerate positive word counts by 100x
                            word_counts[clean_word] = word_counts.get(clean_word, 0) + 100
                        else:
                            word_counts[clean_word] = word_counts.get(clean_word, 0) + 1

    except FileNotFoundError:
        print(f"Error: The file '{text_file_path}' was not found.")
        return {}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}

    return word_counts

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python BATCH8_PROMPT11_Devstral.py <input_text_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    word_counts = count_words_with_sentiment(input_file)

    # Print the results
    for word, count in sorted(word_counts.items()):
        print(f"{word}: {count}")

# ===== GENERATED TESTS =====
```python
#!/usr/bin/env python3

def count_words_with_sentiment(text_file_path):
    """
    Counts words in a text file with exaggerated counts for positive sentiment words.

    Args:
        text_file_path (str): Path to the input text file.

    Returns:
        dict: Dictionary of word counts, with positive words exaggerated.
    """
    # Hard-coded list of positive words
    POSITIVE_WORDS = {'love', 'happy', 'great'}

    # Initialize word count dictionary
    word_counts = {}

    try:
        with open(text_file_path, 'r') as file:
            for line in file:
                words = line.strip().split()
                for word in words:
                    # Convert to lowercase and remove punctuation
                    clean_word = ''.join(char.lower() for char in word if char.isalnum())
                    if clean_word:  # Only count non-empty words
                        if clean_word in POSITIVE_WORDS:
                            # Exaggerate positive word counts by 100x
                            word_counts[clean_word] = word_counts.get(clean_word, 0) + 100
                        else:
                            word_counts[clean_word] = word_counts.get(clean_word, 0) + 1

    except FileNotFoundError:
        print(f"Error: The file '{text_file_path}' was not found.")
        return {}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}

    return word_counts

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python BATCH8_PROMPT11_Devstral.py <input_text_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    word_counts = count_words_with_sentiment(input_file)

    # Print the results
    for word, count in sorted(word_counts.items()):
        print(f"{word}: {count}")

# Test cases

import pytest
from io import StringIO
import os

@pytest.fixture
def text_file(tmpdir):
    """Create a temporary text file with some content."""
    file_path = tmpdir.join("test.txt")
    file_path.write("love happy great love")
    return str(file_path)

def test_count_words_with_sentiment(text_file):
    """Test the count_words_with_sentiment function."""
    result = count_words_with_sentiment(text_file)
    assert result == {'great': 100, 'happy': 100, 'love': 200}

def test_count_words_with_sentiment_empty_file(tmpdir):
    """Test the count_words_with_sentiment function with an empty file."""
    file_path = tmpdir.join("test.txt")
    file_path.write("")
    result = count_words_with_sentiment(str(file_path))
    assert result == {}

def test_count_words_with_sentiment_nonexistent_file():
    """Test the count_words_with_sentiment function with a non-existent file."""
    result = count_words_with_sentiment("/path/to/nonexistent/file.txt")
    assert result == {}

def test_count_words_with_sentiment_mixed_case(tmpdir):
    """Test the count_words_with_sentiment function with mixed case words."""
    file_path = tmpdir.join("test.txt")
    file_path.write("Love Happy Great love")
    result = count_words_with_sentiment(str(file_path))
    assert result == {'great': 100, 'happy': 100, 'love': 200}

def test_count_words_with_sentiment_punctuation(tmpdir):
    """Test the count_words_with_sentiment function with punctuation."""
    file_path = tmpdir.join("test.txt")
    file_path.write("love! happy? great.")
    result = count_words_with_sentiment(str(file_path))
    assert result == {'great': 100, 'happy': 100, 'love': 200}

def test_count_words_with_sentiment_numbers(tmpdir):
    """Test the count_words_with_sentiment function with numbers."""
    file_path = tmpdir.join("test.txt")
    file_path.write("love happy great 123")
    result = count_words_with_sentiment(str(file_path))
    assert result == {'great': 100, 'happy': 100, 'love': 200}

def test_count_words_with_sentiment_multiple_lines(tmpdir):
    """Test the count_words_with_sentiment function with multiple lines."""
    file_path = tmpdir.join("test.txt")
    file_path.write("love happy great\nlove happy great")
    result = count_words_with_sentiment(str(file_path))
    assert result == {'great': 200, 'happy': 200, 'love': 400}

def test_count_words_with_sentiment_space(tmpdir):
    """Test the count_words_with_sentiment function with space."""
    file_path = tmpdir.join("test.txt")
    file_path.write("love happy great ")
    result = count_words_with_sentiment(str(file_path))
    assert result == {'great': 100, 'happy': 100, 'love': 200}

def test_count_words_with_sentiment_special_characters(tmpdir):
    """Test the count_words_with_sentiment function with special characters."""
    file_path = tmpdir.join("test.txt")
    file_path.write("love happy great @#$%^&*()")
    result = count_words_with_sentiment(str(file_path))
    assert result == {'great': 100, 'happy': 100, 'love': 200}

def test_count_words_with_sentiment_large_file(tmpdir):
    """Test the count_words_with_sentiment function with a large file."""
    file_path = tmpdir.join("test.txt")
    content = " ".join(["love happy great"] * 1000)
    file_path.write(content)
    result = count_words_with_sentiment(str(file_path))
    assert result == {'great': 100000, 'happy': 100000, 'love': 200000}

def test_count_words_with_sentiment_case_insensitive(tmpdir):
    """Test the count_words_with_sentiment function with case-insensitive words."""
    file_path = tmpdir.join("test.txt")
    file_path.write("Love Happy Great love")
    result = count_words_with_sentiment(str(file_path))
    assert result == {'great': 100, 'happy': 100, 'love': 200}

def test_count_words_with_sentiment_empty_string(tmpdir):
    """Test the count_words_with_sentiment function with an empty string."""
    file_path = tmpdir.join("test.txt")
    file_path.write("")
    result = count_words_with_sentiment(str(file_path))
    assert result == {}

def test_count_words_with_sentiment_single_word(tmpdir):
    """Test the count_words_with_sentiment function with a single word."""
    file_path = tmpdir.join("test.txt")
    file_path.write("love")
    result = count_words_with_sentiment(str(file_path))
    assert result == {'love': 200}

def test_count_words_with_sentiment_multiple_spaces(tmpdir):
    """Test the count_words_with_sentiment function with multiple spaces."""
    file_path = tmpdir.join("test.txt")
    file_path.write("love   happy great")
    result = count_words_with_sentiment(str(file_path))
    assert result == {'great': 100, 'happy': 100, 'love': 200}

def test_count_words_with_sentiment_non_alphanumeric(tmpdir):
    """Test the count_words_with_sentiment function with non-alphanumeric characters."""
    file_path = tmpdir.join("test.txt")
    file_path.write("love happy great !@#$%^&*()")
    result = count_words_with_sentiment(str(file_path))
    assert result == {'great': 100, 'happy': 100, 'love': 200}

def test_count_words_with_sentiment_large_number_of_lines(tmpdir):
    """Test the count_words_with_sentiment function with a large number of lines."""
    file_path = tmpdir.join("test.txt")
    content = "\n".join(["love happy great"] * 1000)
    file_path.write(content)
    result = count_words_with_sentiment(str(file_path))
    assert result == {'great': 100000, 'happy': 100000, 'love': 200000}

def test_count_words_with_sentiment_large_number_of_words(tmpdir):
    """Test the count_words_with_sentiment function with a large number of words."""
    file_path = tmpdir.join("test.txt")
    content = " ".join(["love happy great"] * 1000)
    file_path.write(content)
    result = count_words_with_sentiment(str(file_path))
    assert result == {'great': 100000, 'happy': 100000, 'love': 200000}

def test_count_words_with_sentiment_large_number_of_characters(tmpdir):
    """Test the count_words_with_sentiment function with a large number of characters."""
    file_path = tmpdir.join("test.txt")
    content = "a" * 1000
    file_path.write(content)
    result = count_words_with_sentiment(str(file_path))
    assert result == {}

def test_count_words_with_sentiment_large_number_of_unique_words(tmpdir):
    """Test the count_words_with_sentiment function with a large number of unique words."""
    file_path = tmpdir.join("test.txt")
    content = " ".join([f"word{i}" for i in range(1000)])
    file_path.write(content)
    result = count_words_with_sentiment(str(file_path))
    assert len(result) == 1000

def test_count_words_with_sentiment_large_number_of_duplicate_words(tmpdir):
    """Test the count_words_with_sentiment function with a large number of duplicate words."""
    file_path = tmpdir.join("test.txt")
    content = " ".join(["love" for _ in range(1000)])
    file_path.write(content)
    result = count_words_with_sentiment(str(file_path))
    assert result == {'love': 200000}

def test_count_words_with_sentiment_large_number_of_special_characters(tmpdir):
    """Test the count_words_with_sentiment function with a large number of special characters."""
    file_path = tmpdir.join("test.txt")
    content = "!@#$%^&*()" * 1000
    file_path.write(content)
    result = count_words_with_sentiment(str(file_path))
    assert result == {}

def test_count_words_with_sentiment_large_number_of_digits(tmpdir):
    """Test the count_words_with_sentiment function with a large number of digits."""
    file_path = tmpdir.join("test.txt")
    content = "1234567890" * 1000
    file_path.write(content)
    result = count_words_with_sentiment(str(file_path))
    assert result == {}

def test_count_words_with_sentiment_large_number_of_punctuation(tmpdir):
    """Test the count_words_with_sentiment function with a large number of punctuation."""
    file_path = tmpdir.join("test.txt")
    content = "!@#$%^&*()" * 1000
    file_path.write(content)
    result = count_words_with_sentiment(str(file_path))
    assert result == {}

def test_count_words_with_sentiment_large_number_of_space(tmpdir):
    """Test the count_words_with_sentiment function with a large number of space."""
    file_path = tmpdir.join("test.txt")
    content = " " * 1000
    file_path.write(content)
    result = count_words_with_sentiment(str(file_path))
    assert result == {}

def test_count_words_with_sentiment_large_number_of_newline(tmpdir):
    """Test the count_words_with_sentiment function with a large number of newline."""
    file_path = tmpdir.join("test.txt")
    content = "\n" * 1000
    file_path.write(content)
    result = count_words_with_sentiment(str(file_path))
    assert result == {}

def test_count_words_with_sentiment_large_number_of_tab(tmpdir):
    """Test the count_words_with_sentiment function with a large number of tab."""
    file_path = tmpdir.join("test.txt")
    content = "\t" * 1000
    file_path.write(content)
    result = count_words_with_sentiment(str(file_path))
    assert result == {}

def test_count_words_with_sentiment_large_number_of_formfeed(tmpdir):
    """Test the count_words_with_sentiment function with a large number of formfeed."""
    file_path = tmpdir.join("test.txt")
    content = "\f" * 1000
    file_path.write(content)
    result = count_words_with_sentiment(str(file_path))
    assert result == {}

def test_count_words_with_sentiment_large_number_of_backspace(tmpdir):
    """Test the count_words_with_sentiment function with a large number of backspace."""
    file_path = tmpdir.join("test.txt")
    content = "\b" * 1000
    file_path.write(content)
    result = count_words_with_sentiment(str(file_path))
    assert result == {}

def test_count_words_with_sentiment_large_number_of_vertical_tab(tmpdir):
    """Test the count_words_with_sentiment function with a large number of vertical tab."""
    file_path = tmpdir.join("test.txt")
    content = "\v" * 1000
    file_path.write(content)
    result = count_words_with_sentiment(str(file_path))
    assert result == {}

def test_count_words_with_sentiment_large_number_of_carriage_return(tmpdir):
    """Test the count_words_with_sentiment function with a large number of carriage return."""
    file_path = tmpdir.join("test.txt")
    content = "\r" * 1000
    file_path.write(content)
    result = count_words_with_sentiment(str(file_path))
    assert result == {}

def test_count_words_with_sentiment_large_number_of_null(tmpdir):
    """Test the count_words_with_sentiment function with a large number of null."""
    file_path = tmpdir.join("test.txt")
    content = "\0" * 1000
    file_path.write(content)
    result = count_words_with_sentiment(str(file_path))
    assert result == {}

def test_count_words_with_sentiment_large_number_of_non_printable(tmpdir):
    """Test the count_words_with_sentiment function with a large number of non-printable."""
    file_path = tmpdir.join("test.txt")
    content = "".join(chr(i) for i in range(128))
    file_path.write(content)
    result = count_words_with_sentiment(str(file_path))
    assert result == {}

def test_count_words_with_sentiment_large_number_of_unicode(tmpdir):
    """Test the count_words_with_sentiment function with a large number of unicode."""
    file_path = tmpdir.join("test.txt")
    content = "".join(chr(i) for i in range(1000))
    file_path.write(content)
    result = count_words_with_sentiment(str(file_path))
    assert result == {}

def test_count_words_with_sentiment_large_number_of_random(tmpdir):
    """Test the count_words_with_sentiment function with a large number of random."""
    file_path = tmpdir.join("test.txt")
    content = "".join(chr(i) for i in range(1000))
    file_path.write(content)
    result = count_words_with_sentiment(str(file_path))
    assert result == {}

def test_count_words_with_sentiment_large_number_of_random_string(tmpdir):
    """Test the count_words_with_sentiment function with a large number of random string."""
    file_path = tmpdir.join("test.txt")
    content = "".join(chr(i) for i in range(1000))
    file_path.write(content)
    result = count_words_with_sentiment(str(file_path))
    assert result == {}

def test_count_words_with_sentiment_large_number_of_random_string_with_special_characters(tmpdir):
    """Test the count_words_with_sentiment function with a large number of random string with special characters."""
    file_path = tmpdir.join("test.txt")
    content = "".join(chr(i) for i in range(1000))
    file_path.write(content)
    result = count_words_with_sentiment(str(file_path))
    assert result == {}

def test_count_words_with_sentiment_large_number_of_random_string_with_digits(tmpdir):
    """Test the count_words_with_sentiment function with a large number of random string with digits."""
    file_path = tmpdir.join("test.txt")
    content = "".join(chr(i) for i in range(1000))
    file_path.write(content)
    result = count_words_with_sentiment(str(file_path))
    assert result == {}

def test_count_words_with_sentiment_large_number_of_random_string_with_punctuation(tmpdir):
    """Test the count_words_with_sentiment function with a large number of random string with punctuation."""
    file_path = tmpdir.join("test.txt")
    content = "".join(chr(i) for i in range(1000))
    file_path.write(content)
    result = count_words_with_sentiment(str(file_path))
    assert result == {}

def test_count_words_with_sentiment_large_number_of_random_string_with_space(tmpdir):
    """Test the count_words_with_sentiment function with a large number of random string with space."""
    file_path = tmpdir.join("test.txt")
    content = "".join(chr(i) for i in range(1000))
    file_path.write(content)
    result = count_words_with_sentiment(str(file_path))
    assert result == {}

def test_count_words_with_sentiment_large_number_of_random_string_with_newline(tmpdir):
    """Test the count_words_with_sentiment function with a large number of random string with newline."""
    file_path = tmpdir.join("test.txt")
    content = "".join(chr(i) for i in range(1000))
    file_path.write(content)
    result = count_words_with_sentiment(str(file_path))
    assert result == {}

def test_count_words_with_sentiment_large_number_of_random_string_with_tab(tmpdir):
    """Test the count_words_with_sentiment function with a large number of random string with tab."""
    file_path = tmpdir.join("test.txt")
    content = "".join(chr(i) for i in range(1000))
    file_path.write(content)
    result = count_words_with_sentiment(str(file_path))
    assert result == {}

def test_count_words_with_sentiment_large_number_of_random_string_with_formfeed(tmpdir):
    """Test the count_words_with_sentiment function with a large number of random string with formfeed."""
    file_path = tmpdir.join("test.txt")
    content = "".join(chr(i) for i in range(100