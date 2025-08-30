```python
import sys
import random
import time

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for i in range(2, n + 1):
        c = a + b
        delay = random.uniform(0.1, 1.0) * i
        time.sleep(delay)
        a, b = b, c
    return b

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python BATCH4_PROMPT1_{{model_name}}.py <n>")
        sys.exit(1)
    n = int(sys.argv[1])
    result = fibonacci(n)
    print(f"F({n}) = {result}")