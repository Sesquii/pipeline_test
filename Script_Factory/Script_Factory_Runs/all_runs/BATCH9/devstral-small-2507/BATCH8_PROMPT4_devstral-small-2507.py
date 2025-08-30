# BATCH8_PROMPT4_Devstral.py

class NumberHolder:
    """Base class that holds a number and provides simple operations."""
    
    def __init__(self, value=0):
        self.value = value
    
    def set_value(self, new_value):
        """Set the internal value."""
        self.value = new_value
    
    def get_value(self):
        """Get the current value."""
        return self.value

class Logger:
    """Base class that provides logging functionality."""
    
    def log(self, message):
        """Log a message to console."""
        print(f"LOG: {message}")

class Calculator:
    """Base class that performs simple calculations."""
    
    def add(self, a, b):
        """Add two numbers and return the result."""
        return a + b

    def subtract(self, a, b):
        """Subtract second number from first and return the result."""
        return a - b

class UnnecessaryOOCalculator(NumberHolder, Logger, Calculator):
    """Final class that combines NumberHolder, Logger, and Calculator functionalities."""
    
    def perform_calculation(self, operation, value):
        """
        Perform a calculation using multiple inheritance in an unnecessary way.

        Args:
            operation (str): The operation to perform ('add' or 'subtract')
            value (int): The number to add/subtract from current value

        Returns:
            int: Result of the calculation
        """
        self.log(f"Starting {operation} with value: {value}")

        # Get current value using NumberHolder method
        current_value = self.get_value()

        # Perform operation using Calculator methods
        if operation == 'add':
            result = self.add(current_value, value)
        elif operation == 'subtract':
            result = self.subtract(current_value, value)
        else:
            raise ValueError("Unsupported operation")

        # Set new value using NumberHolder method  
        self.set_value(result)

        # Log the result
        self.log(f"Result: {result}")

        return result

if __name__ == "__main__":
    # Create instance of UnnecessaryOOCalculator
    calculator = UnnecessaryOOCalculator(10)  # Start with value 10

    # Perform some calculations
    print("Adding 5:")
    calculator.perform_calculation('add', 5)
    
    print("\nSubtracting 3:")
    calculator.perform_calculation('subtract', 3)

    # Final state
    final_value = calculator.get_value()
    print(f"\nFinal value: {final_value}")