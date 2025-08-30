# BATCH8_PROMPT8_Devstral.py

class Handler:
    def __init__(self, successor=None):
        self._successor = successor

    def handle_request(self, request):
        if not self._successor:
            raise ValueError("No handler found for this operation")
        else:
            self._successor.handle_request(request)

class AddHandler(Handler):
    def handle_request(self, request):
        if request['operation'] == 'add':
            result = request['operand1'] + request['operand2']
            print(f"Addition of {request['operand1']} and {request['operand2']} is: {result}")
        else:
            super().handle_request(request)

class SubtractHandler(Handler):
    def handle_request(self, request):
        if request['operation'] == 'subtract':
            result = request['operand1'] - request['operand2']
            print(f"Subtraction of {request['operand1']} and {request['operand2']} is: {result}")
        else:
            super().handle_request(request)

class MultiplyHandler(Handler):
    def handle_request(self, request):
        if request['operation'] == 'multiply':
            result = request['operand1'] * request['operand2']
            print(f"Multiplication of {request['operand1']} and {request['operand2']} is: {result}")
        else:
            super().handle_request(request)

class DivideHandler(Handler):
    def handle_request(self, request):
        if request['operation'] == 'divide':
            result = request['operand1'] / request['operand2']
            print(f"Division of {request['operand1']} by {request['operand2']} is: {result}")
        else:
            super().handle_request(request)

if __name__ == "__main__":
    # Create the chain of responsibility
    divide_handler = DivideHandler()
    multiply_handler = MultiplyHandler(divide_handler)
    subtract_handler = SubtractHandler(multiply_handler)
    add_handler = AddHandler(subtract_handler)

    # Test cases
    requests = [
        {'operation': 'add', 'operand1': 5, 'operand2': 3},
        {'operation': 'subtract', 'operand1': 10, 'operand2': 4},
        {'operation': 'multiply', 'operand1': 6, 'operand2': 7},
        {'operation': 'divide', 'operand1': 8, 'operand2': 2},
        {'operation': 'power', 'operand1': 2, 'operand2': 3} # This will raise an error
    ]

    for request in requests:
        try:
            add_handler.handle_request(request)
        except ValueError as e:
            print(e)