```python
from abc import ABC, abstractmethod

# Abstract base class for calculator operations
class Strategy(ABC):
    @abstractmethod
    def calculate(self, a, b):
        pass

# Concrete strategies for different operations
class AddStrategy(Strategy):
    def calculate(self, a, b):
        return a + b

class SubtractStrategy(Strategy):
    def calculate(self, a, b):
        return a - b

# Calculator class that uses the strategy pattern
class Calculator:
    def __init__(self, strategy: Strategy):
        self.strategy = strategy

    def execute(self, a, b):
        return self.strategy.calculate(a, b)

if __name__ == "__main__":
    # Example usage of different strategies
    add_calculator = Calculator(AddStrategy())
    subtract_calculator = Calculator(SubtractStrategy())

    print("Adding 5 and 3:", add_calculator.execute(5, 3))
    print("Subtracting 5 and 3:", subtract_calculator.execute(5, 3))