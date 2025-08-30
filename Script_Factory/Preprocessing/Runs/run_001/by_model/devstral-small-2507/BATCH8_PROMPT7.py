# BATCH8_PROMPT7_Devstral.py

class Strategy:
    """Interface for all strategy objects"""
    def calculate(self, num1, num2):
        raise NotImplementedError("This method should be overridden in subclasses")

class AddStrategy(Strategy):
    """Concrete strategy for addition operation"""
    def calculate(self, num1, num2):
        return num1 + num2

class SubtractStrategy(Strategy):
    """Concrete strategy for subtraction operation"""
    def calculate(self, num1, num2):
        return num1 - num2

class MultiplyStrategy(Strategy):
    """Concrete strategy for multiplication operation"""
    def calculate(self, num1, num2):
        return num1 * num2

class DivideStrategy(Strategy):
    """Concrete strategy for division operation"""
    def calculate(self, num1, num2):
        if num2 == 0:
            raise ValueError("Cannot divide by zero")
        return num1 / num2

class Calculator:
    """Calculator class that uses a strategy pattern for operations"""
    def __init__(self, strategy: Strategy):
        self._strategy = strategy

    def execute(self, num1, num2):
        """Execute the calculation using the current strategy"""
        return self._strategy.calculate(num1, num2)

if __name__ == "__main__":
    # Example usage
    add_calculator = Calculator(AddStrategy())
    print(f"5 + 3 = {add_calculator.execute(5, 3)}")  # Output: 8

    subtract_calculator = Calculator(SubtractStrategy())
    print(f"10 - 4 = {subtract_calculator.execute(10, 4)}")  # Output: 6

    multiply_calculator = Calculator(MultiplyStrategy())
    print(f"7 * 6 = {multiply_calculator.execute(7, 6)}")  # Output: 42

    divide_calculator = Calculator(DivideStrategy())
    try:
        print(f"15 / 3 = {divide_calculator.execute(15, 3)}")  # Output: 5.0
        print(f"8 / 0 = {divide_calculator.execute(8, 0)}")  # This will raise ValueError
    except ValueError as e:
        print(f"Error: {e}")