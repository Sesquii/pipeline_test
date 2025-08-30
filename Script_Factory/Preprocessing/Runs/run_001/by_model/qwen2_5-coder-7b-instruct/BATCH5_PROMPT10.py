import sys

class ReverseDebugger:
    def __init__(self):
        self.log = []

    def trace(self, frame, event, arg):
        if event == 'line':
            # Log each line before it is executed
            self.log.append((frame.f_lineno, frame.f_code.co_name))
        return self.trace

    def run_with_reverse_debugging(self, func, *args, **kwargs):
        sys.settrace(self.trace)
        try:
            func(*args, **kwargs)
        finally:
            sys.settrace(None)

        # Reverse the log
        reversed_log = list(reversed(self.log))

        # Print the reversed log
        for line, func_name in reversed_log:
            print(f"Line: {line}, Function: {func_name}")

def simple_function():
    a = 1
    b = 2
    c = a + b
    return c

if __name__ == "__main__":
    debugger = ReverseDebugger()
    debugger.run_with_reverse_debugging(simple_function)
```

This Python program implements a "Reverse Debugger" that traces the execution of a simple function and prints a log of events in reverse chronological order. The `ReverseDebugger` class is used to manage the tracing process, and the `run_with_reverse_debugging` method sets up the trace function using `sys.settrace`. After the function execution, the log is reversed and printed.