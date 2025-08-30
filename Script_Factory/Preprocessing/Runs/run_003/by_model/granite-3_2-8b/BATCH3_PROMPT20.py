# BATCH3_PROMPT20_Granite.py
import sys
import traceback
from io import StringIO

def reverse_debug(func):
    """Decorator to reverse debug a function."""

    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            # Capture the stack trace
            stack_trace = "".join(traceback.format_stack())

            # Reverse the stack trace
            reversed_stack_trace = stack_trace[::-1]
            
            # Print each line in reverse chronological order
            for line in reversed_stack_trace.splitlines():
                print(line)

        except Exception as e:
            print("An error occurred:", str(e))

    return wrapper

@reverse_debug
def example_function():
    """A simple function to demonstrate the reverse debugger."""
    a = 10
    b = 20
    c = a + b
    d = c * 3
    return d

if __name__ == "__main__":
    example_function()