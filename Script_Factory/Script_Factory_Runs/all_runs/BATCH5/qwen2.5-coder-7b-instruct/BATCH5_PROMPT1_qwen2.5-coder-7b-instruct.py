import time
import random

def fibonacci(n):
    if n <= 1:
        return n
    else:
        time.sleep(random.uniform(0.01 * n, 0.1 * n))  # Random delay based on Fibonacci number index
        return fibonacci(n-1) + fibonacci(n-2)

if __name__ == "__main__":
    try:
        nth = int(input("Enter the position of Fibonacci number to calculate: "))
        if nth < 0:
            print("Please enter a non-negative integer.")
        else:
            result = fibonacci(nth)
            print(f"The {nth}th Fibonacci number is: {result}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")