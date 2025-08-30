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