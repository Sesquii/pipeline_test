import traceback
import inspect

class ReverseDebugger:
    def __init__(self):
        self.log = []

    def log_event(self, event):
        self.log.append(event)

    def trace_function(self, func, *args, **kwargs):
        # Create a frame object for the function call
        frame = inspect.currentframe()
        try:
            # Set up tracing with our custom trace function
            sys.settrace(self.trace_func)
            # Call the function with arguments
            result = func(*args, **kwargs)
            return result
        finally:
            # Reset tracing to None when done
            sys.settrace(None)

    def trace_func(self, frame, event, arg):
        if event in ('call', 'return', 'line'):
            # Get current line number and function name
            lineno = frame.f_lineno
            func_name = frame.f_code.co_name
            filename = frame.f_code.co_filename
            
            # Create a log entry with the event details
            event_info = f"{filename}:{lineno} in {func_name} - {event}"
            self.log_event(event_info)
        
        return self.trace_func

def sample_function(x, y):
    a = x + y
    b = a * 2
    return b

if __name__ == "__main__":
    debugger = ReverseDebugger()
    debugger.trace_function(sample_function, 3, 4)

    # Print the log in reverse chronological order
    print("Reverse Debugger Log:")
    for entry in reversed(debugger.log):
        print(entry)