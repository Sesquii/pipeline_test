# BATCH10_PROMPT4_{{model_name}}.py

def sarcastic_calculator():
    """
    A sarcastic calculator that insults the user for their mathematical requests.
    """
    print("Welcome to the Sarcastic Calculator! Let's do some math, shall we?")
    
    try:
        num1 = float(input("Enter the first number: "))
        operator = input("Enter an operator (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))
        
        if operator == '+':
            result = num1 + num2
            print(f"{num1} plus {num2}? What a joke! The answer is {result}.")
        elif operator == '-':
            result = num1 - num2
            print(f"{num1} minus {num2}? Pfft, the answer is {result}.")
        elif operator == '*':
            result = num1 * num2
            print(f"{num1} times {num2}? Are you serious? The answer is {result}.")
        elif operator == '/':
            if num2 != 0:
                result = num1 / num2
                print(f"{num1} divided by {num2}? Really? The answer is {result}.")
            else:
                print("Division by zero? Wow, that's a smart one. Don't you know that's impossible?")
        else:
            print("Invalid operator! Try again.")
    
    except ValueError:
        print("That's not a valid number! Try again.")

if __name__ == "__main__":
    sarcastic_calculator()