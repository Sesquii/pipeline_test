# BATCH8_PROMPT6_Granite.py

class GlobalCalculator:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(GlobalCalculator, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def add(self, a, b):
        """Adds two numbers."""
        return a + b

    def subtract(self, a, b):
        """Subtracts second number from the first."""
        return a - b

    def multiply(self, a, b):
        """Multiplies two numbers."""
        return a * b

    def divide(self, a, b):
        """Divides the first number by the second (returns float)."""
        if b != 0:
            return a / b
        else:
            raise ValueError("Cannot divide by zero.")

def main():
    # Demonstrating singleton behavior
    calc1 = GlobalCalculator()
    calc2 = GlobalCalculator()

    assert calc1 is calc2, "GlobalCalculator should be a singleton"

    print(f"5 + 3 = {calc1.add(5, 3)}")
    print(f"7 - 2 = {calc1.subtract(7, 2)}")
    print(f"4 * 6 = {calc1.multiply(4, 6)}")
    try:
        print(f"8 / 0 = {calc1.divide(8, 0)}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()

# ===== GENERATED TESTS =====
```python
# BATCH8_PROMPT6_Granite.py

class GlobalCalculator:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(GlobalCalculator, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def add(self, a: int, b: int) -> int:
        """Adds two numbers."""
        return a + b

    def subtract(self, a: int, b: int) -> int:
        """Subtracts second number from the first."""
        return a - b

    def multiply(self, a: int, b: int) -> int:
        """Multiplies two numbers."""
        return a * b

    def divide(self, a: float, b: float) -> float:
        """Divides the first number by the second (returns float)."""
        if b != 0:
            return a / b
        else:
            raise ValueError("Cannot divide by zero.")

def main():
    # Demonstrating singleton behavior
    calc1 = GlobalCalculator()
    calc2 = GlobalCalculator()

    assert calc1 is calc2, "GlobalCalculator should be a singleton"

    print(f"5 + 3 = {calc1.add(5, 3)}")
    print(f"7 - 2 = {calc1.subtract(7, 2)}")
    print(f"4 * 6 = {calc1.multiply(4, 6)}")
    try:
        print(f"8 / 0 = {calc1.divide(8, 0)}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()

# Test suite for BATCH8_PROMPT6_Granite.py

import pytest
from BATCH8_PROMPT6_Granite import GlobalCalculator

@pytest.fixture
def calculator():
    return GlobalCalculator()

def test_singleton(calculator):
    """Test that the GlobalCalculator is a singleton."""
    calc2 = GlobalCalculator()
    assert calculator is calc2, "GlobalCalculator should be a singleton"

def test_add(calculator):
    """Test the add method with positive numbers."""
    result = calculator.add(5, 3)
    assert result == 8, f"Expected 8, got {result}"

def test_subtract(calculator):
    """Test the subtract method with positive numbers."""
    result = calculator.subtract(7, 2)
    assert result == 5, f"Expected 5, got {result}"

def test_multiply(calculator):
    """Test the multiply method with positive numbers."""
    result = calculator.multiply(4, 6)
    assert result == 24, f"Expected 24, got {result}"

def test_divide(calculator):
    """Test the divide method with positive numbers."""
    result = calculator.divide(8, 2)
    assert result == 4.0, f"Expected 4.0, got {result}"

def test_divide_by_zero(calculator):
    """Test the divide method with division by zero."""
    with pytest.raises(ValueError) as exc_info:
        calculator.divide(8, 0)
    assert str(exc_info.value) == "Cannot divide by zero."

# Additional tests for edge cases
def test_add_negative_numbers(calculator):
    """Test the add method with negative numbers."""
    result = calculator.add(-5, -3)
    assert result == -8, f"Expected -8, got {result}"

def test_subtract_negative_numbers(calculator):
    """Test the subtract method with negative numbers."""
    result = calculator.subtract(7, -2)
    assert result == 9, f"Expected 9, got {result}"

def test_multiply_negative_numbers(calculator):
    """Test the multiply method with negative numbers."""
    result = calculator.multiply(-4, 6)
    assert result == -24, f"Expected -24, got {result}"

def test_divide_negative_numbers(calculator):
    """Test the divide method with negative numbers."""
    result = calculator.divide(-8, 2)
    assert result == -4.0, f"Expected -4.0, got {result}"
```