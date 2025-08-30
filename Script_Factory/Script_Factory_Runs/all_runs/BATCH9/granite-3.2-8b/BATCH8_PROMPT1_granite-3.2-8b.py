# BATCH8_PROMPT1_Granite.py

import sys
import argparse

class UnitConverter:
    def __init__(self, value):
        self.value = value

    def convert(self):
        raise NotImplementedError("Subclasses must implement this method")


class MilesToKilometers(UnitConverter):
    def convert(self):
        return self.value * 1.60934


class KilometersToMiles(UnitConverter):
    def convert(self):
        return self.value / 1.60934


class CelsiusToFahrenheit(UnitConverter):
    def convert(self):
        return (self.value * 9/5) + 32


class FahrenheitToCelsius(UnitConverter):
    def convert(self):
        return (self.value - 32) * 5/9


def main():
    parser = argparse.ArgumentParser(description="Batch 8 Prompt 1: Unnecessary Object-Oriented Calculator")
    parser.add_argument("value", type=float, help="The value to be converted")
    parser.add_argument("conversion_type", choices=["miles_to_km", "km_to_miles", "celsius_to_fahrenheit", "fahrenheit_to_celsius"], help="Type of conversion")

    args = parser.parse_args()

    converter_map = {
        "miles_to_km": MilesToKilometers,
        "km_to_miles": KilometersToMiles,
        "celsius_to_fahrenheit": CelsiusToFahrenheit,
        "fahrenheit_to_celsius": FahrenheitToCelsius
    }

    if args.conversion_type in converter_map:
        ConverterClass = converter_map[args.conversion_type]
        converter = ConverterClass(args.value)
        print(f"{args.value} {args.conversion_type} is {converter.convert():.2f}")
    else:
        print("Invalid conversion type")


if __name__ == "__main__":
    main()