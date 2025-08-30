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