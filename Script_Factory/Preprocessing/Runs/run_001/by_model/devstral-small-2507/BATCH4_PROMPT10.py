import traceback
import sys

class ReverseDebugger:
    def __init__(self):
        self.log = []

    def trace_calls(self, frame, event, arg):
        if event != 'call':
            return self.trace_calls

        filename = frame.f_code.co_filename
        lineno = frame.f_lineno
        function_name = frame.f_code.co_name

        # Log the call event
        self.log.append(f"Call: {filename}:{lineno} in {function_name}")

        return self.trace_calls

    def trace_exceptions(self, frame, arg):
        filename = frame.f_code.co_filename
        lineno = frame.f_lineno
        exception_type = type(arg[0]).__name__
        exception_value = str(arg[0])

        # Log the exception event
        self.log.append(f"Exception: {filename}:{lineno} - {exception_type}: {exception_value}")

        return self.trace_exceptions

    def trace_events(self, frame, event, arg):
        if event == 'call':
            return self.trace_calls(frame, event, arg)
        elif event == 'exception':
            return self.trace_exceptions(frame, arg)
        else:
            return None

def example_function(x, y):
    result = x + y
    print(f"Result: {result}")
    if result > 10:
        raise ValueError("Result is too large")
    return result

if __name__ == "__main__":
    debugger = ReverseDebugger()

    # Enable tracing
    sys.settrace(debugger.trace_events)

    try:
        example_function(5, 7)
    except Exception as e:
        pass

    finally:
        # Disable tracing and print the log in reverse order
        sys.settrace(None)

        for event in reversed(debugger.log):
            print(event)