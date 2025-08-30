import time
from random import randint

def fibonacci(n):
    """Calculate the nth Fibonacci number with a random delay."""
    if n <= 1:
        return n
    else:
        # Random delay between 0 and n seconds
        delay = randint(0, n)
        time.sleep(delay)
        return fibonacci(n-1) + fibonacci(n-2)

if __name__ == "__main__":
    n = int(input("Enter the position in Fibonacci sequence: "))
    result = fibonacci(n)
    print(f"The {n}th Fibonacci number is: {result}")

# ===== GENERATED TESTS =====
import time
from random import randint
from unittest.mock import patch
import pytest

def fibonacci(n):
    """Calculate the nth Fibonacci number with a random delay."""
    if n <= 1:
        return n
    else:
        # Random delay between 0 and n seconds
        delay = randint(0, n)
        time.sleep(delay)
        return fibonacci(n-1) + fibonacci(n-2)

if __name__ == "__main__":
    n = int(input("Enter the position in Fibonacci sequence: "))
    result = fibonacci(n)
    print(f"The {n}th Fibonacci number is: {result}")

# Test suite for the fibonacci function
def test_fibonacci_base_cases():
    """Test the base cases of the fibonacci function."""
    assert fibonacci(0) == 0, "Fibonacci of 0 should be 0"
    assert fibonacci(1) == 1, "Fibonacci of 1 should be 1"

def test_fibonacci_positive_numbers():
    """Test the positive numbers in the Fibonacci sequence."""
    assert fibonacci(2) == 1, "Fibonacci of 2 should be 1"
    assert fibonacci(3) == 2, "Fibonacci of 3 should be 2"
    assert fibonacci(4) == 3, "Fibonacci of 4 should be 3"
    assert fibonacci(5) == 5, "Fibonacci of 5 should be 5"

def test_fibonacci_negative_numbers():
    """Test the negative numbers in the Fibonacci sequence."""
    with pytest.raises(ValueError):
        fibonacci(-1), "Fibonacci function should raise ValueError for negative input"

@patch('time.sleep')
def test_fibonacci_with_mocked_sleep(mock_sleep):
    """Test the fibonacci function with mocked sleep to avoid actual delay."""
    result = fibonacci(2)
    assert result == 1, "Fibonacci of 2 should be 1"
    mock_sleep.assert_called_once()

@patch('random.randint')
def test_fibonacci_with_mocked_randint(mock_randint):
    """Test the fibonacci function with mocked randint to control random delay."""
    mock_randint.return_value = 0
    result = fibonacci(3)
    assert result == 2, "Fibonacci of 3 should be 2"
    mock_randint.assert_called_once()

@patch('random.randint')
def test_fibonacci_with_mocked_randint_negative(mock_randint):
    """Test the fibonacci function with mocked randint returning negative value."""
    mock_randint.return_value = -1
    result = fibonacci(3)
    assert result == 2, "Fibonacci of 3 should be 2"
    mock_randint.assert_called_once()

@patch('random.randint')
def test_fibonacci_with_mocked_randint_large(mock_randint):
    """Test the fibonacci function with mocked randint returning large value."""
    mock_randint.return_value = 10
    result = fibonacci(3)
    assert result == 2, "Fibonacci of 3 should be 2"
    mock_randint.assert_called_once()

@patch('random.randint')
def test_fibonacci_with_mocked_randint_zero(mock_randint):
    """Test the fibonacci function with mocked randint returning zero."""
    mock_randint.return_value = 0
    result = fibonacci(3)
    assert result == 2, "Fibonacci of 3 should be 2"
    mock_randint.assert_called_once()

@patch('random.randint')
def test_fibonacci_with_mocked_randint_one(mock_randint):
    """Test the fibonacci function with mocked randint returning one."""
    mock_randint.return_value = 1
    result = fibonacci(3)
    assert result == 2, "Fibonacci of 3 should be 2"
    mock_randint.assert_called_once()

@patch('random.randint')
def test_fibonacci_with_mocked_randint_two(mock_randint):
    """Test the fibonacci function with mocked randint returning two."""
    mock_randint.return_value = 2
    result = fibonacci(3)
    assert result == 2, "Fibonacci of 3 should be 2"
    mock_randint.assert_called_once()

@patch('random.randint')
def test_fibonacci_with_mocked_randint_three(mock_randint):
    """Test the fibonacci function with mocked randint returning three."""
    mock_randint.return_value = 3
    result = fibonacci(3)
    assert result == 2, "Fibonacci of 3 should be 2"
    mock_randint.assert_called_once()

@patch('random.randint')
def test_fibonacci_with_mocked_randint_four(mock_randint):
    """Test the fibonacci function with mocked randint returning four."""
    mock_randint.return_value = 4
    result = fibonacci(3)
    assert result == 2, "Fibonacci of 3 should be 2"
    mock_randint.assert_called_once()

@patch('random.randint')
def test_fibonacci_with_mocked_randint_five(mock_randint):
    """Test the fibonacci function with mocked randint returning five."""
    mock_randint.return_value = 5
    result = fibonacci(3)
    assert result == 2, "Fibonacci of 3 should be 2"
    mock_randint.assert_called_once()

@patch('random.randint')
def test_fibonacci_with_mocked_randint_six(mock_randint):
    """Test the fibonacci function with mocked randint returning six."""
    mock_randint.return_value = 6
    result = fibonacci(3)
    assert result == 2, "Fibonacci of 3 should be 2"
    mock_randint.assert_called_once()

@patch('random.randint')
def test_fibonacci_with_mocked_randint_seven(mock_randint):
    """Test the fibonacci function with mocked randint returning seven."""
    mock_randint.return_value = 7
    result = fibonacci(3)
    assert result == 2, "Fibonacci of 3 should be 2"
    mock_randint.assert_called_once()

@patch('random.randint')
def test_fibonacci_with_mocked_randint_eight(mock_randint):
    """Test the fibonacci function with mocked randint returning eight."""
    mock_randint.return_value = 8
    result = fibonacci(3)
    assert result == 2, "Fibonacci of 3 should be 2"
    mock_randint.assert_called_once()

@patch('random.randint')
def test_fibonacci_with_mocked_randint_nine(mock_randint):
    """Test the fibonacci function with mocked randint returning nine."""
    mock_randint.return_value = 9
    result = fibonacci(3)
    assert result == 2, "Fibonacci of 3 should be 2"
    mock_randint.assert_called_once()

@patch('random.randint')
def test_fibonacci_with_mocked_randint_ten(mock_randint):
    """Test the fibonacci function with mocked randint returning ten."""
    mock_randint.return_value = 10
    result = fibonacci(3)
    assert result == 2, "Fibonacci of 3 should be 2"
    mock_randint.assert_called_once()
