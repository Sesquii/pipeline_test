```python
# BATCH5_PROMPT4_example.py
from typing import List

class Operation:
    def apply(self, value: float) -> float:
        pass


class Add(Operation):
    def __init__(self, operand: float):
        self.operand = operand

    def apply(self, value: float) -> float:
        return value + self.operand


class Subtract(Operation):
    def __init__(self, operand: float):
        self.operand = operand

    def apply(self, value: float) -> float:
        return value - self.operand


class Multiply(Operation):
    def __init__(self, factor: float):
        self.factor = factor

    def apply(self, value: float) -> float:
        return value * self.factor


class Chain:
    def __init__(self):
        self.operations: List[Operation] = []

    def add(self, op: Operation):
        self.operations.append(op)

    def compute(self, value: float) -> float:
        result = value
        for op in self.operations:
            result = op.apply(result)
        return result


if __name__ == "__main__":
    chain = Chain()
    add_op = Add(5.0)
    mul_op = Multiply(2.0)
    chain.add(add_op)
    chain.add(mul_op)
    print(f"Result of (10 + 5) * 2: {chain.compute(10)}")