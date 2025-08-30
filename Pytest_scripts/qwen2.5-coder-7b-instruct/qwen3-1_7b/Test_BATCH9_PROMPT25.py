```python
def loop():
    while True:
        print("Entering self-referential infinite loop")
        loop()

if __name__ == "__main__":
    loop()

# ===== GENERATED TESTS =====
```python
# Original script

def loop():
    while True:
        print("Entering self-referential infinite loop")
        loop()

if __name__ == "__main__":
    loop()


# Test suite for the original script

import pytest

# Fixture to capture output from the function
@pytest.fixture
def captured_output(monkeypatch, capsys):
    monkeypatch.setattr('builtins.print', lambda *args: None)
    yield capsys.readouterr()

# Test case for the loop function
def test_loop(captured_output):
    """
    Test that the loop function does not cause an infinite loop.
    This test uses a fixture to capture output and checks if the expected message is printed.
    """
    with pytest.raises(RecursionError):
        loop()


# Additional test cases can be added here following the same pattern
```