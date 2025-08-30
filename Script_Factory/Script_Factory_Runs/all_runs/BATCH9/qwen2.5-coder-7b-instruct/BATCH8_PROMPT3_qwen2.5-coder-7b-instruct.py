# BATCH8_PROMPT3_{{model_name}}.py

class Add:
    def execute(self, a, b):
        return a + b

class Subtract:
    def execute(self, a, b):
        return a - b

class CalculationFactory:
    @staticmethod
    def create_operation(operation_type):
        if operation_type == "add":
            return Add()
        elif operation_type == "subtract":
            return Subtract()
        else:
            raise ValueError("Unsupported operation type")

if __name__ == "__main__":
    # Example usage
    operation_type = input("Enter operation (add/subtract): ")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    try:
        operation = CalculationFactory.create_operation(operation_type)
        result = operation.execute(a, b)
        print(f"The result is {result}")
    except ValueError as e:
        print(e)
```

This Python program implements an "Unnecessary Object-Oriented Calculator" using a factory pattern. It defines two operation classes `Add` and `Subtract`, each with an `execute` method to perform the respective arithmetic operation. The `CalculationFactory` class has a static method `create_operation` that returns an instance of the requested operation class based on user input. The main part of the program prompts the user for the operation type and numbers, creates the appropriate operation object using the factory, and prints the result.