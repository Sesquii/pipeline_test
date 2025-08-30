```python
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