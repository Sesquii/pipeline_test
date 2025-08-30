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

# ===== GENERATED TESTS =====
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

# BATCH8_PROMPT3_Devstral_test.py

import pytest
from BATCH8_PROMPT3_Devstral import CalculationFactory, Add, Subtract

def test_create_calculation_add():
    """Test the creation of an 'add' operation."""
    factory = CalculationFactory()
    operation = factory.create_calculation('add')
    assert isinstance(operation, Add)

def test_create_calculation_subtract():
    """Test the creation of a 'subtract' operation."""
    factory = CalculationFactory()
    operation = factory.create_calculation('subtract')
    assert isinstance(operation, Subtract)

def test_create_calculation_invalid():
    """Test the creation with an invalid operation type."""
    factory = CalculationFactory()
    with pytest.raises(ValueError) as excinfo:
        factory.create_calculation('multiply')
    assert "Unsupported operation type" in str(excinfo.value)

def test_add_calculate():
    """Test the calculate method of the Add class."""
    add_operation = Add()
    result = add_operation.calculate(5, 3)
    assert result == 8

def test_subtract_calculate():
    """Test the calculate method of the Subtract class."""
    subtract_operation = Subtract()
    result = subtract_operation.calculate(5, 3)
    assert result == 2

# Add more tests as needed
