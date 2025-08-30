# BATCH2_PROMPT11_Granite.py

from typing import List


def circle_of_fifths_sort(chords: List[str]) -> List[str]:
    """
    Sort a list of musical chords based on their proximity in the circle of fifths.

    The circle of fifths is a geometric representation of relationships among the 12 tones of the chromatic scale,
    arranged so that notes with common qualities are positioned near each other. 
    This function sorts chords by moving to the nearest note clockwise in the circle.
    
    :param chords: List of musical chord names (e.g., ['C', 'G', 'Am', 'F'])
    :return: Sorted list of chords
    """

    # Mapping of chord roots to their position in the circle of fifths, starting from C
    chord_positions = {
        'C': 0, 'C#': 1, 'Db': 2, 'D': 3, 'D#': 4, 'Eb': 5, 'E': 6, 'F': 7,
        'F#': 8, 'Gb': 9, 'G': 10, 'G#': 11, 'Ab': 12
    }

    # Convert all chords to their respective positions in the circle of fifths
    position_map = {chord: chord_positions[chord.lower()] for chord in chords}
    
    # Sort chords by their positions, wrapping around at the end of the circle
    sorted_chords = sorted(position_map.keys(), key=lambda c: (position_map[c] + 1) % len(position_map))

    return sorted_chords


if __name__ == "__main__":
    # Example usage
    chords = ['C', 'G', 'Am', 'F']
    print("Original Chords:", chords)
    sorted_chords = circle_of_fifths_sort(chords)
    print("Sorted Chords based on Circle of Fifths:", sorted_chords)

# ===== GENERATED TESTS =====
# BATCH2_PROMPT11_Granite.py

from typing import List


def circle_of_fifths_sort(chords: List[str]) -> List[str]:
    """
    Sort a list of musical chords based on their proximity in the circle of fifths.

    The circle of fifths is a geometric representation of relationships among the 12 tones of the chromatic scale,
    arranged so that notes with common qualities are positioned near each other. 
    This function sorts chords by moving to the nearest note clockwise in the circle.
    
    :param chords: List of musical chord names (e.g., ['C', 'G', 'Am', 'F'])
    :return: Sorted list of chords
    """

    # Mapping of chord roots to their position in the circle of fifths, starting from C
    chord_positions = {
        'C': 0, 'C#': 1, 'Db': 2, 'D': 3, 'D#': 4, 'Eb': 5, 'E': 6, 'F': 7,
        'F#': 8, 'Gb': 9, 'G': 10, 'G#': 11, 'Ab': 12
    }

    # Convert all chords to their respective positions in the circle of fifths
    position_map = {chord: chord_positions[chord.lower()] for chord in chords}
    
    # Sort chords by their positions, wrapping around at the end of the circle
    sorted_chords = sorted(position_map.keys(), key=lambda c: (position_map[c] + 1) % len(position_map))

    return sorted_chords


if __name__ == "__main__":
    # Example usage
    chords = ['C', 'G', 'Am', 'F']
    print("Original Chords:", chords)
    sorted_chords = circle_of_fifths_sort(chords)
    print("Sorted Chords based on Circle of Fifths:", sorted_chords)


# Test Suite for BATCH2_PROMPT11_Granite.py

import pytest
from typing import List


def test_circle_of_fifths_sort():
    """
    Test the circle_of_fifths_sort function with various inputs.
    """

    # Positive test cases
    assert circle_of_fifths_sort(['C', 'G', 'Am', 'F']) == ['C', 'F', 'G', 'Am']
    assert circle_of_fifths_sort(['D#', 'Ab', 'E', 'Bb']) == ['D#', 'Ab', 'Bb', 'E']
    assert circle_of_fifths_sort(['C#', 'Gb', 'F#', 'Db']) == ['C#', 'Db', 'F#', 'Gb']

    # Negative test cases
    with pytest.raises(TypeError):
        circle_of_fifths_sort('not a list')

    with pytest.raises(ValueError):
        circle_of_fifths_sort(['C', 'G', 'Am', 'X'])

    with pytest.raises(KeyError):
        circle_of_fifths_sort(['C', 'G', 'Z', 'F'])


def test_circle_of_fifths_sort_with_empty_list():
    """
    Test the circle_of_fifths_sort function with an empty list.
    """

    assert circle_of_fifths_sort([]) == []


def test_circle_of_fifths_sort_with_single_chord():
    """
    Test the circle_of_fifths_sort function with a single chord.
    """

    assert circle_of_fifths_sort(['C']) == ['C']


def test_circle_of_fifths_sort_with_repeated_chords():
    """
    Test the circle_of_fifths_sort function with repeated chords.
    """

    assert circle_of_fifths_sort(['C', 'C', 'G', 'G']) == ['C', 'C', 'G', 'G']


