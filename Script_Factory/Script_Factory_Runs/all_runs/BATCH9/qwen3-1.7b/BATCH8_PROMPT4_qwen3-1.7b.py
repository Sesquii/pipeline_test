```python
# BATCH8_PROMPT4_{{model_name}}.py
import sys

class NumberHolder:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value


class Logger:
    def log(self, message):
        print(f"Logged: {message}")


class Calculator:
    def add(self, a, b):
        return a + b


class CalculatedTool(NumberHolder, Logger, Calculator):
    def compute(self):
        # Roundabout way to perform calculation
        self.log("Starting computation")
        value = self.get_value()
        result = self.add(value, 5)
        self.log(f"Result: {result}")
        return result


if __name__ == "__main__":
    calculator_tool = CalculatedTool(10)
    print("Final result:", calculator_tool.compute())