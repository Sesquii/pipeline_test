```python
import argparse
from datetime import datetime
import zoneinfo

def main():
    parser = argparse.ArgumentParser(description='Calculate time difference ignoring timezone')
    parser.add_argument('date1', help='First datetime (YYYY-MM-DDTHH:MM)')
    parser.add_argument('date2', help='Second datetime (YYYY-MM-DDTHH:MM)')
    args = parser.parse_args()
    
    # Parse the dates
    date1 = datetime.strptime(args.date1, "%Y-%m-%dT%H:%M")
    date2 = datetime.strptime(args.date2, "%Y-%m-%dT%H:%M")
    
    # Convert to UTC timezone
    tz = zoneinfo.ZoneInfo('UTC')
    dt1_utc = date1.replace(tzinfo=tz)
    dt2_utc = date2.replace(tzinfo=tz)
    
    delta = dt2_utc - dt1_utc
    print(f"The time difference is {delta.total_seconds() / 3600} hours")

if __name__ == "__main__":
    main()