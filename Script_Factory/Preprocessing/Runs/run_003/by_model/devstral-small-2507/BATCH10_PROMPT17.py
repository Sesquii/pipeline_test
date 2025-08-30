# BATCH10_PROMPT17_Devstral.py

class Holiday:
    def __init__(self, name, celebrates):
        self.name = name
        self.celebrates = celebrates

def generate_circular_holidays(count=5):
    holidays = []
    for i in range(count):
        next_index = (i + 1) % count
        holiday = Holiday(f"Holiday_{i+1}", f"Holiday_{next_index+1}")
        holidays.append(holiday)
    
    # Make the last one celebrate the first to complete the circle
    if holidays:
        holidays[-1].celebrates = holidays[0].name
    
    return holidays

def print_holidays(holidays):
    for holiday in holidays:
        print(f"{holiday.name} celebrates {holiday.celebrates}")

if __name__ == "__main__":
    # Generate 5 circular holidays as an example
    holiday_list = generate_circular_holidays(5)
    print_holidays(holiday_list)