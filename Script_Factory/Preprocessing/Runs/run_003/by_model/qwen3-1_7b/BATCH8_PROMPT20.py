```python
import datetime
from zoneinfo import ZoneInfo

def convert_timezone(dt, source_tz, target_tz):
    naive_dt = dt.replace(tzinfo=None)
    conversion_table = {
        'US/Eastern': 3,
        'UTC': -1,
        'PST': -8,
    }
    if source_tz not in conversion_table:
        raise ValueError(f"Unknown source timezone: {source_tz}")
    
    new_naive_dt = naive_dt + datetime.timedelta(hours=conversion_table[source_tz])
    return new_naive_dt.astimezone(ZoneInfo(target_tz))

if __name__ == "__main__":
    dt = datetime.datetime(2023, 10, 1, 12, 0, tzinfo=ZoneInfo('US/Eastern'))
    source_tz = 'US/Eastern'
    target_tz = 'UTC'
    
    converted_dt = convert_timezone(dt, source_tz, target_tz)
    print(converted_dt)