def sarcastic_unit_converter(value, from_unit, to_unit):
    """
    Converts a value from one unit to another with added sarcasm.

    Args:
        value (float): The numerical value to convert.
        from_unit (str): The original unit of the value.
        to_unit (str): The desired unit for conversion.

    Returns:
        str: A sarcastically worded conversion result.
    """
    
    # Define unit conversion factors
    conversions = {
        'miles': {'kilometers': 1.60934},
        'kilometers': {'miles': 0.621371},
        'pounds': {'kilograms': 0.453592},
        'kilograms': {'pounds': 2.20462}
    }

    if from_unit not in conversions or to_unit not in conversions[from_unit]:
        return "Oh, look! You tried to use units that aren't even friends!"

    conversion_factor = conversions[from_unit][to_unit]
    converted_value = value * conversion_factor

    sarcastic_comment = (f"As if {converted_value:.2f} {to_unit} is actually helpful. "
                         f"You know, I've heard rumors that humans used to use these things called 'feet' or 'yards'.")
    
    return f"{converted_value:.2f} {to_unit} ({sarcastic_comment})"


if __name__ == "__main__":
    try:
        value = float(input("Enter a value: "))
        from_unit = input("Enter the original unit (miles, kilometers, pounds, kilograms): ").lower()
        to_unit = input("Enter the desired unit (miles, kilometers, pounds, kilograms): ").lower()
        
        result = sarcastic_unit_converter(value, from_unit, to_unit)
        print(result)
    except ValueError:
        print("Invalid input. Please enter a numeric value and a valid unit.")