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