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