import random
import time

def fibonacci(n):
    """
    Calculate the nth Fibonacci number using a simple recursive approach.
    Adds a random delay that increases with the value of n to simulate
    time-based computation.
    
    :param n: The position in the Fibonacci sequence
    :return: The nth Fibonacci number
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Introduce a random delay that increases with n
        delay = random.uniform(0.1, 0.5) * n
        time.sleep(delay)
        return fibonacci(n-1) + fibonacci(n-2)

def main():
    """
    Entry point of the program. Prompts the user for a number and calculates
    its Fibonacci value using the time-based approach.
    """
    try:
        n = int(input("Enter a non-negative integer to calculate its Fibonacci number: "))
        if n < 0:
            raise ValueError("The number must be non-negative.")
        result = fibonacci(n)
        print(f"The {n}th Fibonacci number is: {result}")
    except ValueError as e:
        print(f"Invalid input: {e}")

if __name__ == "__main__":
    main()