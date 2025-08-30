```python
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