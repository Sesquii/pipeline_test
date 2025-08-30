# BATCH10_PROMPT17_qwen.py

# Import necessary library
from datetime import timedelta

# Define a list of fictional holidays with their corresponding celebrations
holidays = [
    ("Festival of Lights", "Festival of Fireworks"),
    ("Day of Harmony", "Day of Innovation"),
    ("Month of Magic", "Season of Serenity")
]

# Function to generate circular list of holidays
def circular_holiday_list(holiday_list):
    # Create an empty list to store the circular list
    circular_list = []
    
    # Iterate over each holiday in the list
    for i, (holiday, celebration) in enumerate(holiday_list):
        # Calculate the next index using modulo to ensure it wraps around
        next_index = (i + 1) % len(holiday_list)
        
        # Append a tuple of current holiday and its celebration with the next one's name
        circular_list.append((holiday, f"{celebration} for {holiday_list[next_index][0]}"))
    
    return circular_list

# Entry point of the program
if __name__ == "__main__":
    # Generate the circular list of holidays
    result = circular_holiday_list(holidays)
    
    # Print each holiday and its celebration with the next one's name
    for holiday, celebration in result:
        print(f"{holiday}: {celebration}")