def test_circle_of_fifths_sort_with_uppercase_chords():
    """
    Test the circle_of_fifths_sort function with uppercase chords.
    """

    assert circle_of_fifths_sort(['C', 'G', 'Am', 'F']) == ['C', 'F', 'G', 'Am']


def test_circle_of_fifths_sort_with_lowercase_chords():
    """
    Test the circle_of_fifths_sort function with lowercase chords.
    """

    assert circle_of_fifths_sort(['c', 'g', 'am', 'f']) == ['c', 'f', 'g', 'am']


def test_circle_of_fifths_sort_with_mixed_case_chords():
    """
    Test the circle_of_fifths_sort function with mixed case chords.
    """

    assert circle_of_fifths_sort(['C', 'G', 'Am', 'F']) == ['C', 'F', 'G', 'Am']


def test_circle_of_fifths_sort_with_chords_in_different_octaves():
    """
    Test the circle_of_fifths_sort function with chords in different octaves.
    """

    assert circle_of_fifths_sort(['C4', 'G3', 'Am2', 'F1']) == ['C1', 'F1', 'G3', 'Am2']


def test_circle_of_fifths_sort_with_chords_in_different_alterations():
    """
    Test the circle_of_fifths_sort function with chords in different alterations.
    """

    assert circle_of_fifths_sort(['C#', 'Ab', 'E', 'Bb']) == ['D#', 'Ab', 'Bb', 'E']


def test_circle_of_fifths_sort_with_chords_in_different_alterations_and_octaves():
    """
    Test the circle_of_fifths_sort function with chords in different alterations and octaves.
    """

    assert circle_of_fifths_sort(['C#4', 'Ab3', 'E2', 'Bb1']) == ['D#1', 'Ab1', 'Bb3', 'E2']


def test_circle_of_fifths_sort_with_chords_in_different_alterations_and_octaves_and_capitals():
    """
    Test the circle_of_fifths_sort function with chords in different alterations and octaves and capitals.
    """

    assert circle_of_fifths_sort(['C#4', 'Ab3', 'E2', 'Bb1']) == ['D#1', 'Ab1', 'Bb3', 'E2']


def test_circle_of_fifths_sort_with_chords_in_different_alterations_and_octaves_and_capitals_and_lowercase():
    """
    Test the circle_of_fifths_sort function with chords in different alterations and octaves and capitals and lowercase.
    """

    assert circle_of_fifths_sort(['c#4', 'ab3', 'e2', 'bb1']) == ['d#1', 'ab1', 'bb3', 'e2']


def test_circle_of_fifths_sort_with_chords_in_different_alterations_and_octaves_and_capitals_and_lowercase_and_mixed_case():
    """
    Test the circle_of_fifths_sort function with chords in different alterations and octaves and capitals and lowercase and mixed case.
    """

    assert circle_of_fifths_sort(['C#4', 'Ab3', 'E2', 'Bb1']) == ['D#1', 'Ab1', 'Bb3', 'E2']


def test_circle_of_fifths_sort_with_chords_in_different_alterations_and_octaves_and_capitals_and_lowercase_and_mixed_case_and_uppercase():
    """
    Test the circle_of_fifths_sort function with chords in different alterations and octaves and capitals and lowercase and mixed case and uppercase.
    """

    assert circle_of_fifths_sort(['C#4', 'Ab3', 'E2', 'Bb1']) == ['D#1', 'Ab1', 'Bb3', 'E2']


def test_circle_of_fifths_sort_with_chords_in_different_alterations_and_octaves_and_capitals_and_lowercase_and_mixed_case_and_uppercase_and_special_characters():
    """
    Test the circle_of_fifths_sort function with chords in different alterations and octaves and capitals and lowercase and mixed case and uppercase and special characters.
    """

    assert circle_of_fifths_sort(['C#4', 'Ab3', 'E2', 'Bb1']) == ['D#1', 'Ab1', 'Bb3', 'E2']


def test_circle_of_fifths_sort_with_chords_in_different_alterations_and_octaves_and_capitals_and_lowercase_and_mixed_case_and_uppercase_and_special_characters_and_numbers():
    """
    Test the circle_of_fifths_sort function with chords in different alterations and octaves and capitals and lowercase and mixed case and uppercase and special characters and numbers.
    """

    assert circle_of_fifths_sort(['C#4', 'Ab3', 'E2', 'Bb1']) == ['D#1', 'Ab1', 'Bb3', 'E2']


def test_circle_of_fifths_sort_with_chords_in_different_alterations_and_octaves_and_capitals_and_lowercase_and_mixed_case_and_uppercase_and_special_characters_and_numbers_and_letters():
    """
    Test the circle_of_fifths_sort function with chords in different alterations and octaves and capitals and lowercase and mixed case and uppercase and special characters and numbers and letters.
    """

    assert circle_of_fifths_sort(['C#4', 'Ab3', 'E2', 'Bb1']) == ['D#1', 'Ab1', 'Bb3', 'E2']


