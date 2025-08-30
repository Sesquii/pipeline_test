import random

def main():
    try:
        with open('input.txt', 'r') as f:
            words = f.read().split()
    except FileNotFoundError:
        print("Error: Input file not found.")
        return

    counts = {}
    for word in words:
        lower_word = word.lower()
        if lower_word in counts:
            counts[lower_word] += 1
        else:
            counts[lower_word] = 1

    factors = [random.random() * 2 + 1 for _ in range(len(counts))]

    for i, (word, count) in enumerate(counts.items()):
        counts[word] *= factors[i]

    print(counts)

if __name__ == "__main__":
    main()

# ===== GENERATED TESTS =====
import pytest
from typing import List, Dict

# Original script code
def main():
    try:
        with open('input.txt', 'r') as f:
            words = f.read().split()
    except FileNotFoundError:
        print("Error: Input file not found.")
        return

    counts = {}
    for word in words:
        lower_word = word.lower()
        if lower_word in counts:
            counts[lower_word] += 1
        else:
            counts[lower_word] = 1

    factors = [random.random() * 2 + 1 for _ in range(len(counts))]

    for i, (word, count) in enumerate(counts.items()):
        counts[word] *= factors[i]

    print(counts)

if __name__ == "__main__":
    main()

# Test cases
def test_main_with_valid_input(tmp_path):
    """
    Test the main function with a valid input file.
    """
    # Create a temporary input file
    input_file = tmp_path / 'input.txt'
    input_file.write_text("Hello world hello")

    # Run the main function
    main()

    # Check if the output is as expected
    with open('output.txt', 'r') as f:
        output = f.read()
    assert "hello: 3.0" in output
    assert "world: 2.0" in output

def test_main_with_empty_input(tmp_path):
    """
    Test the main function with an empty input file.
    """
    # Create a temporary input file
    input_file = tmp_path / 'input.txt'
    input_file.write_text("")

    # Run the main function
    main()

    # Check if the output is as expected
    with open('output.txt', 'r') as f:
        output = f.read()
    assert "Error: Input file not found." in output

def test_main_with_nonexistent_input(tmp_path):
    """
    Test the main function with a non-existent input file.
    """
    # Run the main function
    main()

    # Check if the output is as expected
    with open('output.txt', 'r') as f:
        output = f.read()
    assert "Error: Input file not found." in output

def test_main_with_random_input(tmp_path):
    """
    Test the main function with random input.
    """
    # Create a temporary input file
    input_file = tmp_path / 'input.txt'
    words = [f"word{i}" for i in range(10)]
    input_file.write_text(" ".join(words))

    # Run the main function
    main()

    # Check if the output is as expected
    with open('output.txt', 'r') as f:
        output = f.read()
    for word in words:
        assert f"{word.lower()}: " in output

def test_main_with_duplicate_words(tmp_path):
    """
    Test the main function with duplicate words.
    """
    # Create a temporary input file
    input_file = tmp_path / 'input.txt'
    input_file.write_text("hello hello")

    # Run the main function
    main()

    # Check if the output is as expected
    with open('output.txt', 'r') as f:
        output = f.read()
    assert "hello: 3.0" in output

def test_main_with_case_insensitivity(tmp_path):
    """
    Test the main function with case-insensitive words.
    """
    # Create a temporary input file
    input_file = tmp_path / 'input.txt'
    input_file.write_text("Hello hello")

    # Run the main function
    main()

    # Check if the output is as expected
    with open('output.txt', 'r') as f:
        output = f.read()
    assert "hello: 3.0" in output

def test_main_with_large_input(tmp_path):
    """
    Test the main function with a large input file.
    """
    # Create a temporary input file
    input_file = tmp_path / 'input.txt'
    words = [f"word{i}" for i in range(1000)]
    input_file.write_text(" ".join(words))

    # Run the main function
    main()

    # Check if the output is as expected
    with open('output.txt', 'r') as f:
        output = f.read()
    for word in words:
        assert f"{word.lower()}: " in output

def test_main_with_special_characters(tmp_path):
    """
    Test the main function with special characters.
    """
    # Create a temporary input file
    input_file = tmp_path / 'input.txt'
    input_file.write_text("hello! hello?")

    # Run the main function
    main()

    # Check if the output is as expected
    with open('output.txt', 'r') as f:
        output = f.read()
    assert "hello: 3.0" in output

def test_main_with_numbers(tmp_path):
    """
    Test the main function with numbers.
    """
    # Create a temporary input file
    input_file = tmp_path / 'input.txt'
    input_file.write_text("123 456 789")

    # Run the main function
    main()

    # Check if the output is as expected
    with open('output.txt', 'r') as f:
        output = f.read()
    assert "123: " in output
    assert "456: " in output
    assert "789: " in output

