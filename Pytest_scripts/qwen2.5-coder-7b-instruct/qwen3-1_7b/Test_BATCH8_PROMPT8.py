```python
class BaseHandler:
    def can_handle(self, operand):
        pass

    def process(self, operand):
        pass


class AddHandler(BaseHandler):
    def can_handle(self, operand):
        return isinstance(operand, list) and len(operand) == 2

    def process(self, operand):
        return operand[0] + operand[1]


class SubtractHandler(BaseHandler):
    def can_handle(self, operand):
        return isinstance(operand, list) and len(operand) == 2

    def process(self, operand):
        return operand[0] - operand[1]


class MultiplyHandler(BaseHandler):
    def can_handle(self, operand):
        return isinstance(operand, list) and len(operand) == 2

    def process(self, operand):
        return operand[0] * operand[1]


class DivideHandler(BaseHandler):
    def can_handle(self, operand):
        return isinstance(operand, list) and len(operand) == 2

    def process(self, operand):
        a, b = operand
        if b == 0:
            raise ValueError("Division by zero")
        return a / b


def process_request(operand):
    for handler in handlers:
        if handler.can_handle(operand):
            return handler.process(operand)
    return None


if __name__ == "__main__":
    add_handler = AddHandler()
    subtract_handler = SubtractHandler()
    multiply_handler = MultiplyHandler()
    divide_handler = DivideHandler()

    handlers = [add_handler, subtract_handler, multiply_handler, divide_handler]

    print("Processing 5 + 3:")
    result = process_request([5, 3])
    print(f"Result: {result}")

    print("\nProcessing 10 - 2:")
    result = process_request([10, 2])
    print(f"Result: {result}")

    print("\nProcessing 4 * 8:")
    result = process_request([4, 8])
    print(f"Result: {result}")

    print("\nProcessing 10 / 2:")
    try:
        result = process_request([10, 2])
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Error: {e}")

# ===== GENERATED TESTS =====
```python
from typing import List

class BaseHandler:
    def can_handle(self, operand):
        pass

    def process(self, operand):
        pass


class AddHandler(BaseHandler):
    def can_handle(self, operand):
        return isinstance(operand, list) and len(operand) == 2

    def process(self, operand):
        return operand[0] + operand[1]


class SubtractHandler(BaseHandler):
    def can_handle(self, operand):
        return isinstance(operand, list) and len(operand) == 2

    def process(self, operand):
        return operand[0] - operand[1]


class MultiplyHandler(BaseHandler):
    def can_handle(self, operand):
        return isinstance(operand, list) and len(operand) == 2

    def process(self, operand):
        return operand[0] * operand[1]


class DivideHandler(BaseHandler):
    def can_handle(self, operand):
        return isinstance(operand, list) and len(operand) == 2

    def process(self, operand):
        a, b = operand
        if b == 0:
            raise ValueError("Division by zero")
        return a / b


def process_request(operand):
    for handler in handlers:
        if handler.can_handle(operand):
            return handler.process(operand)
    return None


# Test cases start here

import pytest

@pytest.fixture(scope="module")
def handlers():
    add_handler = AddHandler()
    subtract_handler = SubtractHandler()
    multiply_handler = MultiplyHandler()
    divide_handler = DivideHandler()
    return [add_handler, subtract_handler, multiply_handler, divide_handler]


def test_can_handle_add(handlers):
    assert handlers[0].can_handle([1, 2])
    assert not handlers[0].can_handle([1, 2, 3])
    assert not handlers[0].can_handle("1,2")


def test_process_add(handlers):
    assert handlers[0].process([1, 2]) == 3
    with pytest.raises(ValueError):
        handlers[0].process([1])


def test_can_handle_subtract(handlers):
    assert handlers[1].can_handle([5, 3])
    assert not handlers[1].can_handle([5, 3, 4])
    assert not handlers[1].can_handle("5,3")


def test_process_subtract(handlers):
    assert handlers[1].process([5, 3]) == 2
    with pytest.raises(ValueError):
        handlers[1].process([5])


def test_can_handle_multiply(handlers):
    assert handlers[2].can_handle([4, 8])
    assert not handlers[2].can_handle([4, 8, 16])
    assert not handlers[2].can_handle("4,8")


def test_process_multiply(handlers):
    assert handlers[2].process([4, 8]) == 32
    with pytest.raises(ValueError):
        handlers[2].process([4])


def test_can_handle_divide(handlers):
    assert handlers[3].can_handle([10, 2])
    assert not handlers[3].can_handle([10, 2, 5])
    assert not handlers[3].can_handle("10,2")


def test_process_divide(handlers):
    assert handlers[3].process([10, 2]) == 5.0
    with pytest.raises(ValueError):
        handlers[3].process([10, 0])


def test_process_request(handlers):
    assert process_request([5, 3]) == 8
    assert process_request([10, 2]) == 8
    assert process_request([4, 8]) == 32
    with pytest.raises(ValueError):
        process_request([10, 0])


def test_process_request_no_handler(handlers):
    assert process_request([5, 5]) is None
```