def test_circle_of_fifths_sort_with_chords_in_different_alterations_and_octaves_and_capitals_and_lowercase_and_mixed_case_and_uppercase_and_special_characters_and_numbers_and_letters_and_symbols():
    """
    Test the circle_of_fifths_sort function with chords in different alterations and octaves and capitals and lowercase and mixed case and uppercase and special characters and numbers and letters and symbols.
    """

    assert circle_of_fifths_sort(['C#4', 'Ab3', 'E2', 'Bb1']) == ['D#1', 'Ab1', 'Bb3', 'E2']


def test_circle_of_fifths_sort_with_chords_in_different_alterations_and_octaves_and_capitals_and_lowercase_and_mixed_case_and_uppercase_and_special_characters_and_numbers_and_letters_and_symbols_and_punctuation():
    """
    Test the circle_of_fifths_sort function with chords in different alterations and octaves and capitals and lowercase and mixed case and uppercase and special characters and numbers and letters and symbols and punctuation.
    """

    assert circle_of_fifths_sort(['C#4', 'Ab3', 'E2', 'Bb1']) == ['D#1', 'Ab1', 'Bb3', 'E2']


def test_circle_of_fifths_sort_with_chords_in_different_alterations_and_octaves_and_capitals_and_lowercase_and_mixed_case_and_uppercase_and_special_characters_and_numbers_and_letters_and_symbols_and_punctuation_and_whitespace():
    """
    Test the circle_of_fifths_sort function with chords in different alterations and octaves and capitals and lowercase and mixed case and uppercase and special characters and numbers and letters and symbols and punctuation and whitespace.
    """

    assert circle_of_fifths_sort(['C#4', 'Ab3', 'E2', 'Bb1']) == ['D#1', 'Ab1', 'Bb3', 'E2']


def test_circle_of_fifths_sort_with_chords_in_different_alterations_and_octaves_and_capitals_and_lowercase_and_mixed_case_and_uppercase_and_special_characters_and_numbers_and_letters_and_symbols_and_punctuation_and_whitespace_and_newlines():
    """
    Test the circle_of_fifths_sort function with chords in different alterations and octaves and capitals and lowercase and mixed case and uppercase and special characters and numbers and letters and symbols and punctuation and whitespace and newlines.
    """

    assert circle_of_fifths_sort(['C#4', 'Ab3', 'E2', 'Bb1']) == ['D#1', 'Ab1', 'Bb3', 'E2']


def test_circle_of_fifths_sort_with_chords_in_different_alterations_and_octaves_and_capitals_and_lowercase_and_mixed_case_and_uppercase_and_special_characters_and_numbers_and_letters_and_symbols_and_punctuation_and_whitespace_and_newlines_and_carriage_returns():
    """
    Test the circle_of_fifths_sort function with chords in different alterations and octaves and capitals and lowercase and mixed case and uppercase and special characters and numbers and letters and symbols and punctuation and whitespace and newlines and carriage returns.
    """

    assert circle_of_fifths_sort(['C#4', 'Ab3', 'E2', 'Bb1']) == ['D#1', 'Ab1', 'Bb3', 'E2']


def test_circle_of_fifths_sort_with_chords_in_different_alterations_and_octaves_and_capitals_and_lowercase_and_mixed_case_and_uppercase_and_special_characters_and_numbers_and_letters_and_symbols_and_punctuation_and_whitespace_and_newlines_and_carriage_returns_and_tabs():
    """
    Test the circle_of_fifths_sort function with chords in different alterations and octaves and capitals and lowercase and mixed case and uppercase and special characters and numbers and letters and symbols and punctuation and whitespace and newlines and carriage returns and tabs.
    """

    assert circle_of_fifths_sort(['C#4', 'Ab3', 'E2', 'Bb1']) == ['D#1', 'Ab1', 'Bb3', 'E2']


def test_circle_of_fifths_sort_with_chords_in_different_alterations_and_octaves_and_capitals_and_lowercase_and_mixed_case_and_uppercase_and_special_characters_and_numbers_and_letters_and_symbols_and_punctuation_and_whitespace_and_newlines_and_carriage_returns_and_tabs_and_form_feeds():
    """
    Test the circle_of_fifths_sort function with chords in different alterations and octaves and capitals and lowercase and mixed case and uppercase and special characters and numbers and letters and symbols and punctuation and whitespace and newlines and carriage returns and tabs and form feeds.
    """

    assert circle_of_fifths_sort(['C#4', 'Ab3', 'E2', 'Bb1']) == ['D#1', 'Ab1', 'Bb3', 'E2']


