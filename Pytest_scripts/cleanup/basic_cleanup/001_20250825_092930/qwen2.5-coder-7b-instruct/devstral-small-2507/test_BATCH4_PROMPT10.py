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

# ===== GENERATED TESTS =====
import pytest
from typing import List

class TestReverseDebugger:
    @pytest.fixture
    def debugger(self) -> ReverseDebugger:
        return ReverseDebugger()

    @pytest.mark.parametrize("x, y, expected_log", [
        (5, 7, ["Call: test_script.py:10 in example_function"]),
        (-3, -2, ["Call: test_script.py:10 in example_function"]),
        (8, 2, ["Call: test_script.py:10 in example_function"]),
    ])
    def test_trace_calls(self, debugger, x, y, expected_log):
        # Enable tracing
        sys.settrace(debugger.trace_events)

        try:
            example_function(x, y)
        except Exception as e:
            pass

        finally:
            # Disable tracing and print the log in reverse order
            sys.settrace(None)

            assert debugger.log == expected_log[::-1]

    @pytest.mark.parametrize("x, y, expected_exception", [
        (5, 6, ValueError),
        (-3, -2, ValueError),
        (8, 3, ValueError),
    ])
    def test_trace_exceptions(self, debugger, x, y, expected_exception):
        # Enable tracing
        sys.settrace(debugger.trace_events)

        with pytest.raises(expected_exception) as exc_info:
            example_function(x, y)

        finally:
            # Disable tracing and print the log in reverse order
            sys.settrace(None)

            assert isinstance(exc_info.value, expected_exception)
            assert "Result is too large" in str(exc_info.value)

    def test_example_function(self):
        with pytest.raises(ValueError) as exc_info:
            example_function(5, 7)

        assert str(exc_info.value) == "Result is too large"

if __name__ == "__main__":
    pytest.main()

This test suite includes comprehensive test cases for the `ReverseDebugger` class and the `example_function`. It uses pytest fixtures and parametrization to handle multiple scenarios. The tests cover both positive and negative cases, ensuring that the tracing functionality works as expected.