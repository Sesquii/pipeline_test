import sys

# Base class for all conversion classes
class Conversion:
    def convert(self):
        pass

# Specific conversions defined as subclasses inheriting from Conversion
class MilesToKilometers(Conversion):
    def convert(self, value):
        return value * 1.60934

class KilometersToMiles(Conversion):
    def convert(self, value):
        return value / 1.60934

class CelsiusToFahrenheit(Conversion):
    def convert(self, value):
        return (value * 9/5) + 32

class FahrenheitToCelsius(Conversion):
    def convert(self, value):
        return (value - 32) * 5/9

# Conversion chain using composition
class ConversionChain:
    def __init__(self, conversion_list):
        self.conversion_list = conversion_list

    def execute(self, value):
        for conversion in self.conversion_list:
            value = conversion.convert(value)
        return value

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python BATCH8_PROMPT1_{{model_name}}.py <value> <from_unit> <to_unit>")
        sys.exit(1)

    value = float(sys.argv[1])
    from_unit = sys.argv[2]
    to_unit = sys.argv[3]

    conversion_map = {
        ('miles', 'kilometers'): MilesToKilometers(),
        ('kilometers', 'miles'): KilometersToMiles(),
        ('celsius', 'fahrenheit'): CelsiusToFahrenheit(),
        ('fahrenheit', 'celsius'): FahrenheitToCelsius()
    }

    if (from_unit, to_unit) in conversion_map:
        conversion = ConversionChain([conversion_map[(from_unit, to_unit)]])
        result = conversion.execute(value)
        print(f"{value} {from_unit} is {result:.2f} {to_unit}")
    else:
        print("Unsupported conversion type")