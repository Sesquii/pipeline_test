# BATCH8_PROMPT4_Granite.py

class NumberHolder:
    """Base class to hold a number."""

    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value


class Logger:
    """Base class for logging operations."""

    def log_operation(self, operation):
        print(f"Logging operation: {operation}")


class Calculator:
    """Base class for simple calculations."""

    def add(self, num1, num2):
        return num1 + num2


class UnnecessaryCalculator(NumberHolder, Logger, Calculator):
    """Final class that combines all functionalities in an unnecessary way."""

    def perform_calculation(self, num1, num2):
        # Get values from NumberHolder (redundant as they're already held)
        value1 = self.get_value()

        # Log the operation (unnecessary since Calculator already does this internally)
        self.log_operation("Addition")

        # Perform addition (unnecessarily calling a method from each parent class)
        result = NumberHolder.add(self, num2)  # This will raise an AttributeError

        return result


def main():
    # Create an instance of UnnecessaryCalculator
    calc = UnnecessaryCalculator(5)

    # Perform calculation in a roundabout way
    final_result = calc.perform_calculation(3, 4)

    print(f"The result is: {final_result}")


if __name__ == "__main__":
    main()