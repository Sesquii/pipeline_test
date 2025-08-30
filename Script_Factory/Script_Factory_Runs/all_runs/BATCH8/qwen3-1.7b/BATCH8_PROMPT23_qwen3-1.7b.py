```python
if __name__ == "__main__":
    # Example cities and timezone offsets (in hours)
    start_city = "Paris"
    end_city = "New York"
    start_timezone = 2  # UTC+2
    end_timezone = -5   # UTC-5
    
    travel_time_hours = abs(start_timezone - end_timezone)
    
    print(f"The travel time is {travel_time_hours} hours.")