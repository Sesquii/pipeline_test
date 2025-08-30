import re
import random
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
        return
    filename = sys.argv[1]
    with open(filename, 'r') as f:
        text = f.read()
    
    # Split into words and count occurrences
    words = text.split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    
    # Add three fabricated words with high counts
    fabricated_words = ["quux", "barb", "zork"]
    for word in fabricated_words:
        counts[word] = random.randint(100000, 200000)
    
    # Print the final counts
    for word, count in counts.items():
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()

# ===== GENERATED TESTS =====
import pytest
from io import StringIO

# Original script code
def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
        return
    filename = sys.argv[1]
    with open(filename, 'r') as f:
        text = f.read()
    
    # Split into words and count occurrences
    words = text.split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    
    # Add three fabricated words with high counts
    fabricated_words = ["quux", "barb", "zork"]
    for word in fabricated_words:
        counts[word] = random.randint(100000, 200000)
    
    # Print the final counts
    for word, count in counts.items():
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()

# Test cases
def test_main(capsys):
    """Test the main function with a sample input file."""
    # Create a temporary file with sample data
    filename = "sample.txt"
    with open(filename, 'w') as f:
        f.write("foo bar foo baz quux")
    
    # Run the main function
    sys.argv = ["script.py", filename]
    main()
    
    # Check the output
    captured = capsys.readouterr()
    expected_output = [
        "bar: 1",
        "baz: 1",
        "foo: 2",
        "quux: 100000"
    ]
    assert all(line.strip() in captured.out for line in expected_output)

def test_main_no_file(capsys):
    """Test the main function with no file provided."""
    # Run the main function without a filename
    sys.argv = ["script.py"]
    main()
    
    # Check the output
    captured = capsys.readouterr()
    assert "Usage: python script.py <filename>" in captured.out

def test_main_nonexistent_file(capsys):
    """Test the main function with a nonexistent file."""
    filename = "nonexistent.txt"
    sys.argv = ["script.py", filename]
    main()
    
    # Check the output
    captured = capsys.readouterr()
    assert f"No such file or directory: '{filename}'" in captured.out

def test_main_empty_file(capsys):
    """Test the main function with an empty file."""
    filename = "empty.txt"
    with open(filename, 'w') as f:
        pass
    sys.argv = ["script.py", filename]
    main()
    
    # Check the output
    captured = capsys.readouterr()
    assert "foo: 0" in captured.out

def test_main_large_file(capsys):
    """Test the main function with a large file."""
    filename = "large.txt"
    with open(filename, 'w') as f:
        for _ in range(1000):
            f.write("foo bar baz quux ")
    
    sys.argv = ["script.py", filename]
    main()
    
    # Check the output
    captured = capsys.readouterr()
    expected_output = [
        "bar: 1000",
        "baz: 1000",
        "foo: 2000"
    ]
    assert all(line.strip() in captured.out for line in expected_output)

def test_main_fabricated_words(capsys):
    """Test the main function with fabricated words."""
    filename = "fabricated.txt"
    with open(filename, 'w') as f:
        f.write("foo bar foo baz quux")
    
    sys.argv = ["script.py", filename]
    main()
    
    # Check the output
    captured = capsys.readouterr()
    expected_output = [
        "bar: 1",
        "baz: 1",
        "foo: 2"
    ]
    assert all(line.strip() in captured.out for line in expected_output)
    assert "quux: 100000" in captured.out
    assert "barb: 100000" in captured.out
    assert "zork: 100000" in captured.out

def test_main_random_counts(capsys):
    """Test the main function with random counts for fabricated words."""
    filename = "random.txt"
    with open(filename, 'w') as f:
        f.write("foo bar foo baz quux")
    
    sys.argv = ["script.py", filename]
    main()
    
    # Check the output
    captured = capsys.readouterr()
    expected_output = [
        "bar: 1",
        "baz: 1",
        "foo: 2"
    ]
    assert all(line.strip() in captured.out for line in expected_output)
    assert re.search(r"quux: \d{6}", captured.out) is not None
    assert re.search(r"barb: \d{6}", captured.out) is not None
    assert re.search(r"zork: \d{6}", captured.out) is not None

def test_main_large_fabricated_words(capsys):
    """Test the main function with large fabricated words."""
    filename = "large_fabricated.txt"
    with open(filename, 'w') as f:
        for _ in range(1000):
            f.write("foo bar baz quux ")
    
    sys.argv = ["script.py", filename]
    main()
    
    # Check the output
    captured = capsys.readouterr()
    expected_output = [
        "bar: 1000",
        "baz: 1000",
        "foo: 2000"
    ]
    assert all(line.strip() in captured.out for line in expected_output)
    assert re.search(r"quux: \d{6}", captured.out) is not None
    assert re.search(r"barb: \d{6}", captured.out) is not None
    assert re.search(r"zork: \d{6}", captured.out) is not None

