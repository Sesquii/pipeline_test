import pytest
import sys, os

from Script_Factory.Script_Factory_Runs.all_runs.prompt13_qwen30b_default import (
    add_unhelpful_comments,
    calculate_sum,
    main,
    walk
)

def test_add_unhelpful_comments_normal_functionality():
    """Test that the function properly adds unhelpful comments to normal code."""
    sample_code = '''
def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
'''
    
    result = add_unhelpful_comments(sample_code)
    # Should not raise an exception and should return a string
    assert isinstance(result, str)
    # Should contain the original code structure
    assert 'def calculate_sum' in result
    assert 'total = 0' in result

def test_add_unhelpful_comments_empty_string():
    """Test that empty string input returns empty string."""
    result = add_unhelpful_comments("")
    assert result == ""

def test_add_unhelpful_comments_whitespace_only():
    """Test that whitespace-only input returns the same whitespace."""
    result = add_unhelpful_comments("   \n  \n  ")
    assert result == "   \n  \n  "

def test_add_unhelpful_comments_invalid_syntax():
    """Test that invalid syntax input returns original code."""
    invalid_code = '''
def bad_function(
    # Missing closing parenthesis
'''
    
    result = add_unhelpful_comments(invalid_code)
    # Should return the original invalid code without modification
    assert result == invalid_code

def test_add_unhelpful_comments_single_line():
    """Test that single line code works correctly."""
    single_line = "x = 1 + 2"
    result = add_unhelpful_comments(single_line)
    assert isinstance(result, str)
    assert "x = 1 + 2" in result

def test_add_unhelpful_comments_complex_structure():
    """Test that complex code structures are handled properly."""
    complex_code = '''
class MyClass:
    def __init__(self):
        self.value = 0
    
    def method(self):
        if True:
            for i in range(10):
                print(i)
        return self.value

def global_function():
    pass
'''
    
    result = add_unhelpful_comments(complex_code)
    assert isinstance(result, str)
    # Should contain the original structure
    assert 'class MyClass' in result
    assert 'def __init__' in result
    assert 'def method' in result

def test_add_unhelpful_comments_import_statements():
    """Test that import statements are properly handled."""
    import_code = '''
import os
from sys import path

def test():
    pass
'''
    
    result = add_unhelpful_comments(import_code)
    assert isinstance(result, str)
    # Should contain original imports and structure
    assert 'import os' in result
    assert 'from sys import path' in result

def test_add_unhelpful_comments_no_comments_added():
    """Test that code with minimal structure works (no comments added)."""
    minimal_code = "x = 1"
    result = add_unhelpful_comments(minimal_code)
    assert isinstance(result, str)
    assert "x = 1" in result

def test_add_unhelpful_comments_multiple_statements():
    """Test code with multiple statements handles correctly."""
    multi_stmt_code = '''
a = 1
b = 2
c = a + b
print(c)
'''
    
    result = add_unhelpful_comments(multi_stmt_code)
    assert isinstance(result, str)
    # Should contain original statements
    assert 'a = 1' in result
    assert 'b = 2' in result
    assert 'c = a + b' in result
    assert 'print(c)' in result

def test_add_unhelpful_comments_nested_structures():
    """Test nested code structures are handled properly."""
    nested_code = '''
def outer():
    def inner():
        if True:
            while False:
                pass
    return "done"
'''
    
    result = add_unhelpful_comments(nested_code)
    assert isinstance(result, str)
    # Should contain original structure
    assert 'def outer' in result
    assert 'def inner' in result
    assert 'if True' in result
    assert 'while False' in result

def test_add_unhelpful_comments_preserves_indentation():
    """Test that indentation is preserved correctly."""
    indented_code = '''
    def spaced_function():
        if True:
            print("hello")
'''
    
    result = add_unhelpful_comments(indented_code)
    assert isinstance(result, str)
    # Should preserve the indentation structure
    assert '    def spaced_function' in result
    assert '        if True' in result
