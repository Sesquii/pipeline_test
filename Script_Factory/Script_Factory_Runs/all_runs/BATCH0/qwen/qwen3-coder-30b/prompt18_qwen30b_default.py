import random
from typing import Dict, Tuple

def convert(value: float, from_unit: str, to_unit: str) -> float:
    """
    Convert a value from one unit to another with non-deterministic perturbation.
    
    The conversion factors are perturbed uniformly at random within ±5% of their
    standard values to introduce non-determinism. Each call produces potentially
    different results even with identical arguments.
    
    Args:
        value: The numeric value to convert
        from_unit: The source unit ("m", "ft", "km", "mi")
        to_unit: The target unit ("m", "ft", "km", "mi")
        
    Returns:
        The converted value as a float
        
    Raises:
        ValueError: If units are not supported
    """
    # Standard conversion factors to meters
    standard_factors: Dict[str, float] = {
        "m": 1.0,
        "ft": 0.3048,
        "km": 1000.0,
        "mi": 1609.344
    }
    
    if from_unit not in standard_factors or to_unit not in standard_factors:
        raise ValueError(f"Unsupported units: {from_unit} or {to_unit}")
    
    # Convert to meters first
    value_in_meters = value * standard_factors[from_unit]
    
    # Apply random perturbation to the conversion factor (±5%)
    perturbation_factor = random.uniform(0.95, 1.05)
    
    # Convert from meters to target unit with perturbed factor
    converted_value = value_in_meters / (standard_factors[to_unit] * perturbation_factor)
    
    return float(converted_value)

if __name__ == "__main__":
    # Demonstrate converting 10 m → ft twice
    result1 = convert(10.0, "m", "ft")
    result2 = convert(10.0, "m", "ft")
    print(f"10 meters to feet: {result1:.4f} ft")
    print(f"10 meters to feet: {result2:.4f} ft")

# Unit tests
import unittest

class TestNonDeterministicConverter(unittest.TestCase):
    def test_return_type(self):
        """Test that the function returns a float."""
        result = convert(1.0, "m", "ft")
        self.assertIsInstance(result, float)
    
    def test_different_results_same_input(self):
        """Test that two consecutive calls with same args produce different results."""
        result1 = convert(10.0, "m", "ft")
        result2 = convert(10.0, "m", "ft")
        
        # Check they are not equal (with tolerance for very small differences)
        self.assertNotEqual(result1, result2)
        
        # Verify they differ by at least 0.01%
        difference_percent = abs((result1 - result2) / result1) * 100
        self.assertGreater(difference_percent, 0.01)

if __name__ == "__main__":
    unittest.main()
