import time
import random

def fibonacci(n):
    """Calculate the nth Fibonacci number with random delay."""
    if n <= 0:
        return "Input should be a positive integer."
    elif n == 1 or n == 2:
        return 1
    
    # Simulate random delay based on the size of the number
    time.sleep(random.uniform(0.1 * n, 1 * n))
    
    a, b = 1, 1
    for _ in range(3, n + 1):
        a, b = b, a + b
    
    return b

if __name__ == "__main__":
    # Example usage: Calculate the 10th Fibonacci number with random delay
    result = fibonacci(10)
    print(f"The 10th Fibonacci number is: {result}")