def test_main_with_unicode(tmp_path):
    """
    Test the main function with unicode characters.
    """
    # Create a temporary input file
    input_file = tmp_path / 'input.txt'
    input_file.write_text("你好 世界 你好")

    # Run the main function
    main()

    # Check if the output is as expected
    with open('output.txt', 'r') as f:
        output = f.read()
    assert "你: 3.0" in output
    assert "好: 2.0" in output
    assert "世: 1.0" in output

def test_main_with_empty_string(tmp_path):
    """
    Test the main function with an empty string.
    """
    # Create a temporary input file
    input_file = tmp_path / 'input.txt'
    input_file.write_text("")

    # Run the main function
    main()

    # Check if the output is as expected
    with open('output.txt', 'r') as f:
        output = f.read()
    assert "Error: Input file not found." in output

def test_main_with_large_numbers(tmp_path):
    """
    Test the main function with large numbers.
    """
    # Create a temporary input file
    input_file = tmp_path / 'input.txt'
    input_file.write_text("1000000 2000000 3000000")

    # Run the main function
    main()

    # Check if the output is as expected
    with open('output.txt', 'r') as f:
        output = f.read()
    assert "1000000: " in output
    assert "2000000: " in output
    assert "3000000: " in output

def test_main_with_negative_numbers(tmp_path):
    """
    Test the main function with negative numbers.
    """
    # Create a temporary input file
    input_file = tmp_path / 'input.txt'
    input_file.write_text("-1 -2 -3")

    # Run the main function
    main()

    # Check if the output is as expected
    with open('output.txt', 'r') as f:
        output = f.read()
    assert "-1: " in output
    assert "-2: " in output
    assert "-3: " in output

def test_main_with_zero(tmp_path):
    """
    Test the main function with zero.
    """
    # Create a temporary input file
    input_file = tmp_path / 'input.txt'
    input_file.write_text("0 0 0")

    # Run the main function
    main()

    # Check if the output is as expected
    with open('output.txt', 'r') as f:
        output = f.read()
    assert "0: " in output

def test_main_with_mixed_types(tmp_path):
    """
    Test the main function with mixed types.
    """
    # Create a temporary input file
    input_file = tmp_path / 'input.txt'
    input_file.write_text("123 hello 456")

    # Run the main function
    main()

    # Check if the output is as expected
    with open('output.txt', 'r') as f:
        output = f.read()
    assert "123: " in output
    assert "hello: " in output
    assert "456: " in output

def test_main_with_large_strings(tmp_path):
    """
    Test the main function with large strings.
    """
    # Create a temporary input file
    input_file = tmp_path / 'input.txt'
    input_file.write_text("a" * 1000)

    # Run the main function
    main()

    # Check if the output is as expected
    with open('output.txt', 'r') as f:
        output = f.read()
    assert "a: " in output

def test_main_with_small_strings(tmp_path):
    """
    Test the main function with small strings.
    """
    # Create a temporary input file
    input_file = tmp_path / 'input.txt'
    input_file.write_text("a b c")

    # Run the main function
    main()

    # Check if the output is as expected
    with open('output.txt', 'r') as f:
        output = f.read()
    assert "a: " in output
    assert "b: " in output
    assert "c: " in output

def test_main_with_repeated_strings(tmp_path):
    """
    Test the main function with repeated strings.
    """
    # Create a temporary input file
    input_file = tmp_path / 'input.txt'
    input_file.write_text("a a a")

    # Run the main function
    main()

    # Check if the output is as expected
    with open('output.txt', 'r') as f:
        output = f.read()
    assert "a: 3.0" in output

def test_main_with_single_string(tmp_path):
    """
    Test the main function with a single string.
    """
    # Create a temporary input file
    input_file = tmp_path / 'input.txt'
    input_file.write_text("hello")

    # Run the main function
    main()

    # Check if the output is as expected
    with open('output.txt', 'r') as f:
        output = f.read()
    assert "hello: 2.0" in output

def test_main_with_multiple_files(tmp_path):
    """
    Test the main function with multiple files.
    """
    # Create temporary input files
    input_file1 = tmp_path / 'input1.txt'
    input_file1.write_text("hello world")
    input_file2 = tmp_path / 'input2.txt'
    input_file2.write_text("hello universe")

    # Run the main function with both files
    main()

    # Check if the output is as expected
    with open('output.txt', 'r') as f:
        output = f.read()
    assert "hello: 5.0" in output
    assert "world: 2.0" in output
    assert "universe: 3.0" in output

def test_main_with_empty_files(tmp_path):
    """
    Test the main function with empty files.
    """
    # Create temporary input files
    input_file1 = tmp_path / 'input1.txt'
    input_file1.write_text("")
    input_file2 = tmp_path / 'input2.txt'
    input_file2.write_text("")

    # Run the main function with both files
    main()

    # Check if the output is as expected
    with open('output.txt', 'r') as f:
        output = f.read()
    assert "Error: Input file not found." in output

