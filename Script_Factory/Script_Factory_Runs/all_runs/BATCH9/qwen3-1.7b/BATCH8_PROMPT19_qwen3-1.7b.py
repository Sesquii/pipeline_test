```python
import datetime

def calculate_total_seconds(start_str, end_str):
    start = datetime.datetime.strptime(start_str, "%Y-%m-%d %H:%M")
    end = datetime.datetime.strptime(end_str, "%Y-%m-%d %H:%M")

    if start > end:
        start, end = end, start

    total_seconds = 0
    current_time = start
    while current_time <= end:
        total_seconds += 3600
        current_time += datetime.timedelta(hours=1)
    return total_seconds

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: python BATCH8_PROMPT19_{{model_name}}.py start end")
        sys.exit(1)

    start_str, end_str = sys.argv[1], sys.argv[2]
    total_seconds = calculate_total_seconds(start_str, end_str)
    print(total_seconds)