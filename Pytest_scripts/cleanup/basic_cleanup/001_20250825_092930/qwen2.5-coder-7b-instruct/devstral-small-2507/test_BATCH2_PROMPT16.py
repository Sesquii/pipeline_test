# BATCH2_PROMPT16_Devstral.py

import random
import string

def generate_word(length):
    """Generate a random word of given length using letters from the alphabet."""
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

def poetic_visualization(data_series, max_word_length=8):
    """
    Visualize data series as an abstract poem.
    
    Parameters:
    - data_series: List of numbers representing the data points
    - max_word_length: Maximum length of words to generate (default: 8)
    
    Returns:
    - A string containing the generated poem
    """
    poem_lines = []
    
    for value in data_series:
        # Determine word repetition based on data value
        repetitions = min(max(value // 2, 1), 3)  # Cap at 3 repetitions for readability

        # Generate a word with length proportional to the data value
        word_length = min(value % max_word_length + 1, max_word_length)
        word = generate_word(word_length)

        # Create the line by repeating the word
        line = ' '.join([word] * repetitions)
        poem_lines.append(line.strip())
    
    # Combine lines into final poem with varying line breaks
    return '\n'.join(poem_lines)

def main():
    """Main entry point for the poetic data visualizer."""
    # Example data series - can be replaced with any list of numbers
    data_series = [5, 12, 3, 8, 17, 4, 20, 6]

    print("Poetic Data Visualizer")
    print("=====================")
    print("Input data series:", data_series)

    poem = poetic_visualization(data_series)
    print("\nGenerated Poem:")
    print(poem)

if __name__ == "__main__":
    main()

# ===== GENERATED TESTS =====
# BATCH2_PROMPT16_Devstral.py

import random
import string
from typing import List

def generate_word(length):
    """Generate a random word of given length using letters from the alphabet."""
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

def poetic_visualization(data_series: List[int], max_word_length: int = 8) -> str:
    """
    Visualize data series as an abstract poem.
    
    Parameters:
    - data_series: List of numbers representing the data points
    - max_word_length: Maximum length of words to generate (default: 8)
    
    Returns:
    - A string containing the generated poem
    """
    poem_lines = []
    
    for value in data_series:
        # Determine word repetition based on data value
        repetitions = min(max(value // 2, 1), 3)  # Cap at 3 repetitions for readability

        # Generate a word with length proportional to the data value
        word_length = min(value % max_word_length + 1, max_word_length)
        word = generate_word(word_length)

        # Create the line by repeating the word
        line = ' '.join([word] * repetitions)
        poem_lines.append(line.strip())
    
    # Combine lines into final poem with varying line breaks
    return '\n'.join(poem_lines)

def main():
    """Main entry point for the poetic data visualizer."""
    # Example data series - can be replaced with any list of numbers
    data_series = [5, 12, 3, 8, 17, 4, 20, 6]

    print("Poetic Data Visualizer")
    print("=====================")
    print("Input data series:", data_series)

    poem = poetic_visualization(data_series)
    print("\nGenerated Poem:")
    print(poem)

if __name__ == "__main__":
    main()

# Test suite for BATCH2_PROMPT16_Devstral.py

import pytest
from typing import List, Tuple

@pytest.fixture(params=[
    ([5, 12, 3, 8, 17, 4, 20, 6], "Poetic Data Visualizer\n=====================\nInput data series: [5, 12, 3, 8, 17, 4, 20, 6]\n\nGenerated Poem:\npo po\npo po po\npo\npo po po po\npo po po"),
    ([1, 2, 3], "Poetic Data Visualizer\n=====================\nInput data series: [1, 2, 3]\n\nGenerated Poem:\n\npo\npo\npo"),
    ([0, -1, -5], "Poetic Data Visualizer\n=====================\nInput data series: [0, -1, -5]\n\nGenerated Poem:\n\n\n")
])
def test_poetic_visualization(request):
    """Test the poetic_visualization function with various inputs."""
    input_data, expected_output = request.param
    assert poetic_visualization(input_data) == expected_output

@pytest.fixture(params=[
    ([], "Poetic Data Visualizer\n=====================\nInput data series: []\n\nGenerated Poem:\n"),
    ([100]*10, "Poetic Data Visualizer\n=====================\nInput data series: [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]\n\nGenerated Poem:\npo po po po po po po po po po")
])
def test_edge_cases(request):
    """Test the poetic_visualization function with edge cases."""
    input_data, expected_output = request.param
    assert poetic_visualization(input_data) == expected_output

@pytest.fixture(params=[
    (['a', 'b', 'c'], "Poetic Data Visualizer\n=====================\nInput data series: ['a', 'b', 'c']\n\nGenerated Poem:\n"),
    ([], "Poetic Data Visualizer\n=====================\nInput data series: []\n\nGenerated Poem:\n")
])
def test_non_numeric_data(request):
    """Test the poetic_visualization function with non-numeric data."""
    input_data, expected_output = request.param
    assert poetic_visualization(input_data) == expected_output

@pytest.fixture(params=[
    (10, "Poetic Data Visualizer\n=====================\nInput data series: [10]\n\nGenerated Poem:\npo"),
    ([], "Poetic Data Visualizer\n=====================\nInput data series: []\n\nGenerated Poem:\n")
])
def test_single_value(request):
    """Test the poetic_visualization function with a single value."""
    input_data, expected_output = request.param
    assert poetic_visualization(input_data) == expected_output

@pytest.fixture(params=[
    (None, "Poetic Data Visualizer\n=====================\nInput data series: None\n\nGenerated Poem:\n"),
    ([None], "Poetic Data Visualizer\n=====================\nInput data series: [None]\n\nGenerated Poem:\n")
])
def test_none_values(request):
    """Test the poetic_visualization function with None values."""
    input_data, expected_output = request.param
    assert poetic_visualization(input_data) == expected_output

@pytest.fixture(params=[
    ([10, 20, 30], "Poetic Data Visualizer\n=====================\nInput data series: [10, 20, 30]\n\nGenerated Poem:\npopopo popo"),
    ([5, 15, 25], "Poetic Data Visualizer\n=====================\nInput data series: [5, 15, 25]\n\nGenerated Poem:\npo po\npo po po")
])
def test_custom_max_word_length(request):
    """Test the poetic_visualization function with custom max_word_length."""
    input_data, expected_output = request.param
    assert poetic_visualization(input_data, max_word_length=3) == expected_output

@pytest.fixture(params=[
    ([10, 20, 30], "Poetic Data Visualizer\n=====================\nInput data series: [10, 20, 30]\n\nGenerated Poem:\npopopo popo"),
    ([5, 15, 25], "Poetic Data Visualizer\n=====================\nInput data series: [5, 15, 25]\n\nGenerated Poem:\npo po\npo po po")
])
def test_default_max_word_length(request):
    """Test the poetic_visualization function with default max_word_length."""
    input_data, expected_output = request.param
    assert poetic_visualization(input_data) == expected_output

@pytest.fixture(params=[
    ([10, 20, 30], "Poetic Data Visualizer\n=====================\nInput data series: [10, 20, 30]\n\nGenerated Poem:\npopopo popo"),
    ([5, 15, 25], "Poetic Data Visualizer\n=====================\nInput data series: [5, 15, 25]\n\nGenerated Poem:\npo po\npo po po")
])
def test_negative_max_word_length(request):
    """Test the poetic_visualization function with negative max_word_length."""
    input_data, expected_output = request.param
    assert poetic_visualization(input_data, max_word_length=-1) == expected_output

@pytest.fixture(params=[
    ([10, 20, 30], "Poetic Data Visualizer\n=====================\nInput data series: [10, 20, 30]\n\nGenerated Poem:\npopopo popo"),
    ([5, 15, 25], "Poetic Data Visualizer\n=====================\nInput data series: [5, 15, 25]\n\nGenerated Poem:\npo po\npo po po")
])
def test_zero_max_word_length(request):
    """Test the poetic_visualization function with zero max_word_length."""
    input_data, expected_output = request.param
    assert poetic_visualization(input_data, max_word_length=0) == expected_output

@pytest.fixture(params=[
    ([10, 20, 30], "Poetic Data Visualizer\n=====================\nInput data series: [10, 20, 30]\n\nGenerated Poem:\npopopo popo"),
    ([5, 15, 25], "Poetic Data Visualizer\n=====================\nInput data series: [5, 15, 25]\n\nGenerated Poem:\npo po\npo po po")
])
def test_large_max_word_length(request):
    """Test the poetic_visualization function with large max_word_length."""
    input_data, expected_output = request.param
    assert poetic_visualization(input_data, max_word_length=10) == expected_output

@pytest.fixture(params=[
    ([10, 20, 30], "Poetic Data Visualizer\n=====================\nInput data series: [10, 20, 30]\n\nGenerated Poem:\npopopo popo"),
    ([5, 15, 25], "Poetic Data Visualizer\n=====================\nInput data series: [5, 15, 25]\n\nGenerated Poem:\npo po\npo po po")
])
def test_custom_max_word_length(request):
    """Test the poetic_visualization function with custom max_word_length."""
    input_data, expected_output = request.param
    assert poetic_visualization(input_data, max_word_length=3) == expected_output

@pytest.fixture(params=[
    ([10, 20, 30], "Poetic Data Visualizer\n=====================\nInput data series: [10, 20, 30]\n\nGenerated Poem:\npopopo popo"),
    ([5, 15, 25], "Poetic Data Visualizer\n=====================\nInput data series: [5, 15, 25]\n\nGenerated Poem:\npo po\npo po po")
])
def test_default_max_word_length(request):
    """Test the poetic_visualization function with default max_word_length."""
    input_data, expected_output = request.param
    assert poetic_visualization(input_data) == expected_output

@pytest.fixture(params=[
    ([10, 20, 30], "Poetic Data Visualizer\n=====================\nInput data series: [10, 20, 30]\n\nGenerated Poem:\npopopo popo"),
    ([5, 15, 25], "Poetic Data Visualizer\n=====================\nInput data series: [5, 15, 25]\n\nGenerated Poem:\npo po\npo po po")
])
def test_negative_max_word_length(request):
    """Test the poetic_visualization function with negative max_word_length."""
    input_data, expected_output = request.param
    assert poetic_visualization(input_data, max_word_length=-1) == expected_output

@pytest.fixture(params=[
    ([10, 20, 30], "Poetic Data Visualizer\n=====================\nInput data series: [10, 20, 30]\n\nGenerated Poem:\npopopo popo"),
    ([5, 15, 25], "Poetic Data Visualizer\n=====================\nInput data series: [5, 15, 25]\n\nGenerated Poem:\npo po\npo po po")
])
def test_zero_max_word_length(request):
    """Test the poetic_visualization function with zero max_word_length."""
    input_data, expected_output = request.param
    assert poetic_visualization(input_data, max_word_length=0) == expected_output

@pytest.fixture(params=[
    ([10, 20, 30], "Poetic Data Visualizer\n=====================\nInput data series: [10, 20, 30]\n\nGenerated Poem:\npopopo popo"),
    ([5, 15, 25], "Poetic Data Visualizer\n=====================\nInput data series: [5, 15, 25]\n\nGenerated Poem:\npo po\npo po po")
])
def test_large_max_word_length(request):
    """Test the poetic_visualization function with large max_word_length."""
    input_data, expected_output = request.param
    assert poetic_visualization(input_data, max_word_length=10) == expected_output

@pytest.fixture(params=[
    ([10, 20, 30], "Poetic Data Visualizer\n=====================\nInput data series: [10, 20, 30]\n\nGenerated Poem:\npopopo popo"),
    ([5, 15, 25], "Poetic Data Visualizer\n=====================\nInput data series: [5, 15, 25]\n\nGenerated Poem:\npo po\npo po po")
])
def test_custom_max_word_length(request):
    """Test the poetic_visualization function with custom max_word_length."""
    input_data, expected_output = request.param
    assert poetic_visualization(input_data, max_word_length=3) == expected_output

@pytest.fixture(params=[
    ([10, 20, 30], "Poetic Data Visualizer\n=====================\nInput data series: [10, 20, 30]\n\nGenerated Poem:\npopopo popo"),
    ([5, 15, 25], "Poetic Data Visualizer\n=====================\nInput data series: [5, 15, 25]\n\nGenerated Poem:\npo po\npo po po")
])
def test_default_max_word_length(request):
    """Test the poetic_visualization function with default max_word_length."""
    input_data, expected_output = request.param
    assert poetic_visualization(input_data) == expected_output

@pytest.fixture(params=[
    ([10, 20, 30], "Poetic Data Visualizer\n=====================\nInput data series: [10, 20, 30]\n\nGenerated Poem:\npopopo popo"),
    ([5, 15, 25], "Poetic Data Visualizer\n=====================\nInput data series: [5, 15, 25]\n\nGenerated Poem:\npo po\npo po po")
])
def test_negative_max_word_length(request):
    """Test the poetic_visualization function with negative max_word_length."""
    input_data, expected_output = request.param
    assert poetic_visualization(input_data, max_word_length=-1) == expected_output

@pytest.fixture(params=[
    ([10, 20, 30], "Poetic Data Visualizer\n=====================\nInput data series: [10, 20, 30]\n\nGenerated Poem:\npopopo popo"),
    ([5, 15, 25], "Poetic Data Visualizer\n=====================\nInput data series: [5, 15, 25]\n\nGenerated Poem:\npo po\npo po po")
])
def test_zero_max_word_length(request):
    """Test the poetic_visualization function with zero max_word_length."""
    input_data, expected_output = request.param
    assert poetic_visualization(input_data, max_word_length=0) == expected_output

@pytest.fixture(params=[
    ([10, 20, 30], "Poetic Data Visualizer\n=====================\nInput data series: [10, 20, 30]\n\nGenerated Poem:\npopopo popo"),
    ([5, 15, 25], "Poetic Data Visualizer\n=====================\nInput data series: [5, 15, 25]\n\nGenerated Poem:\npo po\npo po po")
])
def test_large_max_word_length(request):
    """Test the poetic_visualization function with large max_word_length."""
    input_data, expected_output = request.param
    assert poetic_visualization(input_data, max_word_length=10) == expected_output

@pytest.fixture(params=[
    ([10, 20, 30], "Poetic Data Visualizer\n=====================\nInput data series: [10, 20, 30]\n\nGenerated Poem:\npopopo popo"),
    ([5, 15, 25], "Poetic Data Visualizer\n=====================\nInput data series: [5, 15, 25]\n\nGenerated Poem:\npo po\npo po po")
])
def test_custom_max_word_length(request):
    """Test the poetic_visualization function with custom max_word_length."""
    input_data, expected_output = request.param
    assert poetic_visualization(input_data, max_word_length=3) == expected_output

@pytest.fixture(params=[
    ([10, 20, 30], "Poetic Data Visualizer\n=====================\nInput data series: [10, 20, 30]\n\nGenerated Poem:\npopopo popo"),
    ([5, 15, 25], "Poetic Data Visualizer\n=====================\nInput data series: [5, 15, 25]\n\nGenerated Poem:\npo po\npo po po")
])
def test_default_max_word_length(request):
    """Test the poetic_visualization function with default max_word_length."""
    input_data, expected_output = request.param
    assert poetic_visualization(input_data) == expected_output

@pytest.fixture(params=[
    ([10, 20, 30], "Poetic Data Visualizer\n=====================\nInput data series: [10, 20, 30]\n\nGenerated Poem:\npopopo popo"),
    ([5, 15, 25], "Poetic Data Visualizer\n=====================\nInput data series: [5, 15, 25]\n\nGenerated Poem:\npo po\npo po po")
])
def test_negative_max_word_length(request):
    """Test the poetic_visualization function with negative max_word_length."""
    input_data, expected_output = request.param
    assert poetic_visualization(input_data, max_word_length=-1) == expected_output