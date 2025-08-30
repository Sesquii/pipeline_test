```python
import random
import time

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for i in range(2, n + 1):
            delay = random.uniform(0.1, 1)
            time.sleep(delay)
            c = a + b
            a = b
            b = c
        return b

if __name__ == "__main__":
    n = int(input("Enter n: "))
    result = fibonacci(n)
    print(f"F({n}) = {result}")