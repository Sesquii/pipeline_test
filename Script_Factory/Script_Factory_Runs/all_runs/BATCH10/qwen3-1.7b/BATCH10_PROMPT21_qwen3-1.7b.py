```python
import datetime
import time

def generate_password():
    now = datetime.datetime.now()
    return f"{now.year}-{now.month}-{now.day} {now.hour}:{now.minute}:{now.second}"

if __name__ == "__main__":
    while True:
        print(generate_password())
        time.sleep(60)