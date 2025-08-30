```python
# BATCH8_PROMPT5_Model1.py
from functools import wraps

class BaseCalculator:
    def calculate(self, a, b):
        """Simple calculation of sum of two numbers."""
        return a + b

class LoggingDecorator:
    """Decorator that logs the method call and result."""
    def __init__(self, func):
        self.func = func
    
    def __call__(self, *args, **kwargs):
        print(f"Calling {self.func.__name__} with args: {args}, {kwargs}")
        result = self.func(*args, **kwargs)
        print(f"Result: {result}")
        return result

class CachingDecorator:
    """Decorator that caches the results of method calls."""
    def __init__(self, func):
        self.func = func
        self.cache = {}
    
    def __call__(self, *args, **kwargs):
        key = (args, kwargs)
        if key in self.cache:
            return self.cache[key]
        result = self.func(*args, **kwargs)
        self.cache[key] = result
        return result

if __name__ == "__main__":
    calc = BaseCalculator()
    decorated = LoggingDecorator(calc.calculate)
    cached = CachingDecorator(decorated)
    print(cached(5, 3))