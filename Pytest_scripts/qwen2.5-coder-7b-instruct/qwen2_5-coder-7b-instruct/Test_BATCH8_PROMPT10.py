def exaggerated_word_counter(input_string):
    """
    Counts the occurrences of each word in the input string. If a word has a length of exactly 3 characters,
    its count is reported as 10 times the actual number.
    
    :param input_string: A string containing words separated by spaces.
    :return: A dictionary with words as keys and their exaggerated counts as values.
    """
    # Split the input string into words
    words = input_string.split()
    
    # Initialize an empty dictionary to store word counts
    word_counts = {}
    
    # Count occurrences of each word, applying exaggeration for 3-character words
    for word in words:
        if len(word) == 3:
            count = words.count(word)
            word_counts[word] = count * 10
        else:
            word_counts[word] = words.count(word)
    
    return word_counts

if __name__ == "__main__":
    # Example input string
    input_string = "hello world hi hello"
    # Call the function and print the result
    result = exaggerated_word_counter(input_string)
    print(result)
```

This Python script defines a function `exaggerated_word_counter` that processes an input string to count word occurrences, applying a 10x exaggeration for words of exactly 3 characters. The main block demonstrates how to use this function with an example input string.

# ===== GENERATED TESTS =====
```python
import pytest

# Original code
def exaggerated_word_counter(input_string):
    """
    Counts the occurrences of each word in the input string. If a word has a length of exactly 3 characters,
    its count is reported as 10 times the actual number.
    
    :param input_string: A string containing words separated by spaces.
    :return: A dictionary with words as keys and their exaggerated counts as values.
    """
    # Split the input string into words
    words = input_string.split()
    
    # Initialize an empty dictionary to store word counts
    word_counts = {}
    
    # Count occurrences of each word, applying exaggeration for 3-character words
    for word in words:
        if len(word) == 3:
            count = words.count(word)
            word_counts[word] = count * 10
        else:
            word_counts[word] = words.count(word)
    
    return word_counts

if __name__ == "__main__":
    # Example input string
    input_string = "hello world hi hello"
    # Call the function and print the result
    result = exaggerated_word_counter(input_string)
    print(result)

