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

# ===== GENERATED TESTS =====
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

# BATCH4_PROMPT4_Devstral_test.py

import pytest
from BATCH4_PROMPT4_Devstral import MathOperation, Add, Subtract, Multiply, Divide, Calculator

@pytest.fixture
def calculator():
    return Calculator()

def test_mathoperation_compute_default_value(calculator):
    """Test the compute method of MathOperation with default value"""
    assert calculator.compute_result() == 0

def test_add_compute(calculator):
    """Test the compute method of Add class"""
    add_op = Add(5, 3)
    assert add_op.compute() == 8

def test_subtract_compute(calculator):
    """Test the compute method of Subtract class"""
    subtract_op = Subtract(10, 4)
    assert subtract_op.compute() == 6

def test_multiply_compute(calculator):
    """Test the compute method of Multiply class"""
    multiply_op = Multiply(3, 7)
    assert multiply_op.compute() == 21

def test_divide_compute(calculator):
    """Test the compute method of Divide class"""
    divide_op = Divide(8, 4)
    assert divide_op.compute() == 2.0

def test_calculator_add_operation(calculator):
    """Test adding an operation to Calculator"""
    add_op = Add(5, 3)
    calculator.add_operation(add_op)
    assert len(calculator.operations) == 1
    assert calculator.operations[0].compute() == 8

def test_calculator_compute_result(calculator):
    """Test computing the result of multiple operations in Calculator"""
    calc = Calculator()
    add_op = Add(5, 3)
    calc.add_operation(add_op)

    multiply_op = Multiply(add_op, 2)
    calc.add_operation(multiply_op)

    subtract_op = Subtract(multiply_op, 4)
    calc.add_operation(subtract_op)

    divide_op = Divide(subtract_op, 2)
    calc.add_operation(divide_op)

    result = calc.compute_result()
    assert result == 6.0

def test_calculator_division_by_zero(calculator):
    """Test division by zero in Calculator"""
    divide_op = Divide(8, 0)
    with pytest.raises(ZeroDivisionError):
        divide_op.compute()

def test_calculator_invalid_operation_type(calculator):
    """Test adding an invalid operation type to Calculator"""
    with pytest.raises(TypeError):
        calculator.add_operation("not a MathOperation instance")

# End of BATCH4_PROMPT4_Devstral_test.py
