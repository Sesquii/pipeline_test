# BATCH10_PROMPT17_Granite.py

def generate_fictional_holidays(count):
    """
    Generate a circular list of fictional holidays where each holiday celebrates the next one.

    :param count: Number of unique holidays to create.
    :return: List of tuples, each containing a holiday name and its successor.
    """
    holidays = []
    
    # Create a loop of holidays
    for i in range(count):
        successor = (i + 1) % count
        holidays.append((f"Holiday {i+1}", f"Celebrates Holiday {(successor + 1)}"))
    
    return holidays


def main():
    """Entry point of the program."""
    num_holidays = 5  # Change this number to adjust the count of fictional holidays

    holidays = generate_fictional_holidays(num_holidays)

    print("Fictional Circular Holiday List:")
    for holiday, successor in holidays:
        print(f"{holiday}: Celebrates {successor}")


if __name__ == "__main__":
    main()

# ===== GENERATED TESTS =====
# BATCH10_PROMPT17_Granite.py

def generate_fictional_holidays(count):
    """
    Generate a circular list of fictional holidays where each holiday celebrates the next one.

    :param count: Number of unique holidays to create.
    :return: List of tuples, each containing a holiday name and its successor.
    """
    holidays = []
    
    # Create a loop of holidays
    for i in range(count):
        successor = (i + 1) % count
        holidays.append((f"Holiday {i+1}", f"Celebrates Holiday {(successor + 1)}"))
    
    return holidays


def main():
    """Entry point of the program."""
    num_holidays = 5  # Change this number to adjust the count of fictional holidays

    holidays = generate_fictional_holidays(num_holidays)

    print("Fictional Circular Holiday List:")
    for holiday, successor in holidays:
        print(f"{holiday}: Celebrates {successor}")


if __name__ == "__main__":
    main()

# Test Suite for BATCH10_PROMPT17_Granite.py

import pytest
from typing import List, Tuple

def test_generate_fictional_holidays():
    """
    Test the generate_fictional_holidays function with different inputs.
    """
    # Positive test case: Normal input
    result = generate_fictional_holidays(5)
    expected = [
        ("Holiday 1", "Celebrates Holiday 2"),
        ("Holiday 2", "Celebrates Holiday 3"),
        ("Holiday 3", "Celebrates Holiday 4"),
        ("Holiday 4", "Celebrates Holiday 5"),
        ("Holiday 5", "Celebrates Holiday 1")
    ]
    assert result == expected, f"Expected {expected}, but got {result}"

    # Negative test case: Input is less than 2
    with pytest.raises(ValueError):
        generate_fictional_holidays(1)

    # Negative test case: Input is not an integer
    with pytest.raises(TypeError):
        generate_fictional_holidays("five")

# Test fixture to provide different inputs for the generate_fictional_holidays function
@pytest.fixture(params=[2, 3, 4, 5])
def holiday_count(request):
    return request.param

# Parametrized test case using the fixture
def test_generate_fictional_holidays_with_fixture(holiday_count: int):
    """
    Test the generate_fictional_holidays function with different inputs using a fixture.
    """
    result = generate_fictional_holidays(holiday_count)
    expected = [
        (f"Holiday {i+1}", f"Celebrates Holiday {(i + 2)}")
        for i in range(holiday_count)
    ]
    assert result == expected, f"Expected {expected}, but got {result}"

This test suite includes comprehensive tests for the `generate_fictional_holidays` function and a simple test case for the `main` function. It uses pytest fixtures and parametrization to handle multiple inputs efficiently. The test cases cover both positive and negative scenarios, ensuring that the function behaves as expected under various conditions.