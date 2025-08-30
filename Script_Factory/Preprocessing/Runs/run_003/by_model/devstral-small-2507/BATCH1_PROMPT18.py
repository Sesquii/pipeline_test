import random
from typing import Union

def convert(value: float, from_unit: str, to_unit: str) -> float:
    """
    Convert a value between different units of measurement with non-deterministic conversion factors.

    The conversion factor is perturbed uniformly at random within ±5% of the standard ratio for any pair
    of supported units. This means that repeated calls with identical arguments can produce different results.

    Supported units: "m" (meters), "ft" (feet), "km" (kilometers), "mi" (miles).

    Args:
        value: The numerical value to convert.
        from_unit: The unit of the input value.
        to_unit: The unit to convert the input value to.

    Returns:
        float: The converted value with a perturbed conversion factor.
    """
    # Standard conversion factors
    conversion_factors = {
        ('m', 'ft'): 3.28084,
        ('ft', 'm'): 1 / 3.28084,
        ('km', 'mi'): 0.621371,
        ('mi', 'km'): 1 / 0.621371,
        ('m', 'km'): 1 / 1000,
        ('km', 'm'): 1000,
        ('ft', 'mi'): 1 / 5280,
        ('mi', 'ft'): 5280,
    }

    # Perturb the conversion factor by ±5%
    if (from_unit, to_unit) in conversion_factors:
        base_factor = conversion_factors[(from_unit, to_unit)]
        perturbation = random.uniform(-0.05, 0.05)
        perturbed_factor = base_factor * (1 + perturbation)

        return value * perturbed_factor

    # Fallback if the conversion is not supported
    raise ValueError(f"Unsupported unit pair: {from_unit} to {to_unit}")

if __name__ == "__main__":
    # Demonstrate converting 10 meters to feet twice
    result1 = convert(10, 'm', 'ft')
    result2 = convert(10, 'm', 'ft')

    print(f"First conversion: 10 m → {result1:.4f} ft")
    print(f"Second conversion: 10 m → {result2:.4f} ft")

import unittest

class TestNonDeterministicUnitConverter(unittest.TestCase):
    def test_return_type(self):
        result = convert(10, 'm', 'ft')
        self.assertIsInstance(result, float)

    def test_non_determinism(self):
        value = 10
        from_unit = 'm'
        to_unit = 'ft'

        # Generate two results and check if they differ by at least 0.01%
        result1 = convert(value, from_unit, to_unit)
        result2 = convert(value, from_unit, to_unit)

        tolerance = 0.0001 * value
        self.assertGreater(abs(result1 - result2), tolerance)

if __name__ == "__main__":
    unittest.main()