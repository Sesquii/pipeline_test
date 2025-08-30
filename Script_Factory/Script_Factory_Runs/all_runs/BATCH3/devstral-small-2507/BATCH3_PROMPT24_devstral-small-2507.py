# BATCH3_PROMPT24_Devstral.py

class Calculator:
    def calculate(self):
        raise NotImplementedError("Subclasses should implement this method.")

class Add(Calculator):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate(self):
        return self.a + self.b

class Subtract(Calculator):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate(self):
        return self.a - self.b

class Multiply(Calculator):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate(self):
        return self.a * self.b

class Divide(Calculator):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate(self):
        if self.b == 0:
            raise ValueError("Cannot divide by zero")
        return self.a / self.b

# Example of chaining calculations using composition
class ChainCalculator(Calculator):
    def __init__(self, *calculators):
        self.calculators = calculators

    def calculate(self):
        result = 0
        for calc in self.calculators:
            result = calc.calculate()
        return result

if __name__ == "__main__":
    # Example usage: (5 + 3) * 2 - 4 / 2
    add = Add(5, 3)
    multiply = Multiply(add.calculate(), 2)
    divide = Divide(4, 2)
    final_calc = Subtract(multiply.calculate(), divide.calculate())

    print("Result:", final_calc.calculate())