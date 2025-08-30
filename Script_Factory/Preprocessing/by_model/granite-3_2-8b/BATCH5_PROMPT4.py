# BATCH5_PROMPT4_Granite.py

class Operation:
    def __init__(self, value):
        self.value = value

    def perform(self):
        raise NotImplementedError("Subclasses must implement this method")


class Add(Operation):
    def perform(self):
        return self.value


class Subtract(Operation):
    def perform(self):
        return -self.value


class Multiply(Operation):
    def perform(self):
        return self.value * 2


class Divide(Operation):
    def perform(self):
        if self.value != 0:
            return 1 / self.value
        else:
            raise ZeroDivisionError("Cannot divide by zero")


class Calculator:
    def __init__(self, operations=[]):
        self.operations = operations

    def add_operation(self, operation):
        self.operations.append(operation)

    def calculate(self):
        result = 0
        for op in self.operations:
            result = op.perform() + result
        return result


def main():
    calc = Calculator([Subtract(5), Add(10), Multiply(2)])
    print("Result of calculation:", calc.calculate())


if __name__ == "__main__":
    main()