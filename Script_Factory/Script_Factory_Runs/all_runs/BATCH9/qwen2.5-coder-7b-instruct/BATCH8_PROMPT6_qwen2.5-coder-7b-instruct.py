# BATCH8_PROMPT6_{{model_name}}.py

class GlobalCalculator:
    _instance = None

    def __new__(cls):
        """
        Singleton method to control object creation.
        Ensures only one instance of GlobalCalculator is created.
        """
        if cls._instance is None:
            cls._instance = super(GlobalCalculator, cls).__new__(cls)
        return cls._instance

    def add(self, a, b):
        """Method to add two numbers."""
        return a + b

    def subtract(self, a, b):
        """Method to subtract two numbers."""
        return a - b

    def multiply(self, a, b):
        """Method to multiply two numbers."""
        return a * b

    def divide(self, a, b):
        """
        Method to divide two numbers.
        Raises ValueError if the divisor is zero.
        """
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

if __name__ == "__main__":
    # Create an instance of GlobalCalculator
    calculator1 = GlobalCalculator()
    
    # Perform some calculations
    print(f"Addition: {calculator1.add(5, 3)}")
    print(f"Subtraction: {calculator1.subtract(5, 3)}")
    print(f"Multiplication: {calculator1.multiply(5, 3)}")
    print(f"Division: {calculator1.divide(5, 3)}")
    
    # Attempt to create another instance
    calculator2 = GlobalCalculator()
    
    # Check if both instances are the same
    assert calculator1 is calculator2, "Instances should be the same."
    
    # Perform the same calculations with the second instance
    print(f"Addition: {calculator2.add(5, 3)}")
    print(f"Subtraction: {calculator2.subtract(5, 3)}")
    print(f"Multiplication: {calculator2.multiply(5, 3)}")
    print(f"Division: {calculator2.divide(5, 3)}")