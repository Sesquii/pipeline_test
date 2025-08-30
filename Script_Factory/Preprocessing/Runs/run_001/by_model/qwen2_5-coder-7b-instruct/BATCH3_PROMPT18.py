# BATCH3_PROMPT18_{{model_name}}.py

import os
import time

class SelfDestructingDataLog:
    def __init__(self, max_size=1024 * 1024, log_dir='logs'):
        self.max_size = max_size
        self.log_dir = log_dir
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)
        self.current_log_file = None

    def get_next_log_filename(self):
        return os.path.join(self.log_dir, f"log_{time.strftime('%Y%m%d%H%M%S')}.txt")

    def write_log_message(self, message):
        if not self.current_log_file or os.path.getsize(self.current_log_file) >= self.max_size:
            if self.current_log_file:
                os.remove(self.current_log_file)
            self.current_log_file = self.get_next_log_filename()
        
        with open(self.current_log_file, 'a') as log_file:
            log_file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {message}\n")

if __name__ == "__main__":
    log_handler = SelfDestructingDataLog(max_size=1024, log_dir='logs')
    
    try:
        while True:
            log_message = input("Enter log message (or type 'exit' to quit): ")
            if log_message.lower() == 'exit':
                break
            log_handler.write_log_message(log_message)
            time.sleep(5)  # Log every 5 seconds
    except KeyboardInterrupt:
        print("\nLog session terminated.")
```

This Python script implements a "Self-Destructing Data Log" as described. It writes log messages to files in a specified directory, deletes the file when it reaches a certain size, and starts a new one. The program runs indefinitely until the user types 'exit'. Each log entry includes a timestamp.