```python
import random
from typing import Union

def convert(value: float, from_unit: str, to_unit: str) -> float:
    """
    Convert a value from one unit to another with non-deterministic conversion.
    
    The conversion factor is computed using the standard ratio and perturbed
    uniformly at random within ±5% of that value. This ensures that repeated
    calls with the same arguments can produce different results.
    
    Args:
        value: The numeric value to convert.
        from_unit: The unit to convert from (m, ft, km, mi).
        to_unit: The unit to convert to (m, ft, km, mi).
        
    Returns:
        float: The converted value.
    """
    if from_unit not in ['m', 'ft', 'km', 'mi'] or to_unit not in ['m', 'ft', 'km', 'mi']:
        raise ValueError("Unsupported unit")
    
    conversion_factors = {
        ('m', 'ft'): 3.28084,
        ('m', 'km'): 1000,
        ('m', 'mi'): 1609.34,
        ('ft', 'm'): 1 / 3.28084, # approx 0.3048
        ('ft', 'km'): 1 / (3.28084 * 1000), # 0.0003048
        ('ft', 'mi'): 5280,
        ('km', 'm'): 1000,
        ('km', 'ft'): 3280.84, # since 1 km is 1000 m * 3.28084 ft/m
        ('km', 'mi'): 1609.34, # since 1 mi = 1.60934 km
        ('mi', 'm'): 1609.34 / 3.28084, # approx 482.8
        ('mi', 'ft'): 5280,
        ('mi', 'km'): 1/1.60934, # approx 0.621371
    }
    
    factor = conversion_factors[(from_unit, to_unit)]
    r = random.uniform(-0.05, 0.05)
    perturbed_factor = factor * (1 + r)
    return value * perturbed_factor

if __name__ == "__main__":
    # Demonstration of non-deterministic conversion
    result1 = convert(10.0, 'm', 'ft')
    print(f"First conversion: {result1}")
    
    result2 = convert(10.0, 'm', 'ft')
    print(f"Second conversion: {result2}")

    # Unit tests using unittest
    import unittest

    class TestConvert(unittest.TestCase):
        def test_non_deterministic_conversion(self):
            value = 10.0
            from_unit = 'm'
            to_unit = 'ft'
            
            result1 = convert(value, from_unit, to_unit)
            result2 = convert(value, from_unit, to_unit)
            
            self.assertTrue(abs(result1 - result2) >= 0.0001)

    if __name__ == "__main__":
        unittest.main()