# BATCH8_PROMPT7_Granite.py

from abc import ABC, abstractmethod


class OperationStrategy(ABC):
    @abstractmethod
    def calculate(self, a: float, b: float) -> float:
        pass


class AddStrategy(OperationStrategy):
    def calculate(self, a: float, b: float) -> float:
        return a + b


class SubtractStrategy(OperationStrategy):
    def calculate(self, a: float, b: float) -> float:
        return a - b


class Calculator:
    def __init__(self, operation_strategy: OperationStrategy):
        self.operation_strategy = operation_strategy

    def execute(self, a: float, b: float) -> float:
        return self.operation_strategy.calculate(a, b)


if __name__ == "__main__":
    # Example usage of the Calculator class with different strategies
    add_calc = Calculator(AddStrategy())
    subtract_calc = Calculator(SubtractStrategy())

    print("Addition result:", add_calc.execute(5, 3))  # Should output: Addition result: 8
    print("Subtraction result:", subtract_calc.execute(5, 3))  # Should output: Subtraction result: 2