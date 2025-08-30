import sys

def example_function(a, b):
    # Log the call to the function with parameters
    logs.append(f"Calling example_function with a={a}, b={b}")
    # Perform some operations (simple addition)
    result = a + b
    # Log the return value of the function
    logs.append(f"Returning {result}")
    return result

if __name__ == "__main__":
    # Initialize list to store events during execution
    logs = []
    # Call the example function with parameters 2 and 3
    result = example_function(2, 3)
    # Print events in reverse order as required
    for event in reversed(logs):
        print(event)

# ===== GENERATED TESTS =====
import pytest
from typing import List

# Original script code
import sys

def example_function(a: int, b: int) -> int:
    # Log the call to the function with parameters
    logs.append(f"Calling example_function with a={a}, b={b}")
    # Perform some operations (simple addition)
    result = a + b
    # Log the return value of the function
    logs.append(f"Returning {result}")
    return result

if __name__ == "__main__":
    # Initialize list to store events during execution
    logs = []
    # Call the example function with parameters 2 and 3
    result = example_function(2, 3)
    # Print events in reverse order as required
    for event in reversed(logs):
        print(event)

# Test suite code

logs: List[str] = []

def test_example_function_positive():
    """Test the example_function with positive integers."""
    assert example_function(2, 3) == 5
    assert logs == [
        "Calling example_function with a=2, b=3",
        "Returning 5"
    ]

def test_example_function_negative():
    """Test the example_function with negative integers."""
    assert example_function(-1, -1) == -2
    assert logs == [
        "Calling example_function with a=-1, b=-1",
        "Returning -2"
    ]

def test_example_function_zero():
    """Test the example_function with zero."""
    assert example_function(0, 0) == 0
    assert logs == [
        "Calling example_function with a=0, b=0",
        "Returning 0"
    ]

def test_example_function_type_checking():
    """Test type checking for input parameters."""
    with pytest.raises(TypeError):
        example_function('a', 'b')

def test_logs_order():
    """Test if logs are printed in the correct order."""
    example_function(1, 2)
    assert logs == [
        "Calling example_function with a=1, b=2",
        "Returning 3"
    ]
    logs.clear()

# Run tests
if __name__ == "__main__":
    pytest.main()

This test suite includes comprehensive test cases for the `example_function` function. It covers positive and negative scenarios, type checking, and ensures that the logs are printed in the correct order. The use of pytest fixtures and parametrization is not necessary in this case as there are no repeated setups or parameterized tests required.