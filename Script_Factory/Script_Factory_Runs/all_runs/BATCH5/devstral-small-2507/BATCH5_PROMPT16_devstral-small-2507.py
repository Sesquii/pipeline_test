def sarcastic_unit_converter():
    """
    A sarcastic unit converter that converts miles to kilometers
    and makes snarky comments about the results.
    """

    import re

    def convert_miles_to_km(miles):
        """Convert miles to kilometers."""
        return miles * 1.60934

    def get_sarcastic_comment(value, converted_value):
        """Generate a sarcastic comment based on the conversion."""
        if value < 1:
            return "Wow, you're really going places! Literally, like 0.5km."
        elif value < 10:
            return "Impressive! You've managed to travel almost nothing in kilometers."
        elif value < 50:
            return "Okay, so you're going about {} km. Big deal.".format(converted_value)
        elif value < 100:
            return "A whole {} km? I'm shaking in my boots.".format(converted_value)
        else:
            return "Wow, {} km! You must be so proud.".format(converted_value)

    def parse_input(input_str):
        """Parse the input string to extract value and unit."""
        match = re.match(r'(\d+\.?\d*)\s*(miles?)', input_str, re.IGNORECASE)
        if not match:
            raise ValueError("Invalid input format. Please enter a number followed by 'miles'.")
        value = float(match.group(1))
        unit = match.group(2).lower()
        return value, unit

    def main():
        """Main function to handle user interaction."""
        try:
            user_input = input("Enter a value and unit (e.g., '100 miles'): ")
            value, unit = parse_input(user_input)

            if unit != "miles":
                raise ValueError("This converter only handles miles to kilometers.")

            converted_value = convert_miles_to_km(value)
            comment = get_sarcastic_comment(value, converted_value)

            print(f"{value} {unit} is equal to {converted_value:.2f} km.")
            print(comment)

        except ValueError as e:
            print(f"Error: {e}")

    if __name__ == "__main__":
        main()