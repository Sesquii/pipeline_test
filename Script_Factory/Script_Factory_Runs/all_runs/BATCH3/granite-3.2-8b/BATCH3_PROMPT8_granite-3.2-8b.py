import time
import random
import math
from typing import Union


def fibonacci(n: int) -> Union[int, str]:
    """
    Calculate the nth Fibonacci number with a delay that increases for larger n.

    :param n: Integer representing the position in the Fibonacci sequence.
    :return: The nth Fibonacci number if n is valid, otherwise an error message.
    """

    # Validate input
    if not isinstance(n, int) or n < 0:
        return "Error: Input must be a non-negative integer."

    # Calculate delay based on the size of 'n'
    delay = max(1, math.log(n + 1))  # Ensures larger 'n' gets more delay

    # Simulate delay before calculation
    time.sleep(delay)

    # Compute Fibonacci number
    if n <= 0:
        return "Error: Input must be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    
    prev, curr = 0, 1
    for _ in range(2, n):
        prev, curr = curr, prev + curr

    return curr


if __name__ == "__main__":
    try:
        n = int(input("Enter the position in Fibonacci sequence (n): "))
        result = fibonacci(n)
        if isinstance(result, str):
            print(result)
        else:
            print(f"The {n}th Fibonacci number is: {result}")
    except ValueError:
        print("Error: Input must be an integer.")