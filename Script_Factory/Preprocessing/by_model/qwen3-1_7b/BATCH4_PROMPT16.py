```python
import sys

conversion_factors = {
    'miles': 1609.34,
    'km': 1,
    'liters': 3.78541,
    'gallons': 0.264172
}

if __name__ == "__main__":
    user_input = input("Enter value and unit (e.g., 100 miles): ").strip()
    if not user_input:
        print("Please enter a valid value and unit.")
        sys.exit()

    parts = user_input.split()
    if len(parts) < 2:
        print("Invalid input. Please provide a value and a unit.")
        sys.exit()

    value_str, unit_str = parts[0], parts[1]

    try:
        original_unit = unit_str
        target_unit = 'km'
        if original_unit not in conversion_factors:
            print(f"Unsupported unit: {original_unit}")
            sys.exit()

        value = float(value_str)
        converted_value = value * conversion_factors[original_unit]

        comment = "Oh, really? That's all you've got?"

        print(f"{converted_value:.2f} {target_unit} ({comment})")
    except ValueError:
        print("Invalid input. Please enter a number and a unit.")