#!/usr/bin/env python3

"""
Unnecessary Object-Oriented Calculator for Unit Conversion

This program demonstrates an overly complex approach to unit conversion
using object-oriented principles where they're not necessarily needed.
"""

import sys

class BaseConverter:
    """Base class for all converters"""
    def convert(self, value):
        raise NotImplementedError("Subclasses should implement this method")

class MilesToKilometers(BaseConverter):
    """Converts miles to kilometers"""
    def convert(self, value):
        return value * 1.60934

class KilometersToMiles(BaseConverter):
    """Converts kilometers to miles"""
    def convert(self, value):
        return value / 1.60934

class CelsiusToFahrenheit(BaseConverter):
    """Converts Celsius to Fahrenheit"""
    def convert(self, value):
        return (value * 9/5) + 32

class FahrenheitToCelsius(BaseConverter):
    """Converts Fahrenheit to Celsius"""
    def convert(self, value):
        return (value - 32) * 5/9

class ConversionChain:
    """Chains together converters using composition"""
    def __init__(self, converters=None):
        self.converters = converters if converters else []

    def add_converter(self, converter):
        """Adds a converter to the chain"""
        self.converters.append(converter)

    def convert(self, value):
        """Runs the conversion through all converters in chain"""
        for converter in self.converters:
            value = converter.convert(value)
        return value

def main():
    """Entry point for the program"""
    if len(sys.argv) != 3:
        print("Usage: python BATCH8_PROMPT1_{model_name}.py <value> <conversion_type>")
        sys.exit(1)

    try:
        value = float(sys.argv[1])
        conversion_type = sys.argv[2].lower()
    except ValueError:
        print("Invalid input. Value must be a number.")
        sys.exit(1)

    # Create conversion chain based on requested conversion type
    if conversion_type == "miles_to_km":
        chain = ConversionChain([MilesToKilometers()])
    elif conversion_type == "km_to_miles":
        chain = ConversionChain([KilometersToMiles()])
    elif conversion_type == "celsius_to_fahrenheit":
        chain = ConversionChain([CelsiusToFahrenheit()])
    elif conversion_type == "fahrenheit_to_celsius":
        chain = ConversionChain([FahrenheitToCelsius()])
    else:
        print(f"Unknown conversion type: {conversion_type}")
        sys.exit(1)

    result = chain.convert(value)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()