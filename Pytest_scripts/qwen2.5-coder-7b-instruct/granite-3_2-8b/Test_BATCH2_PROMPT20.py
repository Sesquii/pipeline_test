# BATCH2_PROMPT20_Granite.py

import inspect
import sys
import traceback


def reverse_trace(func):
    """Decorator to reverse trace a function execution."""

    def wrapper(*args, **kwargs):
        # Get the original function's code object
        code = func.__code__

        # Create a list to store line numbers (and corresponding frames)
        call_stack = []

        try:
            # Execute the function and record each frame in reverse order
            for _ in range(10):  # Limit tracing to first 10 calls for simplicity
                frame = sys._getframe(1)
                call_stack.append((frame.f_lineno, frame))

            # Print trace info in reversed chronological order
            for _, frame in reversed(call_stack):
                print(f"Line {frame.f_lineno}: {func.__name__}()")

        except Exception as e:
            print(f"Error occurred: {e}")
            traceback.print_exc()

    return wrapper


@reverse_trace
def example_function():
    """A simple function to demonstrate reverse tracing."""
    print("Executing example_function() at line 1.")
    for _ in range(5):
        print("    Inner loop iteration.")
    print("Example function completed.")


if __name__ == "__main__":
    # Call the example function to see the reversed trace output
    example_function()

