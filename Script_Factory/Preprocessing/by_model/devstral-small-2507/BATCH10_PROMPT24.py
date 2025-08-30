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