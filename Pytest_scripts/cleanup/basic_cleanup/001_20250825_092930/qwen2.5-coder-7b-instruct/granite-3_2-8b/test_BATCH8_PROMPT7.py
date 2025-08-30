# BATCH8_PROMPT7_Granite.py

from abc import ABC, abstractmethod


class OperationStrategy(ABC):
    @abstractmethod
    def calculate(self, a: float, b: float) -> float:
        pass


class AddStrategy(OperationStrategy):
    def calculate(self, a: float, b: float) -> float:
        return a + b


class SubtractStrategy(OperationStrategy):
    def calculate(self, a: float, b: float) -> float:
        return a - b


class Calculator:
    def __init__(self, operation_strategy: OperationStrategy):
        self.operation_strategy = operation_strategy

    def execute(self, a: float, b: float) -> float:
        return self.operation_strategy.calculate(a, b)


if __name__ == "__main__":
    # Example usage of the Calculator class with different strategies
    add_calc = Calculator(AddStrategy())
    subtract_calc = Calculator(SubtractStrategy())

    print("Addition result:", add_calc.execute(5, 3))  # Should output: Addition result: 8
    print("Subtraction result:", subtract_calc.execute(5, 3))  # Should output: Subtraction result: 2

# ===== GENERATED TESTS =====
# BATCH8_PROMPT7_Granite.py

from abc import ABC, abstractmethod


class OperationStrategy(ABC):
    @abstractmethod
    def calculate(self, a: float, b: float) -> float:
        pass


class AddStrategy(OperationStrategy):
    def calculate(self, a: float, b: float) -> float:
        return a + b


class SubtractStrategy(OperationStrategy):
    def calculate(self, a: float, b: float) -> float:
        return a - b


class Calculator:
    def __init__(self, operation_strategy: OperationStrategy):
        self.operation_strategy = operation_strategy

    def execute(self, a: float, b: float) -> float:
        return self.operation_strategy.calculate(a, b)


if __name__ == "__main__":
    # Example usage of the Calculator class with different strategies
    add_calc = Calculator(AddStrategy())
    subtract_calc = Calculator(SubtractStrategy())

    print("Addition result:", add_calc.execute(5, 3))  # Should output: Addition result: 8
    print("Subtraction result:", subtract_calc.execute(5, 3))  # Should output: Subtraction result: 2


# BATCH8_PROMPT7_Granite_test.py

import pytest
from BATCH8_PROMPT7_Granite import OperationStrategy, AddStrategy, SubtractStrategy, Calculator


@pytest.fixture(params=[AddStrategy(), SubtractStrategy()])
def calculator(request):
    return Calculator(request.param)


def test_calculator_add(calculator: Calculator) -> None:
    """Test the addition functionality of the Calculator class."""
    result = calculator.execute(5, 3)
    assert result == 8, f"Expected 8, but got {result}"


def test_calculator_subtract(calculator: Calculator) -> None:
    """Test the subtraction functionality of the Calculator class."""
    result = calculator.execute(5, 3)
    assert result == 2, f"Expected 2, but got {result}"


def test_calculator_add_negative_numbers(calculator: Calculator) -> None:
    """Test the addition functionality with negative numbers."""
    result = calculator.execute(-5, -3)
    assert result == -8, f"Expected -8, but got {result}"


def test_calculator_subtract_negative_numbers(calculator: Calculator) -> None:
    """Test the subtraction functionality with negative numbers."""
    result = calculator.execute(-5, -3)
    assert result == -2, f"Expected -2, but got {result}"


def test_calculator_add_zero(calculator: Calculator) -> None:
    """Test the addition functionality with zero."""
    result = calculator.execute(0, 0)
    assert result == 0, f"Expected 0, but got {result}"


def test_calculator_subtract_zero(calculator: Calculator) -> None:
    """Test the subtraction functionality with zero."""
    result = calculator.execute(0, 0)
    assert result == 0, f"Expected 0, but got {result}"


def test_calculator_add_mixed_numbers(calculator: Calculator) -> None:
    """Test the addition functionality with mixed positive and negative numbers."""
    result = calculator.execute(-5, 3)
    assert result == -2, f"Expected -2, but got {result}"


def test_calculator_subtract_mixed_numbers(calculator: Calculator) -> None:
    """Test the subtraction functionality with mixed positive and negative numbers."""
    result = calculator.execute(5, -3)
    assert result == 8, f"Expected 8, but got {result}"
