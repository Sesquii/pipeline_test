# BATCH8_PROMPT8_Granite.py

class CalculatorHandler:
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def handle(self, operation):
        if operation == 'add':
            print("Add operation handled.")
        elif operation == 'subtract':
            print("Subtract operation handled.")
        else:
            if self.next_handler:
                return self.next_handler.handle(operation)
            else:
                print("Operation not supported.")


class AddHandler(CalculatorHandler):
    pass


class SubtractHandler(CalculatorHandler):
    pass


def main():
    add_handler = AddHandler()
    subtract_handler = SubtractHandler(add_handler)

    operations = ['add', 'subtract', 'multiply']  # This list could be dynamic from user input or file

    for operation in operations:
        subtract_handler.handle(operation)


if __name__ == "__main__":
    main()