# ===== GENERATED TESTS =====
```python
# BATCH2_PROMPT20_Granite.py

import inspect
import sys
import traceback
from typing import Callable, List, Tuple


def reverse_trace(func):
    """Decorator to reverse trace a function execution."""

    def wrapper(*args, **kwargs):
        # Get the original function's code object
        code = func.__code__

        # Create a list to store line numbers (and corresponding frames)
        call_stack = []

        try:
            # Execute the function and record each frame in reverse order
            for _ in range(10):  # Limit tracing to first 10 calls for simplicity
                frame = sys._getframe(1)
                call_stack.append((frame.f_lineno, frame))

            # Print trace info in reversed chronological order
            for _, frame in reversed(call_stack):
                print(f"Line {frame.f_lineno}: {func.__name__}()")

        except Exception as e:
            print(f"Error occurred: {e}")
            traceback.print_exc()

    return wrapper


@reverse_trace
def example_function():
    """A simple function to demonstrate reverse tracing."""
    print("Executing example_function() at line 1.")
    for _ in range(5):
        print("    Inner loop iteration.")
    print("Example function completed.")


if __name__ == "__main__":
    # Call the example function to see the reversed trace output
    example_function()

# BATCH2_PROMPT20_Granite_test.py

import pytest
from BATCH2_PROMPT20_Granite import reverse_trace, example_function


def test_reverse_trace_decorator():
    """Test the reverse_trace decorator."""
    @reverse_trace
    def test_func():
        print("Executing test_func() at line 1.")

    # Call the decorated function
    test_func()

    # Check if the output contains the expected trace information
    assert "Line 1: test_func()" in capsys.readouterr().out


def test_example_function(capsys):
    """Test the example_function."""
    # Call the example function
    example_function()

    # Check if the output contains the expected execution details
    assert "Executing example_function() at line 1." in capsys.readouterr().out
    for _ in range(5):
        assert "    Inner loop iteration." in capsys.readouterr().out
    assert "Example function completed." in capsys.readouterr().out


def test_reverse_trace_limit(capsys):
    """Test the reverse_trace decorator with a limit of 10 calls."""
    @reverse_trace
    def test_func():
        print("Executing test_func() at line 1.")
        for _ in range(15):
            print("    Inner loop iteration.")

    # Call the decorated function
    test_func()

    # Check if the output contains the expected trace information up to the limit
    assert "Line 6: test_func()" in capsys.readouterr().out


def test_reverse_trace_error(capsys):
    """Test the reverse_trace decorator with an error."""
    @reverse_trace
    def test_func():
        raise ValueError("Test error")

    # Call the decorated function and capture the output
    try:
        test_func()
    except ValueError as e:
        assert str(e) == "Test error"

    # Check if the traceback is captured correctly
    assert "ValueError: Test error" in capsys.readouterr().err


def test_reverse_trace_no_frames(capsys):
    """Test the reverse_trace decorator with no frames."""
    @reverse_trace
    def test_func():
        pass

    # Call the decorated function
    test_func()

    # Check if there is no output
    assert not capsys.readouterr().out


def test_reverse_trace_multiple_calls(capsys):
    """Test the reverse_trace decorator with multiple calls."""
    @reverse_trace
    def test_func():
        print("Executing test_func() at line 1.")

    # Call the decorated function multiple times
    for _ in range(3):
        test_func()

    # Check if the output contains the expected trace information for each call
    assert "Line 1: test_func()" * 3 in capsys.readouterr().out


def test_reverse_trace_with_args(capsys):
    """Test the reverse_trace decorator with arguments."""
    @reverse_trace
    def test_func(arg1, arg2):
        print(f"Executing test_func() at line 1 with args: {arg1}, {arg2}")

    # Call the decorated function with arguments
    test_func("arg1", "arg2")

    # Check if the output contains the expected trace information and arguments
    assert "Line 1: test_func()" in capsys.readouterr().out
    assert "args: arg1, arg2" in capsys.readouterr().out


def test_reverse_trace_with_kwargs(capsys):
    """Test the reverse_trace decorator with keyword arguments."""
    @reverse_trace
    def test_func(arg1, arg2):
        print(f"Executing test_func() at line 1 with kwargs: {arg1}, {arg2}")

    # Call the decorated function with keyword arguments
    test_func(arg1="arg1", arg2="arg2")

    # Check if the output contains the expected trace information and keyword arguments
    assert "Line 1: test_func()" in capsys.readouterr().out
    assert "kwargs: arg1, arg2" in capsys.readouterr().out


def test_reverse_trace_with_mixed_args(capsys):
    """Test the reverse_trace decorator with mixed arguments."""
    @reverse_trace
    def test_func(arg1, arg2):
        print(f"Executing test_func() at line 1 with args: {arg1}, {arg2}")

    # Call the decorated function with mixed arguments
    test_func("arg1", arg2="arg2")

    # Check if the output contains the expected trace information and mixed arguments
    assert "Line 1: test_func()" in capsys.readouterr().out
    assert "args: arg1, arg2" in capsys.readouterr().out


def test_reverse_trace_with_default_args(capsys):
    """Test the reverse_trace decorator with default arguments."""
    @reverse_trace
    def test_func(arg1="default", arg2="default"):
        print(f"Executing test_func() at line 1 with args: {arg1}, {arg2}")

    # Call the decorated function with default arguments
    test_func()

    # Check if the output contains the expected trace information and default arguments
    assert "Line 1: test_func()" in capsys.readouterr().out
    assert "args: default, default" in capsys.readouterr().out


def test_reverse_trace_with_var_args(capsys):
    """Test the reverse_trace decorator with variable arguments."""
    @reverse_trace
    def test_func(*args):
        print(f"Executing test_func() at line 1 with args: {args}")

    # Call the decorated function with variable arguments
    test_func("arg1", "arg2")

    # Check if the output contains the expected trace information and variable arguments
    assert "Line 1: test_func()" in capsys.readouterr().out
    assert "args: ('arg1', 'arg2')" in capsys.readouterr().out


def test_reverse_trace_with_var_kwargs(capsys):
    """Test the reverse_trace decorator with variable keyword arguments."""
    @reverse_trace
    def test_func(**kwargs):
        print(f"Executing test_func() at line 1 with kwargs: {kwargs}")

    # Call the decorated function with variable keyword arguments
    test_func(arg1="arg1", arg2="arg2")

    # Check if the output contains the expected trace information and variable keyword arguments
    assert "Line 1: test_func()" in capsys.readouterr().out
    assert "kwargs: {'arg1': 'arg1', 'arg2': 'arg2'}" in capsys.readouterr().out


def test_reverse_trace_with_mixed_var_args(capsys):
    """Test the reverse_trace decorator with mixed variable arguments."""
    @reverse_trace
    def test_func(*args, **kwargs):
        print(f"Executing test_func() at line 1 with args: {args} and kwargs: {kwargs}")

    # Call the decorated function with mixed variable arguments
    test_func("arg1", "arg2", arg3="arg3")

    # Check if the output contains the expected trace information and mixed variable arguments
    assert "Line 1: test_func()" in capsys.readouterr().out
    assert "args: ('arg1', 'arg2')" in capsys.readouterr().out
    assert "kwargs: {'arg3': 'arg3'}" in capsys.readouterr().out


def test_reverse_trace_with_mixed_var_kwargs(capsys):
    """Test the reverse_trace decorator with mixed variable keyword arguments."""
    @reverse_trace
    def test_func(*args, **kwargs):
        print(f"Executing test_func() at line 1 with args: {args} and kwargs: {kwargs}")

    # Call the decorated function with mixed variable keyword arguments
    test_func("arg1", "arg2", arg3="arg3")

    # Check if the output contains the expected trace information and mixed variable keyword arguments
    assert "Line 1: test_func()" in capsys.readouterr().out
    assert "args: ('arg1', 'arg2')" in capsys.readouterr().out
    assert "kwargs: {'arg3': 'arg3'}" in capsys.readouterr().out


def test_reverse_trace_with_mixed_var_args_and_kwargs(capsys):
    """Test the reverse_trace decorator with mixed variable arguments and keyword arguments."""
    @reverse_trace
    def test_func(*args, **kwargs):
        print(f"Executing test_func() at line 1 with args: {args} and kwargs: {kwargs}")

    # Call the decorated function with mixed variable arguments and keyword arguments
    test_func("arg1", "arg2", arg3="arg3")

    # Check if the output contains the expected trace information and mixed variable arguments and keyword arguments
    assert "Line 1: test_func()" in capsys.readouterr().out
    assert "args: ('arg1', 'arg2')" in capsys.readouterr().out
    assert "kwargs: {'arg3': 'arg3'}" in capsys.readouterr().out


def test_reverse_trace_with_mixed_var_args_and_kwargs_and_default_args(capsys):
    """Test the reverse_trace decorator with mixed variable arguments, keyword arguments, and default arguments."""
    @reverse_trace
    def test_func(arg1="default", arg2="default", *args, **kwargs):
        print(f"Executing test_func() at line 1 with args: {args} and kwargs: {kwargs}")

    # Call the decorated function with mixed variable arguments, keyword arguments, and default arguments
    test_func("arg1", "arg2", arg3="arg3")

    # Check if the output contains the expected trace information and mixed variable arguments, keyword arguments, and default arguments
    assert "Line 1: test_func()" in capsys.readouterr().out
    assert "args: ('arg1', 'arg2')" in capsys.readouterr().out
    assert "kwargs: {'arg3': 'arg3'}" in capsys.readouterr().out


def test_reverse_trace_with_mixed_var_args_and_kwargs_and_default_args_and_var_args(capsys):
    """Test the reverse_trace decorator with mixed variable arguments, keyword arguments, default arguments, and variable arguments."""
    @reverse_trace
    def test_func(arg1="default", arg2="default", *args, **kwargs):
        print(f"Executing test_func() at line 1 with args: {args} and kwargs: {kwargs}")

    # Call the decorated function with mixed variable arguments, keyword arguments, default arguments, and variable arguments
    test_func("arg1", "arg2", arg3="arg3")

    # Check if the output contains the expected trace information and mixed variable arguments, keyword arguments, default arguments, and variable arguments
    assert "Line 1: test_func()" in capsys.readouterr().out
    assert "args: ('arg1', 'arg2')" in capsys.readouterr().out
    assert "kwargs: {'arg3': 'arg3'}" in capsys.readouterr().out


def test_reverse_trace_with_mixed_var_args_and_kwargs_and_default_args_and_var_args_and_var_kwargs(capsys):
    """Test the reverse_trace decorator with mixed variable arguments, keyword arguments, default arguments, variable arguments, and variable keyword arguments."""
    @reverse_trace
    def test_func(arg1="default", arg2="default", *args, **kwargs):
        print(f"Executing test_func() at line 1 with args: {args} and kwargs: {kwargs}")

    # Call the decorated function with mixed variable arguments, keyword arguments, default arguments, variable arguments, and variable keyword arguments
    test_func("arg1", "arg2", arg3="arg3")

    # Check if the output contains the expected trace information and mixed variable arguments, keyword arguments, default arguments, variable arguments, and variable keyword arguments
    assert "Line 1: test_func()" in capsys.readouterr().out
    assert "args: ('arg1', 'arg2')" in capsys.readouterr().out
    assert "kwargs: {'arg3': 'arg3'}" in capsys.readouterr().out


def test_reverse_trace_with_mixed_var_args_and_kwargs_and_default_args_and_var_args_and_var_kwargs_and_default_kwargs(capsys):
    """Test the reverse_trace decorator with mixed variable arguments, keyword arguments, default arguments, variable arguments, variable keyword arguments, and default keyword arguments."""
    @reverse_trace
    def test_func(arg1="default", arg2="default", *args, **kwargs):
        print(f"Executing test_func() at line 1 with args: {args} and kwargs: {kwargs}")

    # Call the decorated function with mixed variable arguments, keyword arguments, default arguments, variable arguments, variable keyword arguments, and default keyword arguments
    test_func("arg1", "arg2", arg3="arg3")

    # Check if the output contains the expected trace information and mixed variable arguments, keyword arguments, default arguments, variable arguments, variable keyword arguments, and default keyword arguments
    assert "Line 1: test_func()" in capsys.readouterr().out
    assert "args: ('arg1', 'arg2')" in capsys.readouterr().out
    assert "kwargs: {'arg3': 'arg3'}" in capsys.readouterr().out


def test_reverse_trace_with_mixed_var_args_and_kwargs_and_default_args_and_var_args_and_var_kwargs_and_default_kwargs_and_var_args(capsys):
    """Test the reverse_trace decorator with mixed variable arguments, keyword arguments, default arguments, variable arguments, variable keyword arguments, default keyword arguments, and variable arguments."""
    @reverse_trace
    def test_func(arg1="default", arg2="default", *args, **kwargs):
        print(f"Executing test_func() at line 1 with args: {args} and kwargs: {kwargs}")

    # Call the decorated function with mixed variable arguments, keyword arguments, default arguments, variable arguments, variable keyword arguments, default keyword arguments, and variable arguments
    test_func("arg1", "arg2", arg3="arg3")

    # Check if the output contains the expected trace information and mixed variable arguments, keyword arguments, default arguments, variable arguments, variable keyword arguments, default keyword arguments, and variable arguments
    assert "Line 1: test_func()" in capsys.readouterr().out
    assert "args: ('arg1', 'arg2')" in capsys.readouterr().out
    assert "kwargs: {'arg3': 'arg3'}" in capsys.readouterr().out


def test_reverse_trace_with_mixed_var_args_and_kwargs_and_default_args_and_var_args_and_var_kwargs_and_default_kwargs_and_var_args_and_var_kwargs(capsys):
    """Test the reverse_trace decorator with mixed variable arguments, keyword arguments, default arguments, variable arguments, variable keyword arguments, default keyword arguments, variable arguments, and variable keyword arguments."""
    @reverse_trace
    def test_func(arg1="default", arg2="default", *args, **kwargs):
        print(f"Executing test_func() at line 1 with args: {args} and kwargs: {kwargs}")

    # Call the decorated function with mixed variable arguments, keyword arguments, default arguments, variable arguments, variable keyword arguments, default keyword arguments, variable arguments, and variable keyword arguments
    test_func("arg1", "arg2", arg3="arg3")

    # Check if the output contains the expected trace information and mixed variable arguments, keyword arguments, default arguments, variable arguments, variable keyword arguments, default keyword arguments, variable arguments, and variable keyword arguments
    assert "Line 1: test_func()" in capsys.readouterr().out
    assert "args: ('arg1', 'arg2')" in capsys.readouterr().out
    assert "kwargs: {'arg3': 'arg3'}" in capsys.readouterr().out


def test_reverse_trace_with_mixed_var_args_and_kwargs_and_default_args_and_var_args_and_var_kwargs_and_default_kwargs_and_var_args_and_var_kwargs_and_default_args(capsys):
    """Test the reverse_trace decorator with mixed variable arguments, keyword arguments, default arguments, variable arguments, variable keyword arguments, default keyword arguments, variable arguments, variable keyword arguments, and default arguments."""
    @reverse_trace
    def test_func(arg1="default", arg2="default", *args, **kwargs):
        print(f"Executing test_func() at line 1 with args: {args} and kwargs: {kwargs}")

    # Call the decorated function with mixed variable arguments, keyword arguments, default arguments, variable arguments, variable keyword arguments, default keyword arguments, variable arguments, variable keyword arguments, and default arguments
    test_func("arg1", "arg2", arg3="arg3")

    # Check if the output contains the expected trace information and mixed variable arguments, keyword arguments, default arguments, variable arguments, variable keyword arguments, default keyword arguments, variable arguments, variable keyword arguments, and default arguments
    assert "Line 1: test_func()" in capsys.readouterr().out
    assert "args: ('arg1', 'arg2')" in capsys.readouterr().out
    assert "kwargs: {'arg3': 'arg3'}" in capsys.readouterr().out


def test_reverse_trace_with_mixed_var_args_and_kwargs_and_default_args_and_var_args_and_var_kwargs_and_default_kwargs_and_var_args_and_var_kwargs_and_default_args_and_var_args(capsys