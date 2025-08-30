```python
class Add:
    def __init__(self, operand1):
        self.operand1 = operand1

    def apply(self, operand2):
        return self.operand1 + operand2


class Subtract:
    def __init__(self, operand2):
        self.operand2 = operand2

    def apply(self, operand1):
        return operand1 - self.operand2


class Multiply:
    def __init__(self, operand):
        self.operand = operand

    def apply(self, value):
        return value * self.operand


class Chain:
    def __init__(self, operations):
        self.operations = operations

    def apply(self, initial_value):
        result = initial_value
        for op in self.operations:
            result = op.apply(result)
        return result


if __name__ == "__main__":
    chain = Chain([Add(5), Multiply(2), Subtract(1)])
    print(chain.apply(0))