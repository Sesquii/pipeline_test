import os
import time

class SelfDestructingDataLog:
    def __init__(self, log_directory='logs', max_size_mb=10, interval_seconds=5):
        self.log_directory = log_directory
        self.max_size_bytes = max_size_mb * 1024 * 1024
        self.interval_seconds = interval_seconds
        self.current_log_file = None
        self.current_log_size = 0

        # Create log directory if it doesn't exist
        os.makedirs(self.log_directory, exist_ok=True)

    def _get_next_log_file(self):
        """Generate the next log file name"""
        timestamp = int(time.time())
        return os.path.join(self.log_directory, f'log_{timestamp}.txt')

    def _write_log_message(self, message):
        """Write a message to the current log file"""
        if not self.current_log_file:
            self.current_log_file = self._get_next_log_file()
            self.current_log_size = 0

        with open(self.current_log_file, 'a') as f:
            f.write(message + '\n')
            self.current_log_size += len(message) + 1  # +1 for newline

    def _check_log_size(self):
        """Check if current log file has reached max size and rotate if needed"""
        if self.current_log_size >= self.max_size_bytes:
            print(f"Log file {self.current_log_file} reached maximum size. Self-destructing...")
            os.remove(self.current_log_file)
            self.current_log_file = None
            self.current_log_size = 0

    def log_message(self, message):
        """Public method to log a message with size checking"""
        self._write_log_message(message)
        self._check_log_size()

    def run(self):
        """Run the logging loop"""
        counter = 1
        while True:
            message = f"Log message {counter} at {time.ctime()}"
            print(f"Logging: {message}")
            self.log_message(message)
            counter += 1
            time.sleep(self.interval_seconds)

if __name__ == "__main__":
    log = SelfDestructingDataLog(max_size_mb=0.1, interval_seconds=2)  # Small size for testing
    print("Starting Self-Destructing Data Log. Press Ctrl+C to stop.")
    try:
        log.run()
    except KeyboardInterrupt:
        print("\nStopping log service...")