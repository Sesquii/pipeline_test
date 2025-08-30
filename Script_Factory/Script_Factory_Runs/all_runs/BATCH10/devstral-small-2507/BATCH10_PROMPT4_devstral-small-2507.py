# BATCH10_PROMPT4_Devstral.py

import operator

def get_insult(operation):
    insults = {
        'add': "You can't even add? That's pathetic.",
        'subtract': "Even a kindergartener could do better than you.",
        'multiply': "Multiplying your intelligence would still be zero.",
        'divide': "I'm surprised you didn't divide by zero and crash the program."
    }
    return insults.get(operation, "You're not even good at basic math?")

def perform_operation(a, b, op):
    operations = {
        'add': operator.add,
        'subtract': operator.sub,
        'multiply': operator.mul,
        'divide': operator.truediv
    }
    
    if op not in operations:
        print("Invalid operation. Please choose from: add, subtract, multiply, divide")
        return None
    
    try:
        result = operations[op](a, b)
        insult = get_insult(op)
        print(f"{insult} The answer is: {result}")
    except ZeroDivisionError:
        print("Seriously? You're trying to divide by zero? That's just sad.")

def main():
    print("Welcome to the Sarcastic Calculator!")
    print("Available operations: add, subtract, multiply, divide")

    while True:
        try:
            a = float(input("Enter first number (or 'q' to quit): "))
            if a == 'q':
                break
            b = float(input("Enter second number: "))
            op = input("Enter operation: ").lower()

            perform_operation(a, b, op)

        except ValueError:
            print("Please enter valid numbers!")

if __name__ == "__main__":
    main()