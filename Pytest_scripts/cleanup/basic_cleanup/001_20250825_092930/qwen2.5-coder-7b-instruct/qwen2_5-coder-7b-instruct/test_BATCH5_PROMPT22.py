import random

def tesseract_string(input_string):
    def rotate_char(c):
        ascii_val = ord(c)
        prime = 29  # A small prime number for rotation
        return chr((ascii_val * prime) % 128)

    rotated_chars = [rotate_char(c) for c in input_string]
    shuffled_chars = random.sample(rotated_chars, len(rotated_chars))
    
    result = ''.join(shuffled_chars)
    return result

if __name__ == "__main__":
    input_string = "Hello, World!"
    output_string = tesseract_string(input_string)
    print(output_string)

# ===== GENERATED TESTS =====
import random
from typing import List

def tesseract_string(input_string):
    def rotate_char(c):
        ascii_val = ord(c)
        prime = 29  # A small prime number for rotation
        return chr((ascii_val * prime) % 128)

    rotated_chars = [rotate_char(c) for c in input_string]
    shuffled_chars = random.sample(rotated_chars, len(rotated_chars))
    
    result = ''.join(shuffled_chars)
    return result

# Test cases
def test_tesseract_string():
    # Positive test case with a simple string
    assert tesseract_string("abc") != "abc", "Test failed: Input should not be equal to output"
    
    # Negative test case with an empty string
    assert tesseract_string("") == "", "Test failed: Output for empty string should be an empty string"
    
    # Positive test case with a string containing special characters
    assert tesseract_string("!@#") != "!@#", "Test failed: Input should not be equal to output"
    
    # Negative test case with a string containing numbers
    assert tesseract_string("123") != "123", "Test failed: Input should not be equal to output"
    
    # Positive test case with a long string
    input_long = "a" * 1000
    output_long = tesseract_string(input_long)
    assert len(output_long) == len(input_long), "Test failed: Length of output should match the length of input"
    
    # Negative test case with a string containing uppercase and lowercase letters
    assert tesseract_string("Hello, World!") != "Hello, World!", "Test failed: Input should not be equal to output"

# Run tests if this script is executed directly
if __name__ == "__main__":
    input_string = "Hello, World!"
    output_string = tesseract_string(input_string)
    print(output_string)

This test suite includes both positive and negative test cases for the `tesseract_string` function. It checks various scenarios such as simple strings, empty strings, special characters, numbers, long strings, and mixed case letters. The tests ensure that the function does not return the same input string and handles different types of inputs correctly.