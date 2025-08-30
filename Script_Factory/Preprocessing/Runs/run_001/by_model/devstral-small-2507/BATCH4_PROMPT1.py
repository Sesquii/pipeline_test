import time
import random

def fibonacci(n):
    """Calculate the nth Fibonacci number."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def time_based_fibonacci(n):
    """Calculate the nth Fibonacci number with random delays."""
    # Introduce a delay based on the size of n (longer for larger numbers)
    delay = random.uniform(0.01, 0.1 * n) if n > 0 else 0
    time.sleep(delay)

    return fibonacci(n)

if __name__ == "__main__":
    # Example usage: Calculate the 5th Fibonacci number with time-based delay
    n = 5
    result = time_based_fibonacci(n)
    print(f"The {n}th Fibonacci number is: {result}")