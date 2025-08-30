```python
class BaseCalculator:
    def calculate(self, a, b):
        return a + b


class LoggingDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f"Calling {self.func.__name__} with args: {args}, kwargs: {kwargs}")
        result = self.func(*args, **kwargs)
        print(f"Result: {result}")
        return result


class CachingDecorator:
    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if key in self.cache:
            return self.cache[key]
        result = self.func(*args, **kwargs)
        self.cache[key] = result
        return result


if __name__ == "__main__":
    calc = BaseCalculator()
    decorated_with_logging = LoggingDecorator(calc.calculate)
    cached_result = CachingDecorator(decorated_with_logging)(3, 5)
    print(f"Final result: {cached_result}")