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