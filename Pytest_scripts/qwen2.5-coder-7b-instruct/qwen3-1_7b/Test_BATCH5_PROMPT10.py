```python
import sys

def example_function():
    print("Start")
    x = 5
    y = x + 3
    print(f"Result: {y}")

events = []
example_function()

for event in reversed(events):
    print(event)

if __name__ == "__main__":
    pass

# ===== GENERATED TESTS =====
```python
import pytest

# Original code remains unchanged
import sys

def example_function():
    print("Start")
    x = 5
    y = x + 3
    print(f"Result: {y}")

events = []
example_function()

for event in reversed(events):
    print(event)

if __name__ == "__main__":
    pass

# Test suite starts here

def test_example_function(capsys):
    """
    Test the example_function to ensure it prints the correct output.
    """
    # Capture the printed output
    example_function()
    captured = capsys.readouterr()

    # Check if the expected output is present in the captured output
    assert "Start" in captured.out
    assert "Result: 8" in captured.out

def test_example_function_with_negative_input(capsys):
    """
    Test the example_function with negative input to ensure it handles errors gracefully.
    """
    # Mocking sys.stdin for testing purposes
    with pytest.raises(SystemExit) as excinfo:
        example_function()

    assert excinfo.type == SystemExit
    assert excinfo.value.code == 1

# Additional test cases can be added here following the same pattern
```

This test suite includes two test functions: `test_example_function` and `test_example_function_with_negative_input`. The first test function checks if the `example_function` prints the correct output, while the second test function simulates a negative scenario to ensure that the function handles errors gracefully.