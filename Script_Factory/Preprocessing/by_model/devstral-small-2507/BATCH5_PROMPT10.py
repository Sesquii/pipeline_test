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