# BATCH8_PROMPT3_Devstral.py

class CalculationFactory:
    """Factory class to create different calculation operation classes."""

    @staticmethod
    def create_calculation(operation_type):
        """Create and return an instance of the requested operation class.

        Args:
            operation_type (str): Type of calculation to perform ('add' or 'subtract')

        Returns:
            Calculation: An instance of the requested calculation class.
        """
        if operation_type == 'add':
            return Add()
        elif operation_type == 'subtract':
            return Subtract()
        else:
            raise ValueError(f"Unsupported operation type: {operation_type}")

class Calculation:
    """Base class for all calculation operations."""
    
    def perform(self, a, b):
        """Perform the calculation with given operands.

        Args:
            a (float): First operand
            b (float): Second operand

        Returns:
            float: Result of the calculation
        """
        raise NotImplementedError("This method should be overridden by subclasses")

class Add(Calculation):
    """Class to perform addition operations."""
    
    def perform(self, a, b):
        return a + b

class Subtract(Calculation):
    """Class to perform subtraction operations."""
    
    def perform(self, a, b):
        return a - b

def main():
    """Main entry point of the program."""
    # Get user input for operation type and operands
    operation_type = input("Enter operation (add/subtract): ").strip().lower()
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    try:
        # Create calculation instance using the factory
        calculator = CalculationFactory.create_calculation(operation_type)

        # Perform the calculation
        result = calculator.perform(a, b)
        print(f"Result: {result}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()