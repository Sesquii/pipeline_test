# BATCH8_PROMPT5_Devstral.py

class BaseCalculator:
    def calculate(self, x, y):
        """Basic calculation method that adds two numbers."""
        return x + y

class LoggingDecorator:
    def __init__(self, calculator):
        self._calculator = calculator

    def calculate(self, x, y):
        """Decorator that logs the calculation process and result."""
        print(f"LoggingDecorator: Calculating {x} + {y}")
        result = self._calculator.calculate(x, y)
        print(f"LoggingDecorator: Result is {result}")
        return result

class CachingDecorator:
    def __init__(self, calculator):
        self._calculator = calculator
        self._cache = {}

    def calculate(self, x, y):
        """Decorator that caches calculation results to avoid redundant calculations."""
        key = (x, y)
        if key in self._cache:
            print(f"CachingDecorator: Returning cached result for {key}")
            return self._cache[key]
        
        print(f"CachingDecorator: Performing new calculation for {key}")
        result = self._calculator.calculate(x, y)
        self._cache[key] = result
        return result

class ValidationDecorator:
    def __init__(self, calculator):
        self._calculator = calculator

    def calculate(self, x, y):
        """Decorator that validates input before calculation."""
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise ValueError("ValidationDecorator: Both inputs must be numbers")
        
        print(f"ValidationDecorator: Inputs are valid ({x}, {y})")
        return self._calculator.calculate(x, y)

def main():
    # Create the base calculator
    calculator = BaseCalculator()

    # Wrap it with decorators in a specific order
    calculator = ValidationDecorator(calculator)
    calculator = CachingDecorator(calculator) 
    calculator = LoggingDecorator(calculator)

    # Perform a calculation using the decorated calculator
    result = calculator.calculate(5, 3)
    print(f"Final Result: {result}")

if __name__ == "__main__":
    main()

# ===== GENERATED TESTS =====
```python
# BATCH8_PROMPT5_Devstral.py

class BaseCalculator:
    def calculate(self, x, y):
        """Basic calculation method that adds two numbers."""
        return x + y

class LoggingDecorator:
    def __init__(self, calculator):
        self._calculator = calculator

    def calculate(self, x, y):
        """Decorator that logs the calculation process and result."""
        print(f"LoggingDecorator: Calculating {x} + {y}")
        result = self._calculator.calculate(x, y)
        print(f"LoggingDecorator: Result is {result}")
        return result

class CachingDecorator:
    def __init__(self, calculator):
        self._calculator = calculator
        self._cache = {}

    def calculate(self, x, y):
        """Decorator that caches calculation results to avoid redundant calculations."""
        key = (x, y)
        if key in self._cache:
            print(f"CachingDecorator: Returning cached result for {key}")
            return self._cache[key]
        
        print(f"CachingDecorator: Performing new calculation for {key}")
        result = self._calculator.calculate(x, y)
        self._cache[key] = result
        return result

class ValidationDecorator:
    def __init__(self, calculator):
        self._calculator = calculator

    def calculate(self, x, y):
        """Decorator that validates input before calculation."""
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise ValueError("ValidationDecorator: Both inputs must be numbers")
        
        print(f"ValidationDecorator: Inputs are valid ({x}, {y})")
        return self._calculator.calculate(x, y)

def main():
    # Create the base calculator
    calculator = BaseCalculator()

    # Wrap it with decorators in a specific order
    calculator = ValidationDecorator(calculator)
    calculator = CachingDecorator(calculator) 
    calculator = LoggingDecorator(calculator)

    # Perform a calculation using the decorated calculator
    result = calculator.calculate(5, 3)
    print(f"Final Result: {result}")

if __name__ == "__main__":
    main()

# BATCH8_PROMPT5_Devstral_test.py

import pytest
from typing import Any, Callable, Tuple
from BATCH8_PROMPT5_Devstral import BaseCalculator, LoggingDecorator, CachingDecorator, ValidationDecorator

def test_base_calculator():
    calculator = BaseCalculator()
    assert calculator.calculate(2, 3) == 5
    assert calculator.calculate(-1, -1) == -2

def test_logging_decorator():
    class MockCalculator:
        def calculate(self, x, y):
            return x + y
    
    calculator = LoggingDecorator(MockCalculator())
    result = calculator.calculate(4, 6)
    assert result == 10
    # Check if the logging statements are printed (this is a bit tricky to test directly)

def test_caching_decorator():
    class MockCalculator:
        def calculate(self, x, y):
            return x + y
    
    calculator = CachingDecorator(MockCalculator())
    result1 = calculator.calculate(7, 8)
    assert result1 == 15
    result2 = calculator.calculate(7, 8)  # Should use cache
    assert result2 == 15

def test_validation_decorator():
    class MockCalculator:
        def calculate(self, x, y):
            return x + y
    
    calculator = ValidationDecorator(MockCalculator())
    with pytest.raises(ValueError):
        calculator.calculate("a", "b")
    
    result = calculator.calculate(9, 10)
    assert result == 19

def test_full_pipeline():
    calculator = BaseCalculator()
    calculator = ValidationDecorator(calculator)
    calculator = CachingDecorator(calculator) 
    calculator = LoggingDecorator(calculator)

    result = calculator.calculate(5, 3)
    assert result == 8
```