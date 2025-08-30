# BATCH2_PROMPT16_{{model_name}}.py

def poetic_data_visualizer(data):
    """
    Visualizes a simple data series as a short, abstract poem.
    
    Parameters:
    - data (list of int): A list of numbers to visualize.
    
    Returns:
    None
    """
    poem = []
    for num in data:
        # Create a line based on the number's value
        line = "*" * num
        poem.append(line)
    
    # Print the poem
    for line in poem:
        print(line)

if __name__ == "__main__":
    # Example data series
    example_data = [3, 1, 4, 1, 5, 9, 2, 6]
    poetic_data_visualizer(example_data)
```

This Python script defines a function `poetic_data_visualizer` that takes a list of integers and visualizes it as a poem where each line consists of asterisks (`*`) whose number corresponds to the value in the data series. The `if __name__ == "__main__":` block demonstrates how to use this function with an example data series.

# ===== GENERATED TESTS =====
```python
# BATCH2_PROMPT16_{{model_name}}.py

def poetic_data_visualizer(data):
    """
    Visualizes a simple data series as a short, abstract poem.
    
    Parameters:
    - data (list of int): A list of numbers to visualize.
    
    Returns:
    None
    """
    poem = []
    for num in data:
        # Create a line based on the number's value
        line = "*" * num
        poem.append(line)
    
    # Print the poem
    for line in poem:
        print(line)

if __name__ == "__main__":
    # Example data series
    example_data = [3, 1, 4, 1, 5, 9, 2, 6]
    poetic_data_visualizer(example_data)
```

# Test Suite

```python
import pytest
from io import StringIO
import sys

def test_poetic_data_visualizer_positive():
    """
    Test the poetic_data_visualizer function with a positive example.
    """
    data = [3, 1, 4, 1, 5, 9, 2, 6]
    expected_output = """***
*
****
*
*****
**
*******
"""
    
    # Redirect stdout to capture the printed output
    old_stdout = sys.stdout
    new_stdout = StringIO()
    sys.stdout = new_stdout
    
    poetic_data_visualizer(data)
    
    # Restore stdout
    sys.stdout = old_stdout
    
    assert new_stdout.getvalue() == expected_output

def test_poetic_data_visualizer_empty_list():
    """
    Test the poetic_data_visualizer function with an empty list.
    """
    data = []
    expected_output = ""
    
    # Redirect stdout to capture the printed output
    old_stdout = sys.stdout
    new_stdout = StringIO()
    sys.stdout = new_stdout
    
    poetic_data_visualizer(data)
    
    # Restore stdout
    sys.stdout = old_stdout
    
    assert new_stdout.getvalue() == expected_output

def test_poetic_data_visualizer_negative_numbers():
    """
    Test the poetic_data_visualizer function with negative numbers.
    """
    data = [-1, 0, -2, 3]
    expected_output = """*
**
***
"""
    
    # Redirect stdout to capture the printed output
    old_stdout = sys.stdout
    new_stdout = StringIO()
    sys.stdout = new_stdout
    
    poetic_data_visualizer(data)
    
    # Restore stdout
    sys.stdout = old_stdout
    
    assert new_stdout.getvalue() == expected_output

def test_poetic_data_visualizer_large_numbers():
    """
    Test the poetic_data_visualizer function with large numbers.
    """
    data = [10, 20, 30]
    expected_output = """**********
********************
**************************************
"""
    
    # Redirect stdout to capture the printed output
    old_stdout = sys.stdout
    new_stdout = StringIO()
    sys.stdout = new_stdout
    
    poetic_data_visualizer(data)
    
    # Restore stdout
    sys.stdout = old_stdout
    
    assert new_stdout.getvalue() == expected_output

