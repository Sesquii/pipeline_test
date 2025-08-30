```python
import os
import datetime
import time

def main():
    filename = 'log.txt'
    threshold_size = 1024 * 1024  # 1MB
    while True:
        current_time = datetime.datetime.now()
        with open(filename, 'a') as f:
            f.write(f"Log entry at {current_time}\n")
        file_size = os.path.getsize(filename)
        if file_size >= threshold_size:
            os.remove(filename)
            new_filename = f"log_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
            with open(new_filename, 'w') as f:
                pass
        time.sleep(5)

if __name__ == "__main__":
    main()