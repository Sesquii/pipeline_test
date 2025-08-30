# BATCH2_PROMPT20_qwen.py

import sys

def trace_execution(func):
    """Decorator to trace and log function execution events."""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        event_log.append((func.__name__, args, kwargs, result))
        return result
    return wrapper

event_log = []

@trace_execution
def example_function(a, b):
    """A simple function to demonstrate the reverse debugger."""
    c = a + b
    d = c * 2
    return d

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python BATCH2_PROMPT20_qwen.py <a> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[2])

    # Execute the function
    result = example_function(a, b)

    # Print events in reverse chronological order
    print("Reverse Execution Log:")
    for event in reversed(event_log):
        func_name, args, kwargs, result = event
        print(f"Function: {func_name}, Args: {args}, Kwargs: {kwargs}, Result: {result}")

# ===== GENERATED TESTS =====
```python
# BATCH2_PROMPT20_qwen.py

import sys

def trace_execution(func):
    """Decorator to trace and log function execution events."""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        event_log.append((func.__name__, args, kwargs, result))
        return result
    return wrapper

event_log = []

@trace_execution
def example_function(a, b):
    """A simple function to demonstrate the reverse debugger."""
    c = a + b
    d = c * 2
    return d

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python BATCH2_PROMPT20_qwen.py <a> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[2])

    # Execute the function
    result = example_function(a, b)

    # Print events in reverse chronological order
    print("Reverse Execution Log:")
    for event in reversed(event_log):
        func_name, args, kwargs, result = event
        print(f"Function: {func_name}, Args: {args}, Kwargs: {kwargs}, Result: {result}")

# Test suite for BATCH2_PROMPT20_qwen.py

import pytest
from typing import List, Tuple

@pytest.fixture
def example_function_fixture():
    """Fixture to provide the example_function."""
    return example_function

def test_example_function_positive(example_function_fixture):
    """Test case for positive input values."""
    result = example_function_fixture(3, 4)
    assert result == 14, f"Expected 14, got {result}"

def test_example_function_negative(example_function_fixture):
    """Test case for negative input values."""
    result = example_function_fixture(-2, -3)
    assert result == -10, f"Expected -10, got {result}"

def test_example_function_zero(example_function_fixture):
    """Test case for zero input values."""
    result = example_function_fixture(0, 0)
    assert result == 0, f"Expected 0, got {result}"

def test_example_function_type_hints():
    """Test case to check type hints of the example_function."""
    with pytest.raises(TypeError):
        example_function("a", "b")

def test_trace_execution_decorator():
    """Test case for the trace_execution decorator."""
    @trace_execution
    def test_func(x, y):
        return x * y

    result = test_func(2, 3)
    assert result == 6, f"Expected 6, got {result}"
    assert len(event_log) == 1, "Expected one event in the log"
    func_name, args, kwargs, result = event_log[0]
    assert func_name == 'test_func', f"Expected function name 'test_func', got '{func_name}'"
    assert args == (2, 3), f"Expected arguments (2, 3), got {args}"
    assert kwargs == {}, f"Expected no keyword arguments, got {kwargs}"
    assert result == 6, f"Expected result 6, got {result}"

def test_example_function_with_event_log():
    """Test case to check if the event log is correctly populated."""
    @trace_execution
    def test_func(x, y):
        return x + y

    result = test_func(5, 7)
    assert result == 12, f"Expected 12, got {result}"
    assert len(event_log) == 1, "Expected one event in the log"
    func_name, args, kwargs, result = event_log[0]
    assert func_name == 'test_func', f"Expected function name 'test_func', got '{func_name}'"
    assert args == (5, 7), f"Expected arguments (5, 7), got {args}"
    assert kwargs == {}, f"Expected no keyword arguments, got {kwargs}"
    assert result == 12, f"Expected result 12, got {result}"

def test_example_function_with_multiple_calls():
    """Test case to check if the event log is correctly populated with multiple calls."""
    @trace_execution
    def test_func(x):
        return x * x

    result1 = test_func(3)
    assert result1 == 9, f"Expected 9, got {result1}"
    result2 = test_func(4)
    assert result2 == 16, f"Expected 16, got {result2}"
    assert len(event_log) == 2, "Expected two events in the log"
    func_name1, args1, kwargs1, result1 = event_log[0]
    assert func_name1 == 'test_func', f"Expected function name 'test_func', got '{func_name1}'"
    assert args1 == (3,), f"Expected arguments (3,), got {args1}"
    assert kwargs1 == {}, f"Expected no keyword arguments, got {kwargs1}"
    assert result1 == 9, f"Expected result 9, got {result1}"
    func_name2, args2, kwargs2, result2 = event_log[1]
    assert func_name2 == 'test_func', f"Expected function name 'test_func', got '{func_name2}'"
    assert args2 == (4,), f"Expected arguments (4,), got {args2}"
    assert kwargs2 == {}, f"Expected no keyword arguments, got {kwargs2}"
    assert result2 == 16, f"Expected result 16, got {result2}"

def test_example_function_with_empty_event_log():
    """Test case to check if the event log is empty before any function calls."""
    assert len(event_log) == 0, "Event log should be empty initially"

def test_example_function_with_parametrization(example_function_fixture):
    """Test case with parametrization for positive input values."""
    @pytest.mark.parametrize("a, b, expected", [
        (3, 4, 14),
        (5, 6, 22),
        (7, 8, 30)
    ])
    def test_parametrized(a, b, expected):
        result = example_function_fixture(a, b)
        assert result == expected, f"Expected {expected}, got {result}"

    test_parametrized(3, 4, 14)
    test_parametrized(5, 6, 22)
    test_parametrized(7, 8, 30)

def test_example_function_with_negative_parametrization(example_function_fixture):
    """Test case with parametrization for negative input values."""
    @pytest.mark.parametrize("a, b, expected", [
        (-2, -3, -10),
        (-4, -5, -18),
        (-6, -7, -26)
    ])
    def test_parametrized(a, b, expected):
        result = example_function_fixture(a, b)
        assert result == expected, f"Expected {expected}, got {result}"

    test_parametrized(-2, -3, -10)
    test_parametrized(-4, -5, -18)
    test_parametrized(-6, -7, -26)

def test_example_function_with_zero_parametrization(example_function_fixture):
    """Test case with parametrization for zero input values."""
    @pytest.mark.parametrize("a, b, expected", [
        (0, 0, 0),
        (1, 0, 2),
        (0, 1, 2)
    ])
    def test_parametrized(a, b, expected):
        result = example_function_fixture(a, b)
        assert result == expected, f"Expected {expected}, got {result}"

    test_parametrized(0, 0, 0)
    test_parametrized(1, 0, 2)
    test_parametrized(0, 1, 2)

def test_example_function_with_type_hints_parametrization(example_function_fixture):
    """Test case with parametrization to check type hints of the example_function."""
    @pytest.mark.parametrize("a, b", [
        ("a", "b"),
        (3.5, 4.5),
        ([1, 2], [3, 4])
    ])
    def test_parametrized(a, b):
        with pytest.raises(TypeError):
            result = example_function_fixture(a, b)

    test_parametrized("a", "b")
    test_parametrized(3.5, 4.5)
    test_parametrized([1, 2], [3, 4])
```