import random
from typing import List


def generate_poem(data: List[float], wordlist: List[str] = None) -> str:
    """
    Generates an abstract poem from a list of numbers using specified or default word lists.
    
    :param data: List of numerical values to be transformed into the poem's structure.
    :param wordlist: Optional list of words for the poem generation. If not provided, defaults to generic word list.
    """

    if wordlist is None:
        wordlist = [
            "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
            "W", "X", "Y", "Z"
        ]

    # Normalize data to range 0-1 for poetic interpretation
    normalized_data = [(x - min(data)) / (max(data) - min(data)) for x in data]

    lines: List[str] = []
    for index, value in enumerate(normalized_data):
        # Map the value to a line length and select words accordingly
        line_length = int(value * 10) + 2  # Ensures minimum of 2 words per line
        line_words = random.sample(wordlist, line_length)

        if index > 0:
            # Introduce rhyme by selecting a word from the previous line's ending sound
            prev_line_last_word = lines[-1].split()[-1]
            last_sound = get_sound(prev_line_last_word)
            new_word = next((word for word in wordlist if get_sound(word) == last_sound), None)
            if new_word:
                line_words.append(new_word)

        # Form the line and add to poem
        lines.append(' '.join(line_words))

    return '\n'.join(lines)


def get_sound(word: str) -> str:
    """
    A simplistic sound-based rhyme finder using the last letter of a word.
    
    :param word: The word to find a rhyming sound for.
    :return: The last letter of the word as a sound identifier.
    """
    return word[-1]


if __name__ == "__main__":
    data = [0.2, 0.5, 0.8]
    poem = generate_poem(data)
    print(poem)

# ===== GENERATED TESTS =====
import pytest
from typing import List, Tuple

# Original code remains unchanged

def test_generate_poem_default_wordlist():
    """Test generate_poem with default word list."""
    data = [0.2, 0.5, 0.8]
    poem = generate_poem(data)
    assert isinstance(poem, str)

def test_generate_poem_custom_wordlist():
    """Test generate_poem with custom word list."""
    data = [0.2, 0.5, 0.8]
    wordlist = ["Apple", "Banana", "Cherry"]
    poem = generate_poem(data, wordlist)
    assert isinstance(poem, str)

def test_generate_poem_empty_data():
    """Test generate_poem with empty data list."""
    data: List[float] = []
    with pytest.raises(ValueError):
        generate_poem(data)

def test_generate_poem_single_value_data():
    """Test generate_poem with single value in data list."""
    data = [0.5]
    poem = generate_poem(data)
    assert isinstance(poem, str)

def test_get_sound():
    """Test get_sound function."""
    word = "Banana"
    sound = get_sound(word)
    assert sound == 'a'

def test_generate_poem_rhyme():
    """Test generate_poem for rhyme introduction."""
    data = [0.2, 0.5, 0.8]
    poem = generate_poem(data)
    lines = poem.split('\n')
    last_sound = get_sound(lines[0].split()[-1])
    new_word = next((word for word in ['Apple', 'Banana'] if get_sound(word) == last_sound), None)
    assert new_word is not None

# Add more test cases as needed
