# BATCH8_PROMPT4_{{model_name}}.py

class NumberHolder:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value

class Logger:
    def log(self, message):
        print(f"Log: {message}")

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

class UnnecessaryObjectOrientedCalculator(NumberHolder, Logger, Calculator):
    def __init__(self, initial_value):
        NumberHolder.__init__(self, initial_value)
        Logger.__init__(self)

    def calculate_and_log(self, operation, *args):
        if operation == 'add':
            result = self.add(self.get_value(), args[0])
        elif operation == 'subtract':
            result = self.subtract(self.get_value(), args[0])
        else:
            raise ValueError("Unsupported operation")
        
        self.log(f"Operation: {operation}, Result: {result}")
        return result

if __name__ == "__main__":
    calc = UnnecessaryObjectOrientedCalculator(10)
    result = calc.calculate_and_log('add', 5)
    print(f"Final result: {result}")