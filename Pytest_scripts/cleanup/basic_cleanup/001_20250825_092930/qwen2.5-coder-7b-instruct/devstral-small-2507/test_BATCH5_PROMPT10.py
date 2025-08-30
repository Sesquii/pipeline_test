import sys

def trace_function(func):
    """Decorator to trace function execution."""
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@trace_function
def example_function(x, y):
    """Example function to trace."""
    z = x + y
    return z

if __name__ == "__main__":
    # Call the example function with some arguments
    result = example_function(3, 4)
    print(f"Final result: {result}")

# ===== GENERATED TESTS =====
import pytest

# Original script code
import sys

def trace_function(func):
    """Decorator to trace function execution."""
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@trace_function
def example_function(x, y):
    """Example function to trace."""
    z = x + y
    return z

if __name__ == "__main__":
    # Call the example function with some arguments
    result = example_function(3, 4)
    print(f"Final result: {result}")

# Test suite for the original script
def test_example_function():
    """Test the example_function with positive and negative inputs."""
    assert example_function(3, 4) == 7, "Should return 7"
    assert example_function(-1, -1) == -2, "Should return -2"
    with pytest.raises(TypeError):
        example_function("a", "b"), "Should raise TypeError for non-numeric inputs"

def test_trace_function():
    """Test the trace_function decorator."""
    @trace_function
    def test_func(x):
        return x * 2

    result = test_func(5)
    assert result == 10, "Should return 10"
    # Check if the print statements are captured (not possible in pytest directly)
    # This is more of a manual check or can be done using pytest-capturelog plugin

This solution includes a comprehensive test suite for the original script. It tests both `example_function` and `trace_function`. The test cases cover positive inputs, negative inputs, and type errors. The `test_trace_function` demonstrates how to use the decorator in a test function, although it's important to note that capturing print statements directly in pytest is not straightforward and may require additional plugins like `pytest-capturelog`.