# BATCH8_PROMPT7_Devstral.py

from abc import ABC, abstractmethod

class Strategy(ABC):
    """Abstract base class for calculation strategies."""
    
    @abstractmethod
    def calculate(self, a: float, b: float) -> float:
        pass

class AddStrategy(Strategy):
    """Concrete strategy for addition."""
    
    def calculate(self, a: float, b: float) -> float:
        return a + b

class SubtractStrategy(Strategy):
    """Concrete strategy for subtraction."""
    
    def calculate(self, a: float, b: float) -> float:
        return a - b

class MultiplyStrategy(Strategy):
    """Concrete strategy for multiplication."""
    
    def calculate(self, a: float, b: float) -> float:
        return a * b

class DivideStrategy(Strategy):
    """Concrete strategy for division."""
    
    def calculate(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

class Calculator:
    """Calculator class that uses strategy pattern for operations."""
    
    def __init__(self, strategy: Strategy):
        self._strategy = strategy
    
    def execute(self, a: float, b: float) -> float:
        """Execute the calculation using the current strategy."""
        return self._strategy.calculate(a, b)

if __name__ == "__main__":
    # Example usage of the calculator with different strategies
    calc_add = Calculator(AddStrategy())
    print(f"5 + 3 = {calc_add.execute(5, 3)}")

    calc_subtract = Calculator(SubtractStrategy())
    print(f"10 - 4 = {calc_subtract.execute(10, 4)}")

    calc_multiply = Calculator(MultiplyStrategy())
    print(f"7 * 6 = {calc_multiply.execute(7, 6)}")

    calc_divide = Calculator(DivideStrategy())
    try:
        print(f"20 / 4 = {calc_divide.execute(20, 4)}")
        print(f"5 / 0 = {calc_divide.execute(5, 0)}")  # This will raise an exception
    except ValueError as e:
        print(e)