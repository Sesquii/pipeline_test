import random
import time

def fibonacci(n):
    """Calculate the nth Fibonacci number with a random delay."""
    if n <= 0:
        return "Input should be positive integer."
    elif n == 1 or n == 2:
        return 1
    else:
        # Introduce random delay based on input value (larger numbers = longer delays)
        delay = max(0.1, min(n, 5))
        time.sleep(delay)
        
        return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    """Entry point of the program."""
    try:
        n = int(input("Enter a positive integer to calculate its Fibonacci number: "))
        if n < 1:
            print("Input should be a positive integer.")
        else:
            result = fibonacci(n)
            print(f"The {n}th Fibonacci number is: {result}")
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

if __name__ == "__main__":
    main()