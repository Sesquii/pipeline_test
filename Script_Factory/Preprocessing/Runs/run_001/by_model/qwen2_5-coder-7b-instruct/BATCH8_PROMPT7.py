# BATCH8_PROMPT7_{{model_name}}.py

class OperationStrategy:
    """Base class for all operation strategies."""
    def calculate(self, a, b):
        pass

class AddStrategy(OperationStrategy):
    """Strategy to add two numbers."""
    def calculate(self, a, b):
        return a + b

class SubtractStrategy(OperationStrategy):
    """Strategy to subtract two numbers."""
    def calculate(self, a, b):
        return a - b

class Calculator:
    """
    Calculator class that uses an operation strategy.
    
    :param strategy: An instance of OperationStrategy
    """
    def __init__(self, strategy: OperationStrategy):
        self.strategy = strategy
    
    def execute(self, a, b):
        """
        Executes the calculation using the current strategy.
        
        :param a: First number
        :param b: Second number
        :return: Result of the calculation
        """
        return self.strategy.calculate(a, b)

# Entry point for the script
if __name__ == "__main__":
    # Create instances of strategies
    add_strategy = AddStrategy()
    subtract_strategy = SubtractStrategy()
    
    # Create calculator instances with different strategies
    add_calculator = Calculator(add_strategy)
    subtract_calculator = Calculator(subtract_strategy)
    
    # Perform calculations
    print("Addition: ", add_calculator.execute(5, 3))
    print("Subtraction: ", subtract_calculator.execute(5, 3))