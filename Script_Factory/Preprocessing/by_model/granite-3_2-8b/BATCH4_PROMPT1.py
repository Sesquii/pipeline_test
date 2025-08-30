import random
import time
from math import sqrt

def fibonacci(n):
    """
    Calculate the nth Fibonacci number with a randomly delayed computation time.

    Args:
        n (int): The position in the Fibonacci sequence to calculate.

    Returns:
        int: The nth Fibonacci number.
    """
    if n <= 0:
        return "Input should be a positive integer."
    
    # Approximate the golden ratio for large n calculations
    phi = (1 + sqrt(5)) / 2

    # Delay time is approximately proportional to logarithm of n, with some randomness
    delay_time = int(log(n) * 0.1 + random.uniform(0.1, 1))
    time.sleep(delay_time)

    if n == 1 or n == 2:
        return 1

    return int((phi**n - (-phi)**(-n)) / sqrt(5))

def main():
    """
    Entry point of the program.
    """
    try:
        n = int(input("Enter the position (n) in Fibonacci sequence: "))
        result = fibonacci(n)

        if isinstance(result, str):
            print(result)
        else:
            print(f"The {n}th number in the Fibonacci sequence is: {result}")
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

if __name__ == "__main__":
    main()