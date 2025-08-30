import random
import time

def fibonacci(n):
    """
    Calculate the nth Fibonacci number using a simple recursive approach.
    Adds a random delay that increases with the value of n to simulate
    time-based computation.
    
    :param n: The position in the Fibonacci sequence
    :return: The nth Fibonacci number
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Introduce a random delay that increases with n
        delay = random.uniform(0.1, 0.5) * n
        time.sleep(delay)
        return fibonacci(n-1) + fibonacci(n-2)

def main():
    """
    Entry point of the program. Prompts the user for a number and calculates
    its Fibonacci value using the time-based approach.
    """
    try:
        n = int(input("Enter a non-negative integer to calculate its Fibonacci number: "))
        if n < 0:
            raise ValueError("The number must be non-negative.")
        result = fibonacci(n)
        print(f"The {n}th Fibonacci number is: {result}")
    except ValueError as e:
        print(f"Invalid input: {e}")

if __name__ == "__main__":
    main()

# ===== GENERATED TESTS =====
```python
import pytest
from unittest.mock import patch

# Original code remains unchanged

def test_fibonacci_base_cases():
    """
    Test the base cases of the fibonacci function.
    """
    assert fibonacci(0) == 0, "Fibonacci of 0 should be 0"
    assert fibonacci(1) == 1, "Fibonacci of 1 should be 1"

def test_fibonacci_positive_cases():
    """
    Test positive cases of the fibonacci function.
    """
    assert fibonacci(2) == 1, "Fibonacci of 2 should be 1"
    assert fibonacci(3) == 2, "Fibonacci of 3 should be 2"
    assert fibonacci(4) == 3, "Fibonacci of 4 should be 3"
    assert fibonacci(5) == 5, "Fibonacci of 5 should be 5"

def test_fibonacci_negative_cases():
    """
    Test negative cases for the fibonacci function.
    """
    with pytest.raises(ValueError):
        fibonacci(-1)

def test_main_positive_input(monkeypatch):
    """
    Test main function with a positive input.
    """
    monkeypatch.setattr('builtins.input', lambda _: '5')
    with patch('sys.stdout') as mock_stdout:
        main()
        assert "The 5th Fibonacci number is: 5" in mock_stdout.getvalue()

def test_main_negative_input(monkeypatch):
    """
    Test main function with a negative input.
    """
    monkeypatch.setattr('builtins.input', lambda _: '-1')
    with patch('sys.stdout') as mock_stdout:
        main()
        assert "Invalid input: The number must be non-negative." in mock_stdout.getvalue()

def test_fibonacci_random_delay(monkeypatch):
    """
    Test the random delay introduced in the fibonacci function.
    """
    with patch('time.sleep') as mock_sleep:
        fibonacci(1)
        assert mock_sleep.called, "time.sleep should be called"
        # We can't predict the exact delay, but we know it should be between 0.1 and 0.5
        assert 0.1 <= mock_sleep.call_args[0][0] <= 0.5, "Delay should be within the expected range"

def test_fibonacci_large_number(monkeypatch):
    """
    Test the fibonacci function with a large number.
    """
    monkeypatch.setattr('builtins.input', lambda _: '20')
    with patch('sys.stdout') as mock_stdout:
        main()
        assert "The 20th Fibonacci number is: 6765" in mock_stdout.getvalue()

def test_fibonacci_zero_input(monkeypatch):
    """
    Test the fibonacci function with zero input.
    """
    monkeypatch.setattr('builtins.input', lambda _: '0')
    with patch('sys.stdout') as mock_stdout:
        main()
        assert "The 0th Fibonacci number is: 0" in mock_stdout.getvalue()

def test_fibonacci_one_input(monkeypatch):
    """
    Test the fibonacci function with one input.
    """
    monkeypatch.setattr('builtins.input', lambda _: '1')
    with patch('sys.stdout') as mock_stdout:
        main()
        assert "The 1st Fibonacci number is: 1" in mock_stdout.getvalue()

def test_fibonacci_two_input(monkeypatch):
    """
    Test the fibonacci function with two input.
    """
    monkeypatch.setattr('builtins.input', lambda _: '2')
    with patch('sys.stdout') as mock_stdout:
        main()
        assert "The 2nd Fibonacci number is: 1" in mock_stdout.getvalue()

def test_fibonacci_three_input(monkeypatch):
    """
    Test the fibonacci function with three input.
    """
    monkeypatch.setattr('builtins.input', lambda _: '3')
    with patch('sys.stdout') as mock_stdout:
        main()
        assert "The 3rd Fibonacci number is: 2" in mock_stdout.getvalue()

def test_fibonacci_four_input(monkeypatch):
    """
    Test the fibonacci function with four input.
    """
    monkeypatch.setattr('builtins.input', lambda _: '4')
    with patch('sys.stdout') as mock_stdout:
        main()
        assert "The 4th Fibonacci number is: 3" in mock_stdout.getvalue()

def test_fibonacci_five_input(monkeypatch):
    """
    Test the fibonacci function with five input.
    """
    monkeypatch.setattr('builtins.input', lambda _: '5')
    with patch('sys.stdout') as mock_stdout:
        main()
        assert "The 5th Fibonacci number is: 5" in mock_stdout.getvalue()

def test_fibonacci_six_input(monkeypatch):
    """
    Test the fibonacci function with six input.
    """
    monkeypatch.setattr('builtins.input', lambda _: '6')
    with patch('sys.stdout') as mock_stdout:
        main()
        assert "The 6th Fibonacci number is: 8" in mock_stdout.getvalue()

def test_fibonacci_seven_input(monkeypatch):
    """
    Test the fibonacci function with seven input.
    """
    monkeypatch.setattr('builtins.input', lambda _: '7')
    with patch('sys.stdout') as mock_stdout:
        main()
        assert "The 7th Fibonacci number is: 13" in mock_stdout.getvalue()

def test_fibonacci_eight_input(monkeypatch):
    """
    Test the fibonacci function with eight input.
    """
    monkeypatch.setattr('builtins.input', lambda _: '8')
    with patch('sys.stdout') as mock_stdout:
        main()
        assert "The 8th Fibonacci number is: 21" in mock_stdout.getvalue()

def test_fibonacci_nine_input(monkeypatch):
    """
    Test the fibonacci function with nine input.
    """
    monkeypatch.setattr('builtins.input', lambda _: '9')
    with patch('sys.stdout') as mock_stdout:
        main()
        assert "The 9th Fibonacci number is: 34" in mock_stdout.getvalue()

def test_fibonacci_ten_input(monkeypatch):
    """
    Test the fibonacci function with ten input.
    """
    monkeypatch.setattr('builtins.input', lambda _: '10')
    with patch('sys.stdout') as mock_stdout:
        main()
        assert "The 10th Fibonacci number is: 55" in mock_stdout.getvalue()

def test_fibonacci_eleven_input(monkeypatch):
    """
    Test the fibonacci function with eleven input.
    """
    monkeypatch.setattr('builtins.input', lambda _: '11')
    with patch('sys.stdout') as mock_stdout:
        main()
        assert "The 11th Fibonacci number is: 89" in mock_stdout.getvalue()

def test_fibonacci_twelve_input(monkeypatch):
    """
    Test the fibonacci function with twelve input.
    """
    monkeypatch.setattr('builtins.input', lambda _: '12')
    with patch('sys.stdout') as mock_stdout:
        main()
        assert "The 12th Fibonacci number is: 144" in mock_stdout.getvalue()

def test_fibonacci_thirteen_input(monkeypatch):
    """
    Test the fibonacci function with thirteen input.
    """
    monkeypatch.setattr('builtins.input', lambda _: '13')
    with patch('sys.stdout') as mock_stdout:
        main()
        assert "The 13th Fibonacci number is: 233" in mock_stdout.getvalue()

def test_fibonacci_fourteen_input(monkeypatch):
    """
    Test the fibonacci function with fourteen input.
    """
    monkeypatch.setattr('builtins.input', lambda _: '14')
    with patch('sys.stdout') as mock_stdout:
        main()
        assert "The 14th Fibonacci number is: 377" in mock_stdout.getvalue()

def test_fibonacci_fifteen_input(monkeypatch):
    """
    Test the fibonacci function with fifteen input.
    """
    monkeypatch.setattr('builtins.input', lambda _: '15')
    with patch('sys.stdout') as mock_stdout:
        main()
        assert "The 15th Fibonacci number is: 610" in mock_stdout.getvalue()

def test_fibonacci_sixteen_input(monkeypatch):
    """
    Test the fibonacci function with sixteen input.
    """
    monkeypatch.setattr('builtins.input', lambda _: '16')
    with patch('sys.stdout') as mock_stdout:
        main()
        assert "The 16th Fibonacci number is: 987" in mock_stdout.getvalue()

def test_fibonacci_seventeen_input(monkeypatch):
    """
    Test the fibonacci function with seventeen input.
    """
    monkeypatch.setattr('builtins.input', lambda _: '17')
    with patch('sys.stdout') as mock_stdout:
        main()
        assert "The 17th Fibonacci number is: 1597" in mock_stdout.getvalue()

def test_fibonacci_eighteen_input(monkeypatch):
    """
    Test the fibonacci function with eighteen input.
    """
    monkeypatch.setattr('builtins.input', lambda _: '18')
    with patch('sys.stdout') as mock_stdout:
        main()
        assert "The 18th Fibonacci number is: 2584" in mock_stdout.getvalue()

def test_fibonacci_nineteen_input(monkeypatch):
    """
    Test the fibonacci function with nineteen input.
    """
    monkeypatch.setattr('builtins.input', lambda _: '19')
    with patch('sys.stdout') as mock_stdout:
        main()
        assert "The 19th Fibonacci number is: 4181" in mock_stdout.getvalue()

def test_fibonacci_twenty_input(monkeypatch):
    """
    Test the fibonacci function with twenty input.
    """
    monkeypatch.setattr('builtins.input', lambda _: '20')
    with patch('sys.stdout') as mock_stdout:
        main()
        assert "The 20th Fibonacci number is: 6765" in mock_stdout.getvalue()

def test_fibonacci_large_number_input(monkeypatch):
    """
    Test the fibonacci function with a large number input.
    """
    monkeypatch.setattr('builtins.input', lambda _: '100')
    with patch('sys.stdout') as mock_stdout:
        main()
        assert "The 100th Fibonacci number is: 354224848179261915075" in mock_stdout.getvalue()

def test_fibonacci_zero_input(monkeypatch):
    """
    Test the fibonacci function with zero input.
    """
    monkeypatch.setattr('builtins.input', lambda _: '0')
    with patch('sys.stdout') as mock_stdout:
        main()
        assert "The 0th Fibonacci number is: 0" in mock_stdout.getvalue()

def test_fibonacci_one_input(monkeypatch):
    """
    Test the fibonacci function with one input.
    """
    monkeypatch.setattr('builtins.input', lambda _: '1')
    with patch('sys.stdout') as mock_stdout:
        main()
        assert "The 1st Fibonacci number is: 1" in mock_stdout.getvalue()

def test_fibonacci_two_input(monkeypatch):
    """
    Test the fibonacci function with two input.
    """
    monkeypatch.setattr('builtins.input', lambda _: '2')
    with patch('sys.stdout') as mock_stdout:
        main()
        assert "The 2nd Fibonacci number is: 1" in mock_stdout.getvalue()

def test_fibonacci_three_input(monkeypatch):
    """
    Test the fibonacci function with three input.
    """
    monkeypatch.setattr('builtins.input', lambda _: '3')
    with patch('sys.stdout') as mock_stdout:
        main()
        assert "The 3rd Fibonacci number is: 2" in mock_stdout.getvalue()

def test_fibonacci_four_input(monkeypatch):
    """
    Test the fibonacci function with four input.
    """
    monkeypatch.setattr('builtins.input', lambda _: '4')
    with patch('sys.stdout') as mock_stdout:
        main()
        assert "The 4th Fibonacci number is: 3" in mock_stdout.getvalue()

def test_fibonacci_five_input(monkeypatch):
    """
    Test the fibonacci function with five input.
    """
    monkeypatch.setattr('builtins.input', lambda _: '5')
    with patch('sys.stdout') as mock_stdout:
        main()
        assert "The 5th Fibonacci number is: 5" in mock_stdout.getvalue()

def test_fibonacci_six_input(monkeypatch):
    """
    Test the fibonacci function with six input.
    """
    monkeypatch.setattr('builtins.input', lambda _: '6')
    with patch('sys.stdout') as mock_stdout:
        main()
        assert "The 6th Fibonacci number is: 8" in mock_stdout.getvalue()

def test_fibonacci_seven_input(monkeypatch):
    """
    Test the fibonacci function with seven input.
    """
    monkeypatch.setattr('builtins.input', lambda _: '7')
    with patch('sys.stdout') as mock_stdout:
        main()
        assert "The 7th Fibonacci number is: 13" in mock_stdout.getvalue()

def test_fibonacci_eight_input(monkeypatch):
    """
    Test the fibonacci function with eight input.
    """
    monkeypatch.setattr('builtins.input', lambda _: '8')
    with patch('sys.stdout') as mock_stdout:
        main()
        assert "The 8th Fibonacci number is: 21" in mock_stdout.getvalue()

def test_fibonacci_nine_input(monkeypatch):
    """
    Test the fibonacci function with nine input.
    """
    monkeypatch.setattr('builtins.input', lambda _: '9')
    with patch('sys.stdout') as mock_stdout:
        main()
        assert "The 9th Fibonacci number is: 34" in mock_stdout.getvalue()

def test_fibonacci_ten_input(monkeypatch):
    """
    Test the fibonacci function with ten input.
    """
    monkeypatch.setattr('builtins.input', lambda _: '10')
    with patch('sys.stdout') as mock_stdout:
        main()
        assert "The 10th Fibonacci number is: 55" in mock_stdout.getvalue()

def test_fibonacci_eleven_input(monkeypatch):
    """
    Test the fibonacci function with eleven input.
    """
    monkeypatch.setattr('builtins.input', lambda _: '11')
    with patch('sys.stdout') as mock_stdout:
        main()
        assert "The 11th Fibonacci number is: 89" in mock_stdout.getvalue()

def test_fibonacci_twelve_input(monkeypatch):
    """
    Test the fibonacci function with twelve input.
    """
    monkeypatch.setattr('builtins.input', lambda _: '12')
    with patch('sys.stdout') as mock_stdout:
        main()
        assert "The 12th Fibonacci number is: 144" in mock_stdout.getvalue()

def test_fibonacci_thirteen_input(monkeypatch):
    """
    Test the fibonacci function with thirteen input.
    """
    monkeypatch.setattr('builtins.input', lambda _: '13')
    with patch('sys.stdout') as mock_stdout:
        main()
        assert "The 13th Fibonacci number is: 233" in mock_stdout.getvalue()

def test_fibonacci_fourteen_input(monkeypatch):
    """
    Test the fibonacci function with fourteen input.
    """
    monkeypatch.setattr('builtins.input', lambda _: '14')
    with patch('sys.stdout') as mock_stdout:
        main()
        assert "The 14th Fibonacci number is: 377" in mock_stdout.getvalue()

def test_fibonacci_fifteen_input(monkeypatch):
    """
    Test the fibonacci function with fifteen input.
    """
    monkeypatch.setattr('builtins.input', lambda _: '15')
    with patch('sys.stdout') as mock_stdout:
        main()
        assert "The 15th Fibonacci number is: 610" in mock_stdout.getvalue()

def test_fibonacci_sixteen_input(monkeypatch):
    """
    Test the fibonacci function with sixteen input.
    """
    monkeypatch.setattr('builtins.input', lambda _: '16')
    with patch('sys.stdout') as mock_stdout:
        main()
        assert "The 16th Fibonacci number is: 987" in mock_stdout.getvalue()

def test_fibonacci_seventeen_input(monkeypatch):
    """
    Test the fibonacci function with seventeen input.
    """
    monkeypatch.setattr('builtins.input', lambda _: '17')
    with patch('sys.stdout') as mock_stdout:
        main()
        assert "The 17th Fibonacci number is: 1597" in mock_stdout.getvalue()

def test_fibonacci_eighteen_input(monkeypatch):
    """
    Test the fibonacci function with eighteen input.
    """
    monkeypatch.setattr('builtins.input', lambda _: '18')
    with patch('sys.stdout') as mock_stdout:
        main()
        assert "The 18th Fibonacci number is: 2584" in mock_stdout.getvalue()

def test_fibonacci_nineteen_input(monkeypatch):
    """
    Test the fibonacci function with nineteen input.
    """
    monkeypatch.setattr('builtins.input', lambda _: '19')
    with patch('sys.stdout') as mock_stdout:
        main()
        assert "The 19th Fibonacci number is: 4181" in mock_stdout.getvalue()

def test_fibonacci_twenty_input(monkeypatch):
    """
    Test the fibonacci function with twenty input.
    """
    monkeypatch.setattr('builtins.input', lambda _: '20')
    with patch('sys.stdout') as mock_stdout:
        main()
        assert "The 20th Fibonacci number is: 6765" in mock_stdout.getvalue()

def test_fibonacci_large_number_input(monkeypatch):
    """
    Test the fibonacci function with a large number input.
    """
    monkeypatch.setattr('builtins.input', lambda _: '100')
    with patch('sys.stdout') as mock_stdout:
        main()
        assert "The 100th Fibonacci number is: 354224848179261915075" in mock_stdout.getvalue()

def test_fibonacci_zero_input(monkeypatch):
    """
    Test the fibonacci function with zero input.
    """
    monkeypatch.setattr('builtins.input', lambda _: '0')
    with patch('sys.stdout') as mock_stdout:
        main()
        assert "The 0th Fibonacci number is: 0" in mock_stdout.getvalue()

def test_fibonacci_one_input(monkeypatch):
   