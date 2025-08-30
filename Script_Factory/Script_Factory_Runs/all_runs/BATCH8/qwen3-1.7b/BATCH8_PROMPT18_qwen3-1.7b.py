```python
import datetime

def main():
    dt_str = input("Enter date and time (YYYY-MM-DD HH:MM:SS): ")
    dt = datetime.datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    utc_time = dt + datetime.timedelta(hours=5)
    print(utc_time)

if __name__ == "__main__":
    main()