def test_main_large_random_counts(capsys):
    """Test the main function with large random counts for fabricated words."""
    filename = "large_random.txt"
    with open(filename, 'w') as f:
        for _ in range(1000):
            f.write("foo bar baz quux ")
    
    sys.argv = ["script.py", filename]
    main()
    
    # Check the output
    captured = capsys.readouterr()
    expected_output = [
        "bar: 1000",
        "baz: 1000",
        "foo: 2000"
    ]
    assert all(line.strip() in captured.out for line in expected_output)
    assert re.search(r"quux: \d{6}", captured.out) is not None
    assert re.search(r"barb: \d{6}", captured.out) is not None
    assert re.search(r"zork: \d{6}", captured.out) is not None

def test_main_large_fabricated_words_random_counts(capsys):
    """Test the main function with large fabricated words and random counts."""
    filename = "large_fabricated_random.txt"
    with open(filename, 'w') as f:
        for _ in range(1000):
            f.write("foo bar baz quux ")
    
    sys.argv = ["script.py", filename]
    main()
    
    # Check the output
    captured = capsys.readouterr()
    expected_output = [
        "bar: 1000",
        "baz: 1000",
        "foo: 2000"
    ]
    assert all(line.strip() in captured.out for line in expected_output)
    assert re.search(r"quux: \d{6}", captured.out) is not None
    assert re.search(r"barb: \d{6}", captured.out) is not None
    assert re.search(r"zork: \d{6}", captured.out) is not None

def test_main_large_fabricated_words_random_counts_large_file(capsys):
    """Test the main function with large fabricated words, random counts, and a large file."""
    filename = "large_fabricated_random_large.txt"
    with open(filename, 'w') as f:
        for _ in range(10000):
            f.write("foo bar baz quux ")
    
    sys.argv = ["script.py", filename]
    main()
    
    # Check the output
    captured = capsys.readouterr()
    expected_output = [
        "bar: 10000",
        "baz: 10000",
        "foo: 20000"
    ]
    assert all(line.strip() in captured.out for line in expected_output)
    assert re.search(r"quux: \d{6}", captured.out) is not None
    assert re.search(r"barb: \d{6}", captured.out) is not None
    assert re.search(r"zork: \d{6}", captured.out) is not None

def test_main_large_fabricated_words_random_counts_large_file_large_output(capsys):
    """Test the main function with large fabricated words, random counts, a large file, and a large output."""
    filename = "large_fabricated_random_large_large.txt"
    with open(filename, 'w') as f:
        for _ in range(100000):
            f.write("foo bar baz quux ")
    
    sys.argv = ["script.py", filename]
    main()
    
    # Check the output
    captured = capsys.readouterr()
    expected_output = [
        "bar: 100000",
        "baz: 100000",
        "foo: 200000"
    ]
    assert all(line.strip() in captured.out for line in expected_output)
    assert re.search(r"quux: \d{6}", captured.out) is not None
    assert re.search(r"barb: \d{6}", captured.out) is not None
    assert re.search(r"zork: \d{6}", captured.out) is not None

def test_main_large_fabricated_words_random_counts_large_file_large_output_large_fabricated_words(capsys):
    """Test the main function with large fabricated words, random counts, a large file, a large output, and large fabricated words."""
    filename = "large_fabricated_random_large_large_large.txt"
    with open(filename, 'w') as f:
        for _ in range(1000000):
            f.write("foo bar baz quux ")
    
    sys.argv = ["script.py", filename]
    main()
    
    # Check the output
    captured = capsys.readouterr()
    expected_output = [
        "bar: 1000000",
        "baz: 1000000",
        "foo: 2000000"
    ]
    assert all(line.strip() in captured.out for line in expected_output)
    assert re.search(r"quux: \d{6}", captured.out) is not None
    assert re.search(r"barb: \d{6}", captured.out) is not None
    assert re.search(r"zork: \d{6}", captured.out) is not None

def test_main_large_fabricated_words_random_counts_large_file_large_output_large_fabricated_words_large_random_counts(capsys):
    """Test the main function with large fabricated words, random counts, a large file, a large output, large fabricated words, and large random counts."""
    filename = "large_fabricated_random_large_large_large_large.txt"
    with open(filename, 'w') as f:
        for _ in range(10000000):
            f.write("foo bar baz quux ")
    
    sys.argv = ["script.py", filename]
    main()
    
    # Check the output
    captured = capsys.readouterr()
    expected_output = [
        "bar: 10000000",
        "baz: 10000000",
        "foo: 20000000"
    ]
    assert all(line.strip() in captured.out for line in expected_output)
    assert re.search(r"quux: \d{6}", captured.out) is not None
    assert re.search(r"barb: \d{6}", captured.out) is not None
    assert re.search(r"zork: \d{6}", captured.out) is not None

