```python
import sys

def expand_acronym(acronym, depth):
    if depth <= 0:
        return acronym
    letters = list(acronym)
    expanded_letters = []
    for letter in letters:
        expanded_letter = expand_letter(letter, depth - 1)
        expanded_letters.append(expanded_letter)
    return ''.join(expanded_letters)

def expand_letter(letter, depth):
    if depth <= 0:
        return letter_map[letter]
    else:
        expanded_word = expand_letter(letter, depth - 1)
        return word_map.get(expanded_word, letter)

# Mapping for initial expansion of letters
letter_map = {
    'N': 'North',
    'A': 'American',
    'S': 'Space'
}

# Mapping for deeper expansions
word_map = {
    'North': 'Nonsensical',
    'American': 'Albatross',
    'Space': 'Agency'
}

def main():
    acronym = input("Enter the acronym: ")
    depth = int(input("Enter the depth: "))
    result = expand_acronym(acronym, depth)
    print(result)

if __name__ == "__main__":
    main()

# ===== GENERATED TESTS =====
```python
import pytest

# Original script code remains unchanged

def test_expand_letter():
    """Test the expand_letter function with various inputs."""
    assert expand_letter('N', 1) == 'North'
    assert expand_letter('A', 2) == 'Albatross'
    assert expand_letter('S', 0) == 'Space'

def test_expand_acronym():
    """Test the expand_acronym function with various inputs."""
    assert expand_acronym('NAS', 1) == 'NonsensicalAmericanSpace'
    assert expand_acronym('NAS', 2) == 'NonsensicalAlbatrossSpaceAgency'
    assert expand_acronym('XYZ', 0) == 'XYZ'

def test_expand_acronym_negative_depth():
    """Test the expand_acronym function with negative depth."""
    assert expand_acronym('NAS', -1) == 'NAS'

def test_expand_letter_negative_depth():
    """Test the expand_letter function with negative depth."""
    assert expand_letter('N', -1) == 'North'

def test_main(capsys):
    """Test the main function using pytest-capsys to capture output."""
    input_values = ['NAS\n', '2\n']
    expected_output = "NonsensicalAlbatrossSpaceAgency\n"
    
    with pytest.raises(SystemExit) as excinfo:
        sys.stdin = io.StringIO(''.join(input_values))
        main()
    
    assert excinfo.type == SystemExit
    captured = capsys.readouterr()
    assert captured.out == expected_output

# Add more test cases as needed
```

This test suite includes comprehensive tests for the `expand_letter` and `expand_acronym` functions, as well as a test for the `main` function using pytest-capsys to capture output. The test cases cover both positive and negative scenarios, including edge cases with negative depth values.