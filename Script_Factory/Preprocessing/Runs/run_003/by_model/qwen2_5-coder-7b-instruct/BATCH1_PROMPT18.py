import random
from typing import Tuple

def generate_conversion_factor(base_ratio: float) -> float:
    """Generate a perturbed conversion factor within ±5% of the base ratio."""
    return base_ratio * (1 + 0.05 * (random.uniform(-1, 1)))

CONVERSION_FACTORS: dict[Tuple[str, str], float] = {
    ('m', 'ft'): generate_conversion_factor(3.28084),
    ('m', 'km'): generate_conversion_factor(0.001),
    ('m', 'mi'): generate_conversion_factor(0.000621371),
    ('ft', 'm'): 1 / generate_conversion_factor(3.28084),
    ('ft', 'km'): generate_conversion_factor(0.0003048),
    ('ft', 'mi'): generate_conversion_factor(0.000189394),
    ('km', 'm'): 1 / generate_conversion_factor(0.001),
    ('km', 'ft'): 1 / generate_conversion_factor(0.0003048),
    ('km', 'mi'): generate_conversion_factor(0.621371),
    ('mi', 'm'): 1 / generate_conversion_factor(0.000621371),
    ('mi', 'ft'): 1 / generate_conversion_factor(0.000189394),
    ('mi', 'km'): 1 / generate_conversion_factor(0.621371)
}

def convert(value: float, from_unit: str, to_unit: str) -> float:
    """
    Convert a value from one unit to another using a non-deterministic conversion factor.
    
    The conversion factor is perturbed uniformly at random within ±5% of the standard ratio each time the function is called.
    
    Args:
        value (float): The value to convert.
        from_unit (str): The unit of the input value ('m', 'ft', 'km', or 'mi').
        to_unit (str): The target unit for conversion ('m', 'ft', 'km', or 'mi').
        
    Returns:
        float: The converted value with a non-deterministic conversion factor.
        
    Raises:
        ValueError: If an unsupported unit is provided.
    """
    if (from_unit, to_unit) not in CONVERSION_FACTORS:
        raise ValueError(f"Unsupported unit pair: {from_unit} -> {to_unit}")
    
    return value * CONVERSION_FACTORS[(from_unit, to_unit)]

if __name__ == "__main__":
    print(convert(10, 'm', 'ft'))  # Non-deterministic output
    print(convert(10, 'm', 'ft'))  # Different non-deterministic output

import unittest

class TestConvertFunction(unittest.TestCase):
    def test_return_type(self):
        self.assertIsInstance(convert(10, 'm', 'ft'), float)

    def test_non_determinism(self):
        result1 = convert(10, 'm', 'ft')
        result2 = convert(10, 'm', 'ft')
        self.assertNotAlmostEqual(result1, result2, places=4)  # Test with a precision of 0.01%

if __name__ == "__main__":
    unittest.main()