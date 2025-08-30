# BATCH8_PROMPT3_Granite.py

from abc import ABC, abstractmethod


class Operation(ABC):
    @abstractmethod
    def calculate(self, a, b):
        pass


class Add(Operation):
    def calculate(self, a, b):
        return a + b


class Subtract(Operation):
    def calculate(self, a, b):
        return a - b


class CalculationFactory:
    @staticmethod
    def create_operation(operation_type):
        operations = {
            'add': Add(),
            'subtract': Subtract()
        }
        return operations.get(operation_type, None)


def main():
    print("Unnecessary Object-Oriented Calculator")

    while True:
        operation_input = input("Enter operation ('quit' to exit): ").strip().lower()

        if operation_input == 'quit':
            break

        operation_factory = CalculationFactory()
        operation_instance = operation_factory.create_operation(operation_input)

        if operation_instance is None:
            print("Invalid operation type.")
            continue

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        result = operation_instance.calculate(num1, num2)
        print(f"Result: {result}")


if __name__ == "__main__":
    main()