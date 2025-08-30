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

# ===== GENERATED TESTS =====
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

# BATCH5_PROMPT4_example_test.py
from typing import List
import pytest

from BATCH5_PROMPT4_example import Operation, Add, Subtract, Multiply, Chain

def test_add_operation():
    """Test the Apply method of Add class"""
    add_op = Add(5.0)
    assert add_op.apply(10) == 15

def test_subtract_operation():
    """Test the Apply method of Subtract class"""
    sub_op = Subtract(3.0)
    assert sub_op.apply(10) == 7

def test_multiply_operation():
    """Test the Apply method of Multiply class"""
    mul_op = Multiply(2.0)
    assert mul_op.apply(5) == 10

def test_chain_compute():
    """Test the compute method of Chain class"""
    chain = Chain()
    add_op = Add(5.0)
    mul_op = Multiply(2.0)
    chain.add(add_op)
    chain.add(mul_op)
    assert chain.compute(10) == 30

def test_chain_with_negative_values():
    """Test the compute method of Chain class with negative values"""
    chain = Chain()
    add_op = Add(-5.0)
    mul_op = Multiply(-2.0)
    chain.add(add_op)
    chain.add(mul_op)
    assert chain.compute(10) == -30

def test_chain_with_no_operations():
    """Test the compute method of Chain class with no operations"""
    chain = Chain()
    assert chain.compute(10) == 10

@pytest.mark.parametrize("value, expected", [
    (10, 25),
    (-10, -5),
    (0, 5)
])
def test_add_operation_with_parametrization(value: float, expected: float):
    """Test the Apply method of Add class with parametrization"""
    add_op = Add(15.0)
    assert add_op.apply(value) == expected

@pytest.mark.parametrize("value, expected", [
    (10, 7),
    (-10, -13),
    (0, -3)
])
def test_subtract_operation_with_parametrization(value: float, expected: float):
    """Test the Apply method of Subtract class with parametrization"""
    sub_op = Subtract(3.0)
    assert sub_op.apply(value) == expected

@pytest.mark.parametrize("value, expected", [
    (10, 20),
    (-10, -20),
    (0, 0)
])
def test_multiply_operation_with_parametrization(value: float, expected: float):
    """Test the Apply method of Multiply class with parametrization"""
    mul_op = Multiply(2.0)
    assert mul_op.apply(value) == expected
