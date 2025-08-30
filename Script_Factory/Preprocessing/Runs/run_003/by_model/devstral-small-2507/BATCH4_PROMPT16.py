def convert_miles_to_kilometers(miles):
    """Convert miles to kilometers."""
    return miles * 1.60934

def sarcastic_unit_converter():
    """Perform unit conversion with sarcastic comments."""
    # Get user input
    user_input = input("Enter a value and unit (e.g., '100 miles'): ")

    try:
        # Split the input into value and unit
        value, unit = user_input.split()

        # Convert the value to float for calculation
        value = float(value)

        if unit.lower() == "miles":
            kilometers = convert_miles_to_kilometers(value)
            print(f"Oh sure, {value} miles is like... {kilometers:.2f} kilometers. Wow.")
        else:
            print("Really? You think I care about that unit? Try 'miles' next time.")

    except ValueError:
        print("Seriously? I can't even parse that. Try again with a number and unit.")

if __name__ == "__main__":
    sarcastic_unit_converter()