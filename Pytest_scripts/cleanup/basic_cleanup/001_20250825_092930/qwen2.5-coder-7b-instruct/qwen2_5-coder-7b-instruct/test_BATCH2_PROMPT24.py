# BATCH2_PROMPT24_{{model_name}}.py

class BaseOperation:
    """Base class for all operations."""
    def __init__(self, value):
        self.value = value
    
    def perform(self):
        raise NotImplementedError("This method should be overridden by subclasses.")

class Add(BaseOperation):
    """Class for addition operation."""
    def __init__(self, value, addend):
        super().__init__(value)
        self.addend = addend
    
    def perform(self):
        return self.value + self.addend

class Subtract(BaseOperation):
    """Class for subtraction operation."""
    def __init__(self, value, subtrahend):
        super().__init__(value)
        self.subtrahend = subtrahend
    
    def perform(self):
        return self.value - self.subtrahend

class Multiply(BaseOperation):
    """Class for multiplication operation."""
    def __init__(self, value, multiplier):
        super().__init__(value)
        self.multiplier = multiplier
    
    def perform(self):
        return self.value * self.multiplier

class Divide(BaseOperation):
    """Class for division operation."""
    def __init__(self, value, divisor):
        super().__init__(value)
        self.divisor = divisor
    
    def perform(self):
        if self.divisor == 0:
            raise ValueError("Division by zero is not allowed.")
        return self.value / self.divisor

if __name__ == "__main__":
    # Example usage
    initial_value = 10
    add_operation = Add(initial_value, 5)
    subtract_operation = Subtract(add_operation.perform(), 3)
    multiply_operation = Multiply(subtract_operation.perform(), 2)
    divide_operation = Divide(multiply_operation.perform(), 4)

    result = divide_operation.perform()
    print(f"The final result is: {result}")

This Python script defines a base class `BaseOperation` and subclasses for each mathematical operation (`Add`, `Subtract`, `Multiply`, `Divide`). It demonstrates how to chain these operations together in the `if __name__ == "__main__":` block to perform a complex calculation. The example usage shows adding 5, subtracting 3, multiplying by 2, and finally dividing by 4 on an initial value of 10, resulting in a final output of 6.

# ===== GENERATED TESTS =====
# BATCH2_PROMPT24_{{model_name}}.py

class BaseOperation:
    """Base class for all operations."""
    def __init__(self, value):
        self.value = value
    
    def perform(self):
        raise NotImplementedError("This method should be overridden by subclasses.")

class Add(BaseOperation):
    """Class for addition operation."""
    def __init__(self, value, addend):
        super().__init__(value)
        self.addend = addend
    
    def perform(self) -> int:
        return self.value + self.addend

class Subtract(BaseOperation):
    """Class for subtraction operation."""
    def __init__(self, value, subtrahend):
        super().__init__(value)
        self.subtrahend = subtrahend
    
    def perform(self) -> int:
        return self.value - self.subtrahend

class Multiply(BaseOperation):
    """Class for multiplication operation."""
    def __init__(self, value, multiplier):
        super().__init__(value)
        self.multiplier = multiplier
    
    def perform(self) -> int:
        return self.value * self.multiplier

class Divide(BaseOperation):
    """Class for division operation."""
    def __init__(self, value, divisor):
        super().__init__(value)
        self.divisor = divisor
    
    def perform(self) -> float:
        if self.divisor == 0:
            raise ValueError("Division by zero is not allowed.")
        return self.value / self.divisor

if __name__ == "__main__":
    # Example usage
    initial_value = 10
    add_operation = Add(initial_value, 5)
    subtract_operation = Subtract(add_operation.perform(), 3)
    multiply_operation = Multiply(subtract_operation.perform(), 2)
    divide_operation = Divide(multiply_operation.perform(), 4)

    result = divide_operation.perform()
    print(f"The final result is: {result}")

# Test cases
import pytest

@pytest.fixture
def base_operation():
    return BaseOperation(10)

@pytest.fixture
def add_operation(base_operation):
    return Add(base_operation.value, 5)

@pytest.fixture
def subtract_operation(add_operation):
    return Subtract(add_operation.perform(), 3)

@pytest.fixture
def multiply_operation(subtract_operation):
    return Multiply(subtract_operation.perform(), 2)

@pytest.fixture
def divide_operation(multiply_operation):
    return Divide(multiply_operation.perform(), 4)

def test_addition(add_operation: Add) -> None:
    """Test the addition operation."""
    assert add_operation.perform() == 15

def test_subtraction(subtract_operation: Subtract) -> None:
    """Test the subtraction operation."""
    assert subtract_operation.perform() == 7

def test_multiplication(multiply_operation: Multiply) -> None:
    """Test the multiplication operation."""
    assert multiply_operation.perform() == 14

def test_division(divide_operation: Divide) -> None:
    """Test the division operation."""
    assert divide_operation.perform() == 3.5

def test_division_by_zero():
    """Test division by zero exception."""
    with pytest.raises(ValueError):
        Divide(10, 0).perform()

def test_base_operation(base_operation: BaseOperation) -> None:
    """Test the base operation class initialization."""
    assert base_operation.value == 10
