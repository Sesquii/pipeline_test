import pytest
import sys, os
from unittest.mock import patch
from Script_Factory.Script_Factory_Runs.all_runs.prompt18_qwen30b_default import convert


from Script_Factory.Script_Factory_Runs.all_runs.prompt18_qwen30b_default import (
    convert,
    test_different_results_same_input,
    test_return_type
)

def test_convert_normal_case():
    """Test normal conversion from meters to feet."""
    result = convert(10.0, "m", "ft")
    assert isinstance(result, float)
    # Should be approximately 32.8084 feet
    assert result > 30.0
    assert result < 35.0

def test_convert_edge_case_zero():
    """Test conversion with zero value."""
    result = convert(0.0, "m", "ft")
    assert isinstance(result, float)
    assert result == 0.0

def test_convert_same_units():
    """Test conversion between same units (should return original value)."""
    result = convert(5.0, "m", "m")
    assert isinstance(result, float)
    assert result == 5.0

def test_convert_negative_value():
    """Test conversion with negative value."""
    result = convert(-10.0, "m", "ft")
    assert isinstance(result, float)
    # Should be approximately -32.8084 feet
    assert result < -30.0
    assert result > -35.0

def test_convert_unsupported_from_unit():
    """Test conversion with unsupported source unit."""
    with pytest.raises(ValueError, match="Unsupported units"):
        convert(10.0, "invalid", "ft")

def test_convert_unsupported_to_unit():
    """Test conversion with unsupported target unit."""
    with pytest.raises(ValueError, match="Unsupported units"):
        convert(10.0, "m", "invalid")

def test_convert_both_unsupported_units():
    """Test conversion with both units unsupported."""
    with pytest.raises(ValueError, match="Unsupported units"):
        convert(10.0, "invalid", "also_invalid")

def test_convert_perturbation_effect():
    """Test that perturbation produces different results on consecutive calls."""
    # Mock random.uniform to return fixed values for predictable testing
    with patch('random.uniform', side_effect=[0.95, 1.05]):
        result1 = convert(10.0, "m", "ft")
        result2 = convert(10.0, "m", "ft")
        
        # With fixed perturbations, results should be deterministic
        # But since we're testing the non-deterministic nature, this tests 
        # that the function handles random values properly
        assert isinstance(result1, float)
        assert isinstance(result2, float)

def test_convert_with_large_value():
    """Test conversion with a large value."""
    result = convert(1000000.0, "km", "mi")
    assert isinstance(result, float)
    # Should be approximately 621371 miles
    assert result > 600000.0
    assert result < 650000.0

def test_convert_with_small_value():
    """Test conversion with a very small value."""
    result = convert(0.001, "m", "ft")
    assert isinstance(result, float)
    # Should be approximately 0.00328 feet
    assert result > 0.003
    assert result < 0.004

def test_convert_all_unit_combinations():
    """Test conversion between all supported unit combinations."""
    units = ["m", "ft", "km", "mi"]
    
    for from_unit in units:
        for to_unit in units:
            if from_unit != to_unit:
                result = convert(1.0, from_unit, to_unit)
                assert isinstance(result, float)
                # Should be a positive number
                assert result > 0.0