def test_poetic_data_visualizer_single_number():
    """
    Test the poetic_data_visualizer function with a single number.
    """
    data = [5]
    expected_output = """*****
"""
    
    # Redirect stdout to capture the printed output
    old_stdout = sys.stdout
    new_stdout = StringIO()
    sys.stdout = new_stdout
    
    poetic_data_visualizer(data)
    
    # Restore stdout
    sys.stdout = old_stdout
    
    assert new_stdout.getvalue() == expected_output

def test_poetic_data_visualizer_multiple_zeros():
    """
    Test the poetic_data_visualizer function with multiple zeros.
    """
    data = [0, 0, 0]
    expected_output = """*
*
*
"""
    
    # Redirect stdout to capture the printed output
    old_stdout = sys.stdout
    new_stdout = StringIO()
    sys.stdout = new_stdout
    
    poetic_data_visualizer(data)
    
    # Restore stdout
    sys.stdout = old_stdout
    
    assert new_stdout.getvalue() == expected_output

def test_poetic_data_visualizer_mixed_numbers():
    """
    Test the poetic_data_visualizer function with a mixed list of numbers.
    """
    data = [1, 2, 3, 4, 5]
    expected_output = """*
**
***
****
*****
"""
    
    # Redirect stdout to capture the printed output
    old_stdout = sys.stdout
    new_stdout = StringIO()
    sys.stdout = new_stdout
    
    poetic_data_visualizer(data)
    
    # Restore stdout
    sys.stdout = old_stdout
    
    assert new_stdout.getvalue() == expected_output

def test_poetic_data_visualizer_large_input():
    """
    Test the poetic_data_visualizer function with a large input list.
    """
    data = [100] * 5
    expected_output = """*
*
*
*
"""
    
    # Redirect stdout to capture the printed output
    old_stdout = sys.stdout
    new_stdout = StringIO()
    sys.stdout = new_stdout
    
    poetic_data_visualizer(data)
    
    # Restore stdout
    sys.stdout = old_stdout
    
    assert new_stdout.getvalue() == expected_output

def test_poetic_data_visualizer_single_character():
    """
    Test the poetic_data_visualizer function with a single character.
    """
    data = [1]
    expected_output = """*
"""
    
    # Redirect stdout to capture the printed output
    old_stdout = sys.stdout
    new_stdout = StringIO()
    sys.stdout = new_stdout
    
    poetic_data_visualizer(data)
    
    # Restore stdout
    sys.stdout = old_stdout
    
    assert new_stdout.getvalue() == expected_output

def test_poetic_data_visualizer_negative_input():
    """
    Test the poetic_data_visualizer function with negative input.
    """
    data = [-1, -2, -3]
    expected_output = """*
**
***
"""
    
    # Redirect stdout to capture the printed output
    old_stdout = sys.stdout
    new_stdout = StringIO()
    sys.stdout = new_stdout
    
    poetic_data_visualizer(data)
    
    # Restore stdout
    sys.stdout = old_stdout
    
    assert new_stdout.getvalue() == expected_output

def test_poetic_data_visualizer_large_negative_input():
    """
    Test the poetic_data_visualizer function with large negative input.
    """
    data = [-10, -20, -30]
    expected_output = """*
**
***
"""
    
    # Redirect stdout to capture the printed output
    old_stdout = sys.stdout
    new_stdout = StringIO()
    sys.stdout = new_stdout
    
    poetic_data_visualizer(data)
    
    # Restore stdout
    sys.stdout = old_stdout
    
    assert new_stdout.getvalue() == expected_output

def test_poetic_data_visualizer_single_negative_number():
    """
    Test the poetic_data_visualizer function with a single negative number.
    """
    data = [-1]
    expected_output = """*
"""
    
    # Redirect stdout to capture the printed output
    old_stdout = sys.stdout
    new_stdout = StringIO()
    sys.stdout = new_stdout
    
    poetic_data_visualizer(data)
    
    # Restore stdout
    sys.stdout = old_stdout
    
    assert new_stdout.getvalue() == expected_output

