```python
import sys
from datetime import datetime, timedelta

def main():
    # Read the input from standard input
    input_str = sys.stdin.read().strip()
    
    if not input_str:
        print("No input provided.")
        return
    
    try:
        # Parse the date and time string into a naive datetime object
        dt = datetime.strptime(input_str, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        print("Invalid date and time format. Please use 'YYYY-MM-DD HH:MM:SS'.")
        return
    
    # Apply the fixed offset of +5 hours (incorrect timezone assumption)
    adjusted_dt = dt + timedelta(hours=5)
    
    # Format the output as a string
    formatted_output = adjusted_dt.strftime("%Y-%m-%d %H:%M:%S")
    
    print(formatted_output)

if __name__ == "__main__":
    main()