# BATCH4_PROMPT4_Devstral.py

class MathOperation:
    """Base class for all mathematical operations"""

    def __init__(self, value=0):
        self.value = value

    def compute(self):
        return self.value

class Add(MathOperation):
    """Class to handle addition operation"""

    def __init__(self, operand1, operand2):
        super().__init__()
        self.operand1 = operand1
        self.operand2 = operand2

    def compute(self):
        return self.operand1 + self.operand2

class Subtract(MathOperation):
    """Class to handle subtraction operation"""

    def __init__(self, operand1, operand2):
        super().__init__()
        self.operand1 = operand1
        self.operand2 = operand2

    def compute(self):
        return self.operand1 - self.operand2

class Multiply(MathOperation):
    """Class to handle multiplication operation"""

    def __init__(self, operand1, operand2):
        super().__init__()
        self.operand1 = operand1
        self.operand2 = operand2

    def compute(self):
        return self.operand1 * self.operand2

class Divide(MathOperation):
    """Class to handle division operation"""

    def __init__(self, operand1, operand2):
        super().__init__()
        self.operand1 = operand1
        self.operand2 = operand2

    def compute(self):
        return self.operand1 / self.operand2

class Calculator:
    """Main calculator class that chains operations together"""

    def __init__(self, operations=None):
        self.operations = operations if operations else []

    def add_operation(self, operation):
        self.operations.append(operation)

    def compute_result(self):
        result = 0
        for operation in self.operations:
            result = operation.compute()
        return result

if __name__ == "__main__":
    # Example calculation: (5 + 3) * 2 - 4 / 2
    calc = Calculator()

    # First, add the addition operation
    add_op = Add(5, 3)
    calc.add_operation(add_op)

    # Then multiply the result by 2
    multiply_op = Multiply(add_op, 2)
    calc.add_operation(multiply_op)

    # Subtract 4 from the previous result
    subtract_op = Subtract(multiply_op, 4)
    calc.add_operation(subtract_op)

    # Finally, divide by 2  
    divide_op = Divide(subtract_op, 2)
    calc.add_operation(divide_op)

    # Get the final result
    result = calc.compute_result()
    print(f"Calculation result: {result}")