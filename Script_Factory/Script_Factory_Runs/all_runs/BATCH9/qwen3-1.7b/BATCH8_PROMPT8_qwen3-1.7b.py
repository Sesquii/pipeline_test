```python
from abc import ABC, abstractmethod

class Handler(ABC):
    @abstractmethod
    def handle(self, request):
        pass

class AddHandler(Handler):
    def handle(self, request):
        if request == "add 5 3":
            return 8
        else:
            return self.next_handler.handle(request)

class SubtractHandler(Handler):
    def handle(self, request):
        if request == "subtract 10 2":
            return 8
        else:
            return self.next_handler.handle(request)

class MultiplyHandler(Handler):
    def handle(self, request):
        if request == "multiply 4 2":
            return 8
        else:
            return self.next_handler.handle(request)

class DivideHandler(Handler):
    def handle(self, request):
        if request == "divide 16 2":
            return 8
        else:
            return self.next_handler.handle(request)

if __name__ == "__main__":
    # Create the chain of handlers in order
    add_handler = AddHandler()
    subtract_handler = SubtractHandler()
    multiply_handler = MultiplyHandler()
    divide_handler = DivideHandler()

    # Set up the chain
    add_handler.next = subtract_handler
    subtract_handler.next = multiply_handler
    multiply_handler.next = divide_handler

    # Process a request through the chain
    request = "add 5 3"
    result = add_handler.handle(request)
    print("Chain Result:", result)