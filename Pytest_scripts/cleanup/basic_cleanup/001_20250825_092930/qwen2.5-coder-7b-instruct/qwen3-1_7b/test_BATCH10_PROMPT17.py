import sys

# Generate a circular list of fictional holidays
holidays = [
    "Eclipse Festival", "Moonlight Mela", "Starlit Celebration",
    "Galaxy Day", "Celestial Dance", "Nova Event", "Solar Eclipse",
    "Lunar Marvel", "Stellar Harmony", "Cosmic Rite"
]

def main():
    for i, holiday in enumerate(holidays):
        next_holiday = holidays[(i + 1) % len(holidays)]
        print(f"{holiday} is celebrated on {next_holiday}")

if __name__ == "__main__":
    main()

# ===== GENERATED TESTS =====
import pytest

# Original script remains unchanged

def main():
    for i, holiday in enumerate(holidays):
        next_holiday = holidays[(i + 1) % len(holidays)]
        print(f"{holiday} is celebrated on {next_holiday}")

if __name__ == "__main__":
    main()

# Test suite starts here
@pytest.fixture(scope="module")
def circular_holidays():
    return [
        "Eclipse Festival", "Moonlight Mela", "Starlit Celebration",
        "Galaxy Day", "Celestial Dance", "Nova Event", "Solar Eclipse",
        "Lunar Marvel", "Stellar Harmony", "Cosmic Rite"
    ]

@pytest.mark.parametrize("holiday, expected_next_holiday", [
    ("Eclipse Festival", "Moonlight Mela"),
    ("Starlit Celebration", "Galaxy Day"),
    ("Celestial Dance", "Nova Event"),
    ("Solar Eclipse", "Lunar Marvel"),
    ("Stellar Harmony", "Cosmic Rite"),
    ("Cosmic Rite", "Eclipse Festival")
])
def test_next_holiday(circular_holidays, holiday, expected_next_holiday):
    """
    Test that the next holiday is correctly calculated.
    """
    index = circular_holidays.index(holiday)
    assert circular_holidays[(index + 1) % len(circular_holidays)] == expected_next_holiday

def test_empty_list():
    """
    Test that an empty list raises a ValueError.
    """
    with pytest.raises(ValueError):
        next_holiday = [""][0]

def test_single_element_list():
    """
    Test that a single element list returns the same element as the next holiday.
    """
    single_holiday = ["Eclipse Festival"]
    assert single_holiday[0] == single_holiday[(0 + 1) % len(single_holiday)]

def test_negative_index():
    """
    Test that a negative index raises an IndexError.
    """
    with pytest.raises(IndexError):
        circular_holidays[-1]

def test_large_index():
    """
    Test that an index larger than the list length raises an IndexError.
    """
    with pytest.raises(IndexError):
        circular_holidays[len(circular_holidays)]

def test_non_string_element():
    """
    Test that a non-string element in the list raises a TypeError.
    """
    mixed_list = ["Eclipse Festival", 123, "Starlit Celebration"]
    with pytest.raises(TypeError):
        next_holiday = [mixed_list[0], mixed_list[1]][0]
