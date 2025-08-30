```python
class Chain:
    def __init__(self, ops):
        self.ops = ops

    def calculate(self):
        result = None
        for op in self.ops:
            if result is None:
                result = op.calculate()
            else:
                result = op.calculate(result)
        return result


class Add:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate(self):
        return self.a + self.b


class Subtract:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate(self):
        return self.a - self.b


class Multiply:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate(self):
        return self.a * self.b


class Divide:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate(self):
        if self.b == 0:
            raise ValueError("Division by zero")
        return self.a / self.b


if __name__ == "__main__":
    add_op = Add(5, 3)
    multiply_op = Multiply(2)
    subtract_op = Subtract(10, 4)
    chain = Chain([add_op, multiply_op, subtract_op])
    result = chain.calculate()
    print(f"Result: {result}")