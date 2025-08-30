# BATCH8_PROMPT7_{{model_name}}.py

class OperationStrategy:
    """Abstract base class for operation strategies."""
    
    def calculate(self, x, y):
        raise NotImplementedError("This method should be overridden by subclasses")

class AddStrategy(OperationStrategy):
    """Addition strategy implementation."""
    
    def calculate(self, x, y):
        return x + y

class SubtractStrategy(OperationStrategy):
    """Subtraction strategy implementation."""
    
    def calculate(self, x, y):
        return x - y

class Calculator:
    """Calculator class that uses an operation strategy to perform calculations."""
    
    def __init__(self, strategy: OperationStrategy):
        self.strategy = strategy
    
    def execute(self, x, y):
        """Execute the calculation using the current strategy."""
        return self.strategy.calculate(x, y)

if __name__ == "__main__":
    # Example usage:
    add_strategy = AddStrategy()
    calculator_add = Calculator(add_strategy)
    print("5 + 3 =", calculator_add.execute(5, 3))
    
    subtract_strategy = SubtractStrategy()
    calculator_subtract = Calculator(subtract_strategy)
    print("5 - 3 =", calculator_subtract.execute(5, 3))