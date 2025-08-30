```python
import sys

# Generate a circular list of fictional holidays
holidays = [
    "Eclipse Festival", "Moonlight Mela", "Starlit Celebration",
    "Galaxy Day", "Celestial Dance", "Nova Event", "Solar Eclipse",
    "Lunar Marvel", "Stellar Harmony", "Cosmic Rite"
]

def main():
    for i, holiday in enumerate(holidays):
        next_holiday = holidays[(i + 1) % len(holidays)]
        print(f"{holiday} is celebrated on {next_holiday}")

if __name__ == "__main__":
    main()