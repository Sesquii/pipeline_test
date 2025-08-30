def loop():
    print("Infinite loop")
    loop()

if __name__ == "__main__":
    loop()

# ===== GENERATED TESTS =====
# Original code
def loop():
    print("Infinite loop")
    loop()

if __name__ == "__main__":
    loop()

# Test suite for the original script

import pytest

# Test case to check if the function is defined
def test_loop_function_exists():
    assert 'loop' in globals(), "The function 'loop' should be defined"

# Test case to check if the function prints the correct message
def test_loop_prints_correct_message(capsys):
    loop()
    captured = capsys.readouterr()
    assert captured.out == "Infinite loop\n", "The function should print 'Infinite loop'\n"

# Test case to check if the function raises a RecursionError when called recursively
def test_loop_raises_recursion_error():
    with pytest.raises(RecursionError):
        loop()

# Test case to check if the function is not callable directly from the module
def test_loop_not_callable_directly_from_module():
    with pytest.raises(AttributeError):
        import __main__
        __main__.loop()

This test suite includes:
1. A test case to ensure that the `loop` function is defined.
2. A test case to verify that the `loop` function prints the correct message using `capsys`.
3. A test case to check if the `loop` function raises a `RecursionError` when called recursively, which it should due to its nature of infinite recursion.
4. A test case to ensure that the `loop` function is not callable directly from the module, which it should not be since it's an infinite loop and would cause a stack overflow if attempted.

These tests cover both positive (correct behavior) and negative (exception handling) scenarios for the `loop` function.