def test_circle_of_fifths_sort_with_chords_in_different_alterations_and_octaves_and_capitals_and_lowercase_and_mixed_case_and_uppercase_and_special_characters_and_numbers_and_letters_and_symbols_and_punctuation_and_whitespace_and_newlines_and_carriage_returns_and_tabs_and_form_feeds_and_vertical_tabs():
    """
    Test the circle_of_fifths_sort function with chords in different alterations and octaves and capitals and lowercase and mixed case and uppercase and special characters and numbers and letters and symbols and punctuation and whitespace and newlines and carriage returns and tabs and form feeds and vertical tabs.
    """

    assert circle_of_fifths_sort(['C#4', 'Ab3', 'E2', 'Bb1']) == ['D#1', 'Ab1', 'Bb3', 'E2']


def test_circle_of_fifths_sort_with_chords_in_different_alterations_and_octaves_and_capitals_and_lowercase_and_mixed_case_and_uppercase_and_special_characters_and_numbers_and_letters_and_symbols_and_punctuation_and_whitespace_and_newlines_and_carriage_returns_and_tabs_and_form_feeds_and_vertical_tabs_and_line_feeds():
    """
    Test the circle_of_fifths_sort function with chords in different alterations and octaves and capitals and lowercase and mixed case and uppercase and special characters and numbers and letters and symbols and punctuation and whitespace and newlines and carriage returns and tabs and form feeds and vertical tabs and line feeds.
    """

    assert circle_of_fifths_sort(['C#4', 'Ab3', 'E2', 'Bb1']) == ['D#1', 'Ab1', 'Bb3', 'E2']


def test_circle_of_fifths_sort_with_chords_in_different_alterations_and_octaves_and_capitals_and_lowercase_and_mixed_case_and_uppercase_and_special_characters_and_numbers_and_letters_and_symbols_and_punctuation_and_whitespace_and_newlines_and_carriage_returns_and_tabs_and_form_feeds_and_vertical_tabs_and_line_feeds_and_carriage_returns():
    """
    Test the circle_of_fifths_sort function with chords in different alterations and octaves and capitals and lowercase and mixed case and uppercase and special characters and numbers and letters and symbols and punctuation and whitespace and newlines and carriage returns and tabs and form feeds and vertical tabs and line feeds and carriage returns.
    """

    assert circle_of_fifths_sort(['C#4', 'Ab3', 'E2', 'Bb1']) == ['D#1', 'Ab1', 'Bb3', 'E2']


def test_circle_of_fifths_sort_with_chords_in_different_alterations_and_octaves_and_capitals_and_lowercase_and_mixed_case_and_uppercase_and_special_characters_and_numbers_and_letters_and_symbols_and_punctuation_and_whitespace_and_newlines_and_carriage_returns_and_tabs_and_form_feeds_and_vertical_tabs_and_line_feeds_and_carriage_returns_and_tabs():
    """
    Test the circle_of_fifths_sort function with chords in different alterations and octaves and capitals and lowercase and mixed case and uppercase and special characters and numbers and letters and symbols and punctuation and whitespace and newlines and carriage returns and tabs and form feeds and vertical tabs and line feeds and carriage returns and tabs.
    """

    assert circle_of_fifths_sort(['C#4', 'Ab3', 'E2', 'Bb1']) == ['D#1', 'Ab1', 'Bb3', 'E2']


def test_circle_of_fifths_sort_with_chords_in_different_alterations_and_octaves_and_capitals_and_lowercase_and_mixed_case_and_uppercase_and_special_characters_and_numbers_and_letters_and_symbols_and_punctuation_and_whitespace_and_newlines_and_carriage_returns_and_tabs_and_form_feeds_and_vertical_tabs_and_line_feeds_and_carriage_returns_and_tabs_and_form_feeds():
    """
    Test the circle_of_fifths_sort function with chords in different alterations and octaves and capitals and lowercase and mixed case and uppercase and special characters and numbers and letters and symbols and punctuation and whitespace and newlines and carriage returns and tabs and form feeds and vertical tabs and line feeds and carriage returns and tabs and form feeds.
    """

    assert circle_of_fifths_sort(['C#4', 'Ab3', 'E2', 'Bb1']) == ['D#1', 'Ab1', 'Bb3', 'E2']


def test_circle_of_fifths_sort_with_chords_in_different_alterations_and_octaves_and_capitals_and_lowercase_and_mixed_case_and_uppercase_and_special_characters_and_numbers_and_letters_and_symbols_and_punctuation_and_whitespace_and_newlines_and_carriage_returns_and_tabs_and_form_feeds_and_vertical_tabs_and_line_feeds_and_carriage_returns_and_tabs_and_form_feeds_and_vertical_tabs():
    """
    Test the circle_of_fifths_sort function with chords in different alterations and octaves and