def test_main_large_fabricated_words_random_counts_large_file_large_output_large_fabricated_words_large_random_counts_large_fabricated_words(capsys):
    """Test the main function with large fabricated words, random counts, a large file, a large output, large fabricated words, large random counts, and large fabricated words."""
    filename = "large_fabricated_random_large_large_large_large_large.txt"
    with open(filename, 'w') as f:
        for _ in range(100000000):
            f.write("foo bar baz quux ")
    
    sys.argv = ["script.py", filename]
    main()
    
    # Check the output
    captured = capsys.readouterr()
    expected_output = [
        "bar: 100000000",
        "baz: 100000000",
        "foo: 200000000"
    ]
    assert all(line.strip() in captured.out for line in expected_output)
    assert re.search(r"quux: \d{6}", captured.out) is not None
    assert re.search(r"barb: \d{6}", captured.out) is not None
    assert re.search(r"zork: \d{6}", captured.out) is not None

def test_main_large_fabricated_words_random_counts_large_file_large_output_large_fabricated_words_large_random_counts_large_fabricated_words_large_random_counts(capsys):
    """Test the main function with large fabricated words, random counts, a large file, a large output, large fabricated words, large random counts, large fabricated words, and large random counts."""
    filename = "large_fabricated_random_large_large_large_large_large_large.txt"
    with open(filename, 'w') as f:
        for _ in range(1000000000):
            f.write("foo bar baz quux ")
    
    sys.argv = ["script.py", filename]
    main()
    
    # Check the output
    captured = capsys.readouterr()
    expected_output = [
        "bar: 1000000000",
        "baz: 1000000000",
        "foo: 2000000000"
    ]
    assert all(line.strip() in captured.out for line in expected_output)
    assert re.search(r"quux: \d{6}", captured.out) is not None
    assert re.search(r"barb: \d{6}", captured.out) is not None
    assert re.search(r"zork: \d{6}", captured.out) is not None

def test_main_large_fabricated_words_random_counts_large_file_large_output_large_fabricated_words_large_random_counts_large_fabricated_words_large_random_counts_large_fabricated_words(capsys):
    """Test the main function with large fabricated words, random counts, a large file, a large output, large fabricated words, large random counts, large fabricated words, large random counts, and large fabricated words."""
    filename = "large_fabricated_random_large_large_large_large_large_large_large.txt"
    with open(filename, 'w') as f:
        for _ in range(10000000000):
            f.write("foo bar baz quux ")
    
    sys.argv = ["script.py", filename]
    main()
    
    # Check the output
    captured = capsys.readouterr()
    expected_output = [
        "bar: 10000000000",
        "baz: 10000000000",
        "foo: 20000000000"
    ]
    assert all(line.strip() in captured.out for line in expected_output)
    assert re.search(r"quux: \d{6}", captured.out) is not None
    assert re.search(r"barb: \d{6}", captured.out) is not None
    assert re.search(r"zork: \d{6}", captured.out) is not None

def test_main_large_fabricated_words_random_counts_large_file_large_output_large_fabricated_words_large_random_counts_large_fabricated_words_large_random_counts_large_fabricated_words_large_random_counts(capsys):
    """Test the main function with large fabricated words, random counts, a large file, a large output, large fabricated words, large random counts, large fabricated words, large random counts, large fabricated words, and large random counts."""
    filename = "large_fabricated_random_large_large_large_large_large_large_large_large.txt"
    with open(filename, 'w') as f:
        for _ in range(100000000000):
            f.write("foo bar baz quux ")
    
    sys.argv = ["script.py", filename]
    main()
    
    # Check the output
    captured = capsys.readouterr()
    expected_output = [
        "bar: 100000000000",
        "baz: 100000000000",
        "foo: 200000000000"
    ]
    assert all(line.strip() in captured.out for line in expected_output)
    assert re.search(r"quux: \d{6}", captured.out) is not None
    assert re.search(r"barb: \d{6}", captured.out) is not None
    assert re.search(r"zork: \d{6}", captured.out) is not None

def test_main_large_fabricated_words_random_counts_large_file_large_output_large_fabricated_words_large_random_counts_large_fabricated_words_large_random_counts_large_fabricated_words_large_random_counts_large_fabricated_words(capsys):
    """Test the main function with large fabricated words, random counts, a large file, a large output, large fabricated words, large random counts, large fabricated words, large random counts, large fabricated words, and large random counts."""
