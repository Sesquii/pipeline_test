import random
import unittest
from typing import Dict

CONVERSION_FACTORS: Dict[str, float] = {
    "m": 1.0,
    "ft": 0.3048,
    "km": 1000.0,
    "mi": 0.621371
}


def convert(value: float, from_unit: str, to_unit: str) -> float:
    """
    Converts a value between supported units with non-deterministic perturbation.

    The conversion factors are based on standard ratios but include a uniform random
    perturbation of up to ±5% to ensure non-determinism. This is useful for testing
    systems that must handle variability in input data.

    Args:
        value (float): The value to convert.
        from_unit (str): The unit of the input value.
        to_unit (str): The desired output unit.

    Returns:
        float: The converted value with added non-deterministic perturbation.
    """
    if from_unit not in CONVERSION_FACTORS or to_unit not in CONVERSION_FACTORS:
        raise ValueError("Unsupported unit")

    factor = CONVERSION_FACTORS[from_unit] / CONVERSION_FACTORS[to_unit]
    perturbation = random.uniform(-0.05, 0.05) * factor
    return value * factor + perturbation


class TestNonDeterministicConverter(unittest.TestCase):
    def test_return_type(self):
        self.assertIsInstance(convert(10, "m", "ft"), float)

    def test_non_determinism(self):
        conversion = convert(10, "m", "ft")
        next_conversion = convert(10, "m", "ft")
        self.assertGreaterEqual(abs((next_conversion - conversion) / conversion), 0.0001)


if __name__ == "__main__":
    print(convert(10, "m", "ft"))  # Should print a value around 32.808 (perturbed)
    print(convert(10, "m", "ft"))  # Should print another value around 32.808 (possibly different due to perturbation)