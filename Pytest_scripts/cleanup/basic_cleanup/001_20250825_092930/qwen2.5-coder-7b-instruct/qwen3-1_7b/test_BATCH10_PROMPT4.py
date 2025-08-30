if __name__ == "__main__":
    print("Welcome to the sarcastic calculator! What would you like to compute? (add, subtract, multiply, divide)")
    operation = input().strip().lower()
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if operation == 'add':
        result = a + b
        print(f"Adding {a} and {b}: Oh, you want to add 2 and 3? That's so basic! The result is {result}")
    elif operation == 'subtract':
        result = a - b
        print(f"Subtracting {b} from {a}: You're trying to subtract 1 from 5? That's so sad! The result is {result}")
    elif operation == 'multiply':
        result = a * b
        print(f"Multiplying {a} and {b}: Multiplication is the ultimate art! The result is {result}")
    elif operation == 'divide':
        if b == 0:
            print("You're trying to divide by zero? That's so unhelpful!")
        else:
            result = a / b
            print(f"Dividing {a} by {b}: You're trying to divide 10 by 2? That's so helpful! The result is {result}")
    else:
        print("Invalid operation. Please choose add, subtract, multiply, or divide.")

# ===== GENERATED TESTS =====
from typing import Callable

# Original script code
if __name__ == "__main__":
    print("Welcome to the sarcastic calculator! What would you like to compute? (add, subtract, multiply, divide)")
    operation = input().strip().lower()
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if operation == 'add':
        result = a + b
        print(f"Adding {a} and {b}: Oh, you want to add 2 and 3? That's so basic! The result is {result}")
    elif operation == 'subtract':
        result = a - b
        print(f"Subtracting {b} from {a}: You're trying to subtract 1 from 5? That's so sad! The result is {result}")
    elif operation == 'multiply':
        result = a * b
        print(f"Multiplying {a} and {b}: Multiplication is the ultimate art! The result is {result}")
    elif operation == 'divide':
        if b == 0:
            print("You're trying to divide by zero? That's so unhelpful!")
        else:
            result = a / b
            print(f"Dividing {a} by {b}: You're trying to divide 10 by 2? That's so helpful! The result is {result}")
    else:
        print("Invalid operation. Please choose add, subtract, multiply, or divide.")

# Test cases
import pytest

def test_calculator_add():
    """Test the calculator with addition"""
    assert calculator('add', 2, 3) == "Oh, you want to add 2 and 3? That's so basic! The result is 5"

def test_calculator_subtract():
    """Test the calculator with subtraction"""
    assert calculator('subtract', 5, 1) == "You're trying to subtract 1 from 5? That's so sad! The result is 4"

def test_calculator_multiply():
    """Test the calculator with multiplication"""
    assert calculator('multiply', 2, 3) == "Multiplication is the ultimate art! The result is 6"

def test_calculator_divide():
    """Test the calculator with division"""
    assert calculator('divide', 10, 2) == "You're trying to divide 10 by 2? That's so helpful! The result is 5.0"

def test_calculator_divide_by_zero():
    """Test the calculator with division by zero"""
    assert calculator('divide', 10, 0) == "You're trying to divide by zero? That's so unhelpful!"

def test_calculator_invalid_operation():
    """Test the calculator with an invalid operation"""
    assert calculator('modulus', 2, 3) == "Invalid operation. Please choose add, subtract, multiply, or divide."

# Helper function to simulate user input and capture output
def calculator(operation: str, a: float, b: float) -> str:
    import sys
    from io import StringIO

    # Redirect stdin and stdout
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO(f"{operation}\n{a}\n{b}")
    sys.stdout = StringIO()

    # Run the original script
    exec(open(__file__).read())

    # Restore stdin and stdout
    output = sys.stdout.getvalue()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    return output.strip()
