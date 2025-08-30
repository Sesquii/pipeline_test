class GlobalCalculator:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(GlobalCalculator, cls).__new__(cls)
            # Initialize any instance-specific data here if needed
        return cls._instance

    def add(self, a, b):
        """Add two numbers."""
        return a + b

    def subtract(self, a, b):
        """Subtract the second number from the first."""
        return a - b

    def multiply(self, a, b):
        """Multiply two numbers."""
        return a * b

    def divide(self, a, b):
        """Divide the first number by the second. Return None if division by zero."""
        if b == 0:
            print("Error: Division by zero")
            return None
        return a / b

if __name__ == "__main__":
    # Create the first instance
    calc1 = GlobalCalculator()
    print(f"First instance ID: {id(calc1)}")

    # Attempt to create a second instance - should return the same object
    calc2 = GlobalCalculator()
    print(f"Second instance ID: {id(calc2)}")

    # Verify both variables point to the same object
    if id(calc1) == id(calc2):
        print("Singleton pattern confirmed: Both instances are the same.")
    else:
        print("Error: Instances are different!")

    # Demonstrate calculator functionality
    print("\nCalculator operations:")
    print(f"Addition: 5 + 3 = {calc1.add(5, 3)}")
    print(f"Subtraction: 10 - 4 = {calc1.subtract(10, 4)}")
    print(f"Multiplication: 7 * 6 = {calc1.multiply(7, 6)}")
    print(f"Division: 20 / 4 = {calc1.divide(20, 4)}")
    print(f"Division by zero: 5 / 0 = {calc1.divide(5, 0)}")