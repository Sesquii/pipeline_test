# BATCH8_PROMPT8_{{model_name}}.py

class Handler:
    def __init__(self):
        self.next_handler = None

    def set_next(self, handler):
        self.next_handler = handler

    def handle_request(self, request):
        if not self.next_handler:
            raise ValueError("No handler available for this operation")
        return self.next_handler.handle_request(request)

class AddHandler(Handler):
    def handle_request(self, request):
        if request['operation'] == 'add':
            result = request['operand1'] + request['operand2']
            return f"Result of addition: {result}"
        else:
            return super().handle_request(request)

class SubtractHandler(Handler):
    def handle_request(self, request):
        if request['operation'] == 'subtract':
            result = request['operand1'] - request['operand2']
            return f"Result of subtraction: {result}"
        else:
            return super().handle_request(request)

class MultiplyHandler(Handler):
    def handle_request(self, request):
        if request['operation'] == 'multiply':
            result = request['operand1'] * request['operand2']
            return f"Result of multiplication: {result}"
        else:
            return super().handle_request(request)

class DivideHandler(Handler):
    def handle_request(self, request):
        if request['operation'] == 'divide':
            if request['operand2'] == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            result = request['operand1'] / request['operand2']
            return f"Result of division: {result}"
        else:
            return super().handle_request(request)

if __name__ == "__main__":
    # Create handlers and set the chain
    add_handler = AddHandler()
    subtract_handler = SubtractHandler()
    multiply_handler = MultiplyHandler()
    divide_handler = DivideHandler()

    add_handler.set_next(subtract_handler)
    subtract_handler.set_next(multiply_handler)
    multiply_handler.set_next(divide_handler)

    # Test cases
    test_cases = [
        {'operation': 'add', 'operand1': 5, 'operand2': 3},
        {'operation': 'subtract', 'operand1': 10, 'operand2': 4},
        {'operation': 'multiply', 'operand1': 6, 'operand2': 7},
        {'operation': 'divide', 'operand1': 8, 'operand2': 2},
        {'operation': 'divide', 'operand1': 8, 'operand2': 0}  # This will raise an error
    ]

    for test_case in test_cases:
        try:
            print(add_handler.handle_request(test_case))
        except Exception as e:
            print(f"Error: {e}")

# ===== GENERATED TESTS =====
# BATCH8_PROMPT8_{{model_name}}.py

class Handler:
    def __init__(self):
        self.next_handler = None

    def set_next(self, handler):
        self.next_handler = handler

    def handle_request(self, request):
        if not self.next_handler:
            raise ValueError("No handler available for this operation")
        return self.next_handler.handle_request(request)

class AddHandler(Handler):
    def handle_request(self, request):
        if request['operation'] == 'add':
            result = request['operand1'] + request['operand2']
            return f"Result of addition: {result}"
        else:
            return super().handle_request(request)

class SubtractHandler(Handler):
    def handle_request(self, request):
        if request['operation'] == 'subtract':
            result = request['operand1'] - request['operand2']
            return f"Result of subtraction: {result}"
        else:
            return super().handle_request(request)

class MultiplyHandler(Handler):
    def handle_request(self, request):
        if request['operation'] == 'multiply':
            result = request['operand1'] * request['operand2']
            return f"Result of multiplication: {result}"
        else:
            return super().handle_request(request)

class DivideHandler(Handler):
    def handle_request(self, request):
        if request['operation'] == 'divide':
            if request['operand2'] == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            result = request['operand1'] / request['operand2']
            return f"Result of division: {result}"
        else:
            return super().handle_request(request)

if __name__ == "__main__":
    # Create handlers and set the chain
    add_handler = AddHandler()
    subtract_handler = SubtractHandler()
    multiply_handler = MultiplyHandler()
    divide_handler = DivideHandler()

    add_handler.set_next(subtract_handler)
    subtract_handler.set_next(multiply_handler)
    multiply_handler.set_next(divide_handler)

    # Test cases
    test_cases = [
        {'operation': 'add', 'operand1': 5, 'operand2': 3},
        {'operation': 'subtract', 'operand1': 10, 'operand2': 4},
        {'operation': 'multiply', 'operand1': 6, 'operand2': 7},
        {'operation': 'divide', 'operand1': 8, 'operand2': 2},
        {'operation': 'divide', 'operand1': 8, 'operand2': 0}  # This will raise an error
    ]

    for test_case in test_cases:
        try:
            print(add_handler.handle_request(test_case))
        except Exception as e:
            print(f"Error: {e}")

# Test suite for the script

import pytest

def create_handler_chain():
    add_handler = AddHandler()
    subtract_handler = SubtractHandler()
    multiply_handler = MultiplyHandler()
    divide_handler = DivideHandler()

    add_handler.set_next(subtract_handler)
    subtract_handler.set_next(multiply_handler)
    multiply_handler.set_next(divide_handler)

    return add_handler

@pytest.mark.parametrize("test_case, expected", [
    ({'operation': 'add', 'operand1': 5, 'operand2': 3}, "Result of addition: 8"),
    ({'operation': 'subtract', 'operand1': 10, 'operand2': 4}, "Result of subtraction: 6"),
    ({'operation': 'multiply', 'operand1': 6, 'operand2': 7}, "Result of multiplication: 42"),
    ({'operation': 'divide', 'operand1': 8, 'operand2': 2}, "Result of division: 4.0")
])
def test_valid_operations(handler_chain, test_case, expected):
    """Test valid operations in the handler chain."""
    result = handler_chain.handle_request(test_case)
    assert result == expected

def test_divide_by_zero(handler_chain):
    """Test division by zero case."""
    with pytest.raises(ZeroDivisionError) as exc_info:
        handler_chain.handle_request({'operation': 'divide', 'operand1': 8, 'operand2': 0})
    assert "Cannot divide by zero" in str(exc_info.value)

def test_invalid_operation(handler_chain):
    """Test invalid operation case."""
    with pytest.raises(ValueError) as exc_info:
        handler_chain.handle_request({'operation': 'modulus', 'operand1': 8, 'operand2': 3})
    assert "No handler available for this operation" in str(exc_info.value)

# Fixture to create the handler chain
@pytest.fixture
def handler_chain():
    return create_handler_chain()
