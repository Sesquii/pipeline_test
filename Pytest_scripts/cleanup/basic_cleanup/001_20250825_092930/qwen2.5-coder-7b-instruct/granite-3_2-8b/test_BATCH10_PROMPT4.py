# BATCH10_PROMPT4_Granite.py

import sys
from random import choice, randint

def sarcastic_response(operation, num1, num2):
    responses = [
        f"Oh, {num1} {operation} {num2}. How utterly original.", 
        f"{num1} {operation} {num2}. You're a real math genius, you know that?",
        f"{num1} {operation} {num2}. I'm simply awestruck by your computational prowess."
    ]
    
    return choice(responses)

def main():
    print("Welcome to the Sarcasm-O-Matic Calculator!")

    while True:
        try:
            operation = input("Enter an operation (+, -, *, /): ")
            num1 = float(input("First number: "))
            num2 = float(input("Second number: "))

            if operation not in ('+', '-', '*', '/'):
                print("Invalid operation. Try again, Einstein.")
                continue
            
            result = eval(f"{num1} {operation} {num2}")  # Using eval for simplicity

            if operation == '//':
                result = int(result)  # Floor division
            elif operation == '%':
                result = num1 % num2  # Modulus

            print(f"Result: {result}")
            print(sarcastic_response(operation, num1, num2))
            
            another = input("Do you want to continue? (yes/no): ")
            if another.lower() != 'yes':
                break
        except Exception as e:
            print(f"Oops! Something went wrong: {e}. Better luck next time.")

if __name__ == "__main__":
    main()

# ===== GENERATED TESTS =====
# BATCH10_PROMPT4_Granite.py

import sys
from random import choice, randint
from io import StringIO
from unittest.mock import patch
import pytest

def sarcastic_response(operation, num1, num2):
    responses = [
        f"Oh, {num1} {operation} {num2}. How utterly original.", 
        f"{num1} {operation} {num2}. You're a real math genius, you know that?",
        f"{num1} {operation} {num2}. I'm simply awestruck by your computational prowess."
    ]
    
    return choice(responses)

def main():
    print("Welcome to the Sarcasm-O-Matic Calculator!")

    while True:
        try:
            operation = input("Enter an operation (+, -, *, /): ")
            num1 = float(input("First number: "))
            num2 = float(input("Second number: "))

            if operation not in ('+', '-', '*', '/'):
                print("Invalid operation. Try again, Einstein.")
                continue
            
            result = eval(f"{num1} {operation} {num2}")  # Using eval for simplicity

            if operation == '//':
                result = int(result)  # Floor division
            elif operation == '%':
                result = num1 % num2  # Modulus

            print(f"Result: {result}")
            print(sarcastic_response(operation, num1, num2))
            
            another = input("Do you want to continue? (yes/no): ")
            if another.lower() != 'yes':
                break
        except Exception as e:
            print(f"Oops! Something went wrong: {e}. Better luck next time.")

if __name__ == "__main__":
    main()

# Test suite for BATCH10_PROMPT4_Granite.py

def test_sarcastic_response():
    """Test the sarcastic_response function with different operations and numbers."""
    assert sarcastic_response('+', 5, 3) in [
        "Oh, 5 + 3. How utterly original.",
        "5 + 3. You're a real math genius, you know that?",
        "5 + 3. I'm simply awestruck by your computational prowess."
    ]
    
    assert sarcastic_response('-', 10, 4) in [
        "Oh, 10 - 4. How utterly original.",
        "10 - 4. You're a real math genius, you know that?",
        "10 - 4. I'm simply awestruck by your computational prowess."
    ]
    
    assert sarcastic_response('*', 6, 7) in [
        "Oh, 6 * 7. How utterly original.",
        "6 * 7. You're a real math genius, you know that?",
        "6 * 7. I'm simply awestruck by your computational prowess."
    ]
    
    assert sarcastic_response('/', 20, 5) in [
        "Oh, 20 / 5. How utterly original.",
        "20 / 5. You're a real math genius, you know that?",
        "20 / 5. I'm simply awestruck by your computational prowess."
    ]

def test_main(capsys):
    """Test the main function with different inputs and outputs."""
    # Test addition
    input_data = ['+', '1', '2', 'yes']
    expected_output = "Result: 3\nOh, 1 + 2. How utterly original.\nDo you want to continue? (yes/no): "
    with patch('builtins.input', side_effect=input_data):
        main()
        captured = capsys.readouterr()
        assert captured.out.strip() == expected_output

    # Test division
    input_data = ['/', '10', '2', 'no']
    expected_output = "Result: 5.0\nOh, 10 / 2. How utterly original.\nDo you want to continue? (yes/no): "
    with patch('builtins.input', side_effect=input_data):
        main()
        captured = capsys.readouterr()
        assert captured.out.strip() == expected_output

    # Test invalid operation
    input_data = ['^', '10', '2', 'no']
    expected_output = "Invalid operation. Try again, Einstein.\nDo you want to continue? (yes/no): "
    with patch('builtins.input', side_effect=input_data):
        main()
        captured = capsys.readouterr()
        assert captured.out.strip() == expected_output

    # Test division by zero
    input_data = ['/', '10', '0', 'no']
    expected_output = "Oops! Something went wrong: division by zero. Better luck next time.\nDo you want to continue? (yes/no): "
    with patch('builtins.input', side_effect=input_data):
        main()
        captured = capsys.readouterr()
        assert captured.out.strip() == expected_output

# Add more test cases as needed
