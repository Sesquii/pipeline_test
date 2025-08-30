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

# ===== GENERATED TESTS =====
import pytest

# Original code remains unchanged as per requirement 1.

def test_calculator_add():
    """Test adding operations."""
    calc = Calculator()
    calc.add(5).add(3)
    assert calc.calculate() == 8


def test_calculator_subtract():
    """Test subtracting operations."""
    calc = Calculator()
    calc.subtract(2).subtract(1)
    assert calc.calculate() == -3


def test_calculator_multiply():
    """Test multiplying operations."""
    calc = Calculator()
    calc.multiply(2).multiply(3)
    assert calc.calculate() == 12


def test_calculator_mixed_operations():
    """Test mixed addition, subtraction, and multiplication operations."""
    calc = Calculator()
    calc.add(5).subtract(2).multiply(3).add(4)
    assert calc.calculate() == 20


def test_calculator_empty_ops():
    """Test calculator with no operations."""
    calc = Calculator()
    assert calc.calculate() == 0


def test_calculator_negative_values():
    """Test calculator with negative values."""
    calc = Calculator()
    calc.add(-5).subtract(3).multiply(-2)
    assert calc.calculate() == -16


def test_calculator_division_by_zero():
    """Test division by zero (should raise ValueError)."""
    calc = Calculator()
    calc.multiply(0)
    with pytest.raises(ValueError):
        calc.calculate()


# Test cases using fixtures and parametrization
@pytest.fixture(params=[Add, Subtract, Multiply])
def operation(request):
    return request.param


@pytest.mark.parametrize("value", [1, -1, 0, 100])
def test_operation_apply(operation, value):
    """Test the apply method of operations."""
    obj = operation(value)
    assert obj.apply(5) == (5 + value if isinstance(obj, Add) else
                          5 - value if isinstance(obj, Subtract) else
                          5 * value)


@pytest.mark.parametrize("factor", [1, -1, 0, 100])
def test_multiply_apply(factor):
    """Test the apply method of Multiply operation."""
    obj = Multiply(factor)
    assert obj.apply(5) == (5 * factor)


# Test cases with type hints
def test_calculator_type_hints():
    """Test type hints in Calculator class methods."""
    calc: Calculator = Calculator()
    result: int = calc.add(5).subtract(2).multiply(3).add(4).calculate()
    assert isinstance(result, int)
