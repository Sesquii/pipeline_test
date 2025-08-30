```python
# BATCH8_PROMPT4_{{model_name}}.py
"""
Unnecessary Object-Oriented Calculator using multiple inheritance
"""

class NumberHolder:
    def __init__(self, value):
        self._value = value
    
    def get_value(self):
        return self._value


class Logger:
    def log_info(self, message):
        print(f"Logging: {message}")


class TimeTracker(Logger):
    def log_time(self, message):
        print(f"Time: {message}")


class UnnecessaryCalculator(NumberHolder, Logger, TimeTracker):
    def compute(self):
        # Roundabout way to perform a calculation
        self.log_info("Starting computation")
        num1 = self.get_value()
        num2 = self.get_value()
        result = num1 + num2
        self.log_time(f"Result: {result}")
        return result


if __name__ == "__main__":
    calculator = UnnecessaryCalculator(5)
    print(calculator.compute())