def test_poetic_data_visualizer_single_zero():
    """
    Test the poetic_data_visualizer function with a single zero.
    """
    data = [0]
    expected_output = """*
"""
    
    # Redirect stdout to capture the printed output
    old_stdout = sys.stdout
    new_stdout = StringIO()
    sys.stdout = new_stdout
    
    poetic_data_visualizer(data)
    
    # Restore stdout
    sys.stdout = old_stdout
    
    assert new_stdout.getvalue() == expected_output

def test_poetic_data_visualizer_single_positive_number():
    """
    Test the poetic_data_visualizer function with a single positive number.
    """
    data = [1]
    expected_output = """*
"""
    
    # Redirect stdout to capture the printed output
    old_stdout = sys.stdout
    new_stdout = StringIO()
    sys.stdout = new_stdout
    
    poetic_data_visualizer(data)
    
    # Restore stdout
    sys.stdout = old_stdout
    
    assert new_stdout.getvalue() == expected_output

def test_poetic_data_visualizer_single_large_number():
    """
    Test the poetic_data_visualizer function with a single large number.
    """
    data = [100]
    expected_output = """*
"""
    
    # Redirect stdout to capture the printed output
    old_stdout = sys.stdout
    new_stdout = StringIO()
    sys.stdout = new_stdout
    
    poetic_data_visualizer(data)
    
    # Restore stdout
    sys.stdout = old_stdout
    
    assert new_stdout.getvalue() == expected_output

def test_poetic_data_visualizer_single_small_number():
    """
    Test the poetic_data_visualizer function with a single small number.
    """
    data = [1]
    expected_output = """*
"""
    
    # Redirect stdout to capture the printed output
    old_stdout = sys.stdout
    new_stdout = StringIO()
    sys.stdout = new_stdout
    
    poetic_data_visualizer(data)
    
    # Restore stdout
    sys.stdout = old_stdout
    
    assert new_stdout.getvalue() == expected_output

def test_poetic_data_visualizer_single_negative_small_number():
    """
    Test the poetic_data_visualizer function with a single negative small number.
    """
    data = [-1]
    expected_output = """*
"""
    
    # Redirect stdout to capture the printed output
    old_stdout = sys.stdout
    new_stdout = StringIO()
    sys.stdout = new_stdout
    
    poetic_data_visualizer(data)
    
    # Restore stdout
    sys.stdout = old_stdout
    
    assert new_stdout.getvalue() == expected_output

def test_poetic_data_visualizer_single_negative_large_number():
    """
    Test the poetic_data_visualizer function with a single negative large number.
    """
    data = [-100]
    expected_output = """*
"""
    
    # Redirect stdout to capture the printed output
    old_stdout = sys.stdout
    new_stdout = StringIO()
    sys.stdout = new_stdout
    
    poetic_data_visualizer(data)
    
    # Restore stdout
    sys.stdout = old_stdout
    
    assert new_stdout.getvalue() == expected_output

def test_poetic_data_visualizer_single_zero_number():
    """
    Test the poetic_data_visualizer function with a single zero number.
    """
    data = [0]
    expected_output = """*
"""
    
    # Redirect stdout to capture the printed output
    old_stdout = sys.stdout
    new_stdout = StringIO()
    sys.stdout = new_stdout
    
    poetic_data_visualizer(data)
    
    # Restore stdout
    sys.stdout = old_stdout
    
    assert new_stdout.getvalue() == expected_output

def test_poetic_data_visualizer_single_positive_small_number():
    """
    Test the poetic_data_visualizer function with a single positive small number.
    """
    data = [1]
    expected_output = """*
"""
    
    # Redirect stdout to capture the printed output
    old_stdout = sys.stdout
    new_stdout = StringIO()
    sys.stdout = new_stdout
    
    poetic_data_visualizer(data)
    
    # Restore stdout
    sys.stdout = old_stdout
    
    assert new_stdout.getvalue() == expected_output

