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

# ===== GENERATED TESTS =====
```python
# BATCH8_PROMPT1_Devstral.py

import sys

class MilesToKilometers:
    def __init__(self, miles):
        self.miles = miles

    def convert(self) -> float:
        """Converts miles to kilometers."""
        return self.miles * 1.60934

class CelsiusToFahrenheit:
    def __init__(self, celsius):
        self.celsius = celsius

    def convert(self) -> float:
        """Converts Celsius to Fahrenheit."""
        return (self.celsius * 9/5) + 32

# Example of chaining conversions
class MilesPerHourToKilometersPerHour:
    def __init__(self, mph_converter):
        self.mph_converter = mph_converter

    def convert(self) -> float:
        """Converts miles per hour to kilometers per hour."""
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

# Test suite for BATCH8_PROMPT1_Devstral.py

import pytest
from io import StringIO
import sys

def capture_output(func, *args):
    """Captures the output of a function."""
    old_stdout = sys.stdout
    new_stdout = StringIO()
    sys.stdout = new_stdout
    func(*args)
    output = new_stdout.getvalue()
    sys.stdout = old_stdout
    return output

# Test cases for MilesToKilometers class
def test_miles_to_kilometers_convert():
    converter = MilesToKilometers(5)
    assert converter.convert() == 8.0467, "Conversion from miles to kilometers is incorrect"

# Test cases for CelsiusToFahrenheit class
def test_celsius_to_fahrenheit_convert():
    converter = CelsiusToFahrenheit(32)
    assert converter.convert() == 89.6, "Conversion from Celsius to Fahrenheit is incorrect"

# Test cases for MilesPerHourToKilometersPerHour class
def test_mph_to_kph_convert():
    mph_converter = MilesToKilometers(5)
    converter = MilesPerHourToKilometersPerHour(mph_converter)
    assert converter.convert() == 8.0467, "Conversion from miles per hour to kilometers per hour is incorrect"

# Test cases for main function
def test_main_valid_conversion():
    sys.argv = ["python", "BATCH8_PROMPT1_Devstral.py", "5", "miles_to_km"]
    output = capture_output(main)
    assert "8.0467" in output, "Output does not contain the correct conversion result"

def test_main_invalid_conversion_type():
    sys.argv = ["python", "BATCH8_PROMPT1_Devstral.py", "5", "invalid_type"]
    output = capture_output(main)
    assert "Unknown conversion type: invalid_type" in output, "Output does not contain the correct error message"

def test_main_missing_arguments():
    sys.argv = ["python", "BATCH8_PROMPT1_Devstral.py"]
    output = capture_output(main)
    assert "Usage:" in output, "Output does not contain the correct usage message"
```