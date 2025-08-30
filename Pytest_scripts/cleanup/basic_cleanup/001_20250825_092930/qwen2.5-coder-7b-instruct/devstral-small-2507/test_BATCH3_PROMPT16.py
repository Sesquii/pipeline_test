# BATCH3_PROMPT16_Devstral.py

import random

def generate_poem(data_series):
    """
    Generate a poetic visualization based on a data series.

    Args:
        data_series (list): A list of numbers representing the data to visualize.

    Returns:
        str: A poetic representation of the data series.
    """

    # Word banks for different data ranges
    words_short = ["spark", "gleam", "whisper", "dream"]
    words_medium = ["river", "forest", "echo", "shadow"]
    words_long = ["mountain", "galaxy", "ocean", "horizon"]

    # Determine word choice based on data value ranges
    def get_word_for_value(value):
        if value < 3:
            return random.choice(words_short)
        elif value < 7:
            return random.choice(words_medium)
        else:
            return random.choice(words_long)

    # Generate lines for each data point
    poem_lines = []
    for i, value in enumerate(data_series):
        word = get_word_for_value(value)

        # Line length proportional to data value (clamped between 1 and max_value)
        line_length = min(max(1, int(value)), 20)
        repetition_count = min(max(1, int(value / 3)), 5)

        # Create repeated pattern
        line = " ".join([word] * repetition_count) + "\n" * (line_length - repetition_count)

        poem_lines.append(line.strip())

    return "\n".join(poem_lines)

def main():
    # Example data series
    data_series = [1, 4, 2, 8, 5, 9, 3]

    # Generate and print the poetic visualization
    poem = generate_poem(data_series)
    print("Poetic Data Visualization:")
    print(poem)

if __name__ == "__main__":
    main()

# ===== GENERATED TESTS =====
# BATCH3_PROMPT16_Devstral.py

import random
from typing import List

def generate_poem(data_series: List[int]) -> str:
    """
    Generate a poetic visualization based on a data series.

    Args:
        data_series (list): A list of numbers representing the data to visualize.

    Returns:
        str: A poetic representation of the data series.
    """

    # Word banks for different data ranges
    words_short = ["spark", "gleam", "whisper", "dream"]
    words_medium = ["river", "forest", "echo", "shadow"]
    words_long = ["mountain", "galaxy", "ocean", "horizon"]

    # Determine word choice based on data value ranges
    def get_word_for_value(value: int) -> str:
        if value < 3:
            return random.choice(words_short)
        elif value < 7:
            return random.choice(words_medium)
        else:
            return random.choice(words_long)

    # Generate lines for each data point
    poem_lines = []
    for i, value in enumerate(data_series):
        word = get_word_for_value(value)

        # Line length proportional to data value (clamped between 1 and max_value)
        line_length = min(max(1, int(value)), 20)
        repetition_count = min(max(1, int(value / 3)), 5)

        # Create repeated pattern
        line = " ".join([word] * repetition_count) + "\n" * (line_length - repetition_count)

        poem_lines.append(line.strip())

    return "\n".join(poem_lines)

def main():
    # Example data series
    data_series = [1, 4, 2, 8, 5, 9, 3]

    # Generate and print the poetic visualization
    poem = generate_poem(data_series)
    print("Poetic Data Visualization:")
    print(poem)

if __name__ == "__main__":
    main()

# BATCH3_PROMPT16_Devstral_test.py

import pytest
from BATCH3_PROMPT16_Devstral import generate_poem, words_short, words_medium, words_long

@pytest.fixture(params=[words_short, words_medium, words_long])
def word_bank(request):
    return request.param

def test_get_word_for_value(word_bank):
    """
    Test the get_word_for_value function with different data points.
    """

    # Test cases for each range
    test_cases = [
        (1, 2),  # Short range
        (3, 6),  # Medium range
        (7, 10)  # Long range
    ]

    for value, expected_range in test_cases:
        word = generate_poem([value])[0].split()[0]
        assert word in word_bank[expected_range]

def test_generate_poem():
    """
    Test the generate_poem function with different data series.
    """

    # Positive test case
    data_series_positive = [1, 4, 2, 8, 5, 9, 3]
    poem_positive = generate_poem(data_series_positive)
    assert isinstance(poem_positive, str)
    assert len(poem_positive.split('\n')) == len(data_series_positive)

    # Negative test case
    data_series_negative = []
    with pytest.raises(ValueError):
        generate_poem(data_series_negative)

def test_generate_poem_with_random_values():
    """
    Test the generate_poem function with random values.
    """

    for _ in range(10):
        data_series = [random.randint(1, 10) for _ in range(5)]
        poem = generate_poem(data_series)
        assert isinstance(poem, str)
        assert len(poem.split('\n')) == len(data_series)

def test_generate_poem_with_large_values():
    """
    Test the generate_poem function with large values.
    """

    data_series_large = [10, 20, 30, 40, 50]
    poem_large = generate_poem(data_series_large)
    assert isinstance(poem_large, str)
    assert len(poem_large.split('\n')) == len(data_series_large)

def test_generate_poem_with_small_values():
    """
    Test the generate_poem function with small values.
    """

    data_series_small = [1, 2, 3]
    poem_small = generate_poem(data_series_small)
    assert isinstance(poem_small, str)
    assert len(poem_small.split('\n')) == len(data_series_small)

def test_generate_poem_with_negative_values():
    """
    Test the generate_poem function with negative values.
    """

    data_series_negative = [-1, -2, -3]
    poem_negative = generate_poem(data_series_negative)
    assert isinstance(poem_negative, str)
    assert len(poem_negative.split('\n')) == len(data_series_negative)

def test_generate_poem_with_zero_values():
    """
    Test the generate_poem function with zero values.
    """

    data_series_zero = [0, 0, 0]
    poem_zero = generate_poem(data_series_zero)
    assert isinstance(poem_zero, str)
    assert len(poem_zero.split('\n')) == len(data_series_zero)

def test_generate_poem_with_repeated_values():
    """
    Test the generate_poem function with repeated values.
    """

    data_series_repeated = [3, 3, 3]
    poem_repeated = generate_poem(data_series_repeated)
    assert isinstance(poem_repeated, str)
    assert len(poem_repeated.split('\n')) == len(data_series_repeated)

def test_generate_poem_with_empty_string():
    """
    Test the generate_poem function with an empty string.
    """

    data_series_empty = []
    with pytest.raises(ValueError):
        generate_poem(data_series_empty)
