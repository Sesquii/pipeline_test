import sys

def sample_function():
    print("Start")
    print("Inside function")
    print("End")

events = []
sample_function()
events.reverse()
for event in events:
    print(event)

if __name__ == "__main__":
    pass  # Entry point to ensure script runs when executed

# ===== GENERATED TESTS =====
import sys
from typing import List

def sample_function():
    """Function that prints a sequence of strings."""
    print("Start")
    print("Inside function")
    print("End")

events = []
sample_function()
events.reverse()
for event in events:
    print(event)

if __name__ == "__main__":
    pass  # Entry point to ensure script runs when executed

# Test suite for the sample_function
import pytest

def test_sample_function(capsys):
    """Test that sample_function prints the correct sequence of strings."""
    expected_output = [
        "End",
        "Inside function",
        "Start"
    ]
    
    sample_function()
    
    captured = capsys.readouterr()
    output_lines = captured.out.strip().split('\n')
    
    assert output_lines == expected_output, f"Expected output does not match. Got: {output_lines}"

def test_sample_function_with_no_events(capsys):
    """Test that sample_function prints the correct sequence of strings even if events list is empty."""
    global events
    events = []
    expected_output = [
        "End",
        "Inside function",
        "Start"
    ]
    
    sample_function()
    
    captured = capsys.readouterr()
    output_lines = captured.out.strip().split('\n')
    
    assert output_lines == expected_output, f"Expected output does not match. Got: {output_lines}"

def test_sample_function_with_reversed_events(capsys):
    """Test that sample_function prints the correct sequence of strings even if events list is reversed."""
    global events
    events = ["Start", "Inside function", "End"]
    expected_output = [
        "End",
        "Inside function",
        "Start"
    ]
    
    sample_function()
    
    captured = capsys.readouterr()
    output_lines = captured.out.strip().split('\n')
    
    assert output_lines == expected_output, f"Expected output does not match. Got: {output_lines}"
