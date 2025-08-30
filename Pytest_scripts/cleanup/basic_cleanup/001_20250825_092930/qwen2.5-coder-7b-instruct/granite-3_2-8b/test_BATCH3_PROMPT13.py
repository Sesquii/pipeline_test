import random
import string

def generate_random_word(length=5):
    """Generates a random word of given length."""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def expand_acronym(acronym, depth):
    """Recursively expands an acronym to a certain depth."""
    if depth == 0:
        return acronym

    # Split the current acronym into its components
    parts = [char.title() + generate_random_word(4) for char in acronym]
    
    # Join them back together with spaces
    expanded_acronym = ' '.join(parts)
    return expand_acronym(expanded_acronym, depth - 1)

def main():
    print("Recursive Acronym Expander")
    acronym = input("Enter an acronym: ")
    max_depth = int(input("Enter the maximum depth for expansion: "))

    try:
        expanded_acronym = expand_acronym(acronym, max_depth)
        print(f"Expanded Acronym: {expanded_acronym}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

# ===== GENERATED TESTS =====
import pytest

# Original script remains unchanged

def test_generate_random_word():
    """Test the generate_random_word function."""
    word = generate_random_word(10)
    assert isinstance(word, str)
    assert len(word) == 10
    assert all(char in string.ascii_lowercase for char in word)

def test_expand_acronym_depth_0():
    """Test the expand_acronym function with depth 0."""
    acronym = "abc"
    expanded_acronym = expand_acronym(acronym, 0)
    assert expanded_acronym == acronym

def test_expand_acronym_positive_depth():
    """Test the expand_acronym function with positive depth."""
    acronym = "abc"
    max_depth = 2
    expanded_acronym = expand_acronym(acronym, max_depth)
    assert isinstance(expanded_acronym, str)
    assert len(expanded_acronym.split()) == 3 * (max_depth + 1)

def test_expand_acronym_negative_depth():
    """Test the expand_acronym function with negative depth."""
    acronym = "abc"
    max_depth = -1
    with pytest.raises(ValueError):
        expand_acronym(acronym, max_depth)

def test_main_function():
    """Test the main function using a fixture to capture output."""
    from io import StringIO
    import sys

    def mock_input(prompt):
        return {
            "Enter an acronym: ": "abc",
            "Enter the maximum depth for expansion: ": "2"
        }[prompt]

    def mock_print(*args, **kwargs):
        print(*args, file=output)

    input_data = StringIO()
    output = StringIO()

    sys.stdin = input_data
    sys.stdout = output

    with pytest.raises(SystemExit) as exc_info:
        main()

    assert exc_info.type == SystemExit
    assert exc_info.value.code == 0
    assert "Expanded Acronym: ABC ABC ABC" in output.getvalue()

# Add more test cases as needed
