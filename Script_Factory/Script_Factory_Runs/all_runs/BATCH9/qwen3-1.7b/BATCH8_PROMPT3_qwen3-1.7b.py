```python
class Operation:
    def calculate(self, a, b):
        pass


class Add(Operation):
    def calculate(self, a, b):
        return a + b


class Subtract(Operation):
    def calculate(self, a, b):
        return b - a


class Multiply(Operation):
    def calculate(self, a, b):
        return a * b


class Divide(Operation):
    def calculate(self, a, b):
        if b == 0:
            raise ValueError("Division by zero")
        return a / b


class CalculationFactory:
    @staticmethod
    def create_operation(operation_type):
        if operation_type == 'add':
            return Add()
        elif operation_type == 'subtract':
            return Subtract()
        elif operation_type == 'multiply':
            return Multiply()
        elif operation_type == 'divide':
            return Divide()
        else:
            raise ValueError(f"Unknown operation: {operation_type}")


if __name__ == "__main__":
    op_type = input("Enter operation type (add, subtract, multiply, divide): ")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    factory = CalculationFactory()
    operation = factory.create_operation(op_type)
    result = operation.calculate(a, b)
    print(f"Result: {result}")