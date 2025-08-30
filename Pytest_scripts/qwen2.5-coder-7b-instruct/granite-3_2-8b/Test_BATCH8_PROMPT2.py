# BATCH8_PROMPT2_Granite.py

import sys


class StringManipulator:
    """Base class for string manipulation operations"""

    def manipulate(self, input_string):
        """Abstract method to be overridden by subclasses"""
        raise NotImplementedError("Subclasses must implement this method")


class StringReverser(StringManipulator):
    """Class to reverse a given string"""

    def manipulate(self, input_string):
        return input_string[::-1]


class CaseConverter(StringManipulator):
    """Class to convert string case"""

    def __init__(self, mode='upper'):
        self.mode = mode

    def manipulate(self, input_string):
        if self.mode == 'upper':
            return input_string.upper()
        elif self.mode == 'lower':
            return input_string.lower()
        else:
            raise ValueError("Invalid case conversion mode. Use 'upper' or 'lower'.")


class StringConcatenator(StringManipulator):
    """Class to concatenate strings"""

    def __init__(self, prefix='', suffix=''):
        self.prefix = prefix
        self.suffix = suffix

    def manipulate(self, input_string):
        return f"{self.prefix}{input_string}{self.suffix}"


def chain_manipulations(*operations):
    """Function to chain multiple string manipulators"""
    current_string = ''

    for op in operations:
        current_string = op().manipulate(current_string)

    return current_string


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python BATCH8_PROMPT2_Granite.py <input_string>")
        sys.exit(1)

    input_string = sys.argv[1]

    # Example of chaining operations
    reverser = StringReverser()
    converter = CaseConverter('upper')
    concatenator = StringConcatenator(prefix='Pre_', suffix='_Post')

    result = chain_manipulations(reverser, converter, concatenator)

    print("Result:", result)

# ===== GENERATED TESTS =====
```python
# BATCH8_PROMPT2_Granite.py

import sys


class StringManipulator:
    """Base class for string manipulation operations"""

    def manipulate(self, input_string):
        """Abstract method to be overridden by subclasses"""
        raise NotImplementedError("Subclasses must implement this method")


class StringReverser(StringManipulator):
    """Class to reverse a given string"""

    def manipulate(self, input_string):
        return input_string[::-1]


class CaseConverter(StringManipulator):
    """Class to convert string case"""

    def __init__(self, mode='upper'):
        self.mode = mode

    def manipulate(self, input_string):
        if self.mode == 'upper':
            return input_string.upper()
        elif self.mode == 'lower':
            return input_string.lower()
        else:
            raise ValueError("Invalid case conversion mode. Use 'upper' or 'lower'.")


class StringConcatenator(StringManipulator):
    """Class to concatenate strings"""

    def __init__(self, prefix='', suffix=''):
        self.prefix = prefix
        self.suffix = suffix

    def manipulate(self, input_string):
        return f"{self.prefix}{input_string}{self.suffix}"


def chain_manipulations(*operations):
    """Function to chain multiple string manipulators"""
    current_string = ''

    for op in operations:
        current_string = op().manipulate(current_string)

    return current_string


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python BATCH8_PROMPT2_Granite.py <input_string>")
        sys.exit(1)

    input_string = sys.argv[1]

    # Example of chaining operations
    reverser = StringReverser()
    converter = CaseConverter('upper')
    concatenator = StringConcatenator(prefix='Pre_', suffix='_Post')

    result = chain_manipulations(reverser, converter, concatenator)

    print("Result:", result)


# Test suite for BATCH8_PROMPT2_Granite.py

import pytest
from typing import List


@pytest.fixture(params=['hello', 'WORLD', 'Python3.8'])
def input_string(request) -> str:
    """Fixture to provide different input strings"""
    return request.param


@pytest.fixture(params=[StringReverser, CaseConverter, StringConcatenator])
def manipulator_class(request):
    """Fixture to provide different string manipulator classes"""
    return request.param


def test_manipulators(manipulator_class: type, input_string: str) -> None:
    """Test cases for the string manipulator classes"""
    manipulator = manipulator_class()
    result = manipulator.manipulate(input_string)
    assert isinstance(result, str)


def test_case_converter_mode_upper(input_string: str) -> None:
    """Test case for CaseConverter with mode 'upper'"""
    converter = CaseConverter('upper')
    result = converter.manipulate(input_string)
    assert result == input_string.upper()


def test_case_converter_mode_lower(input_string: str) -> None:
    """Test case for CaseConverter with mode 'lower'"""
    converter = CaseConverter('lower')
    result = converter.manipulate(input_string)
    assert result == input_string.lower()


def test_case_converter_invalid_mode() -> None:
    """Test case for CaseConverter with invalid mode"""
    with pytest.raises(ValueError):
        converter = CaseConverter('invalid')


def test_string_concatenator_with_prefix_suffix(input_string: str) -> None:
    """Test case for StringConcatenator with prefix and suffix"""
    concatenator = StringConcatenator(prefix='Pre_', suffix='_Post')
    result = concatenator.manipulate(input_string)
    assert result == f"Pre_{input_string}_Post"


def test_chain_manipulations_with_multiple_operations(input_string: str) -> None:
    """Test case for chaining multiple string manipulators"""
    reverser = StringReverser()
    converter = CaseConverter('upper')
    concatenator = StringConcatenator(prefix='Pre_', suffix='_Post')

    result = chain_manipulations(reverser, converter, concatenator)
    expected_result = f"Pre_{input_string[::-1].upper()}_Post"
    assert result == expected_result


def test_chain_manipulations_with_empty_operations(input_string: str) -> None:
    """Test case for chaining multiple string manipulators with empty operations"""
    result = chain_manipulations()
    assert result == ''
```