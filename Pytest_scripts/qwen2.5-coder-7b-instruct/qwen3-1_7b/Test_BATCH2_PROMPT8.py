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

# ===== GENERATED TESTS =====
```python
import time
from typing import Any

def compute_fib(n):
    """Compute the nth Fibonacci number with random delays."""
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

# Test suite for compute_fib function using pytest

import pytest

@pytest.fixture
def fib_values():
    """Provide a dictionary with known Fibonacci values."""
    return {
        0: 0,
        1: 1,
        2: 1,
        3: 2,
        4: 3,
        5: 5,
        6: 8,
        7: 13,
        8: 21,
        9: 34,
        10: 55
    }

def test_compute_fib(fib_values):
    """Test the compute_fib function with known values."""
    for n, expected in fib_values.items():
        assert compute_fib(n) == expected

def test_compute_fib_negative_input():
    """Test the compute_fib function with negative input."""
    with pytest.raises(ValueError):
        compute_fib(-1)

def test_compute_fib_large_value(fib_values):
    """Test the compute_fib function with a large value of n."""
    # Since we are using random delays, we cannot predict the exact result,
    # but we can check if the function does not raise an exception.
    try:
        result = compute_fib(20)
        assert result == fib_values[20]
    except Exception as e:
        pytest.fail(f"Exception occurred: {e}")

def test_compute_fib_zero():
    """Test the compute_fib function with zero."""
    assert compute_fib(0) == 0

def test_compute_fib_one():
    """Test the compute_fib function with one."""
    assert compute_fib(1) == 1

def test_compute_fib_two():
    """Test the compute_fib function with two."""
    assert compute_fib(2) == 1
```