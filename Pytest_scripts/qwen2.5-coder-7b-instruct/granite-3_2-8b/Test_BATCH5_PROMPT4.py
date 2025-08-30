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

# ===== GENERATED TESTS =====
```python
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

# BATCH5_PROMPT4_Granite_test.py

import pytest
from typing import List, Type
from BATCH5_PROMPT4_Granite import Operation, Add, Subtract, Multiply, Divide, Calculator

# Test cases for the Operation class and its subclasses

def test_operation_subclass():
    """Test that subclasses of Operation are instances of Operation"""
    assert issubclass(Add, Operation)
    assert issubclass(Subtract, Operation)
    assert issubclass(Multiply, Operation)
    assert issubclass(Divide, Operation)


def test_add_perform():
    """Test the perform method of Add class"""
    add = Add(5)
    assert add.perform() == 5


def test_subtract_perform():
    """Test the perform method of Subtract class"""
    subtract = Subtract(3)
    assert subtract.perform() == -3


def test_multiply_perform():
    """Test the perform method of Multiply class"""
    multiply = Multiply(4)
    assert multiply.perform() == 8


def test_divide_perform():
    """Test the perform method of Divide class with non-zero value"""
    divide_non_zero = Divide(2)
    assert divide_non_zero.perform() == 0.5

    # Test the perform method of Divide class with zero value
    with pytest.raises(ZeroDivisionError):
        divide_zero = Divide(0)
        divide_zero.perform()


# Test cases for the Calculator class

def test_calculator_init():
    """Test the initialization of Calculator class"""
    calc = Calculator()
    assert isinstance(calc, Calculator)
    assert len(calc.operations) == 0


def test_calculator_add_operation():
    """Test adding operations to Calculator"""
    calc = Calculator()
    add = Add(5)
    subtract = Subtract(3)
    multiply = Multiply(2)

    calc.add_operation(add)
    calc.add_operation(subtract)
    calc.add_operation(multiply)

    assert len(calc.operations) == 3
    assert isinstance(calc.operations[0], Add)
    assert isinstance(calc.operations[1], Subtract)
    assert isinstance(calc.operations[2], Multiply)


def test_calculator_calculate():
    """Test the calculate method of Calculator"""
    calc = Calculator([Subtract(5), Add(10), Multiply(2)])
    result = calc.calculate()
    assert result == 7


def test_calculator_calculate_with_empty_operations():
    """Test the calculate method with no operations"""
    calc = Calculator()
    result = calc.calculate()
    assert result == 0
```