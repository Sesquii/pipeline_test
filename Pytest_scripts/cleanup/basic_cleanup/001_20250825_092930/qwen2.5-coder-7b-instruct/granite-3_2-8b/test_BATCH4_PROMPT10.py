# BATCH4_PROMPT10_Granite.py

import sys
import traceback
from collections import deque


def reverse_debug(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        # Collect stack trace information in reverse order
        trace_back = traceback.extract_stack()[::-1]

        # Format and print the trace back in reverse chronological order
        for frame in trace_back:
            print(f"File: {frame.filename}, Line: {frame.lineno}, Function: {frame.name}")

        return result
    return wrapper


@reverse_debug
def example_function():
    """A simple function to demonstrate the reverse debugger."""
    a = 10
    b = 20
    print(f"In example_function, a + b equals {a + b}")


if __name__ == "__main__":
    try:
        example_function()
    except Exception as e:
        print(f"An error occurred: {e}")

# ===== GENERATED TESTS =====
# BATCH4_PROMPT10_Granite.py

import sys
import traceback
from collections import deque
from typing import Any, Callable


def reverse_debug(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        # Collect stack trace information in reverse order
        trace_back = traceback.extract_stack()[::-1]

        # Format and print the trace back in reverse chronological order
        for frame in trace_back:
            print(f"File: {frame.filename}, Line: {frame.lineno}, Function: {frame.name}")

        return result
    return wrapper


@reverse_debug
def example_function():
    """A simple function to demonstrate the reverse debugger."""
    a = 10
    b = 20
    print(f"In example_function, a + b equals {a + b}")


if __name__ == "__main__":
    try:
        example_function()
    except Exception as e:
        print(f"An error occurred: {e}")

# Test suite for BATCH4_PROMPT10_Granite.py

import pytest
from io import StringIO


def test_reverse_debug(capsys):
    """Test the reverse_debug decorator."""
    @reverse_debug
    def test_function():
        a = 5
        b = 3
        print(f"Result: {a + b}")

    test_function()
    captured = capsys.readouterr()
    assert "File: BATCH4_PROMPT10_Granite.py, Line:" in captured.out


def test_example_function(capsys):
    """Test the example_function."""
    example_function()
    captured = capsys.readouterr()
    assert "In example_function, a + b equals 30" in captured.out


def test_reverse_debug_with_exception(capsys):
    """Test the reverse_debug decorator with an exception."""
    @reverse_debug
    def test_function():
        raise ValueError("An error occurred")

    try:
        test_function()
    except Exception as e:
        assert str(e) == "An error occurred"
    
    captured = capsys.readouterr()
    assert "File: BATCH4_PROMPT10_Granite.py, Line:" in captured.out


def test_reverse_debug_with_no_print(capsys):
    """Test the reverse_debug decorator with no print statement."""
    @reverse_debug
    def test_function():
        a = 5
        b = 3

    test_function()
    captured = capsys.readouterr()
    assert not captured.out


@pytest.mark.parametrize("input_data, expected", [
    (10, "In example_function, a + b equals 30"),
    (-5, "In example_function, a + b equals -15")
])
def test_example_function_with_parametrization(capsys, input_data):
    """Test the example_function with parametrized inputs."""
    def modified_example_function():
        a = input_data
        b = 20
        print(f"In example_function, a + b equals {a + b}")

    modified_example_function()
    captured = capsys.readouterr()
    assert expected in captured.out


def test_reverse_debug_with_multiple_frames(capsys):
    """Test the reverse_debug decorator with multiple frames."""
    def inner_function():
        a = 5
        b = 3
        print(f"Inner function result: {a + b}")

    @reverse_debug
    def outer_function():
        inner_function()

    outer_function()
    captured = capsys.readouterr()
    assert "File: BATCH4_PROMPT10_Granite.py, Line:" in captured.out
    assert "inner_function" in captured.out
    assert "outer_function" in captured.out


def test_reverse_debug_with_no_stack_trace(capsys):
    """Test the reverse_debug decorator with no stack trace."""
    @reverse_debug
    def test_function():
        pass

    test_function()
    captured = capsys.readouterr()
    assert not captured.out