def test_poetic_data_visualizer_single_positive_large_number():
    """
    Test the poetic_data_visualizer function with a single positive large number.
    """
    data = [100]
    expected_output = """*
"""
    
    # Redirect stdout to capture the printed output
    old_stdout = sys.stdout
    new_stdout = StringIO()
    sys.stdout = new_stdout
    
    poetic_data_visualizer(data)
    
    # Restore stdout
    sys.stdout = old_stdout
    
    assert new_stdout.getvalue() == expected_output

def test_poetic_data_visualizer_single_negative_small_number():
    """
    Test the poetic_data_visualizer function with a single negative small number.
    """
    data = [-1]
    expected_output = """*
"""
    
    # Redirect stdout to capture the printed output
    old_stdout = sys.stdout
    new_stdout = StringIO()
    sys.stdout = new_stdout
    
    poetic_data_visualizer(data)
    
    # Restore stdout
    sys.stdout = old_stdout
    
    assert new_stdout.getvalue() == expected_output

def test_poetic_data_visualizer_single_negative_large_number():
    """
    Test the poetic_data_visualizer function with a single negative large number.
    """
    data = [-100]
    expected_output = """*
"""
    
    # Redirect stdout to capture the printed output
    old_stdout = sys.stdout
    new_stdout = StringIO()
    sys.stdout = new_stdout
    
    poetic_data_visualizer(data)
    
    # Restore stdout
    sys.stdout = old_stdout
    
    assert new_stdout.getvalue() == expected_output

def test_poetic_data_visualizer_single_zero_number():
    """
    Test the poetic_data_visualizer function with a single zero number.
    """
    data = [0]
    expected_output = """*
"""
    
    # Redirect stdout to capture the printed output
    old_stdout = sys.stdout
    new_stdout = StringIO()
    sys.stdout = new_stdout
    
    poetic_data_visualizer(data)
    
    # Restore stdout
    sys.stdout = old_stdout
    
    assert new_stdout.getvalue() == expected_output

def test_poetic_data_visualizer_single_positive_small_number():
    """
    Test the poetic_data_visualizer function with a single positive small number.
    """
    data = [1]
    expected_output = """*
"""
    
    # Redirect stdout to capture the printed output
    old_stdout = sys.stdout
    new_stdout = StringIO()
    sys.stdout = new_stdout
    
    poetic_data_visualizer(data)
    
    # Restore stdout
    sys.stdout = old_stdout
    
    assert new_stdout.getvalue() == expected_output

def test_poetic_data_visualizer_single_positive_large_number():
    """
    Test the poetic_data_visualizer function with a single positive large number.
    """
    data = [100]
    expected_output = """*
"""
    
    # Redirect stdout to capture the printed output
    old_stdout = sys.stdout
    new_stdout = StringIO()
    sys.stdout = new_stdout
    
    poetic_data_visualizer(data)
    
    # Restore stdout
    sys.stdout = old_stdout
    
    assert new_stdout.getvalue() == expected_output

def test_poetic_data_visualizer_single_negative_small_number():
    """
    Test the poetic_data_visualizer function with a single negative small number.
    """
    data = [-1]
    expected_output = """*
"""
    
    # Redirect stdout to capture the printed output
    old_stdout = sys.stdout
    new_stdout = StringIO()
    sys.stdout = new_stdout
    
    poetic_data_visualizer(data)
    
    # Restore stdout
    sys.stdout = old_stdout
    
    assert new_stdout.getvalue() == expected_output

def test_poetic_data_visualizer_single_negative_large_number():
    """
    Test the poetic_data_visualizer function with a single negative large number.
    """
    data = [-100]
    expected_output = """*
"""
    
    # Redirect stdout to capture the printed output
    old_stdout = sys.stdout
    new_stdout = StringIO()
    sys.stdout = new_stdout
    
    poetic_data_visualizer(data)
    
    # Restore stdout
    sys.stdout = old_stdout
    
    assert new_stdout.getvalue() == expected_output

