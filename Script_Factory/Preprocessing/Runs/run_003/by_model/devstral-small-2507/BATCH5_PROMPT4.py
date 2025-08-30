# BATCH5_PROMPT4_Devstral.py

class Calculator:
    def calculate(self):
        raise NotImplementedError("Subclasses should implement this method")

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
        if b == 0:
            raise ValueError("Cannot divide by zero")
        self.a = a
        self.b = b

    def calculate(self):
        return self.a / self.b

# Example of composition and chaining operations
class ComplexCalculator(Calculator):
    def __init__(self, calculator1, calculator2):
        self.calculator1 = calculator1
        self.calculator2 = calculator2

    def calculate(self):
        first_result = self.calculator1.calculate()
        second_result = self.calculator2.calculate()
        return (first_result + second_result) / 2  # Example operation on results

if __name__ == "__main__":
    # Perform a simple calculation using the classes
    add_op = Add(5, 3)
    subtract_op = Subtract(10, 4)

    print("Addition result:", add_op.calculate())
    print("Subtraction result:", subtract_op.calculate())

    # Example of composition
    complex_calc = ComplexCalculator(add_op, subtract_op)
    print("Complex calculation result:", complex_calc.calculate())