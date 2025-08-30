# BATCH8_PROMPT3_Devstral.py

class CalculationFactory:
    """Factory class to create different calculation operation objects."""

    @staticmethod
    def create_calculation(operation_type):
        """
        Create a new instance of the requested operation class.

        Args:
            operation_type (str): The type of operation to create ('add' or 'subtract').

        Returns:
            An instance of the appropriate operation class.
        """
        if operation_type == 'add':
            return Add()
        elif operation_type == 'subtract':
            return Subtract()
        else:
            raise ValueError(f"Unsupported operation type: {operation_type}")

class Operation:
    """Base class for all calculation operations."""

    def calculate(self, a, b):
        """
        Perform the calculation with given operands.

        Args:
            a (float): First operand.
            b (float): Second operand.

        Returns:
            float: Result of the operation.
        """
        raise NotImplementedError("This method should be overridden by subclasses")

class Add(Operation):
    """Class to perform addition."""

    def calculate(self, a, b):
        return a + b

class Subtract(Operation):
    """Class to perform subtraction."""

    def calculate(self, a, b):
        return a - b

def main():
    """Main function to demonstrate the calculator."""

    # Create factory instance (though static methods don't require instantiation)
    factory = CalculationFactory()

    # Get user input for operation type
    operation_type = input("Enter operation (add/subtract): ").strip().lower()

    try:
        # Create the appropriate operation object
        operation = factory.create_calculation(operation_type)

        # Get operands from user
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        # Perform the calculation
        result = operation.calculate(a, b)

        print(f"Result of {operation_type}: {result}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()