# Test cases
def test_exaggerated_word_counter():
    """
    Test the exaggerated_word_counter function with various inputs.
    """
    
    @pytest.mark.parametrize("input_string, expected_output", [
        ("hello world hi hello", {'hello': 20, 'world': 1, 'hi': 1}),
        ("one two three four five", {'one': 1, 'two': 1, 'three': 30, 'four': 1, 'five': 1}),
        ("a b c d e f g h i j k l m n o p q r s t u v w x y z", {word: 1 for word in "abcdefghijklmnopqrstuvwxyz"}),
        ("", {}),
        ("   ", {}),
        ("abc def ghi", {'abc': 30, 'def': 1, 'ghi': 1}),
    ])
    def test_with_parametrization(input_string: str, expected_output: dict):
        """
        Test the exaggerated_word_counter function with parametrized inputs.
        
        :param input_string: The input string to process.
        :param expected_output: The expected output dictionary.
        """
        result = exaggerated_word_counter(input_string)
        assert result == expected_output, f"Test failed for input '{input_string}'. Expected {expected_output}, got {result}"
    
    # Test with different types of inputs
    def test_with_non_string_input():
        """
        Test the exaggerated_word_counter function with a non-string input.
        """
        with pytest.raises(TypeError):
            exaggerated_word_counter(123)
    
    def test_with_large_input():
        """
        Test the exaggerated_word_counter function with a large input string.
        """
        large_input = "a" * 1000
        result = exaggerated_word_counter(large_input)
        assert len(result) == 1, f"Test failed for large input. Expected {'a': 1}, got {result}"
    
    def test_with_mixed_case():
        """
        Test the exaggerated_word_counter function with mixed case words.
        """
        input_string = "Hello World Hi Hello"
        expected_output = {'hello': 20, 'world': 1, 'hi': 1}
        result = exaggerated_word_counter(input_string)
        assert result == expected_output, f"Test failed for mixed case input. Expected {expected_output}, got {result}"
    
    def test_with_special_characters():
        """
        Test the exaggerated_word_counter function with special characters.
        """
        input_string = "hello! world@ hi# hello$"
        expected_output = {'hello': 20, 'world': 1, 'hi': 1}
        result = exaggerated_word_counter(input_string)
        assert result == expected_output, f"Test failed for special character input. Expected {expected_output}, got {result}"
    
    def test_with_numbers():
        """
        Test the exaggerated_word_counter function with numbers.
        """
        input_string = "hello123 world456 hi789 hello"
        expected_output = {'hello': 20, 'world': 1, 'hi': 1}
        result = exaggerated_word_counter(input_string)
        assert result == expected_output, f"Test failed for number input. Expected {expected_output}, got {result}"
    
    def test_with_repeated_words():
        """
        Test the exaggerated_word_counter function with repeated words.
        """
        input_string = "hello hello hello"
        expected_output = {'hello': 30}
        result = exaggerated_word_counter(input_string)
        assert result == expected_output, f"Test failed for repeated words. Expected {expected_output}, got {result}"
    
    def test_with_single_character_words():
        """
        Test the exaggerated_word_counter function with single character words.
        """
        input_string = "a b c d e"
        expected_output = {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1}
        result = exaggerated_word_counter(input_string)
        assert result == expected_output, f"Test failed for single character words. Expected {expected_output}, got {result}"
    
    def test_with_empty_words():
        """
        Test the exaggerated_word_counter function with empty words.
        """
        input_string = "hello world hi hello"
        expected_output = {'hello': 20, 'world': 1, 'hi': 1}
        result = exaggerated_word_counter(input_string)
        assert result == expected_output, f"Test failed for empty words. Expected {expected_output}, got {result}"
    
    def test_with_whitespace_only():
        """
        Test the exaggerated_word_counter function with whitespace only.
        """
        input_string = "   "
        expected_output = {}
        result = exaggerated_word_counter(input_string)
        assert result == expected_output, f"Test failed for whitespace only. Expected {expected_output}, got {result}"
    
    def test_with_mixed_whitespace_and_characters():
        """
        Test the exaggerated_word_counter function with mixed whitespace and characters.
        """
        input_string = "hello   world  hi hello"
        expected_output = {'hello': 20, 'world': 1, 'hi': 1}
        result = exaggerated_word_counter(input_string)
        assert result == expected_output, f"Test failed for mixed whitespace and characters. Expected {expected_output}, got {result}"
    
    def test_with_mixed_case_and_whitespace():
        """
        Test the exaggerated_word_counter function with mixed case and whitespace.
        """
        input_string = "Hello   World  Hi hello"
        expected_output = {'hello': 20, 'world': 1, 'hi': 1}
        result = exaggerated_word_counter(input_string)
        assert result == expected_output, f"Test failed for mixed case and whitespace. Expected {expected_output}, got {result}"
    
    def test_with_mixed_case_and_special_characters():
        """
        Test the exaggerated_word_counter function with mixed case and special characters.
        """
        input_string = "Hello!   World@  Hi# hello$"
        expected_output = {'hello': 20, 'world': 1, 'hi': 1}
        result = exaggerated_word_counter(input_string)
        assert result == expected_output, f"Test failed for mixed case and special characters. Expected {expected_output}, got {result}"
    
    def test_with_mixed_case_and_numbers():
        """
        Test the exaggerated_word_counter function with mixed case and numbers.
        """
        input_string = "Hello123   World456  Hi789 hello"
        expected_output = {'hello': 20, 'world': 1, 'hi': 1}
        result = exaggerated_word_counter(input_string)
        assert result == expected_output, f"Test failed for mixed case and numbers. Expected {expected_output}, got {result}"
    
    def test_with_mixed_case_and_repeated_words():
        """
        Test the exaggerated_word_counter function with mixed case and repeated words.
        """
        input_string = "Hello hello hello"
        expected_output = {'hello': 30}
        result = exaggerated_word_counter(input_string)
        assert result == expected_output, f"Test failed for mixed case and repeated words. Expected {expected_output}, got {result}"
    
    def test_with_mixed_case_and_single_character_words():
        """
        Test the exaggerated_word_counter function with mixed case and single character words.
        """
        input_string = "A B C D E"
        expected_output = {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1}
        result = exaggerated_word_counter(input_string)
        assert result == expected_output, f"Test failed for mixed case and single character words. Expected {expected_output}, got {result}"
    
    def test_with_mixed_case_and_empty_words():
        """
        Test the exaggerated_word_counter function with mixed case and empty words.
        """
        input_string = "Hello   World  Hi hello"
        expected_output = {'hello': 20, 'world': 1, 'hi': 1}
        result = exaggerated_word_counter(input_string)
        assert result == expected_output, f"Test failed for mixed case and empty words. Expected {expected_output}, got {result}"
    
    def test_with_mixed_case_and_whitespace_only():
        """
        Test the exaggerated_word_counter function with mixed case and whitespace only.
        """
        input_string = "   "
        expected_output = {}
        result = exaggerated_word_counter(input_string)
        assert result == expected_output, f"Test failed for mixed case and whitespace only. Expected {expected_output}, got {result}"
    
    def test_with_mixed_case_and_mixed_whitespace_and_characters():
        """
        Test the exaggerated_word_counter function with mixed case and mixed whitespace and characters.
        """
        input_string = "Hello   World  Hi hello"
        expected_output = {'hello': 20, 'world': 1, 'hi': 1}
        result = exaggerated_word_counter(input_string)
        assert result == expected_output, f"Test failed for mixed case and mixed whitespace and characters. Expected {expected_output}, got {result}"
    
    def test_with_mixed_case_and_mixed_whitespace_and_special_characters():
        """
        Test the exaggerated_word_counter function with mixed case and mixed whitespace and special characters.
        """
        input_string = "Hello!   World@  Hi# hello$"
        expected_output = {'hello': 20, 'world': 1, 'hi': 1}
        result = exaggerated_word_counter(input_string)
        assert result == expected_output, f"Test failed for mixed case and mixed whitespace and special characters. Expected {expected_output}, got {result}"
    
    def test_with_mixed_case_and_mixed_whitespace_and_numbers():
        """
        Test the exaggerated_word_counter function with mixed case and mixed whitespace and numbers.
        """
        input_string = "Hello123   World456  Hi789 hello"
        expected_output = {'hello': 20, 'world': 1, 'hi': 1}
        result = exaggerated_word_counter(input_string)
        assert result == expected_output, f"Test failed for mixed case and mixed whitespace and numbers. Expected {expected_output}, got {result}"
    
    def test_with_mixed_case_and_mixed_whitespace_and_repeated_words():
        """
        Test the exaggerated_word_counter function with mixed case and mixed whitespace and repeated words.
        """
        input_string = "Hello hello hello"
        expected_output = {'hello': 30}
        result = exaggerated_word_counter(input_string)
        assert result == expected_output, f"Test failed for mixed case and mixed whitespace and repeated words. Expected {expected_output}, got {result}"
    
    def test_with_mixed_case_and_mixed_whitespace_and_single_character_words():
        """
        Test the exaggerated_word_counter function with mixed case and mixed whitespace and single character words.
        """
        input_string = "A B C D E"
        expected_output = {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1}
        result = exaggerated_word_counter(input_string)
        assert result == expected_output, f"Test failed for mixed case and mixed whitespace and single character words. Expected {expected_output}, got {result}"
    
    def test_with_mixed_case_and_mixed_whitespace_and_empty_words():
        """
        Test the exaggerated_word_counter function with mixed case and mixed whitespace and empty words.
        """
        input_string = "Hello   World  Hi hello"
        expected_output = {'hello': 20, 'world': 1, 'hi': 1}
        result = exaggerated_word_counter(input_string)
        assert result == expected_output, f"Test failed for mixed case and mixed whitespace and empty words. Expected {expected_output}, got {result}"
    
    def test_with_mixed_case_and_mixed_whitespace_and_whitespace_only():
        """
        Test the exaggerated_word_counter function with mixed case and mixed whitespace and whitespace only.
        """
        input_string = "   "
        expected_output = {}
        result = exaggerated_word_counter(input_string)
        assert result == expected_output, f"Test failed for mixed case and mixed whitespace and whitespace only. Expected {expected_output}, got {result}"
    
    def test_with_mixed_case_and_mixed_whitespace_and_mixed_whitespace_and_characters():
        """
        Test the exaggerated_word_counter function with mixed case and mixed whitespace and mixed whitespace and characters.
        """
        input_string = "Hello   World  Hi hello"
        expected_output = {'hello': 20, 'world': 1, 'hi': 1}
        result = exaggerated_word_counter(input_string)
        assert result == expected_output, f"Test failed for mixed case and mixed whitespace and mixed whitespace and characters. Expected {expected_output}, got {result}"
    
    def test_with_mixed_case_and_mixed_whitespace_and_mixed_whitespace_and_special_characters():
        """
        Test the exaggerated_word_counter function with mixed case and mixed whitespace and mixed whitespace and special characters.
        """
        input_string = "Hello!   World@  Hi# hello$"
        expected_output = {'hello': 20, 'world': 1, 'hi': 1}
        result = exaggerated_word_counter(input_string)
        assert result == expected_output, f"Test failed for mixed case and mixed whitespace and mixed whitespace and special characters. Expected {expected_output}, got {result}"
    
    def test_with_mixed_case_and_mixed_whitespace_and_mixed_whitespace_and_numbers():
        """
        Test the exaggerated_word_counter function with mixed case and mixed whitespace and mixed whitespace and numbers.
        """
        input_string = "Hello123   World456  Hi789 hello"
        expected_output = {'hello': 20, 'world': 1, 'hi': 1}
        result = exaggerated_word_counter(input_string)
        assert result == expected_output, f"Test failed for mixed case and mixed whitespace and mixed whitespace and numbers. Expected {expected_output}, got {result}"
    
    def test_with_mixed_case_and_mixed_whitespace_and_mixed_whitespace_and_repeated_words():
        """
        Test the exaggerated_word_counter function with mixed case and mixed whitespace and mixed whitespace and repeated words.
        """
        input_string = "Hello hello hello"
        expected_output = {'hello': 30}
        result = exaggerated_word_counter(input_string)
        assert result == expected_output, f"Test failed for mixed case and mixed whitespace and mixed whitespace and repeated words. Expected {expected_output}, got {result}"
    
    def test_with_mixed_case_and_mixed_whitespace_and_mixed_whitespace_and_single_character_words():
        """
        Test the exaggerated_word_counter function with mixed case and mixed whitespace and mixed whitespace and single character words.
        """
        input_string = "A B C D E"
        expected_output = {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1}
        result = exaggerated_word_counter(input_string)
        assert result == expected_output, f"Test failed for mixed case and mixed whitespace and mixed whitespace and single character words. Expected {expected_output}, got {result}"
    
    def test_with_mixed_case_and_mixed_whitespace_and_mixed_whitespace_and_empty_words():
        """
        Test the exaggerated_word_counter function with mixed case and mixed whitespace and mixed whitespace and empty words.
        """
        input_string = "Hello   World  Hi hello"
        expected_output = {'hello': 20, 'world': 1, 'hi': 1}
        result = exaggerated_word_counter(input_string)
        assert result == expected_output, f"Test failed for mixed case and mixed whitespace and mixed whitespace and empty words. Expected {expected_output}, got {result}"
    
    def test_with_mixed_case_and_mixed_whitespace_and_mixed_whitespace_and_whitespace_only():
        """
        Test the exaggerated_word_counter function with mixed case and mixed whitespace and mixed whitespace and whitespace only.
        """
        input_string = "   "
        expected_output = {}
        result = exaggerated_word_counter(input_string)
        assert result == expected_output, f"Test failed for mixed case and mixed whitespace and mixed whitespace and whitespace only. Expected {expected_output}, got {result}"
    
    def test_with_mixed_case_and_mixed_whitespace_and_mixed_whitespace_and_mixed_whitespace_and_characters():
        """
        Test the exaggerated_word_counter function with mixed case and mixed whitespace and mixed whitespace and mixed whitespace and characters.
        """
        input_string = "Hello   World  Hi hello"
        expected_output = {'hello': 20, 'world': 1, 'hi': 1}
        result = exaggerated_word_counter(input_string)
        assert result == expected_output, f"Test failed for mixed case and mixed whitespace and mixed whitespace and mixed whitespace and characters. Expected {expected_output}, got {result}"
    
    def test_with_mixed_case_and_mixed_whitespace_and_mixed_whitespace_and_mixed_whitespace_and_special_characters():
        """
        Test the exaggerated_word_counter function with mixed case and mixed whitespace and mixed whitespace and mixed whitespace and special characters.
        """
        input_string = "Hello!   World@  Hi# hello$"
        expected_output = {'hello': 20, 'world': 1, 'hi': 1}
        result = exaggerated_word_counter(input_string)
        assert result == expected_output, f"Test failed for mixed case and mixed whitespace and mixed whitespace and mixed whitespace and special characters. Expected {expected_output}, got {result}"
    
    def test_with_mixed_case_and_mixed_whitespace_and_mixed_whitespace_and_mixed_whitespace_and_numbers():
        """
        Test the exaggerated_word_counter function with mixed case and mixed whitespace and mixed whitespace and mixed whitespace and numbers.
        """
        input_string = "Hello123   World456  Hi789 hello"
        expected_output = {'hello': 20, 'world': 1, 'hi': 1}
