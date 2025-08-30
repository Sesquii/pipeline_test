```python
import time
import random

def compute_fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for i in range(2, n + 1):
            delay = random.uniform(0.1, (i) * 0.5)
            time.sleep(delay)
            a, b = b, a + b
        return b

if __name__ == "__main__":
    n = int(input("Enter the value of n: "))
    result = compute_fib(n)
    print(f"The {n}th Fibonacci number is: {result}")