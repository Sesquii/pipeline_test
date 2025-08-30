```python
if __name__ == "__main__":
    input_line = input("Enter value and unit (e.g., '100 miles'): ")
    parts = input_line.strip().split()
    
    if len(parts) < 2:
        print("Invalid input. Please enter a value and a unit.")
        exit()
    
    try:
        value_str, unit_str = parts
        value = float(value_str)
    except ValueError:
        print("Invalid value. Please enter a number.")
        exit()
    
    unit_conversions = {
        'miles': 1609.34,
        'km': 1,
        'meters': 1000,
    }
    
    if unit_str not in unit_conversions:
        print("Unsupported unit.")
        exit()
    
    conversion_factor = unit_conversions[unit_str]
    converted_value = value * conversion_factor
    
    print(f"{value} {unit_str} is equal to {converted_value:.2f} kilometers. Oh no, you're converting miles to kilometers? That's so sad.")

# ===== GENERATED TESTS =====
```python
import pytest

# Original script code remains unchanged

def test_input_validation():
    """Test input validation for valid and invalid inputs."""
    assert input_validation("100 miles") == (100.0, 'miles')
    with pytest.raises(SystemExit):
        input_validation("abc miles")
    with pytest.raises(SystemExit):
        input_validation("100")

def test_unit_conversion():
    """Test unit conversion for supported and unsupported units."""
    assert unit_conversion(100, 'miles') == 160934.0
    assert unit_conversion(100, 'km') == 100.0
    assert unit_conversion(100, 'meters') == 100000.0
    with pytest.raises(SystemExit):
        unit_conversion(100, 'yards')

def test_main_function():
    """Test the main function for different scenarios."""
    # Mocking input and output
    import io
    from contextlib import redirect_stdout
    
    def mock_input(prompt):
        return "100 miles"
    
    with io.StringIO() as buf, redirect_stdout(buf), pytest.raises(SystemExit):
        main()
        assert buf.getvalue().strip() == "Invalid value. Please enter a number."
    
    with io.StringIO() as buf, redirect_stdout(buf), pytest.raises(SystemExit):
        with patch('builtins.input', return_value="abc miles"):
            main()
        assert buf.getvalue().strip() == "Unsupported unit."
    
    with io.StringIO() as buf, redirect_stdout(buf):
        with patch('builtins.input', return_value="100 km"):
            main()
        assert buf.getvalue().strip() == "100.0 km is equal to 100.00 kilometers. Oh no, you're converting miles to kilometers? That's so sad."

# Test functions follow the requirements above
```