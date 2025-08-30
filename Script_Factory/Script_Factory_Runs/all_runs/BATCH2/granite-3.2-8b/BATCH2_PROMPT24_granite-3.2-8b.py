# BATCH2_PROMPT24_Granite.py

class Operation:
    def compute(self):
        raise NotImplementedError("Subclasses must implement this method")


class Add(Operation):
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def compute(self):
        return self.value1 + self.value2


class Subtract(Operation):
    def __init__(self, minuend, subtrahend):
        self.minuend = minuend
        self.subtrahend = subtrahend

    def compute(self):
        return self.minuend - self.subtrahend


class Calculator:
    def __init__(self):
        self.operations = []

    def add_operation(self, operation):
        self.operations.append(operation)

    def calculate(self):
        result = None

        for op in self.operations:
            if result is None:
                result = op.compute()
            else:
                result = op.compute()(result)

        return result


def main():
    calc = Calculator()

    add_op1 = Add(5, 3)
    subtract_op1 = Subtract(add_op1.compute(), 2)

    calc.add_operation(add_op1)
    calc.add_operation(subtract_op1)

    print("Result:", calc.calculate())


if __name__ == "__main__":
    main()