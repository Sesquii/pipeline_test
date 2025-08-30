```python
import os
import time

def main():
    current_log = 'log.txt'
    threshold_size = 1024 * 1024  # 1MB
    interval = 5  # seconds
    counter = 0

    while True:
        with open(current_log, 'a') as f:
            f.write(f"Log message at {time.time()}\n")
        file_size = os.path.getsize(current_log)
        if file_size >= threshold_size:
            os.remove(current_log)
            current_log = f"log_{counter}.txt"
            counter += 1
        time.sleep(interval)

if __name__ == "__main__":
    main()