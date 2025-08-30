# BATCH4_PROMPT4_Granite.py

class Operation:
    def __init__(self, value):
        self.value = value

    def perform(self):
        raise NotImplementedError("Subclasses must implement this method")


class Add(Operation):
    def perform(self):
        return self.value + 1


class Subtract(Operation):
    def perform(self):
        return self.value - 1


class Calculator:
    def __init__(self, initial_value=0):
        self.operations = [Add(initial_value)]

    def add_operation(self, operation_type='Add', value=1):
        new_op = globals()[f"{operation_type.capitalize()}"]() if operation_type.lower() in ['add', 'subtract'] else None

        if new_op:
            self.operations.append(new_op)

    def calculate(self):
        result = self.operations[0].value
        for op in self.operations[1:]:
            result = op.perform() + result  # Accumulate the results
        return result


if __name__ == "__main__":
    calc = Calculator(5)
    calc.add_operation('Subtract', 2)

    print("Result:", calc.calculate())  # Should output: Result: 4

# ===== GENERATED TESTS =====
```python
# BATCH4_PROMPT4_Granite.py

class Operation:
    def __init__(self, value):
        self.value = value

    def perform(self):
        raise NotImplementedError("Subclasses must implement this method")


class Add(Operation):
    def perform(self):
        return self.value + 1


class Subtract(Operation):
    def perform(self):
        return self.value - 1


class Calculator:
    def __init__(self, initial_value=0):
        self.operations = [Add(initial_value)]

    def add_operation(self, operation_type='Add', value=1):
        new_op = globals()[f"{operation_type.capitalize()}"]() if operation_type.lower() in ['add', 'subtract'] else None

        if new_op:
            self.operations.append(new_op)

    def calculate(self):
        result = self.operations[0].value
        for op in self.operations[1:]:
            result = op.perform() + result  # Accumulate the results
        return result


if __name__ == "__main__":
    calc = Calculator(5)
    calc.add_operation('Subtract', 2)

    print("Result:", calc.calculate())  # Should output: Result: 4

# BATCH4_PROMPT4_Granite_test.py

import pytest
from typing import List, Tuple
from BATCH4_PROMPT4_Granite import Operation, Add, Subtract, Calculator


@pytest.fixture(params=[Add(1), Subtract(1)])
def operation(request) -> Operation:
    return request.param


def test_operation_perform(operation: Operation):
    """
    Test the perform method of different operations.
    """
    assert isinstance(operation.perform(), int)


def test_calculator_initial_value():
    """
    Test the initial value of the Calculator class.
    """
    calc = Calculator(5)
    assert calc.calculate() == 5


def test_calculator_add_operation():
    """
    Test adding an operation to the Calculator class.
    """
    calc = Calculator(5)
    calc.add_operation('Subtract', 2)
    assert calc.calculate() == 4


def test_calculator_add_invalid_operation():
    """
    Test adding an invalid operation to the Calculator class.
    """
    calc = Calculator(5)
    with pytest.raises(AttributeError):
        calc.add_operation('Multiply', 2)


def test_calculator_with_no_operations():
    """
    Test the Calculator class with no operations.
    """
    calc = Calculator(0)
    assert calc.calculate() == 0


def test_calculator_with_multiple_operations():
    """
    Test the Calculator class with multiple operations.
    """
    calc = Calculator(5)
    calc.add_operation('Subtract', 2)
    calc.add_operation('Add', 3)
    assert calc.calculate() == 6
```