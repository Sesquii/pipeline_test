import random
import time

def fibonacci(n):
    """Calculate the nth Fibonacci number using recursion with memoization."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def time_based_fibonacci(n, delay_factor=0.1):
    """Calculate the nth Fibonacci number with a random delay that increases with n."""
    # Introduce a delay based on the size of n
    delay = random.uniform(0, delay_factor * n)
    print(f"Calculating Fibonacci({n})... Delay: {delay:.2f} seconds")
    time.sleep(delay)

    result = fibonacci(n)
    return result

def main():
    """Main function to demonstrate the Time-Based Fibonacci Calculator."""
    try:
        n = int(input("Enter a positive integer to calculate its Fibonacci number: "))
        if n < 0:
            raise ValueError("The input must be a non-negative integer.")

        start_time = time.time()
        result = time_based_fibonacci(n)
        end_time = time.time()

        print(f"Fibonacci({n}) = {result}")
        print(f"Total computation time: {end_time - start_time:.2f} seconds")

    except ValueError as e:
        print(f"Invalid input: {e}")

if __name__ == "__main__":
    main()