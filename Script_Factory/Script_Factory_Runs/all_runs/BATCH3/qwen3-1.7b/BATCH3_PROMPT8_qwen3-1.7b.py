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
        for _ in range(2, n + 1):
            delay = random.randint(0, _ * 10)
            time.sleep(delay / 1000)
            c = a + b
            a, b = b, c
        return b

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python BATCH3_PROMPT8_{{model_name}}.py n")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
        result = fibonacci(n)
        print(f"F({n}) = {result}")
    except ValueError:
        print("Please provide a valid integer.")