def test_main_with_nonexistent_files(tmp_path):
    """
    Test the main function with nonexistent files.
    """
    # Run the main function with nonexistent files
    main()

    # Check if the output is as expected
    with open('output.txt', 'r') as f:
        output = f.read()
    assert "Error: Input file not found." in output

def test_main_with_large_files(tmp_path):
    """
    Test the main function with large files.
    """
    # Create temporary input files
    input_file1 = tmp_path / 'input1.txt'
    input_file1.write_text("a" * 1000)
    input_file2 = tmp_path / 'input2.txt'
    input_file2.write_text("b" * 1000)

    # Run the main function with both files
    main()

    # Check if the output is as expected
    with open('output.txt', 'r') as f:
        output = f.read()
    assert "a: " in output
    assert "b: " in output

def test_main_with_small_files(tmp_path):
    """
    Test the main function with small files.
    """
    # Create temporary input files
    input_file1 = tmp_path / 'input1.txt'
    input_file1.write_text("a b c")
    input_file2 = tmp_path / 'input2.txt'
    input_file2.write_text("d e f")

    # Run the main function with both files
    main()

    # Check if the output is as expected
    with open('output.txt', 'r') as f:
        output = f.read()
    assert "a: " in output
    assert "b: " in output
    assert "c: " in output
    assert "d: " in output
    assert "e: " in output
    assert "f: " in output

def test_main_with_repeated_files(tmp_path):
    """
    Test the main function with repeated files.
    """
    # Create temporary input files
    input_file1 = tmp_path / 'input1.txt'
    input_file1.write_text("a b c")
    input_file2 = tmp_path / 'input2.txt'
    input_file2.write_text("a b c")

    # Run the main function with both files
    main()

    # Check if the output is as expected
    with open('output.txt', 'r') as f:
        output = f.read()
    assert "a: 6.0" in output
    assert "b: 4.0" in output
    assert "c: 4.0" in output

def test_main_with_single_file(tmp_path):
    """
    Test the main function with a single file.
    """
    # Create temporary input files
    input_file1 = tmp_path / 'input1.txt'
    input_file1.write_text("hello world")

    # Run the main function with both files
    main()

    # Check if the output is as expected
    with open('output.txt', 'r') as f:
        output = f.read()
    assert "hello: 3.0" in output
    assert "world: 2.0" in output

def test_main_with_multiple_files_and_empty_files(tmp_path):
    """
    Test the main function with multiple files and empty files.
    """
    # Create temporary input files
    input_file1 = tmp_path / 'input1.txt'
    input_file1.write_text("hello world")
    input_file2 = tmp_path / 'input2.txt'
    input_file2.write_text("")

    # Run the main function with both files
    main()

    # Check if the output is as expected
    with open('output.txt', 'r') as f:
        output = f.read()
    assert "hello: 3.0" in output
    assert "world: 2.0" in output

def test_main_with_multiple_files_and_nonexistent_files(tmp_path):
    """
    Test the main function with multiple files and nonexistent files.
    """
    # Create temporary input files
    input_file1 = tmp_path / 'input1.txt'
    input_file1.write_text("hello world")
    input_file2 = tmp_path / 'input2.txt'

    # Run the main function with both files
    main()

    # Check if the output is as expected
    with open('output.txt', 'r') as f:
        output = f.read()
    assert "hello: 3.0" in output
    assert "world: 2.0" in output

def test_main_with_multiple_files_and_large_files(tmp_path):
    """
    Test the main function with multiple files and large files.
    """
    # Create temporary input files
    input_file1 = tmp_path / 'input1.txt'
    input_file1.write_text("a" * 1000)
    input_file2 = tmp_path / 'input2.txt'
    input_file2.write_text("b" * 1000)

    # Run the main function with both files
    main()

    # Check if the output is as expected
    with open('output.txt', 'r') as f:
        output = f.read()
    assert "a: " in output
    assert "b: " in output

def test_main_with_multiple_files_and_small_files(tmp_path):
    """
    Test the main function with multiple files and small files.
    """
    # Create temporary input files
    input_file1 = tmp_path / 'input1.txt'
    input_file1.write_text("a b c")
    input_file2 = tmp_path / 'input2.txt'
    input_file2.write_text("d e f")

    # Run the main function with both files
    main()

    # Check if the output is as expected
    with open('output.txt', 'r') as f:
        output = f.read()
    assert "a: " in output
    assert "b: " in output
    assert "c: " in output
    assert "d: " in output
    assert "e: " in output
    assert "f: " in output

def test_main_with_multiple_files_and_repeated_files(tmp_path):
    """
    Test the main function with multiple files and repeated files.
    """
    # Create temporary input files
    input_file1 = tmp_path / 'input1.txt'
    input_file1.write_text("a b c")
    input_file2 = tmp_path / 'input2.txt'
    input_file2.write_text("a b c")

    # Run the main function with both files
    main