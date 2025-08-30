# BATCH8_PROMPT1_Devstral.py

import sys

class MilesToKilometers:
    def __init__(self, miles):
        self.miles = miles

    def convert(self):
        return self.miles * 1.60934

class CelsiusToFahrenheit:
    def __init__(self, celsius):
        self.celsius = celsius

    def convert(self):
        return (self.celsius * 9/5) + 32

# Example of chaining conversions
class MilesPerHourToKilometersPerHour:
    def __init__(self, mph_converter):
        self.mph_converter = mph_converter

    def convert(self):
        km_per_hr = self.mph_converter.convert()
        return km_per_hr

def main():
    if len(sys.argv) != 3:
        print("Usage: python BATCH8_PROMPT1_Devstral.py <value> <conversion_type>")
        sys.exit(1)

    value = float(sys.argv[1])
    conversion_type = sys.argv[2]

    if conversion_type == "miles_to_km":
        converter = MilesToKilometers(value)
    elif conversion_type == "celsius_to_fahrenheit":
        converter = CelsiusToFahrenheit(value)
    elif conversion_type == "mph_to_kph":
        mph_converter = MilesToKilometers(value)
        converter = MilesPerHourToKilometersPerHour(mph_converter)
    else:
        print(f"Unknown conversion type: {conversion_type}")
        sys.exit(1)

    result = converter.convert()
    print(result)

if __name__ == "__main__":
    main()