# BATCH3_PROMPT24_Granite.py

class CalculatorOperation:
    """Base class for all calculator operations"""

    def execute(self):
        raise NotImplementedError("Subclasses must implement this method")


class Add(CalculatorOperation):
    """Class to represent addition operation"""

    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def execute(self):
        return self.value1 + self.value2


class Subtract(CalculatorOperation):
    """Class to represent subtraction operation"""

    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def execute(self):
        return self.value1 - self.value2


class Calculator:
    """Main calculator class that chains operations together"""

    def __init__(self):
        self.operations = []

    def add_operation(self, operation):
        """Add an operation to the list of operations"""
        self.operations.append(operation)

    def calculate(self):
        """Execute all registered operations in sequence"""
        result = None
        for op in self.operations:
            if result is None:
                result = op.execute()
            else:
                result = op.execute() + result
        return result


def main():
    # Create calculator instance
    calc = Calculator()

    # Add addition operation (5 + 3)
    calc.add_operation(Add(5, 3))

    # Add subtraction operation ((5+3) - 1)
    calc.add_operation(Subtract(calc.calculate(), 1))

    print("The final result is:", calc.calculate())


if __name__ == "__main__":
    main()