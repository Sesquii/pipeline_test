# BATCH8_PROMPT8_{{model_name}}.py

class CalculatorHandler:
    """Base class for calculator handlers."""
    def __init__(self, successor=None):
        self.successor = successor

    def handle(self, operation, a, b):
        if self.can_handle(operation):
            return self.perform_operation(operation, a, b)
        elif self.successor:
            return self.successor.handle(operation, a, b)
        else:
            raise ValueError("Operation not supported")

    def can_handle(self, operation):
        """Determine if this handler can handle the given operation."""
        raise NotImplementedError

    def perform_operation(self, operation, a, b):
        """Perform the operation. This method should be overridden by subclasses."""
        raise NotImplementedError


class AddHandler(CalculatorHandler):
    """Handler for addition operations."""
    def can_handle(self, operation):
        return operation == "add"

    def perform_operation(self, operation, a, b):
        return a + b


class SubtractHandler(CalculatorHandler):
    """Handler for subtraction operations."""
    def can_handle(self, operation):
        return operation == "subtract"

    def perform_operation(self, operation, a, b):
        return a - b


class Calculator:
    """Main calculator class that sets up the chain of responsibility."""
    def __init__(self):
        self.add_handler = AddHandler()
        self.subtract_handler = SubtractHandler(self.add_handler)
        self.handler = self.subtract_handler

    def calculate(self, operation, a, b):
        return self.handler.handle(operation, a, b)


if __name__ == "__main__":
    calculator = Calculator()
    print(calculator.calculate("add", 5, 3))       # Output: 8
    print(calculator.calculate("subtract", 10, 4))  # Output: 6