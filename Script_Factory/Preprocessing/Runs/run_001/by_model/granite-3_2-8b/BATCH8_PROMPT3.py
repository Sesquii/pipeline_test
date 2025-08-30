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
    def create_operation(operation_str):
        operations = {
            'add': Add(),
            'subtract': Subtract()
        }

        if operation_str in operations:
            return operations[operation_str]
        else:
            raise ValueError(f"Unknown operation: {operation_str}")


def main():
    print("Unnecessary Object-Oriented Calculator")

    while True:
        operation_str = input("Enter operation (add/subtract) or 'quit' to exit: ")

        if operation_str.lower() == 'quit':
            break

        try:
            op_instance = CalculationFactory.create_operation(operation_str)
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            result = op_instance.calculate(num1, num2)
            print(f"Result: {result}")
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    main()