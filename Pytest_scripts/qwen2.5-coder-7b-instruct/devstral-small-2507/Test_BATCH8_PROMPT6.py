class GlobalCalculator:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(GlobalCalculator, cls).__new__(cls)
            # Initialize any instance-specific data here if needed
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
        """Divide the first number by the second. Return None if division by zero."""
        if b == 0:
            print("Error: Division by zero")
            return None
        return a / b

if __name__ == "__main__":
    # Create the first instance
    calc1 = GlobalCalculator()
    print(f"First instance ID: {id(calc1)}")

    # Attempt to create a second instance - should return the same object
    calc2 = GlobalCalculator()
    print(f"Second instance ID: {id(calc2)}")

    # Verify both variables point to the same object
    if id(calc1) == id(calc2):
        print("Singleton pattern confirmed: Both instances are the same.")
    else:
        print("Error: Instances are different!")

    # Demonstrate calculator functionality
    print("\nCalculator operations:")
    print(f"Addition: 5 + 3 = {calc1.add(5, 3)}")
    print(f"Subtraction: 10 - 4 = {calc1.subtract(10, 4)}")
    print(f"Multiplication: 7 * 6 = {calc1.multiply(7, 6)}")
    print(f"Division: 20 / 4 = {calc1.divide(20, 4)}")
    print(f"Division by zero: 5 / 0 = {calc1.divide(5, 0)}")

# ===== GENERATED TESTS =====
```python
import pytest

class GlobalCalculator:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(GlobalCalculator, cls).__new__(cls)
            # Initialize any instance-specific data here if needed
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

    def divide(self, a: float, b: float) -> float or None:
        """Divide the first number by the second. Return None if division by zero."""
        if b == 0:
            print("Error: Division by zero")
            return None
        return a / b

if __name__ == "__main__":
    # Create the first instance
    calc1 = GlobalCalculator()
    print(f"First instance ID: {id(calc1)}")

    # Attempt to create a second instance - should return the same object
    calc2 = GlobalCalculator()
    print(f"Second instance ID: {id(calc2)}")

    # Verify both variables point to the same object
    if id(calc1) == id(calc2):
        print("Singleton pattern confirmed: Both instances are the same.")
    else:
        print("Error: Instances are different!")

    # Demonstrate calculator functionality
    print("\nCalculator operations:")
    print(f"Addition: 5 + 3 = {calc1.add(5, 3)}")
    print(f"Subtraction: 10 - 4 = {calc1.subtract(10, 4)}")
    print(f"Multiplication: 7 * 6 = {calc1.multiply(7, 6)}")
    print(f"Division: 20 / 4 = {calc1.divide(20, 4)}")
    print(f"Division by zero: 5 / 0 = {calc1.divide(5, 0)}")

# Test cases
def test_singleton():
    calc1 = GlobalCalculator()
    calc2 = GlobalCalculator()
    assert id(calc1) == id(calc2), "Instances are different"

def test_addition():
    calc = GlobalCalculator()
    result = calc.add(5, 3)
    assert result == 8, f"Expected 8, got {result}"

def test_subtraction():
    calc = GlobalCalculator()
    result = calc.subtract(10, 4)
    assert result == 6, f"Expected 6, got {result}"

def test_multiplication():
    calc = GlobalCalculator()
    result = calc.multiply(7, 6)
    assert result == 42, f"Expected 42, got {result}"

@pytest.mark.parametrize("a, b, expected", [
    (20, 4, 5),
    (10, 3, 3.3333333333333335),  # Using float for division to handle floating point precision
])
def test_division(a: float, b: float, expected: float):
    calc = GlobalCalculator()
    result = calc.divide(a, b)
    assert result == expected, f"Expected {expected}, got {result}"

def test_division_by_zero():
    calc = GlobalCalculator()
    result = calc.divide(5, 0)
    assert result is None, "Expected None for division by zero"
```