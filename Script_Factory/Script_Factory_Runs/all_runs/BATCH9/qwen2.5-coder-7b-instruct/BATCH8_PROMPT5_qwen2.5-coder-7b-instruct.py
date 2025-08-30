class BaseCalculator:
    """A simple calculator class with a single method to add two numbers."""
    
    def add(self, a, b):
        """Add two numbers and return the result."""
        return a + b

class LoggingDecorator:
    """A decorator that logs the input and output of the function it decorates."""
    
    def __init__(self, func):
        self.func = func
    
    def __call__(self, *args, **kwargs):
        print(f"Calling {self.func.__name__} with args: {args}, kwargs: {kwargs}")
        result = self.func(*args, **kwargs)
        print(f"{self.func.__name__} returned: {result}")
        return result

class CachingDecorator:
    """A decorator that caches the results of the function it decorates to avoid redundant calculations."""
    
    def __init__(self, func):
        self.func = func
        self.cache = {}
    
    def __call__(self, *args):
        if args in self.cache:
            print(f"Returning cached result for {self.func.__name__} with args: {args}")
            return self.cache[args]
        else:
            result = self.func(*args)
            self.cache[args] = result
            print(f"Caching result for {self.func.__name__} with args: {args}, result: {result}")
            return result

# Entry point of the program
if __name__ == "__main__":
    # Create an instance of the BaseCalculator class
    calculator = BaseCalculator()
    
    # Decorate the add method with both LoggingDecorator and CachingDecorator
    decorated_calculator = LoggingDecorator(CachingDecorator(calculator.add))
    
    # Perform a calculation using the decorated method
    result = decorated_calculator(3, 4)