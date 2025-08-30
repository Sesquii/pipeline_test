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

# ===== GENERATED TESTS =====
import pytest

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


# Test suite for BaseCalculator class
def test_calculate():
    calc = BaseCalculator()
    assert calc.calculate(2, 3) == 5
    assert calc.calculate(-1, -1) == -2
    with pytest.raises(TypeError):
        calc.calculate("a", "b")


# Test suite for LoggingDecorator class
def test_logging_decorator(capsys):
    calc = BaseCalculator()
    decorated_with_logging = LoggingDecorator(calc.calculate)
    result = decorated_with_logging(3, 5)
    assert result == 8
    captured = capsys.readouterr()
    assert "Calling calculate with args: (3, 5), kwargs: {}" in captured.out
    assert "Result: 8" in captured.out


# Test suite for CachingDecorator class
def test_caching_decorator():
    calc = BaseCalculator()
    decorated_with_logging = LoggingDecorator(calc.calculate)
    cached_result = CachingDecorator(decorated_with_logging)(3, 5)
    assert cached_result == 8
    assert CachingDecorator(decorated_with_logging)(3, 5) == 8  # Should use cache

    # Test with different arguments
    assert CachingDecorator(decorated_with_logging)(4, 6) == 10
    assert CachingDecorator(decorated_with_logging)(4, 6) == 10  # Should use cache

    # Test with keyword arguments
    assert CachingDecorator(decorated_with_logging)(a=4, b=6) == 10
    assert CachingDecorator(decorated_with_logging)(b=6, a=4) == 10  # Should use cache
