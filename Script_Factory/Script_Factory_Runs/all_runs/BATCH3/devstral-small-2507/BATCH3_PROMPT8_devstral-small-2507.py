import time
import random

def fibonacci(n):
    """Calculate the nth Fibonacci number."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def delayed_fibonacci(n, min_delay=0.1, max_delay=2.0):
    """Calculate the nth Fibonacci number with a random delay."""
    delay = min_delay + (max_delay - min_delay) * (n / 10)
    time.sleep(random.uniform(0, delay))
    return fibonacci(n)

def main():
    """Main function to calculate and print Fibonacci numbers with delays."""
    while True:
        try:
            n = int(input("Enter a non-negative integer to calculate its Fibonacci number (or -1 to exit): "))
            if n == -1:
                break
            elif n < 0:
                print("Please enter a non-negative integer.")
                continue

            result = delayed_fibonacci(n)
            print(f"Fibonacci({n}) = {result}")

        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()