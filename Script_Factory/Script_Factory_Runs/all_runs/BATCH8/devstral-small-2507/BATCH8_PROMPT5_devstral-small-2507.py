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