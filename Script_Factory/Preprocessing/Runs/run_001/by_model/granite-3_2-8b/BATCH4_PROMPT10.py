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