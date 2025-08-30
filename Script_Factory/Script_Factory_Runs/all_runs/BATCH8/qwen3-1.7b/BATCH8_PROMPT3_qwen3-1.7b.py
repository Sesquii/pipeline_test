```python
class BaseOperation:
    def calculate(self, a, b):
        pass


class Add(BaseOperation):
    def calculate(self, a, b):
        return a + b


class Subtract(BaseOperation):
    def calculate(self, a, b):
        return a - b


class CalculationFactory:
    @staticmethod
    def create_operation(op_type):
        if op_type == 'Add':
            return Add
        elif op_type == 'Subtract':
            return Subtract
        else:
            raise ValueError(f"Unknown operation: {op_type}")


if __name__ == "__main__":
    op_type = input("Enter operation (Add/Subtract): ")
    a = float(input("First number: "))
    b = float(input("Second number: "))

    factory = CalculationFactory()
    op_class = factory.create_operation(op_type)
    op_instance = op_class()
    result = op_instance.calculate(a, b)
    print(f"Result: {result}")