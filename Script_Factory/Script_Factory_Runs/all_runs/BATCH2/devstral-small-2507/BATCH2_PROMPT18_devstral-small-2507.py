import os
import time

class SelfDestructingDataLog:
    def __init__(self, directory='.', max_size=1024, interval=5):
        """
        Initialize the self-destructing data log.

        :param directory: Directory to store log files (default is current directory)
        :param max_size: Maximum size of log file in bytes before self-destruction
        :param interval: Time interval between log entries in seconds
        """
        self.directory = directory
        self.max_size = max_size
        self.interval = interval
        self.current_log_file = None
        self.current_log_size = 0

    def _get_next_log_file(self):
        """Generate the next log file name."""
        timestamp = int(time.time())
        return os.path.join(self.directory, f'log_{timestamp}.txt')

    def _write_log_entry(self, message):
        """Write a log entry to the current log file."""
        if not self.current_log_file or self.current_log_size >= self.max_size:
            # Close current file if it exists and has reached max size
            if self.current_log_file and os.path.exists(self.current_log_file):
                os.remove(self.current_log_file)
            # Create new log file
            self.current_log_file = self._get_next_log_file()
            self.current_log_size = 0

        with open(self.current_log_file, 'a') as f:
            f.write(message + '\n')
            self.current_log_size = os.path.getsize(self.current_log_file)

    def start_logging(self):
        """Start the logging process."""
        log_counter = 1
        while True:
            message = f'Log entry {log_counter} - {time.ctime()}'
            print(f"Writing: {message}")  # Debug output to console
            self._write_log_entry(message)
            log_counter += 1
            time.sleep(self.interval)

if __name__ == "__main__":
    # Create and start the self-destructing data log
    logger = SelfDestructingDataLog(max_size=100, interval=2)  # Small size for demo purposes
    try:
        logger.start_logging()
    except KeyboardInterrupt:
        print("\nLogging stopped by user.")