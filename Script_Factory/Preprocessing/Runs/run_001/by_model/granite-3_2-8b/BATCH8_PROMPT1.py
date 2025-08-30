#!/usr/bin/env python3

import argparse
import sys


class UnitConverter:
    """Base class for unit converters"""

    def convert(self, value):
        raise NotImplementedError("Subclasses should implement this")


class MilesToKilometers(UnitConverter):
    """Converts miles to kilometers"""

    def __init__(self):
        self.mile_to_km = 1.60934

    def convert(self, value):
        return value * self.mile_to_km


class CelsiusToFahrenheit(UnitConverter):
    """Converts Celsius to Fahrenheit"""

    def __init__(self):
        self.celsius_to_fahrenheit = 9 / 5

    def convert(self, value):
        return value * self.celsius_to_fahrenheit + 32


class ChainConverter:
    """A class to chain together multiple unit converters"""

    def __init__(self, converters):
        self.converters = converters

    def convert(self, value):
        for conv in self.converters:
            value = conv.convert(value)
        return value


def main():
    parser = argparse.ArgumentParser(description="Unit Converter")
    parser.add_argument("value", type=float, help="The value to convert")
    parser.add_argument("conversion", choices=["miles2km", "celsius2fahrenheit"], help="Conversion type")

    args = parser.parse_args()

    if args.conversion == "miles2km":
        converters = [MilesToKilometers()]
    elif args.conversion == "celsius2fahrenheit":
        converters = [CelsiusToFahrenheit()]

    chain_converter = ChainConverter(converters)
    result = chain_converter.convert(args.value)

    print(f"{args.value} {args.conversion} is {result}")


if __name__ == "__main__":
    main()