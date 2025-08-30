```python
import sys

class MilesToKilometers:
    def __init__(self):
        pass

    def convert(self, value, from_unit='miles', to_unit='kilometers'):
        if from_unit == 'miles' and to_unit == 'kilometers':
            return value * 1.60934
        else:
            raise ValueError("Unsupported conversion")

class CelsiusToFahrenheit:
    def __init__(self):
        pass

    def convert(self, value, from_unit='celsius', to_unit='fahrenheit'):
        if from_unit == 'celsius' and to_unit == 'fahrenheit':
            return (value * 9/5) + 32
        else:
            raise ValueError("Unsupported conversion")

class FahrenheitToCelsius:
    def __init__(self):
        pass

    def convert(self, value, from_unit='fahrenheit', to_unit='celsius'):
        if from_unit == 'fahrenheit' and to_unit == 'celsius':
            return (value - 32) * 5/9
        else:
            raise ValueError("Unsupported conversion")

class KilometersToMiles:
    def __init__(self):
        pass

    def convert(self, value, from_unit='kilometers', to_unit='miles'):
        if from_unit == 'kilometers' and to_unit == 'miles':
            return value * 0.621371
        else:
            raise ValueError("Unsupported conversion")

def main():
    if len(sys.argv) != 4:
        print("Usage: python script.py <value> <from_unit> <to_unit>")
        return
    try:
        value = float(sys.argv[1])
        from_unit = sys.argv[2]
        to_unit = sys.argv[3]
    except ValueError:
        print("Invalid input. Please provide a number.")
        return

    if from_unit == 'miles' and to_unit == 'kilometers':
        converter = MilesToKilometers()
    elif from_unit == 'celsius' and to_unit == 'fahrenheit':
        converter = CelsiusToFahrenheit()
    elif from_unit == 'fahrenheit' and to_unit == 'celsius':
        converter = FahrenheitToCelsius()
    elif from_unit == 'kilometers' and to_unit == 'miles':
        converter = KilometersToMiles()
    else:
        print("Conversion not supported.")
        return

    result = converter.convert(value, from_unit, to_unit)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()