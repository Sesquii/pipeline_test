# BATCH2_PROMPT24_Devstral.py

class Operation:
    """Base class for all mathematical operations"""
    def __init__(self):
        pass

    def calculate(self):
        raise NotImplementedError("Subclasses should implement this method")

class Add(Operation):
    """Class to perform addition operation"""
    def __init__(self, a, b):
        super().__init__()
        self.a = a
        self.b = b

    def calculate(self):
        return self.a + self.b

class Subtract(Operation):
    """Class to perform subtraction operation"""
    def __init__(self, a, b):
        super().__init__()
        self.a = a
        self.b = b

    def calculate(self):
        return self.a - self.b

class Multiply(Operation):
    """Class to perform multiplication operation"""
    def __init__(self, a, b):
        super().__init__()
        self.a = a
        self.b = b

    def calculate(self):
        return self.a * self.b

class Divide(Operation):
    """Class to perform division operation"""
    def __init__(self, a, b):
        super().__init__()
        self.a = a
        self.b = b

    def calculate(self):
        if self.b == 0:
            raise ValueError("Cannot divide by zero")
        return self.a / self.b

class Calculator:
    """Class to chain operations together"""
    def __init__(self, first_operation):
        self.operations = [first_operation]

    def add_operation(self, operation):
        self.operations.append(operation)

    def calculate(self):
        result = self.operations[0].calculate()
        for op in self.operations[1:]:
            result = op.calculate()
        return result

if __name__ == "__main__":
    # Create operations
    add_op = Add(5, 3)
    subtract_op = Subtract(10, 4)
    multiply_op = Multiply(add_op.calculate(), subtract_op.calculate())
    divide_op = Divide(multiply_op.calculate(), 2)

    # Chain operations using Calculator class
    calculator = Calculator(divide_op)
    result = calculator.calculate()

    print(f"Result of the calculation: {result}")