# BATCH8_PROMPT8_{{model_name}}.py

class OperationHandler:
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def handle(self, operation, a, b):
        if self.can_handle(operation):
            return self.perform_operation(operation, a, b)
        elif self.next_handler:
            return self.next_handler.handle(operation, a, b)
        else:
            raise ValueError("Operation not supported")

    def can_handle(self, operation):
        raise NotImplementedError

    def perform_operation(self, operation, a, b):
        raise NotImplementedError


class AddHandler(OperationHandler):
    def can_handle(self, operation):
        return operation == "add"

    def perform_operation(self, operation, a, b):
        return a + b


class SubtractHandler(OperationHandler):
    def can_handle(self, operation):
        return operation == "subtract"

    def perform_operation(self, operation, a, b):
        return a - b


if __name__ == "__main__":
    # Create the chain of handlers
    add_handler = AddHandler()
    subtract_handler = SubtractHandler(add_handler)

    # Perform operations through the chain
    print(subtract_handler.handle("subtract", 10, 5))  # Output: 5
    print(add_handler.handle("add", 3, 7))         # Output: 10

    try:
        print(subtract_handler.handle("multiply", 2, 3))
    except ValueError as e:
        print(e)  # Output: Operation not supported
```

This Python program defines a chain of responsibility pattern where `OperationHandler` is the base class for all specific operation handlers like `AddHandler` and `SubtractHandler`. Each handler checks if it can handle the requested operation and performs it if possible. If not, it passes the request to the next handler in the chain. The entry point demonstrates how to use this chain to perform addition and subtraction operations.

# ===== GENERATED TESTS =====
```python
# BATCH8_PROMPT8_{{model_name}}.py

class OperationHandler:
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def handle(self, operation, a, b):
        if self.can_handle(operation):
            return self.perform_operation(operation, a, b)
        elif self.next_handler:
            return self.next_handler.handle(operation, a, b)
        else:
            raise ValueError("Operation not supported")

    def can_handle(self, operation):
        raise NotImplementedError

    def perform_operation(self, operation, a, b):
        raise NotImplementedError


class AddHandler(OperationHandler):
    def can_handle(self, operation):
        return operation == "add"

    def perform_operation(self, operation, a, b):
        return a + b


class SubtractHandler(OperationHandler):
    def can_handle(self, operation):
        return operation == "subtract"

    def perform_operation(self, operation, a, b):
        return a - b


if __name__ == "__main__":
    # Create the chain of handlers
    add_handler = AddHandler()
    subtract_handler = SubtractHandler(add_handler)

    # Perform operations through the chain
    print(subtract_handler.handle("subtract", 10, 5))  # Output: 5
    print(add_handler.handle("add", 3, 7))         # Output: 10

    try:
        print(subtract_handler.handle("multiply", 2, 3))
    except ValueError as e:
        print(e)  # Output: Operation not supported


# Test suite for BATCH8_PROMPT8_{{model_name}}.py
import pytest
from typing import Callable, Any

@pytest.fixture
def handler_chain():
    add_handler = AddHandler()
    subtract_handler = SubtractHandler(add_handler)
    return subtract_handler

def test_add_operation(handler_chain):
    """Test addition operation"""
    result = handler_chain.handle("add", 3, 7)
    assert result == 10, f"Expected 10, got {result}"

def test_subtract_operation(handler_chain):
    """Test subtraction operation"""
    result = handler_chain.handle("subtract", 10, 5)
    assert result == 5, f"Expected 5, got {result}"

def test_unsupported_operation(handler_chain):
    """Test handling of unsupported operation"""
    with pytest.raises(ValueError) as exc_info:
        handler_chain.handle("multiply", 2, 3)
    assert str(exc_info.value) == "Operation not supported"

def test_can_handle_method():
    """Test can_handle method in AddHandler"""
    add_handler = AddHandler()
    assert add_handler.can_handle("add"), "Expected to handle 'add' operation"
    assert not add_handler.can_handle("subtract"), "Should not handle 'subtract' operation"

def test_perform_operation_method():
    """Test perform_operation method in AddHandler"""
    add_handler = AddHandler()
    result = add_handler.perform_operation("add", 3, 7)
    assert result == 10, f"Expected 10, got {result}"

def test_can_handle_subtract_method():
    """Test can_handle method in SubtractHandler"""
    subtract_handler = SubtractHandler()
    assert subtract_handler.can_handle("subtract"), "Expected to handle 'subtract' operation"
    assert not subtract_handler.can_handle("add"), "Should not handle 'add' operation"

def test_perform_operation_subtract_method():
    """Test perform_operation method in SubtractHandler"""
    subtract_handler = SubtractHandler()
    result = subtract_handler.perform_operation("subtract", 10, 5)
    assert result == 5, f"Expected 5, got {result}"
```