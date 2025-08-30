# BATCH8_PROMPT7_Granite.py

from abc import ABC, abstractmethod


class OperationStrategy(ABC):
    @abstractmethod
    def calculate(self, a, b):
        pass


class AddStrategy(OperationStrategy):
    def calculate(self, a, b):
        return a + b


class SubtractStrategy(OperationStrategy):
    def calculate(self, a, b):
        return a - b


class Calculator:
    def __init__(self, strategy: OperationStrategy):
        self.strategy = strategy

    def execute(self, a, b):
        return self.strategy.calculate(a, b)


def main():
    print("Unnecessary Object-Oriented Calculator")

    # Example usages
    calc_add = Calculator(AddStrategy())
    result_add = calc_add.execute(5, 3)
    print(f"Addition: {result_add}")  # Output: Addition: 8

    calc_sub = Calculator(SubtractStrategy())
    result_sub = calc_sub.execute(5, 3)
    print(f"Subtraction: {result_sub}")  # Output: Subtraction: 2


if __name__ == "__main__":
    main()