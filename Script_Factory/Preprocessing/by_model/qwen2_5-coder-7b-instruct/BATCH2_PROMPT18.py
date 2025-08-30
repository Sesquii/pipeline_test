import time
import os

# Constants
LOG_FILE = 'log.txt'
MAX_LOG_SIZE = 1024 * 1024  # 1 MB
SLEEP_INTERVAL = 5  # seconds

def write_log_message(message):
    """Write a log message to the file."""
    with open(LOG_FILE, 'a') as file:
        file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {message}\n")

def check_and_rotate_log():
    """Check if the log file size exceeds MAX_LOG_SIZE and rotate it if necessary."""
    if os.path.exists(LOG_FILE):
        if os.path.getsize(LOG_FILE) >= MAX_LOG_SIZE:
            os.remove(LOG_FILE)
            write_log_message("Log has been rotated.")

if __name__ == "__main__":
    while True:
        message = input("Enter a log message (or 'exit' to quit): ")
        if message.lower() == 'exit':
            break
        write_log_message(message)
        check_and_rotate_log()
        time.sleep(SLEEP_INTERVAL)