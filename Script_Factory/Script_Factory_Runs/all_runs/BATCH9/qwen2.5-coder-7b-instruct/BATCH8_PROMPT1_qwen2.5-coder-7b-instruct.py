import sys

class Converter:
    def convert(self, value):
        raise NotImplementedError("This method should be overridden by subclasses")

class MilesToKilometers(Converter):
    def convert(self, value):
        return value * 1.60934

class KilometersToMiles(MilesToKilometers):
    def convert(self, value):
        return super().convert(value) ** -1

class CelsiusToFahrenheit(Converter):
    def convert(self, value):
        return (value * 9/5) + 32

class FahrenheitToCelsius(CelsiusToFahrenheit):
    def convert(self, value):
        return super().convert(value) ** -1

def get_converter(conversion_type):
    if conversion_type == "miles_to_km":
        return MilesToKilometers()
    elif conversion_type == "km_to_miles":
        return KilometersToMiles()
    elif conversion_type == "celsius_to_fahrenheit":
        return CelsiusToFahrenheit()
    elif conversion_type == "fahrenheit_to_celsius":
        return FahrenheitToCelsius()
    else:
        raise ValueError("Invalid conversion type")

def main():
    if len(sys.argv) != 3:
        print("Usage: python BATCH8_PROMPT1_{{model_name}}.py <value> <conversion_type>")
        sys.exit(1)

    value = float(sys.argv[1])
    conversion_type = sys.argv[2]

    converter = get_converter(conversion_type)
    result = converter.convert(value)
    print(f"{value} {conversion_type.replace('_', ' ').title()} is {result}")

if __name__ == "__main__":
    main()