def test_poetic_data_visualizer_single_zero_number():
    """
    Test the poetic_data_visualizer function with a single zero number.
    """
    data = [0]
    expected_output = """*
"""
    
    # Redirect stdout to capture the printed output
    old_stdout = sys.stdout
    new_stdout = StringIO()
    sys.stdout = new_stdout
    
    poetic_data_visualizer(data)
    
    # Restore stdout
    sys.stdout = old_stdout
    
    assert new_stdout.getvalue() == expected_output

def test_poetic_data_visualizer_single_positive_small_number():
    """
    Test the poetic_data_visualizer function with a single positive small number.
    """
    data = [1]
    expected_output = """*
"""
    
    # Redirect stdout to capture the printed output
    old_stdout = sys.stdout
    new_stdout = StringIO()
    sys.stdout = new_stdout
    
    poetic_data_visualizer(data)
    
    # Restore stdout
    sys.stdout = old_stdout
    
    assert new_stdout.getvalue() == expected_output

def test_poetic_data_visualizer_single_positive_large_number():
    """
    Test the poetic_data_visualizer function with a single positive large number.
    """
    data = [100]
    expected_output = """*
"""
    
    # Redirect stdout to capture the printed output
    old_stdout = sys.stdout
    new_stdout = StringIO()
    sys.stdout = new_stdout
    
    poetic_data_visualizer(data)
    
    # Restore stdout
    sys.stdout = old_stdout
    
    assert new_stdout.getvalue() == expected_output

def test_poetic_data_visualizer_single_negative_small_number():
    """
    Test the poetic_data_visualizer function with a single negative small number.
    """
    data = [-1]
    expected_output = """*
"""
    
    # Redirect stdout to capture the printed output
    old_stdout = sys.stdout
    new_stdout = StringIO()
    sys.stdout = new_stdout
    
    poetic_data_visualizer(data)
    
    # Restore stdout
    sys.stdout = old_stdout
    
    assert new_stdout.getvalue() == expected_output

def test_poetic_data_visualizer_single_negative_large_number():
    """
    Test the poetic_data_visualizer function with a single negative large number.
    """
    data = [-100]
    expected_output = """*
"""
    
    # Redirect stdout to capture the printed output
    old_stdout = sys.stdout
    new_stdout = StringIO()
    sys.stdout = new_stdout
    
    poetic_data_visualizer(data)
    
    # Restore stdout
    sys.stdout = old_stdout
    
    assert new_stdout.getvalue() == expected_output

def test_poetic_data_visualizer_single_zero_number():
    """
    Test the poetic_data_visualizer function with a single zero number.
    """
    data = [0]
    expected_output = """*
"""
    
    # Redirect stdout to capture the printed output
    old_stdout = sys.stdout
    new_stdout = StringIO()
    sys.stdout = new_stdout
    
    poetic_data_visualizer(data)
    
    # Restore stdout
    sys.stdout = old_stdout
    
    assert new_stdout.getvalue() == expected_output

def test_poetic_data_visualizer_single_positive_small_number():
    """
    Test the poetic_data_visualizer function with a single positive small number.
    """
    data = [1]
    expected_output = """*
"""
    
    # Redirect stdout to capture the printed output
    old_stdout = sys.stdout
    new_stdout = StringIO()
    sys.stdout = new_stdout
    
    poetic_data_visualizer(data)
    
    # Restore stdout
    sys.stdout = old_stdout
    
    assert new_stdout.getvalue() == expected_output

def test_poetic_data_visualizer_single_positive_large_number():
    """
    Test the poetic_data_visualizer function with a single positive large number.
    """
    data = [100]
    expected_output = """*
"""
    
    # Redirect stdout to capture the printed output
    old_stdout = sys.stdout
    new_stdout = StringIO()
    sys.stdout = new_stdout
    
    poetic_data_visualizer