# BATCH8_PROMPT5_{{model_name}}.py

class BaseCalculator:
    """A simple calculator class with a single method to add two numbers."""
    
    def add(self, x, y):
        return x + y

class LoggingDecorator:
    """A decorator that logs the arguments and result of the function it decorates."""
    
    def __init__(self, func):
        self.func = func
    
    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs)
        print(f"Arguments: {args}, {kwargs}; Result: {result}")
        return result

class CachingDecorator:
    """A decorator that caches the results of the function it decorates to avoid redundant calculations."""
    
    def __init__(self, func):
        self.func = func
        self.cache = {}
    
    def __call__(self, *args):
        if args in self.cache:
            return self.cache[args]
        result = self.func(*args)
        self.cache[args] = result
        return result

# Entry point of the program
if __name__ == "__main__":
    # Create an instance of BaseCalculator
    calculator = BaseCalculator()
    
    # Decorate the add method with LoggingDecorator and CachingDecorator
    decorated_calculator = CachingDecorator(LoggingDecorator(calculator.add))
    
    # Perform a calculation using the decorated method
    result = decorated_calculator(3, 4)
```

This Python script defines a simple `BaseCalculator` class with an `add` method. It then creates two decorator classes: `LoggingDecorator`, which logs the arguments and result of the function it decorates, and `CachingDecorator`, which caches the results to avoid redundant calculations. The decorators are applied to the `add` method, and a calculation is performed using the decorated method.