import random
from typing import Dict, Tuple

def convert(value: float, from_unit: str, to_unit: str) -> float:
    """
    Convert a value from one unit to another with non-deterministic perturbation.
    
    The conversion factor is computed using the standard ratio and then perturbed
    uniformly at random within ±5% of that value. This makes each call produce
    potentially different results even with identical arguments, making the converter
    non-deterministic.
    
    Args:
        value: The numeric value to convert
        from_unit: The source unit ("m", "ft", "km", "mi")
        to_unit: The target unit ("m", "ft", "km", "mi")
        
    Returns:
        The converted value as a float
        
    Raises:
        ValueError: If units are not supported
    """
    # Define standard conversion factors to meters
    standard_conversions: Dict[str, float] = {
        "m": 1.0,
        "ft": 0.3048,
        "km": 1000.0,
        "mi": 1609.344
    }
    
    if from_unit not in standard_conversions or to_unit not in standard_conversions:
        raise ValueError(f"Unsupported units: {from_unit} or {to_unit}")
    
    # Convert value to meters first
    value_in_meters = value * standard_conversions[from_unit]
    
    # Convert from meters to target unit with perturbation
    base_factor = standard_conversions[to_unit]
    perturbation = random.uniform(-0.05, 0.05)
    perturbed_factor = base_factor * (1 + perturbation)
    
    result = value_in_meters / perturbed_factor
    
    return float(result)

if __name__ == "__main__":
    # Demonstrate converting 10 m to ft twice
    print("Converting 10 meters to feet:")
    result1 = convert(10.0, "m", "ft")
    result2 = convert(10.0, "m", "ft")
    print(f"First conversion: {result1:.4f} ft")
    print(f"Second conversion: {result2:.4f} ft")

import unittest

class TestNonDeterministicConverter(unittest.TestCase):
    def test_return_type(self):
        """Test that the function returns a float."""
        result = convert(10.0, "m", "ft")
        self.assertIsInstance(result, float)
        
    def test_non_deterministic_behavior(self):
        """Test that two consecutive calls with same args produce different results."""
        result1 = convert(10.0, "m", "ft")
        result2 = convert(10.0, "m", "ft")
        
        # Ensure they are not exactly equal (with tolerance)
        self.assertNotEqual(result1, result2)
        
        # Check that they differ by at least 0.01%
        difference_percent = abs((result1 - result2) / result1) * 100
        self.assertGreater(difference_percent, 0.01)

