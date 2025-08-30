# BATCH8_PROMPT4_Devstral.py

class NumberHolder:
    """Class to hold and manipulate numbers."""

    def __init__(self, value=0):
        self.value = value

    def set_value(self, value):
        """Set the held number."""
        self.value = value

    def get_value(self):
        """Return the held number."""
        return self.value

class Logger:
    """Class to log messages."""

    def log(self, message):
        """Log a message with timestamp."""
        from datetime import datetime
        print(f"[{datetime.now()}] {message}")

class Calculator:
    """Class to perform simple calculations."""

    @staticmethod
    def add(a, b):
        """Add two numbers."""
        return a + b

    @staticmethod
    def subtract(a, b):
        """Subtract the second number from the first."""
        return a - b

class UnnecessaryOOCalculator(NumberHolder, Logger, Calculator):
    """A roundabout calculator using multiple inheritance."""

    def calculate(self, operation, value2):
        """
        Perform calculation in an unnecessarily complex way:
        1. Get current value
        2. Log the operation being performed  
        3. Use Calculator methods to perform operation
        4. Set new value
        """
        # Step 1: Get current value from NumberHolder
        current_value = self.get_value()

        # Step 2: Log what we're doing (from Logger)
        if operation == "add":
            self.log(f"Adding {value2} to current value")
        elif operation == "subtract":
            self.log(f"Subtracting {value2} from current value")

        # Step 3: Perform calculation using Calculator methods
        if operation == "add":
            result = self.add(current_value, value2)
        elif operation == "subtract":
            result = self.subtract(current_value, value2)

        # Step 4: Set new value back to NumberHolder
        self.set_value(result)

    def get_result(self):
        """Return the current calculated value."""
        return self.get_value()

# Entry point for the program
if __name__ == "__main__":
    # Create our unnecessary OO calculator
    calc = UnnecessaryOOCalculator(10)  # Start with initial value of 10

    print("Initial value:", calc.get_result())

    # Perform some operations in a roundabout way
    calc.calculate("add", 5)
    print("After adding 5:", calc.get_result())

    calc.calculate("subtract", 3)
    print("After subtracting 3:", calc.get_result())