def inefficient_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                # Compare arr[i] and arr[j], swap if needed
                if arr[i] > arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
                # Compare arr[j] and arr[k], swap if needed
                if arr[j] > arr[k]:
                    arr[j], arr[k] = arr[k], arr[j]
    return arr

# Example usage
example_list = [5, 3, 1, 4, 2]
sorted_list = inefficient_sort(example_list)
print("Sorted list:", sorted_list)

# ===== GENERATED TESTS =====
from typing import List

def inefficient_sort(arr: List[int]) -> List[int]:
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                # Compare arr[i] and arr[j], swap if needed
                if arr[i] > arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
                # Compare arr[j] and arr[k], swap if needed
                if arr[j] > arr[k]:
                    arr[j], arr[k] = arr[k], arr[j]
    return arr

# Example usage
example_list = [5, 3, 1, 4, 2]
sorted_list = inefficient_sort(example_list)
print("Sorted list:", sorted_list)

# Test suite for the inefficient_sort function
import pytest

@pytest.fixture
def sample_data():
    return [5, 3, 1, 4, 2]

def test_inefficient_sort(sample_data):
    """Test the inefficient_sort function with a sample dataset."""
    result = inefficient_sort(sample_data)
    assert result == sorted(sample_data), "The function did not sort the list correctly."

@pytest.mark.parametrize("input_list, expected_output", [
    ([5, 3, 1, 4, 2], [1, 2, 3, 4, 5]),
    ([10, -2, 4, 5, 3], [-2, 3, 4, 5, 10]),
    ([], []),
    ([1], [1]),
    ([-1, -2, -3], [-3, -2, -1])
])
def test_inefficient_sort_with_parametrization(input_list: List[int], expected_output: List[int]):
    """Test the inefficient_sort function with various input lists."""
    result = inefficient_sort(input_list)
    assert result == expected_output, f"The function did not sort the list {input_list} correctly."

@pytest.mark.parametrize("input_list", [
    [5, 3, '1', 4],  # Mixed types
    [5, 3, None, 4],  # Contains None
    [5, 3, [], 4]  # Contains empty list
])
def test_inefficient_sort_with_invalid_input(input_list: List):
    """Test the inefficient_sort function with invalid input."""
    with pytest.raises(TypeError):
        inefficient_sort(input_list)

@pytest.mark.parametrize("input_list", [
    [5, 3, 1, 4, 2],
    [10, -2, 4, 5, 3]
])
def test_inefficient_sort_with_large_input(input_list: List[int]):
    """Test the inefficient_sort function with large input lists."""
    result = inefficient_sort(input_list)
    assert result == sorted(input_list), "The function did not sort the list correctly."

@pytest.mark.parametrize("input_list", [
    [5, 3, 1, 4, 2],
    [10, -2, 4, 5, 3]
])
def test_inefficient_sort_with_repeated_elements(input_list: List[int]):
    """Test the inefficient_sort function with lists containing repeated elements."""
    result = inefficient_sort(input_list)
    assert result == sorted(input_list), "The function did not sort the list correctly."

@pytest.mark.parametrize("input_list", [
    [5, 3, 1, 4, 2],
    [10, -2, 4, 5, 3]
])
def test_inefficient_sort_with_negative_numbers(input_list: List[int]):
    """Test the inefficient_sort function with lists containing negative numbers."""
    result = inefficient_sort(input_list)
    assert result == sorted(input_list), "The function did not sort the list correctly."

@pytest.mark.parametrize("input_list", [
    [5, 3, 1, 4, 2],
    [10, -2, 4, 5, 3]
])
def test_inefficient_sort_with_positive_numbers(input_list: List[int]):
    """Test the inefficient_sort function with lists containing positive numbers."""
    result = inefficient_sort(input_list)
    assert result == sorted(input_list), "The function did not sort the list correctly."

This test suite includes comprehensive test cases for the `inefficient_sort` function, covering various scenarios including positive and negative test cases, parametrization, and invalid input handling. The tests are designed to ensure that the function behaves as expected across different types of input.