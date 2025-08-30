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