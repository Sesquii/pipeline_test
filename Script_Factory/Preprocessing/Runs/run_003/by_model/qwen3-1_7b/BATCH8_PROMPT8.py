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