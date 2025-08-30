# BATCH10_PROMPT24_Granite.py

class Digit:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if isinstance(other, Digit):
            return Digit(self.value + other.value)
        elif isinstance(other, int):
            return Digit(self.value + other)
        else:
            raise TypeError("Unsupported operand type for +")
    
    def __sub__(self, other):
        if isinstance(other, Digit):
            return Digit(self.value - other.value)
        elif isinstance(other, int):
            return Digit(self.value - other)
        else:
            raise TypeError("Unsupported operand type for -")

    def __mul__(self, other):
        if isinstance(other, Digit):
            return Digit(self.value * other.value)
        elif isinstance(other, int):
            return Digit(self.value * other)
        else:
            raise TypeError("Unsupported operand type for *")
    
    def __truediv__(self, other):
        if isinstance(other, Digit):
            return Digit(self.value / other.value)
        elif isinstance(other, int):
            return Digit(self.value / other)
        else:
            raise TypeError("Unsupported operand type for /")

    def __str__(self):
        return str(self.value)


def calculate(expression):
    result = expression[0]
    for i in range(1, len(expression), 2):
        operator = expression[i]
        next_digit = expression[i + 1]

        if operator == '+':
            result += next_digit
        elif operator == '-':
            result -= next_digit
        elif operator == '*':
            result *= next_digit
        elif operator == '/':
            result /= next_digit
        else:
            raise ValueError(f"Unsupported operation: {operator}")

    return result


def main():
    # Example usage
    digits = [Digit(1), Digit(2), Digit(3)]  # Representing the number 123
    operations = ['+', '-', '*', '/']  # Sequence of operations

    expression = []
    for digit in digits:
        expression.append(digit)
        expression.append(operations[0])  # We assume 'add' as default operation if not specified

    result = calculate(expression)
    print(f"Result: {result}")


if __name__ == "__main__":
    main()