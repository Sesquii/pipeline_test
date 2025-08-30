# BATCH8_PROMPT5_Devstral.py

"""
Unnecessary Object-Oriented Calculator with Decorator Pattern

This program demonstrates the decorator pattern using an unnecessary 
object-oriented calculator that adds logging and caching functionality.
"""

class BaseCalculator:
    """Base calculator class with a single method to add numbers."""

    def add(self, x: float, y: float) -> float:
        """Add two numbers together."""
        return x + y

class LoggingDecorator:
    """Decorator that adds logging functionality."""

    def __init__(self, calculator):
        self._calculator = calculator

    def add(self, x: float, y: float) -> float:
        print(f"Logging: Adding {x} and {y}")
        result = self._calculator.add(x, y)
        print(f"Logging: Result is {result}")
        return result

class CachingDecorator:
    """Decorator that adds unnecessary caching functionality."""

    def __init__(self, calculator):
        self._calculator = calculator
        self._cache = {}

    def add(self, x: float, y: float) -> float:
        key = (x, y)
        if key in self._cache:
            print(f"Caching: Returning cached result for {key}: {self._cache[key]}")
            return self._cache[key]
        else:
            result = self._calculator.add(x, y)
            self._cache[key] = result
            print(f"Caching: Storing new result for {key}: {result}")
            return result

def main():
    """Entry point of the program."""
    # Create base calculator
    calculator = BaseCalculator()

    # Add decorators to the base calculator
    calculator = LoggingDecorator(calculator)
    calculator = CachingDecorator(calculator)

    # Perform some calculations
    print("\nFirst addition:")
    result1 = calculator.add(2, 3)

    print("\nSecond addition (same values - should use cache):")
    result2 = calculator.add(2, 3)

    print("\nThird addition (different values):")
    result3 = calculator.add(5, 7)

if __name__ == "__main__":
    main()