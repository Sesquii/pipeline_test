import os
import time
from datetime import datetime

# Define parameters
LOG_FILE = 'data_log.txt'
MAX_SIZE_BYTES = 1024 * 1024  # 1MB
DELAY_SECONDS = 5  # Time between log entries in seconds

def write_to_log(message):
    """Write a message to the current log file."""
    with open(LOG_FILE, 'a') as f:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        f.write(f"{timestamp} - {message}\n")

def check_log_size():
    """Check if the log file size is over the maximum allowed."""
    return os.path.getsize(LOG_FILE) > MAX_SIZE_BYTES

def main():
    while True:
        write_to_log('Log entry')

        # Check if log file has exceeded max size
        if check_log_size():
            # Rename current log file to a timestamped backup
            backup_filename = f"{LOG_FILE}.{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"
            os.rename(LOG_FILE, backup_filename)

            print(f"Log file size exceeded {MAX_SIZE_BYTES} bytes. Rotated to {backup_filename}")

        # Wait before next log entry
        time.sleep(DELAY_SECONDS)

if __name__ == "__main__":
    main()