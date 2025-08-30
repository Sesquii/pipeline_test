import pytest
import sys, os
from Script_Factory.Script_Factory_Runs.all_runs.prompt22_qwen30b_default import inefficient_sort


from Script_Factory.Script_Factory_Runs.all_runs.prompt22_qwen30b_default import (
    inefficient_sort
)

def test_inefficient_sort_normal_case():
    """
    Test inefficient_sort with a normal, expected input.
    This tests that the function can sort a typical list of integers.
    """
    sample_list = [64, 34, 25, 12, 22, 11, 90]
    expected = [11, 12, 22, 25, 34, 64, 90]
    result = inefficient_sort(sample_list)
    assert result == expected

def test_inefficient_sort_empty_list():
    """
    Test inefficient_sort with an empty list (edge case).
    This tests that the function handles empty input correctly.
    """
    empty_list = []
    result = inefficient_sort(empty_list)
    assert result == []

def test_inefficient_sort_single_element():
    """
    Test inefficient_sort with a single element list (edge case).
    This tests that the function handles minimal input correctly.
    """
    single_element = [42]
    expected = [42]
    result = inefficient_sort(single_element)
    assert result == expected

def test_inefficient_sort_already_sorted():
    """
    Test inefficient_sort with an already sorted list (edge case).
    This tests that the function works correctly even when input is sorted.
    """
    sorted_list = [1, 2, 3, 4, 5]
    expected = [1, 2, 3, 4, 5]
    result = inefficient_sort(sorted_list)
    assert result == expected

def test_inefficient_sort_reverse_sorted():
    """
    Test inefficient_sort with a reverse sorted list (edge case).
    This tests that the function can sort descending input correctly.
    """
    reverse_sorted = [5, 4, 3, 2, 1]
    expected = [1, 2, 3, 4, 5]
    result = inefficient_sort(reverse_sorted)
    assert result == expected

def test_inefficient_sort_with_duplicates():
    """
    Test inefficient_sort with duplicate values (edge case).
    This tests that the function handles duplicate elements correctly.
    """
    with_duplicates = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    expected = [1, 1, 2, 3, 4, 5, 5, 6, 9]
    result = inefficient_sort(with_duplicates)
    assert result == expected

def test_inefficient_sort_negative_numbers():
    """
    Test inefficient_sort with negative numbers (edge case).
    This tests that the function handles negative integers correctly.
    """
    negative_list = [-3, -1, -4, -1, -5, -9, -2, -6, -5]
    expected = [-9, -6, -5, -5, -4, -3, -2, -1, -1]
    result = inefficient_sort(negative_list)
    assert result == expected

def test_inefficient_sort_mixed_positive_negative():
    """
    Test inefficient_sort with mixed positive and negative numbers (edge case).
    This tests that the function handles mixed sign integers correctly.
    """
    mixed_list = [3, -1, 4, -1, 5, -9, 2, -6, 5]
    expected = [-9, -6, -1, -1, 2, 3, 4, 5, 5]
    result = inefficient_sort(mixed_list)
    assert result == expected

def test_inefficient_sort_original_unchanged():
    """
    Test that the original array is not modified (behavioral requirement).
    This tests that the function creates a copy and doesn't mutate the input.
    """
    original_list = [64, 34, 25, 12, 22, 11, 90]
    original_copy = original_list[:]  # Make a copy to compare
    result = inefficient_sort(original_list)
    assert original_list == original_copy  # Original should be unchanged
    assert result != original_list  # Result should be different object

def test_inefficient_sort_large_numbers():
    """
    Test inefficient_sort with large numbers (edge case).
    This tests that the function handles large integers correctly.
    """
    large_numbers = [1000000, 999999, 1000001, 500000]
    expected = [500000, 999999, 1000000, 1000001]
    result = inefficient_sort(large_numbers)
    assert result == expected
