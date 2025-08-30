def convert_unit(value, unit):
    if "miles" in unit:
        converted_value = value * 1.60934
        return f"{value} miles is {converted_value:.2f} kilometers. Wow, who needs metric anyway?"
    elif "kilometers" in unit:
        converted_value = value / 1.60934
        return f"{value} kilometers is {converted_value:.2f} miles. You're still using kilometers? Outdated!"
    else:
        return "Unsupported unit conversion."

if __name__ == "__main__":
    try:
        value = float(input("Enter the value: "))
        unit = input("Enter the unit (e.g., '100 miles'): ")
        result = convert_unit(value, unit)
        print(result)
    except ValueError:
        print("Please enter a valid number for the value.")