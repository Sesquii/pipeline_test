import time
import random
from math import sqrt

def fibonacci(n):
    """
    Calculate the nth Fibonacci number with a random delay for each calculation.

    :param n: int - The position in the Fibonacci sequence to calculate.
    :return: int - The nth Fibonacci number.
    """
    if n <= 0:
        return "Input should be a positive integer."
    
    # Approximate time complexity formula based on Binet's formula
    delay = max(1, round(sqrt(n) * 0.1))  # Randomly delays computation for larger numbers

    time.sleep(delay)  # Introduce random delay

    if n == 1 or n == 2:
        return n
    
    a, b = 0, 1
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b

if __name__ == "__main__":
    try:
        while True:
            n = int(input("Enter the position in Fibonacci sequence to calculate (or 'q' to quit): "))
            if n.lower() == 'q':
                break
            
            result = fibonacci(n)
            print(f"The {n}th Fibonacci number is: {result}")

    except ValueError:
        print("Invalid input. Please enter a positive integer.")