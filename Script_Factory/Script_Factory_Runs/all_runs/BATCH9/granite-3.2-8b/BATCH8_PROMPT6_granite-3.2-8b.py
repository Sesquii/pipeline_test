# BATCH8_PROMPT6_Granite.py

class GlobalCalculator:
    """Singleton Calculator Class"""

    # Private attribute to store instance
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(GlobalCalculator, cls).__new__(cls)
            print("Creating new GlobalCalculator instance")
        return cls.__instance

    def add(self, a, b):
        """Add two numbers"""
        return a + b

    def subtract(self, a, b):
        """Subtract second number from the first"""
        return a - b

    def multiply(self, a, b):
        """Multiply two numbers"""
        return a * b

    def divide(self, a, b):
        """Divide first number by the second (handle division by zero)"""
        if b != 0:
            return a / b
        else:
            print("Error: Division by zero is not allowed.")
            return None

if __name__ == "__main__":
    # Demonstrate singleton behavior
    calc1 = GlobalCalculator()

    try:
        calc2 = GlobalCalculator()
    except Exception as e:
        print(f"Failed to create another instance: {e}")

    print("Results:")
    print(calc1.add(5, 3))
    print(calc1.subtract(7, 4))
    print(calc1.multiply(2, 6))
    print(calc1.divide(8, 2))