```python
import sys

class Strategy:
    @abstractmethod
    def calculate(self, a, b):
        pass

class AddStrategy(Strategy):
    def calculate(self, a, b):
        return a + b

class SubtractStrategy(Strategy):
    def calculate(self, a, b):
        return a - b

class MultiplyStrategy(Strategy):
    def calculate(self, a, b):
        return a * b

class DivideStrategy(Strategy):
    def calculate(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

class Calculator:
    def __init__(self, strategy):
        self.strategy = strategy

    def execute(self, a, b):
        return self.strategy.calculate(a, b)

if __name__ == "__main__":
    # Example usage of the calculator with different strategies
    add_strategy = AddStrategy()
    calc = Calculator(add_strategy)
    print("Addition:", calc.execute(5, 3))

    sub_strategy = SubtractStrategy()
    calc = Calculator(sub_strategy)
    print("Subtraction:", calc.execute(10, 4))

    mul_strategy = MultiplyStrategy()
    calc = Calculator(mul_strategy)
    print("Multiplication:", calc.execute(2, 3))

    div_strategy = DivideStrategy()
    calc = Calculator(div_strategy)
    print("Division:", calc.execute(10, 2))