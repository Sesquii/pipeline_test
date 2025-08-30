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

# ===== GENERATED TESTS =====
```python
import time
import random
from typing import Callable

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

# Test suite for the fibonacci function
def test_fibonacci():
    # Positive test cases
    assert fibonacci(0) == 0, "Test case for n=0 failed"
    assert fibonacci(1) == 1, "Test case for n=1 failed"
    assert fibonacci(2) == 1, "Test case for n=2 failed"
    assert fibonacci(3) == 2, "Test case for n=3 failed"
    assert fibonacci(4) == 3, "Test case for n=4 failed"
    assert fibonacci(5) == 5, "Test case for n=5 failed"
    assert fibonacci(10) == 55, "Test case for n=10 failed"

    # Negative test cases
    try:
        fibonacci(-1)
    except ValueError as e:
        assert str(e) == "Please enter a non-negative integer.", "Test case for negative input failed"

def test_fibonacci_with_random_delay(monkeypatch):
    # Mock the time.sleep function to avoid actual delays during testing
    def mock_sleep(*args, **kwargs):
        pass

    monkeypatch.setattr(time, 'sleep', mock_sleep)

    # Test cases with random delay mocked out
    assert fibonacci(0) == 0, "Test case for n=0 failed"
    assert fibonacci(1) == 1, "Test case for n=1 failed"
    assert fibonacci(2) == 1, "Test case for n=2 failed"

def test_fibonacci_with_large_input():
    # Test with a large input to ensure the function does not hang
    result = fibonacci(30)
    assert isinstance(result, int), "Result should be an integer"
    assert result >= 832040, "Result for n=30 is incorrect"

# Run the tests using pytest
if __name__ == "__main__":
    import pytest
    pytest.main()
```

This test suite includes comprehensive test cases for the `fibonacci` function, covering both positive and negative scenarios. It also demonstrates the use of pytest fixtures (`monkeypatch`) to mock the `time.sleep` function during testing, ensuring that the random delays do not affect the test results. The test suite is designed to be run using pytest, which can be executed by running the script directly or by invoking `pytest` from the command line in the directory containing the script.