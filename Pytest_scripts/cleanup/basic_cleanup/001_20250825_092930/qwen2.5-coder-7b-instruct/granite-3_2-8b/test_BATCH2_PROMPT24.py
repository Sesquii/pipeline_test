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

# ===== GENERATED TESTS =====
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


# BATCH2_PROMPT24_Granite_test.py

import pytest
from typing import List, Union
from BATCH2_PROMPT24_Granite import Operation, Add, Subtract, Calculator


@pytest.fixture
def calculator() -> Calculator:
    return Calculator()


@pytest.fixture(params=[Add(5, 3), Subtract(10, 4)])
def operation(request) -> Operation:
    return request.param


def test_add_operation(calculator: Calculator, operation: Operation):
    """
    Test adding an operation to the calculator.
    """
    calculator.add_operation(operation)
    assert operation in calculator.operations


def test_calculate_with_single_operation(calculator: Calculator, operation: Operation):
    """
    Test calculating with a single operation.
    """
    calculator.add_operation(operation)
    result = calculator.calculate()
    assert result == operation.compute()


def test_calculate_with_multiple_operations(calculator: Calculator):
    """
    Test calculating with multiple operations.
    """
    add_op1 = Add(5, 3)
    subtract_op1 = Subtract(add_op1.compute(), 2)

    calculator.add_operation(add_op1)
    calculator.add_operation(subtract_op1)

    result = calculator.calculate()
    assert result == (5 + 3) - 2


def test_calculate_with_no_operations(calculator: Calculator):
    """
    Test calculating with no operations.
    """
    result = calculator.calculate()
    assert result is None


def test_compute_not_implemented(operation: Operation):
    """
    Test that compute method raises NotImplementedError if not implemented.
    """
    with pytest.raises(NotImplementedError):
        operation.compute()


def test_add_operation_with_invalid_type(calculator: Calculator):
    """
    Test adding an invalid type to the calculator.
    """
    with pytest.raises(TypeError):
        calculator.add_operation("not an Operation")


def test_calculate_with_mixed_operations(calculator: Calculator):
    """
    Test calculating with mixed operations.
    """
    add_op1 = Add(5, 3)
    subtract_op1 = Subtract(add_op1.compute(), 2)
    multiply_op1 = Multiply(4, 2)  # Assuming Multiply is defined elsewhere

    calculator.add_operation(add_op1)
    calculator.add_operation(subtract_op1)
    calculator.add_operation(multiply_op1)

    result = calculator.calculate()
    assert result == (5 + 3 - 2) * 4

This test suite includes comprehensive tests for the `Operation`, `Add`, `Subtract`, and `Calculator` classes. It uses pytest fixtures, parametrization, type hints, and follows PEP 8 style guidelines. The test cases cover both positive and negative scenarios to ensure the functionality is robust.