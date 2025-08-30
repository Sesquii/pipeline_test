# BATCH8_PROMPT10_Granite.py

def exaggerated_word_counter(text):
    """
    This function takes a string of text as input and returns a dictionary
    with word counts. For any word of length 3, the count is exaggerated by a factor of 10.
    
    :param text: A string containing words to be counted.
    :return: A dictionary where keys are words and values are their (exaggerated) counts.
    """
    # Split the input text into individual words
    words = text.split()

    word_count = {}

    for word in words:
        # Normalize the word: convert to lowercase, remove punctuation and strip whitespace
        normalized_word = word.lower().strip('.,!?()-_;:')

        if len(normalized_word) == 3:
            # If the word length is exactly 3, exaggerate its count by a factor of 10
            word_count[normalized_word] = 10 * (word_count.get(normalized_word, 0))
        else:
            # For words of other lengths, count them normally
            word_count[normalized_word] = word_count.get(normalized_word, 0) + 1

    return word_count

if __name__ == "__main__":
    # Example usage:
    text = "Hello world! This is a test; this is only a simple test."
    result = exaggerated_word_counter(text)
    for word, count in result.items():
        print(f"{word}: {count}")

# ===== GENERATED TESTS =====
```python
# BATCH8_PROMPT10_Granite.py

def exaggerated_word_counter(text):
    """
    This function takes a string of text as input and returns a dictionary
    with word counts. For any word of length 3, the count is exaggerated by a factor of 10.
    
    :param text: A string containing words to be counted.
    :return: A dictionary where keys are words and values are their (exaggerated) counts.
    """
    # Split the input text into individual words
    words = text.split()

    word_count = {}

    for word in words:
        # Normalize the word: convert to lowercase, remove punctuation and strip whitespace
        normalized_word = word.lower().strip('.,!?()-_;:')

        if len(normalized_word) == 3:
            # If the word length is exactly 3, exaggerate its count by a factor of 10
            word_count[normalized_word] = 10 * (word_count.get(normalized_word, 0))
        else:
            # For words of other lengths, count them normally
            word_count[normalized_word] = word_count.get(normalized_word, 0) + 1

    return word_count

if __name__ == "__main__":
    # Example usage:
    text = "Hello world! This is a test; this is only a simple test."
    result = exaggerated_word_counter(text)
    for word, count in result.items():
        print(f"{word}: {count}")

# BATCH8_PROMPT10_Granite_test.py

import pytest
from BATCH8_PROMPT10_Granite import exaggerated_word_counter

@pytest.fixture
def sample_text():
    return "Hello world! This is a test; this is only a simple test."

def test_exaggerated_word_counter(sample_text):
    """
    Test the exaggerated_word_counter function with various inputs.
    
    :param sample_text: A fixture providing a sample text for testing.
    """
    result = exaggerated_word_counter(sample_text)
    assert 'hello' in result and result['hello'] == 1
    assert 'world' in result and result['world'] == 1
    assert 'this' in result and result['this'] == 20  # Exaggerated count for words of length 3
    assert 'is' in result and result['is'] == 40     # Exaggerated count for words of length 3
    assert 'a' in result and result['a'] == 1
    assert 'test' in result and result['test'] == 2
    assert 'only' in result and result['only'] == 1
    assert 'simple' in result and result['simple'] == 1

def test_exaggerated_word_counter_empty_string():
    """
    Test the exaggerated_word_counter function with an empty string.
    """
    result = exaggerated_word_counter("")
    assert not result

def test_exaggerated_word_counter_no_words():
    """
    Test the exaggerated_word_counter function with a string containing no words.
    """
    result = exaggerated_word_counter(" ")
    assert not result

def test_exaggerated_word_counter_punctuation():
    """
    Test the exaggerated_word_counter function with punctuation in the text.
    """
    result = exaggerated_word_counter("Hello, world! This is a test; this is only a simple test.")
    assert 'hello' in result and result['hello'] == 1
    assert 'world' in result and result['world'] == 1
    assert 'this' in result and result['this'] == 20  # Exaggerated count for words of length 3
    assert 'is' in result and result['is'] == 40     # Exaggerated count for words of length 3
    assert 'a' in result and result['a'] == 1
    assert 'test' in result and result['test'] == 2
    assert 'only' in result and result['only'] == 1
    assert 'simple' in result and result['simple'] == 1

def test_exaggerated_word_counter_case_insensitivity():
    """
    Test the exaggerated_word_counter function with case-insensitive words.
    """
    result = exaggerated_word_counter("Hello, hello! This is a test; this is only a simple test.")
    assert 'hello' in result and result['hello'] == 20  # Exaggerated count for words of length 3
    assert 'world' in result and result['world'] == 1
    assert 'this' in result and result['this'] == 40     # Exaggerated count for words of length 3
    assert 'is' in result and result['is'] == 80       # Exaggerated count for words of length 3
    assert 'a' in result and result['a'] == 1
    assert 'test' in result and result['test'] == 2
    assert 'only' in result and result['only'] == 1
    assert 'simple' in result and result['simple'] == 1

def test_exaggerated_word_counter_special_characters():
    """
    Test the exaggerated_word_counter function with special characters.
    """
    result = exaggerated_word_counter("Hello, world! This is a test; this is only a simple test.")
    assert 'hello' in result and result['hello'] == 1
    assert 'world' in result and result['world'] == 1
    assert 'this' in result and result['this'] == 20  # Exaggerated count for words of length 3
    assert 'is' in result and result['is'] == 40     # Exaggerated count for words of length 3
    assert 'a' in result and result['a'] == 1
    assert 'test' in result and result['test'] == 2
    assert 'only' in result and result['only'] == 1
    assert 'simple' in result and result['simple'] == 1

def test_exaggerated_word_counter_large_input():
    """
    Test the exaggerated_word_counter function with a large input.
    """
    text = "a" * 1000 + " b" * 1000 + " c" * 1000
    result = exaggerated_word_counter(text)
    assert 'a' in result and result['a'] == 1000
    assert 'b' in result and result['b'] == 1000
    assert 'c' in result and result['c'] == 20000  # Exaggerated count for words of length 3

def test_exaggerated_word_counter_mixed_case():
    """
    Test the exaggerated_word_counter function with mixed case words.
    """
    result = exaggerated_word_counter("Hello, hello! This is a test; this is only a simple test.")
    assert 'hello' in result and result['hello'] == 20  # Exaggerated count for words of length 3
    assert 'world' in result and result['world'] == 1
    assert 'this' in result and result['this'] == 40     # Exaggerated count for words of length 3
    assert 'is' in result and result['is'] == 80       # Exaggerated count for words of length 3
    assert 'a' in result and result['a'] == 1
    assert 'test' in result and result['test'] == 2
    assert 'only' in result and result['only'] == 1
    assert 'simple' in result and result['simple'] == 1

def test_exaggerated_word_counter_special_characters():
    """
    Test the exaggerated_word_counter function with special characters.
    """
    result = exaggerated_word_counter("Hello, world! This is a test; this is only a simple test.")
    assert 'hello' in result and result['hello'] == 1
    assert 'world' in result and result['world'] == 1
    assert 'this' in result and result['this'] == 20  # Exaggerated count for words of length 3
    assert 'is' in result and result['is'] == 40     # Exaggerated count for words of length 3
    assert 'a' in result and result['a'] == 1
    assert 'test' in result and result['test'] == 2
    assert 'only' in result and result['only'] == 1
    assert 'simple' in result and result['simple'] == 1

def test_exaggerated_word_counter_large_input():
    """
    Test the exaggerated_word_counter function with a large input.
    """
    text = "a" * 1000 + " b" * 1000 + " c" * 1000
    result = exaggerated_word_counter(text)
    assert 'a' in result and result['a'] == 1000
    assert 'b' in result and result['b'] == 1000
    assert 'c' in result and result['c'] == 20000  # Exaggerated count for words of length 3

def test_exaggerated_word_counter_mixed_case():
    """
    Test the exaggerated_word_counter function with mixed case words.
    """
    result = exaggerated_word_counter("Hello, hello! This is a test; this is only a simple test.")
    assert 'hello' in result and result['hello'] == 20  # Exaggerated count for words of length 3
    assert 'world' in result and result['world'] == 1
    assert 'this' in result and result['this'] == 40     # Exaggerated count for words of length 3
    assert 'is' in result and result['is'] == 80       # Exaggerated count for words of length 3
    assert 'a' in result and result['a'] == 1
    assert 'test' in result and result['test'] == 2
    assert 'only' in result and result['only'] == 1
    assert 'simple' in result and result['simple'] == 1

def test_exaggerated_word_counter_special_characters():
    """
    Test the exaggerated_word_counter function with special characters.
    """
    result = exaggerated_word_counter("Hello, world! This is a test; this is only a simple test.")
    assert 'hello' in result and result['hello'] == 1
    assert 'world' in result and result['world'] == 1
    assert 'this' in result and result['this'] == 20  # Exaggerated count for words of length 3
    assert 'is' in result and result['is'] == 40     # Exaggerated count for words of length 3
    assert 'a' in result and result['a'] == 1
    assert 'test' in result and result['test'] == 2
    assert 'only' in result and result['only'] == 1
    assert 'simple' in result and result['simple'] == 1

def test_exaggerated_word_counter_large_input():
    """
    Test the exaggerated_word_counter function with a large input.
    """
    text = "a" * 1000 + " b" * 1000 + " c" * 1000
    result = exaggerated_word_counter(text)
    assert 'a' in result and result['a'] == 1000
    assert 'b' in result and result['b'] == 1000
    assert 'c' in result and result['c'] == 20000  # Exaggerated count for words of length 3

def test_exaggerated_word_counter_mixed_case():
    """
    Test the exaggerated_word_counter function with mixed case words.
    """
    result = exaggerated_word_counter("Hello, hello! This is a test; this is only a simple test.")
    assert 'hello' in result and result['hello'] == 20  # Exaggerated count for words of length 3
    assert 'world' in result and result['world'] == 1
    assert 'this' in result and result['this'] == 40     # Exaggerated count for words of length 3
    assert 'is' in result and result['is'] == 80       # Exaggerated count for words of length 3
    assert 'a' in result and result['a'] == 1
    assert 'test' in result and result['test'] == 2
    assert 'only' in result and result['only'] == 1
    assert 'simple' in result and result['simple'] == 1

def test_exaggerated_word_counter_special_characters():
    """
    Test the exaggerated_word_counter function with special characters.
    """
    result = exaggerated_word_counter("Hello, world! This is a test; this is only a simple test.")
    assert 'hello' in result and result['hello'] == 1
    assert 'world' in result and result['world'] == 1
    assert 'this' in result and result['this'] == 20  # Exaggerated count for words of length 3
    assert 'is' in result and result['is'] == 40     # Exaggerated count for words of length 3
    assert 'a' in result and result['a'] == 1
    assert 'test' in result and result['test'] == 2
    assert 'only' in result and result['only'] == 1
    assert 'simple' in result and result['simple'] == 1

def test_exaggerated_word_counter_large_input():
    """
    Test the exaggerated_word_counter function with a large input.
    """
    text = "a" * 1000 + " b" * 1000 + " c" * 1000
    result = exaggerated_word_counter(text)
    assert 'a' in result and result['a'] == 1000
    assert 'b' in result and result['b'] == 1000
    assert 'c' in result and result['c'] == 20000  # Exaggerated count for words of length 3

def test_exaggerated_word_counter_mixed_case():
    """
    Test the exaggerated_word_counter function with mixed case words.
    """
    result = exaggerated_word_counter("Hello, hello! This is a test; this is only a simple test.")
    assert 'hello' in result and result['hello'] == 20  # Exaggerated count for words of length 3
    assert 'world' in result and result['world'] == 1
    assert 'this' in result and result['this'] == 40     # Exaggerated count for words of length 3
    assert 'is' in result and result['is'] == 80       # Exaggerated count for words of length 3
    assert 'a' in result and result['a'] == 1
    assert 'test' in result and result['test'] == 2
    assert 'only' in result and result['only'] == 1
    assert 'simple' in result and result['simple'] == 1

def test_exaggerated_word_counter_special_characters():
    """
    Test the exaggerated_word_counter function with special characters.
    """
    result = exaggerated_word_counter("Hello, world! This is a test; this is only a simple test.")
    assert 'hello' in result and result['hello'] == 1
    assert 'world' in result and result['world'] == 1
    assert 'this' in result and result['this'] == 20  # Exaggerated count for words of length 3
    assert 'is' in result and result['is'] == 40     # Exaggerated count for words of length 3
    assert 'a' in result and result['a'] == 1
    assert 'test' in result and result['test'] == 2
    assert 'only' in result and result['only'] == 1
    assert 'simple' in result and result['simple'] == 1

def test_exaggerated_word_counter_large_input():
    """
    Test the exaggerated_word_counter function with a large input.
    """
    text = "a" * 1000 + " b" * 1000 + " c" * 1000
    result = exaggerated_word_counter(text)
    assert 'a' in result and result['a'] == 1000
    assert 'b' in result and result['b'] == 1000
    assert 'c' in result and result['c'] == 20000  # Exaggerated count for words of length 3

def test_exaggerated_word_counter_mixed_case():
    """
    Test the exaggerated_word_counter function with mixed case words.
    """
    result = exaggerated_word_counter("Hello, hello! This is a test; this is only a simple test.")
    assert 'hello' in result and result['hello'] == 20  # Exaggerated count for words of length 3
    assert 'world' in result and result['world'] == 1
    assert 'this' in result and result['this'] == 40     # Exaggerated count for words of length 3
    assert 'is' in result and result['is'] == 80       # Exaggerated count for words of length 3
    assert 'a' in result and result['a'] == 1
    assert 'test' in result and result['test'] == 2
    assert 'only' in result and result['only'] == 1
    assert 'simple' in result and result['simple'] == 1

def test_exaggerated_word_counter_special_characters():
    """
    Test the exaggerated_word_counter function with special characters.
    """
    result = exaggerated_word_counter("Hello, world! This is a test; this is only a simple test.")
    assert 'hello' in result and result['hello'] == 1
    assert 'world' in result and result['world'] == 1
    assert 'this' in result and result['this'] == 20  # Exaggerated count for words of length 3
    assert 'is' in result and result['is'] == 40     # Exaggerated count for words of length 3
    assert '