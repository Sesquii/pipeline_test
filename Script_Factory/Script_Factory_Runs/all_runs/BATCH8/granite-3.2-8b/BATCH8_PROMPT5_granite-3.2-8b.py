# BATCH8_PROMPT5_Granite.py

from functools import wraps


class BaseCalculator:
    """Base Calculator class with a single method for addition."""

    def add(self, a, b):
        """Add two numbers."""
        return a + b


class LoggingDecorator:
    """Decorator that logs the addition operation."""

    def __init__(self, calculator):
        self.calculator = calculator

    @wraps(calculator.add)
    def add(self, a, b):
        print(f"Logging: Adding {a} and {b}")
        return self.calculator.add(a, b)


class CachingDecorator:
    """Decorator that caches the results of previous additions."""

    def __init__(self):
        self._cache = {}

    @wraps(BaseCalculator.add)
    def add(self, a, b):
        key = f"{a},{b}"
        if key in self._cache:
            print(f"Caching hit: Returning cached result for {a} + {b}")
            return self._cache[key]
        else:
            result = BaseCalculator().add(a, b)
            self._cache[key] = result
            print(f"Caching miss: Storing result {result} for {a} + {b}")
            return result


# Main execution block
if __name__ == "__main__":
    base_calculator = BaseCalculator()

    logging_calc = LoggingDecorator(base_calculator)
    caching_calc = CachingDecorator()

    print("Result with LoggingDecorator:")
    print(logging_calc.add(5, 3))

    print("\nResult with CachingDecorator:")
    print(caching_calc.add(5, 3))
    print(caching_calc.add(5, 3))