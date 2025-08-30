import pytest
from BATCH1_PROMPT18_qwen3-1_7b import Union

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

    # Unit tests using pytest
    import pytest

    def test_convert_normal_case():
        """Test with normal input values."""
        assert convert(10.0, 'm', 'ft') == pytest.approx(32.8084)

    def test_convert_edge_case_empty_list():
        """Test with empty list as input."""
        with pytest.raises(TypeError):
            convert([], 'm', 'ft')

    def test_convert_edge_case_zero():
        """Test with zero value."""
        assert convert(0.0, 'm', 'ft') == 0.0

    def test_convert_edge_case_negative_number():
        """Test with negative number."""
        assert convert(-10.0, 'm', 'ft') == pytest.approx(-32.8084)

    def test_convert_edge_case_null_value():
        """Test with null value."""
        with pytest.raises(TypeError):
            convert(None, 'm', 'ft')

    def test_convert_invalid_unit():
        """Test with invalid unit."""
        with pytest.raises(ValueError):
            convert(10.0, 'invalid', 'ft')

    def test_convert_non_deterministic_conversion():
        """Test non-deterministic conversion."""
        result1 = convert(10.0, 'm', 'ft')
        result2 = convert(10.0, 'm', 'ft')
        assert abs(result1 - result2) >= 0.0001

    def test_convert_conversion_factor():
        """Test conversion factor calculation."""
        assert convert(1.0, 'm', 'km') == pytest.approx(1.0)
        assert convert(1.0, 'm', 'mi') == pytest.approx(0.621371)

    def test_convert_conversion_factor_with_perturbation():
        """Test conversion factor with perturbation."""
        result = convert(1.0, 'm', 'ft')
        expected = 3.28084 * (1 + random.uniform(-0.05, 0.05))
        assert abs(result - expected) < 0.0001