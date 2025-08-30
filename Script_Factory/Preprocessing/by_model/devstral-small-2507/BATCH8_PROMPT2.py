#!/usr/bin/env python3

"""
Unnecessary Object-Oriented Calculator for String Manipulation

This program demonstrates an overly-complicated object-oriented approach to
performing simple string manipulations through method chaining.
"""

import sys

class StringReverser:
    """Reverses the input string."""
    def __init__(self, string):
        self.string = string

    def reverse(self):
        return self.string[::-1]

    def __str__(self):
        return self.reverse()

class CaseConverter:
    """Converts the case of the input string (upper to lower or vice versa)."""
    def __init__(self, string):
        self.string = string

    def convert_case(self):
        if self.string.islower():
            return self.string.upper()
        else:
            return self.string.lower()

    def __str__(self):
        return self.convert_case()

class StringConcatenator:
    """Concatenates a suffix to the input string."""
    def __init__(self, string, suffix="!"):
        self.string = string
        self.suffix = suffix

    def concatenate(self):
        return f"{self.string}{self.suffix}"

    def __str__(self):
        return self.concatenate()

class StringManipulator:
    """Main class to perform a series of string manipulations."""
    def __init__(self, input_string):
        self.input_string = input_string

    def manipulate(self):
        # Create chain of operations
        reversed_str = StringReverser(self.input_string).reverse()
        case_converted = CaseConverter(reversed_str).convert_case()
        final_result = StringConcatenator(case_converted, "!").concatenate()

        return final_result

def main():
    if len(sys.argv) != 2:
        print("Usage: python BATCH8_PROMPT2_Devstral.py <input_string>")
        sys.exit(1)

    input_string = sys.argv[1]
    manipulator = StringManipulator(input_string)
    result = manipulator.manipulate()
    print(result)

if __name__ == "__main__":
    main()