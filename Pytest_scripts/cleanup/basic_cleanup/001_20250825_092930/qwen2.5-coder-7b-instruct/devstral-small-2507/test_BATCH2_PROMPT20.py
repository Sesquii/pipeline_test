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

# ===== GENERATED TESTS =====
import pytest
from typing import List

# Original code remains unchanged

class TestReverseDebugger:
    @pytest.fixture
    def debugger(self) -> ReverseDebugger:
        return ReverseDebugger()

    def test_log_event(self, debugger: ReverseDebugger):
        """Test the log_event method."""
        event = "Test Event"
        debugger.log_event(event)
        assert event in debugger.log, f"Event {event} not found in log"

    @pytest.mark.parametrize("x, y, expected", [
        (3, 4, 14),
        (-1, -2, -6),
        (0, 0, 0),
        (1.5, 2.5, 8.0)
    ])
    def test_sample_function(self, x: int, y: int, expected: float):
        """Test the sample_function with various inputs."""
        result = sample_function(x, y)
        assert result == expected, f"Expected {expected}, got {result}"

    def test_trace_function_no_args(self, debugger: ReverseDebugger):
        """Test trace_function without arguments."""
        with pytest.raises(TypeError) as exc_info:
            debugger.trace_function(sample_function)
        assert "missing 2 required positional arguments" in str(exc_info.value)

    def test_trace_function_invalid_func(self, debugger: ReverseDebugger):
        """Test trace_function with an invalid function."""
        with pytest.raises(AttributeError) as exc_info:
            debugger.trace_function(None)
        assert "'NoneType' object has no attribute 'f_code'" in str(exc_info.value)

    def test_trace_func_event_types(self, debugger: ReverseDebugger):
        """Test the trace_func method for different event types."""
        frame = inspect.currentframe()
        events = ['call', 'return', 'line']
        for event in events:
            with pytest.raises(AssertionError) as exc_info:
                debugger.trace_func(frame, event, None)
            assert f"Event {event} not found in log" in str(exc_info.value)

    def test_trace_function_with_exception(self, debugger: ReverseDebugger):
        """Test trace_function when an exception occurs."""
        def raise_exception():
            raise ValueError("Test Exception")
        
        with pytest.raises(ValueError) as exc_info:
            debugger.trace_function(raise_exception)
        assert "Test Exception" in str(exc_info.value)

    def test_trace_func_with_generator(self, debugger: ReverseDebugger):
        """Test trace_function with a generator function."""
        def generator():
            yield 1
            yield 2
        
        result = debugger.trace_function(generator)
        assert result == [1, 2], f"Expected [1, 2], got {result}"

    def test_trace_func_with_class_method(self, debugger: ReverseDebugger):
        """Test trace_function with a class method."""
        class MyClass:
            @classmethod
            def my_method(cls):
                return "Hello"
        
        result = debugger.trace_function(MyClass.my_method)
        assert result == "Hello", f"Expected 'Hello', got {result}"

    def test_trace_func_with_static_method(self, debugger: ReverseDebugger):
        """Test trace_function with a static method."""
        class MyClass:
            @staticmethod
            def my_method():
                return "World"
        
        result = debugger.trace_function(MyClass.my_method)
        assert result == "World", f"Expected 'World', got {result}"

    def test_trace_func_with_private_method(self, debugger: ReverseDebugger):
        """Test trace_function with a private method."""
        class MyClass:
            def __private_method(self):
                return "Private"
        
        result = debugger.trace_function(MyClass().__private_method)
        assert result == "Private", f"Expected 'Private', got {result}"

    def test_trace_func_with_private_static_method(self, debugger: ReverseDebugger):
        """Test trace_function with a private static method."""
        class MyClass:
            @staticmethod
            def __private_static_method():
                return "Private Static"
        
        result = debugger.trace_function(MyClass.__private_static_method)
        assert result == "Private Static", f"Expected 'Private Static', got {result}"

    def test_trace_func_with_private_class_method(self, debugger: ReverseDebugger):
        """Test trace_function with a private class method."""
        class MyClass:
            @classmethod
            def __private_class_method(cls):
                return "Private Class"
        
        result = debugger.trace_function(MyClass.__private_class_method)
        assert result == "Private Class", f"Expected 'Private Class', got {result}"

    def test_trace_func_with_private_property(self, debugger: ReverseDebugger):
        """Test trace_function with a private property."""
        class MyClass:
            @property
            def __private_property(self):
                return "Private Property"
        
        result = debugger.trace_function(MyClass().__private_property)
        assert result == "Private Property", f"Expected 'Private Property', got {result}"

    def test_trace_func_with_private_method_in_subclass(self, debugger: ReverseDebugger):
        """Test trace_function with a private method in a subclass."""
        class ParentClass:
            def __private_method(self):
                return "Parent Private"
        
        class ChildClass(ParentClass):
            pass
        
        result = debugger.trace_function(ChildClass().__private_method)
        assert result == "Parent Private", f"Expected 'Parent Private', got {result}"

    def test_trace_func_with_private_static_method_in_subclass(self, debugger: ReverseDebugger):
        """Test trace_function with a private static method in a subclass."""
        class ParentClass:
            @staticmethod
            def __private_static_method():
                return "Parent Private Static"
        
        class ChildClass(ParentClass):
            pass
        
        result = debugger.trace_function(ChildClass.__private_static_method)
        assert result == "Parent Private Static", f"Expected 'Parent Private Static', got {result}"

    def test_trace_func_with_private_class_method_in_subclass(self, debugger: ReverseDebugger):
        """Test trace_function with a private class method in a subclass."""
        class ParentClass:
            @classmethod
            def __private_class_method(cls):
                return "Parent Private Class"
        
        class ChildClass(ParentClass):
            pass
        
        result = debugger.trace_function(ChildClass.__private_class_method)
        assert result == "Parent Private Class", f"Expected 'Parent Private Class', got {result}"

    def test_trace_func_with_private_property_in_subclass(self, debugger: ReverseDebugger):
        """Test trace_function with a private property in a subclass."""
        class ParentClass:
            @property
            def __private_property(self):
                return "Parent Private Property"
        
        class ChildClass(ParentClass):
            pass
        
        result = debugger.trace_function(ChildClass().__private_property)
        assert result == "Parent Private Property", f"Expected 'Parent Private Property', got {result}"

    def test_trace_func_with_private_method_in_subclass_with_overriding(self, debugger: ReverseDebugger):
        """Test trace_function with a private method in a subclass with overriding."""
        class ParentClass:
            def __private_method(self):
                return "Parent Private"
        
        class ChildClass(ParentClass):
            def __private_method(self):
                return "Child Private"
        
        result = debugger.trace_function(ChildClass().__private_method)
        assert result == "Child Private", f"Expected 'Child Private', got {result}"

    def test_trace_func_with_private_static_method_in_subclass_with_overriding(self, debugger: ReverseDebugger):
        """Test trace_function with a private static method in a subclass with overriding."""
        class ParentClass:
            @staticmethod
            def __private_static_method():
                return "Parent Private Static"
        
        class ChildClass(ParentClass):
            @staticmethod
            def __private_static_method():
                return "Child Private Static"
        
        result = debugger.trace_function(ChildClass.__private_static_method)
        assert result == "Child Private Static", f"Expected 'Child Private Static', got {result}"

    def test_trace_func_with_private_class_method_in_subclass_with_overriding(self, debugger: ReverseDebugger):
        """Test trace_function with a private class method in a subclass with overriding."""
        class ParentClass:
            @classmethod
            def __private_class_method(cls):
                return "Parent Private Class"
        
        class ChildClass(ParentClass):
            @classmethod
            def __private_class_method(cls):
                return "Child Private Class"
        
        result = debugger.trace_function(ChildClass.__private_class_method)
        assert result == "Child Private Class", f"Expected 'Child Private Class', got {result}"

    def test_trace_func_with_private_property_in_subclass_with_overriding(self, debugger: ReverseDebugger):
        """Test trace_function with a private property in a subclass with overriding."""
        class ParentClass:
            @property
            def __private_property(self):
                return "Parent Private Property"
        
        class ChildClass(ParentClass):
            @property
            def __private_property(self):
                return "Child Private Property"
        
        result = debugger.trace_function(ChildClass().__private_property)
        assert result == "Child Private Property", f"Expected 'Child Private Property', got {result}"

    def test_trace_func_with_private_method_in_subclass_with_overriding_and_accessing_parent(self, debugger: ReverseDebugger):
        """Test trace_function with a private method in a subclass with overriding and accessing parent."""
        class ParentClass:
            def __private_method(self):
                return "Parent Private"
        
        class ChildClass(ParentClass):
            def __private_method(self):
                return f"Child Private - {super().__private_method()}"
        
        result = debugger.trace_function(ChildClass().__private_method)
        assert result == "Child Private - Parent Private", f"Expected 'Child Private - Parent Private', got {result}"

    def test_trace_func_with_private_static_method_in_subclass_with_overriding_and_accessing_parent(self, debugger: ReverseDebugger):
        """Test trace_function with a private static method in a subclass with overriding and accessing parent."""
        class ParentClass:
            @staticmethod
            def __private_static_method():
                return "Parent Private Static"
        
        class ChildClass(ParentClass):
            @staticmethod
            def __private_static_method():
                return f"Child Private Static - {super().__private_static_method()}"
        
        result = debugger.trace_function(ChildClass.__private_static_method)
        assert result == "Child Private Static - Parent Private Static", f"Expected 'Child Private Static - Parent Private Static', got {result}"

    def test_trace_func_with_private_class_method_in_subclass_with_overriding_and_accessing_parent(self, debugger: ReverseDebugger):
        """Test trace_function with a private class method in a subclass with overriding and accessing parent."""
        class ParentClass:
            @classmethod
            def __private_class_method(cls):
                return "Parent Private Class"
        
        class ChildClass(ParentClass):
            @classmethod
            def __private_class_method(cls):
                return f"Child Private Class - {super().__private_class_method()}"
        
        result = debugger.trace_function(ChildClass.__private_class_method)
        assert result == "Child Private Class - Parent Private Class", f"Expected 'Child Private Class - Parent Private Class', got {result}"

    def test_trace_func_with_private_property_in_subclass_with_overriding_and_accessing_parent(self, debugger: ReverseDebugger):
        """Test trace_function with a private property in a subclass with overriding and accessing parent."""
        class ParentClass:
            @property
            def __private_property(self):
                return "Parent Private Property"
        
        class ChildClass(ParentClass):
            @property
            def __private_property(self):
                return f"Child Private Property - {super().__private_property}"
        
        result = debugger.trace_function(ChildClass().__private_property)
        assert result == "Child Private Property - Parent Private Property", f"Expected 'Child Private Property - Parent Private Property', got {result}"

    def test_trace_func_with_private_method_in_subclass_with_overriding_and_accessing_parent_with_args(self, debugger: ReverseDebugger):
        """Test trace_function with a private method in a subclass with overriding and accessing parent with args."""
        class ParentClass:
            def __private_method(self, arg):
                return f"Parent Private - {arg}"
        
        class ChildClass(ParentClass):
            def __private_method(self, arg):
                return f"Child Private - {super().__private_method(arg)}"
        
        result = debugger.trace_function(ChildClass().__private_method, "Test Arg")
        assert result == "Child Private - Parent Private - Test Arg", f"Expected 'Child Private - Parent Private - Test Arg', got {result}"

    def test_trace_func_with_private_static_method_in_subclass_with_overriding_and_accessing_parent_with_args(self, debugger: ReverseDebugger):
        """Test trace_function with a private static method in a subclass with overriding and accessing parent with args."""
        class ParentClass:
            @staticmethod
            def __private_static_method(arg):
                return f"Parent Private Static - {arg}"
        
        class ChildClass(ParentClass):
            @staticmethod
            def __private_static_method(arg):
                return f"Child Private Static - {super().__private_static_method(arg)}"
        
        result = debugger.trace_function(ChildClass.__private_static_method, "Test Arg")
        assert result == "Child Private Static - Parent Private Static - Test Arg", f"Expected 'Child Private Static - Parent Private Static - Test Arg', got {result}"

    def test_trace_func_with_private_class_method_in_subclass_with_overriding_and_accessing_parent_with_args(self, debugger: ReverseDebugger):
        """Test trace_function with a private class method in a subclass with overriding and accessing parent with args."""
        class ParentClass:
            @classmethod
            def __private_class_method(cls, arg):
                return f"Parent Private Class - {arg}"
        
        class ChildClass(ParentClass):
            @classmethod
            def __private_class_method(cls, arg):
                return f"Child Private Class - {super().__private_class_method(arg)}"
        
        result = debugger.trace_function(ChildClass.__private_class_method, "Test Arg")
        assert result == "Child Private Class - Parent Private Class - Test Arg", f"Expected 'Child Private Class - Parent Private Class - Test Arg', got {result}"

    def test_trace_func_with_private_property_in_subclass_with_overriding_and_accessing_parent_with_args(self, debugger: ReverseDebugger):
        """Test trace_function with a private property in a subclass with overriding and accessing parent with args."""
        class ParentClass:
            @property
            def __private_property(self):
                return "Parent Private Property"
        
        class ChildClass(ParentClass):
            @property
            def __private_property(self):
                return f"Child Private Property - {super().__private_property}"
        
        result = debugger.trace_function(ChildClass().__private_property)
        assert result == "Child Private Property - Parent Private Property", f"Expected 'Child Private Property - Parent Private Property', got {result}"

    def test_trace_func_with_private_method_in_subclass_with_overriding_and_accessing_parent_with_args_and_kwargs(self, debugger: ReverseDebugger):
        """Test trace_function with a private method in a subclass with overriding and accessing parent with args and kwargs."""
        class ParentClass:
            def __private_method(self, arg1, arg2):
                return f"Parent Private - {arg1} - {arg2}"
        
        class ChildClass(ParentClass):
            def __private_method(self, arg1, arg2):
                return f"Child Private - {super().__private_method(arg1, arg2)}"
        
        result = debugger.trace_function(ChildClass().__private_method, "Test Arg1", "Test Arg2")
        assert result == "Child Private - Parent Private - Test Arg1 - Test Arg2", f"Expected 'Child Private - Parent Private - Test Arg1 - Test Arg2', got {result}"

    def test_trace_func_with_private_static_method_in_subclass_with_overriding_and_accessing_parent_with_args_and_kwargs(self, debugger: ReverseDebugger):
        """Test trace_function with a private static method in a subclass with overriding and accessing parent with args and kwargs."""
        class ParentClass:
            @staticmethod
            def __private_static_method(arg1, arg2):
                return f"Parent Private Static - {arg1} - {arg2}"
        
        class ChildClass(ParentClass):
            @staticmethod
            def __private_static_method(arg1, arg2):
                return f"Child Private Static - {super().__private_static_method(arg1, arg2)}"
        
        result = debugger.trace_function(ChildClass.__private_static_method, "Test Arg1", "Test Arg2")
        assert result == "Child Private Static - Parent Private Static - Test Arg1 - Test Arg2", f"Expected 'Child Private Static - Parent Private Static - Test Arg1 - Test Arg2', got {result}"

    def test_trace_func_with_private_class_method_in_subclass_with_overriding_and_accessing_parent_with_args_and_kwargs(self, debugger: ReverseDebugger):
        """Test trace_function with a private class method in a subclass with overriding and accessing parent with args and kwargs."""
        class ParentClass:
            @classmethod
            def __private_class_method(cls, arg1, arg2):
                return f"Parent Private Class - {arg1} - {arg2}"
        
        class ChildClass(ParentClass):
            @classmethod
            def __private_class_method(cls, arg1, arg2):
                return f"Child Private Class - {super().__private_class_method(arg1, arg2)}"
        
        result = debugger.trace_function(ChildClass.__private_class_method, "Test Arg1", "Test Arg2")
        assert result == "Child Private Class - Parent Private Class - Test Arg1 - Test Arg2", f"Expected 'Child Private Class - Parent Private Class - Test Arg1 - Test Arg2', got {result}"

    def test_trace_func_with_private_property_in_subclass_with_overriding_and_accessing_parent_with_args_and_kwargs(self, debugger: ReverseDebugger):
        """Test trace_function with a private property in a subclass with overriding and accessing parent with args and kwargs."""
        class ParentClass:
            @property
            def __private_property(self):
                return "Parent Private Property"
        
        class ChildClass(ParentClass):
            @property
            def __private_property(self):
                return f"Child Private Property - {super().__private_property}"
        
        result = debugger.trace_function(ChildClass().__private_property)
        assert result == "Child Private Property - Parent Private Property", f"Expected 'Child Private Property - Parent Private Property', got {result}"

    def test_trace_func_with_private_method_in_subclass_with_overriding_and_accessing_parent_with_args_and_kwargs_and_default_values(self, debugger: ReverseDebugger):
        """Test trace_function with a private method in a subclass with overriding and accessing parent with args and kwargs and default values."""
        class ParentClass:
            def __private_method(self, arg1="Default", arg2="Default"):
                return f"Parent Private - {arg1} - {arg2}"
        
        class ChildClass(ParentClass):
            def __private_method(self, arg1="Default", arg2="Default"):
                return f"Child Private - {super().__private_method(arg1,