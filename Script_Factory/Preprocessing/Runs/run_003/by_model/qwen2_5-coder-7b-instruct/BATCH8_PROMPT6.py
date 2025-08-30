class GlobalCalculator:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(GlobalCalculator, cls).__new__(cls)
            # Initialize arithmetic methods here if needed
        return cls._instance

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            raise ValueError("Cannot divide by zero")

if __name__ == "__main__":
    # Create an instance of GlobalCalculator
    calc1 = GlobalCalculator()
    
    # Perform arithmetic operations using the singleton instance
    print(calc1.add(5, 3))       # Output: 8
    print(calc1.subtract(5, 3))  # Output: 2
    print(calc1.multiply(5, 3))  # Output: 15
    print(calc1.divide(5, 3))    # Output: 1.6666666666666667
    
    # Attempt to create a second instance
    calc2 = GlobalCalculator()
    
    # Check if both instances are the same
    print(calc1 is calc2)        # Output: True
    
    # Perform an operation with the second "instance"
    print(calc2.add(4, 2))       # Output: 6