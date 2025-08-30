import sys
import traceback

class ReverseDebugger:
    def __init__(self):
        self.events = []

    def log_event(self, event_type, frame, arg):
        # Capture the current call stack
        stack = traceback.extract_stack(frame)
        # Store the event with reverse chronological order in mind
        self.events.append((event_type, frame.f_code.co_name, stack))

    def print_reverse_log(self):
        # Print events in reverse chronological order (last to first)
        for i, (event_type, func_name, stack) in enumerate(reversed(self.events)):
            print(f"\nEvent {len(self.events) - i}: {event_type} in function '{func_name}'")
            print("Call stack:")
            for frame_summary in stack:
                print(f"  File: {frame_summary.filename}, Line: {frame_summary.lineno}, Function: {frame_summary.name}")

def trace_calls(frame, event, arg):
    if event != 'call':
        return
    reverse_debugger.log_event(event, frame, arg)
    for line in frame.f_code.co_consts:
        if isinstance(line, str) and callable(globals().get(line)):
            return trace_calls
    return

def sample_function(x):
    y = x * 2
    z = y + 3
    return z

if __name__ == "__main__":
    reverse_debugger = ReverseDebugger()
    sys.settrace(trace_calls)
    result = sample_function(5)
    sys.settrace(None)
    print(f"\nFunction result: {result}")
    reverse_debugger.print_reverse_log()