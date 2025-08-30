```python
import sys

def main():
    time_zones = {
        'Paris': 1,
        'New York': -4,
        'London': 0,
        'Tokyo': 9,
        'Singapore': 8
    }
    
    start_city = sys.argv[1]
    end_city = sys.argv[2]
    
    if start_city not in time_zones or end_city not in time_zones:
        print("Invalid city")
        return
    
    start_offset = time_zones[start_city]
    end_offset = time_zones[end_city]
    
    travel_time_hours = abs(end_offset - start_offset)
    print(f"The travel time is {travel_time_hours} hours.")

if __name__ == "__main__":
    main()