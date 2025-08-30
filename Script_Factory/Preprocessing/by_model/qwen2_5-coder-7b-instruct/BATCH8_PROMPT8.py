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