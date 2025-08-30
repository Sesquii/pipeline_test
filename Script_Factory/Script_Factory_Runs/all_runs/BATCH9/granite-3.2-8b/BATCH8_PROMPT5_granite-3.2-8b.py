# BATCH8_PROMPT5_Granite.py

import functools
from abc import ABC, abstractmethod

class BaseCalculator(ABC):
    """Abstract base class for calculator."""

    @abstractmethod
    def calculate(self, a, b):
        pass


class SimpleCalculator(BaseCalculator):
    """A simple calculator that adds two numbers."""

    def calculate(self, a, b):
        return a + b


def logging_decorator(func):
    """Decorator to log the calculation process."""

    @functools.wraps(func)
    def wrapper(self, a, b):
        print(f"Calculating: {a} + {b}")
        result = func(self, a, b)
        print(f"Result: {result}")
        return result

    return wrapper


def caching_decorator(func):
    """Decorator to cache the results of calculations."""

    cache = {}

    @functools.wraps(func)
    def wrapper(self, a, b):
        key = f"{a}_{b}"
        if key not in cache:
            cache[key] = func(self, a, b)
        return cache[key]

    return wrapper


# Apply decorators to the SimpleCalculator class
SimpleCalculatorWithLogging = logging_decorator(SimpleCalculator)
SimpleCalculatorWithCaching = caching_decorator(logging_decorator(SimpleCalculator))


def main():
    # Initialize calculators with their respective decorators
    simple = SimpleCalculator()
    logged = SimpleCalculatorWithLogging()
    cached = SimpleCalculatorWithCaching()

    # Perform calculations
    print("Basic calculation:", simple.calculate(5, 3))
    print("Logged calculation:", logged.calculate(5, 3))
    print("Cached calculation:", cached.calculate(5, 3))
    print("Cached calculation (should be fetched from cache):", cached.calculate(5, 3))


if __name__ == "__main__":
    main()