import time
from os import path, remove

LOG_FILE = 'data_log.txt'
MAX_LOG_SIZE = 1024 * 50  # 50 KB


def write_to_log(message):
    with open(LOG_FILE, 'a') as file:
        file.write(f'{time.ctime()} - {message}\n')

    check_and_rotate_log()


def check_and_rotate_log():
    if path.getsize(LOG_FILE) > MAX_LOG_SIZE:
        remove(LOG_FILE)
        print('Log rotated and started fresh.')
        open(LOG_FILE, 'a').close()  # Ensure the log file is created again


if __name__ == "__main__":
    while True:
        message = input("Enter a log message (or type 'quit' to exit): ")
        if message.lower() == 'quit':
            break

        write_to_log(message)
        time.sleep(2)  # Wait for 2 seconds before the next log entry