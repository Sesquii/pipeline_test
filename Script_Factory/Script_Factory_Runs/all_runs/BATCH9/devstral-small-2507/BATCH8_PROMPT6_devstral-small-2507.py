class GlobalCalculator:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(GlobalCalculator, cls).__new__(cls)
            # Initialize any necessary state here
        return cls._instance

    def add(self, a, b):
        """Add two numbers"""
        return a + b

    def subtract(self, a, b):
        """Subtract the second number from the first"""
        return a - b

    def multiply(self, a, b):
        """Multiply two numbers"""
        return a * b

    def divide(self, a, b):
        """Divide the first number by the second"""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

if __name__ == "__main__":
    # Demonstrate singleton behavior
    calculator1 = GlobalCalculator()
    calculator2 = GlobalCalculator()

    print(f"calculator1 id: {id(calculator1)}")  # Should show the same object ID
    print(f"calculator2 id: {id(calculator2)}")  # Should show the same object ID

    if calculator1 is calculator2:
        print("Singleton works - both variables point to the same instance")
    else:
        print("Singleton failed - different instances created")

    # Demonstrate basic arithmetic operations
    print(f"5 + 3 = {calculator1.add(5, 3)}")
    print(f"7 - 2 = {calculator1.subtract(7, 2)}")
    print(f"4 * 6 = {calculator1.multiply(4, 6)}")
    print(f"8 / 2 = {calculator1.divide(8, 2)}")

    # Try to create a second instance (should return the original)
    calculator3 = GlobalCalculator()
    if calculator3 is calculator1:
        print("Attempt to create second instance returns original instance")
    else:
        print("Second instance creation failed - different object returned")