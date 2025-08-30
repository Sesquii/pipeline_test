# BATCH8_PROMPT4_{{model_name}}.py

# Base class to hold a number and provide basic operations
class NumberHolder:
    def __init__(self, number):
        self.number = number
    
    def get_number(self):
        return self.number
    
    def set_number(self, number):
        self.number = number

# Base class to handle logging of messages
class Logger:
    def log(self, message):
        print(f"Log: {message}")

# Base class for basic arithmetic operations
class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b

# Final class inheriting from NumberHolder, Logger, and Calculator
class UnnecessaryObjectOrientedCalculator(NumberHolder, Logger, Calculator):
    def __init__(self, number):
        super().__init__(number)
    
    def perform_calculation(self):
        # Get the current number using NumberHolder's method
        number = self.get_number()
        
        # Add 5 to the number using Calculator's method
        result_add = self.add(number, 5)
        
        # Subtract 2 from the result using Calculator's method
        final_result = self.subtract(result_add, 2)
        
        # Log the final result using Logger's method
        self.log(f"Final Result: {final_result}")
        
        return final_result

# Entry point of the program
if __name__ == "__main__":
    calculator = UnnecessaryObjectOrientedCalculator(10)
    calculator.perform_calculation()
```

This Python script defines an "Unnecessary Object-Oriented Calculator" using multiple inheritance. It includes three base classes: `NumberHolder` for holding and manipulating a number, `Logger` for logging messages, and `Calculator` for basic arithmetic operations. The final class, `UnnecessaryObjectOrientedCalculator`, inherits from all three base classes and demonstrates calling methods from the parent classes in a roundabout way to perform a simple calculation (adding 5 and then subtracting 2 from an initial number).