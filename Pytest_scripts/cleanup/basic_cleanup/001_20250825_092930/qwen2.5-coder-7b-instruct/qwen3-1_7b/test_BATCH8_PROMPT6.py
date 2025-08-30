class GlobalCalculator:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def add(self, a, b):
        """Add two numbers."""
        return a + b

    def subtract(self, a, b):
        """Subtract the second number from the first."""
        return a - b

    def multiply(self, a, b):
        """Multiply two numbers."""
        return a * b

    def divide(self, a, b):
        """Divide the first number by the second. Raises ValueError if division by zero."""
        if b == 0:
            raise ValueError("Division by zero")
        return a / b

if __name__ == "__main__":
    calc1 = GlobalCalculator()
    print(f"First instance: {calc1}")
    calc2 = GlobalCalculator()
    print(f"Second instance: {calc2} (same as first instance)")
    try:
        result = calc1.divide(10, 0)
        print(f"Divide 10 by 0: {result}")
    except ValueError as e:
        print(f"Error: {e}")

# ===== GENERATED TESTS =====
import pytest

class GlobalCalculator:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def add(self, a: int, b: int) -> int:
        """Add two numbers."""
        return a + b

    def subtract(self, a: int, b: int) -> int:
        """Subtract the second number from the first."""
        return a - b

    def multiply(self, a: int, b: int) -> int:
        """Multiply two numbers."""
        return a * b

    def divide(self, a: float, b: float) -> float:
        """Divide the first number by the second. Raises ValueError if division by zero."""
        if b == 0:
            raise ValueError("Division by zero")
        return a / b

if __name__ == "__main__":
    calc1 = GlobalCalculator()
    print(f"First instance: {calc1}")
    calc2 = GlobalCalculator()
    print(f"Second instance: {calc2} (same as first instance)")
    try:
        result = calc1.divide(10, 0)
        print(f"Divide 10 by 0: {result}")
    except ValueError as e:
        print(f"Error: {e}")

# Test cases
def test_add():
    """Test the add method."""
    calc = GlobalCalculator()
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0

def test_subtract():
    """Test the subtract method."""
    calc = GlobalCalculator()
    assert calc.subtract(5, 3) == 2
    assert calc.subtract(0, 0) == 0

def test_multiply():
    """Test the multiply method."""
    calc = GlobalCalculator()
    assert calc.multiply(4, 3) == 12
    assert calc.multiply(-2, -3) == 6

def test_divide():
    """Test the divide method."""
    calc = GlobalCalculator()
    assert calc.divide(8, 2) == 4.0
    assert calc.divide(0, 5) == 0.0

def test_divide_by_zero():
    """Test division by zero."""
    calc = GlobalCalculator()
    with pytest.raises(ValueError):
        calc.divide(10, 0)

# Fixtures for testing the singleton behavior
@pytest.fixture(scope="module")
def calculator():
    return GlobalCalculator()

def test_singleton(calculator):
    """Test that the calculator is a singleton."""
    assert id(GlobalCalculator()) == id(calculator)
