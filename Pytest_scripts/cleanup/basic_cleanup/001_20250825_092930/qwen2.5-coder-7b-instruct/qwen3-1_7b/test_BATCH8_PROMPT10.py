from collections import defaultdict

def main():
    input_str = input("Enter a string: ")
    words = input_str.split()
    counts = defaultdict(int)
    for word in words:
        counts[word] += 1
    result = {}
    for word, count in counts.items():
        if len(word) == 3:
            result[word] = count * 10
        else:
            result[word] = count
    print(result)

if __name__ == "__main__":
    main()

# ===== GENERATED TESTS =====
from collections import defaultdict
import pytest

def process_string(input_str: str) -> dict:
    """
    Processes a string to count occurrences of each word and modifies counts based on word length.
    
    Args:
        input_str (str): The input string to process.
        
    Returns:
        dict: A dictionary with words as keys and modified counts as values.
    """
    words = input_str.split()
    counts = defaultdict(int)
    for word in words:
        counts[word] += 1
    result = {}
    for word, count in counts.items():
        if len(word) == 3:
            result[word] = count * 10
        else:
            result[word] = count
    return result

def test_process_string():
    # Test with a simple input
    assert process_string("hello world hello") == {'hello': 20, 'world': 1}
    
    # Test with a string containing words of different lengths
    assert process_string("one two three four five six seven eight nine ten") == {
        'one': 1, 'two': 1, 'three': 30, 'four': 1, 'five': 1, 'six': 1, 
        'seven': 1, 'eight': 1, 'nine': 1, 'ten': 1
    }
    
    # Test with a string containing repeated words of the same length
    assert process_string("apple apple apple") == {'apple': 30}
    
    # Test with an empty string
    assert process_string("") == {}
    
    # Test with a string containing only spaces
    assert process_string("   ") == {}

# Run the tests using pytest
if __name__ == "__main__":
    pytest.main()

This test suite includes comprehensive test cases for the `process_string` function. It covers various scenarios, including different word lengths, repeated words, and edge cases like empty strings or strings with only spaces. The use of pytest fixtures and parametrization is not necessary in this case since we are testing a simple function with a fixed set of inputs and outputs.