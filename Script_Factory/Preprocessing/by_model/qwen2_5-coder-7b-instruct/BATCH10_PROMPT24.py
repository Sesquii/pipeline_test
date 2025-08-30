class DigitCalculator:
    def __init__(self, digit):
        self.digit = digit

    def add(self, other):
        if isinstance(other, DigitCalculator):
            return DigitCalculator((self.digit + other.digit) % 10)
        raise ValueError("Unsupported operand type for +: 'DigitCalculator' and '{}'".format(type(other).__name__))

    def subtract(self, other):
        if isinstance(other, DigitCalculator):
            result = self.digit - other.digit
            return DigitCalculator((result + 10) % 10)
        raise ValueError("Unsupported operand type for -: 'DigitCalculator' and '{}'".format(type(other).__name__))

    def multiply(self, other):
        if isinstance(other, DigitCalculator):
            return DigitCalculator((self.digit * other.digit) % 10)
        raise ValueError("Unsupported operand type for *: 'DigitCalculator' and '{}'".format(type(other).__name__))

    def divide(self, other):
        if isinstance(other, DigitCalculator):
            if other.digit == 0:
                raise ZeroDivisionError
            return DigitCalculator((self.digit // other.digit) % 10)
        raise ValueError("Unsupported operand type for /: 'DigitCalculator' and '{}'".format(type(other).__name__))

    def __str__(self):
        return str(self.digit)

if __name__ == "__main__":
    # Example usage
    num1 = DigitCalculator(3)
    num2 = DigitCalculator(7)

    print("Addition:", num1 + num2)
    print("Subtraction:", num1 - num2)
    print("Multiplication:", num1 * num2)
    print("Division:", num1 / num2)