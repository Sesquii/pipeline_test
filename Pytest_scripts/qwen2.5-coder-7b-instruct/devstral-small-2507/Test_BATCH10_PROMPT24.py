# BATCH10_PROMPT24_Devstral.py

class Digit:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def __str__(self):
        return str(self.value)

class Number:
    def __init__(self, digits=None):
        if digits is None:
            digits = []
        self.digits = digits

    def add_digit(self, digit):
        self.digits.append(digit)

    def get_value(self):
        number_str = ''.join([str(digit.get_value()) for digit in self.digits])
        return int(number_str) if number_str else 0

    def __str__(self):
        return ''.join([str(digit) for digit in self.digits])

class Calculator:
    def add(self, num1, num2):
        return Number(value=num1.get_value() + num2.get_value())

    def subtract(self, num1, num2):
        return Number(value=num1.get_value() - num2.get_value())

    def multiply(self, num1, num2):
        return Number(value=num1.get_value() * num2.get_value())

    def divide(self, num1, num2):
        if num2.get_value() == 0:
            raise ValueError("Cannot divide by zero")
        return Number(value=num1.get_value() / num2.get_value())

def main():
    # Create digits for number 123
    num1_digits = [Digit(1), Digit(2), Digit(3)]
    num1 = Number(num1_digits)

    # Create digits for number 456
    num2_digits = [Digit(4), Digit(5), Digit(6)]
    num2 = Number(num2_digits)

    calculator = Calculator()

    print(f"Number 1: {num1}")
    print(f"Number 2: {num2}")

    # Perform addition
    sum_result = calculator.add(num1, num2)
    print(f"Sum: {sum_result.get_value()}")

    # Perform subtraction
    diff_result = calculator.subtract(num1, num2)
    print(f"Difference: {diff_result.get_value()}")

    # Perform multiplication
    prod_result = calculator.multiply(num1, num2)
    print(f"Product: {prod_result.get_value()}")

    # Perform division
    try:
        div_result = calculator.divide(num1, num2)
        print(f"Quotient: {div_result.get_value()}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()

# ===== GENERATED TESTS =====
```python
# BATCH10_PROMPT24_Devstral.py

class Digit:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def __str__(self):
        return str(self.value)

class Number:
    def __init__(self, digits=None):
        if digits is None:
            digits = []
        self.digits = digits

    def add_digit(self, digit):
        self.digits.append(digit)

    def get_value(self):
        number_str = ''.join([str(digit.get_value()) for digit in self.digits])
        return int(number_str) if number_str else 0

    def __str__(self):
        return ''.join([str(digit) for digit in self.digits])

class Calculator:
    def add(self, num1, num2):
        return Number(value=num1.get_value() + num2.get_value())

    def subtract(self, num1, num2):
        return Number(value=num1.get_value() - num2.get_value())

    def multiply(self, num1, num2):
        return Number(value=num1.get_value() * num2.get_value())

    def divide(self, num1, num2):
        if num2.get_value() == 0:
            raise ValueError("Cannot divide by zero")
        return Number(value=num1.get_value() / num2.get_value())

def main():
    # Create digits for number 123
    num1_digits = [Digit(1), Digit(2), Digit(3)]
    num1 = Number(num1_digits)

    # Create digits for number 456
    num2_digits = [Digit(4), Digit(5), Digit(6)]
    num2 = Number(num2_digits)

    calculator = Calculator()

    print(f"Number 1: {num1}")
    print(f"Number 2: {num2}")

    # Perform addition
    sum_result = calculator.add(num1, num2)
    print(f"Sum: {sum_result.get_value()}")

    # Perform subtraction
    diff_result = calculator.subtract(num1, num2)
    print(f"Difference: {diff_result.get_value()}")

    # Perform multiplication
    prod_result = calculator.multiply(num1, num2)
    print(f"Product: {prod_result.get_value()}")

    # Perform division
    try:
        div_result = calculator.divide(num1, num2)
        print(f"Quotient: {div_result.get_value()}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()

# Test cases
import pytest

def test_digit_get_value():
    """Test the get_value method of Digit class."""
    digit = Digit(5)
    assert digit.get_value() == 5

def test_number_add_digit():
    """Test adding a digit to Number class."""
    number = Number()
    digit = Digit(3)
    number.add_digit(digit)
    assert len(number.digits) == 1
    assert number.digits[0].get_value() == 3

def test_number_get_value_empty():
    """Test get_value method of Number class with no digits."""
    number = Number()
    assert number.get_value() == 0

def test_calculator_add():
    """Test add method of Calculator class."""
    calculator = Calculator()
    num1 = Number([Digit(2), Digit(3)])
    num2 = Number([Digit(4), Digit(5)])
    result = calculator.add(num1, num2)
    assert result.get_value() == 68

def test_calculator_subtract():
    """Test subtract method of Calculator class."""
    calculator = Calculator()
    num1 = Number([Digit(7), Digit(8)])
    num2 = Number([Digit(3), Digit(4)])
    result = calculator.subtract(num1, num2)
    assert result.get_value() == 44

def test_calculator_multiply():
    """Test multiply method of Calculator class."""
    calculator = Calculator()
    num1 = Number([Digit(5), Digit(6)])
    num2 = Number([Digit(7), Digit(8)])
    result = calculator.multiply(num1, num2)
    assert result.get_value() == 3960

def test_calculator_divide():
    """Test divide method of Calculator class."""
    calculator = Calculator()
    num1 = Number([Digit(1), Digit(0), Digit(0)])
    num2 = Number([Digit(5)])
    result = calculator.divide(num1, num2)
    assert result.get_value() == 20

def test_calculator_divide_by_zero():
    """Test divide method of Calculator class with division by zero."""
    calculator = Calculator()
    num1 = Number([Digit(1), Digit(0), Digit(0)])
    num2 = Number([Digit(0)])
    with pytest.raises(ValueError):
        calculator.divide(num1, num2)
```