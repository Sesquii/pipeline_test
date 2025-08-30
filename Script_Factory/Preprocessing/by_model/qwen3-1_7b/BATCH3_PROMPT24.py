```python
import sys

class Add:
    def __init__(self, value):
        self.value = value

    def apply(self, other):
        return self.value + other


class Subtract:
    def __init__(self, value):
        self.value = value

    def apply(self, other):
        return other - self.value


class Multiply:
    def __init__(self, factor):
        self.factor = factor

    def apply(self, other):
        return other * self.factor


class Calculator:
    def __init__(self):
        self.ops = []

    def add(self, value):
        self.ops.append(Add(value))
        return self

    def subtract(self, value):
        self.ops.append(Subtract(value))
        return self

    def multiply(self, factor):
        self.ops.append(Multiply(factor))
        return self

    def calculate(self):
        result = 0
        for op in self.ops:
            if isinstance(op, Add):
                result += op.value
            elif isinstance(op, Subtract):
                result -= op.value
            elif isinstance(op, Multiply):
                result *= op.factor
        return result


if __name__ == "__main__":
    calc = Calculator()
    calc.add(5).subtract(2).multiply(3).add(4)
    print("Result:", calc.calculate())