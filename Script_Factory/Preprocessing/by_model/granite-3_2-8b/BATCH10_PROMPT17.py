# BATCH10_PROMPT17_Granite.py

def generate_fictional_holidays(count):
    """
    Generate a circular list of fictional holidays where each holiday celebrates the next one.

    :param count: Number of unique holidays to create.
    :return: List of tuples, each containing a holiday name and its successor.
    """
    holidays = []
    
    # Create a loop of holidays
    for i in range(count):
        successor = (i + 1) % count
        holidays.append((f"Holiday {i+1}", f"Celebrates Holiday {(successor + 1)}"))
    
    return holidays


def main():
    """Entry point of the program."""
    num_holidays = 5  # Change this number to adjust the count of fictional holidays

    holidays = generate_fictional_holidays(num_holidays)

    print("Fictional Circular Holiday List:")
    for holiday, successor in holidays:
        print(f"{holiday}: Celebrates {successor}")


if __name__ == "__main__":
    main()