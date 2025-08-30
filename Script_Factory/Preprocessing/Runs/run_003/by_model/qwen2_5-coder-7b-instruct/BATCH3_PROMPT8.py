import time
from random import randint

def fibonacci(n):
    """Calculate the nth Fibonacci number with a random delay."""
    if n <= 1:
        return n
    else:
        # Random delay between 0 and n seconds
        delay = randint(0, n)
        time.sleep(delay)
        return fibonacci(n-1) + fibonacci(n-2)

if __name__ == "__main__":
    n = int(input("Enter the position in Fibonacci sequence: "))
    result = fibonacci(n)
    print(f"The {n}th Fibonacci number is: {result}")