# BATCH8_PROMPT4_Granite.py

class NumberHolder:
    """Base class to hold numbers."""

    def __init__(self, number):
        self.number = number

    def get_number(self):
        return self.number


class Logger:
    """Base class for logging operations."""

    def log_operation(self, operation):
        print(f"Operation logged: {operation}")


class Calculator:
    """Base class for simple calculations."""

    def add(self, other):
        return self.get_number() + other.get_number()


class UnnecessaryCalculator(NumberHolder, Logger, Calculator):
    """Final class combining all functionalities in an unnecessary manner."""

    def __init__(self, number, log_message="Adding numbers"):
        NumberHolder.__init__(self, number)
        Logger.__init__(self)
        self.log_message = log_message

    def calculate(self, other):
        # Unnecessarily complex calculation process
        result = Calculator.add(self, other)
        
        # Logging the operation in a roundabout way
        self._logger_setup()  # Simulating setting up logger which should be done elsewhere
        Logger.log_operation(f"Adding {self.get_number()} and {other.get_number()}")

        return result

    def _logger_setup(self):
        """Simulates the setup of a logger."""
        pass


# Entry point for the program
if __name__ == "__main__":
    num1 = UnnecessaryCalculator(5, "Initial Addition")
    num2 = UnnecessaryCalculator(3)
    
    result = num1.calculate(num2)
    print(f"The result of the calculation is: {result}")