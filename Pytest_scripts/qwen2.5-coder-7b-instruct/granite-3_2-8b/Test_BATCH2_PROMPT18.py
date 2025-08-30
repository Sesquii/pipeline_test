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

# ===== GENERATED TESTS =====
```python
import os
import pytest
from datetime import timedelta

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

# Test cases

@pytest.fixture
def setup_log_file():
    """Setup a test log file."""
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)
    yield
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)

def test_write_to_log(setup_log_file):
    """Test the write_to_log function."""
    write_to_log('Test message')
    with open(LOG_FILE, 'r') as f:
        content = f.read()
    assert 'Test message' in content

def test_check_log_size_empty_file(setup_log_file):
    """Test check_log_size function with an empty log file."""
    assert not check_log_size()

def test_check_log_size_full_file(setup_log_file):
    """Test check_log_size function with a full log file."""
    write_to_log('a' * MAX_SIZE_BYTES)
    assert check_log_size()

def test_main_with_rotation(setup_log_file, monkeypatch):
    """Test the main function with log rotation."""
    # Mock time.sleep to speed up the test
    def mock_sleep(seconds):
        pass
    monkeypatch.setattr(time, 'sleep', mock_sleep)

    # Write enough messages to trigger rotation
    for _ in range(MAX_SIZE_BYTES // 10 + 1):
        write_to_log('a' * 10)

    # Check if a backup file was created
    backup_files = [f for f in os.listdir() if f.startswith(LOG_FILE)]
    assert len(backup_files) == 1

def test_main_no_rotation(setup_log_file, monkeypatch):
    """Test the main function without log rotation."""
    # Mock time.sleep to speed up the test
    def mock_sleep(seconds):
        pass
    monkeypatch.setattr(time, 'sleep', mock_sleep)

    # Write less messages than to trigger rotation
    for _ in range(MAX_SIZE_BYTES // 10):
        write_to_log('a' * 10)

    # Check if no backup file was created
    backup_files = [f for f in os.listdir() if f.startswith(LOG_FILE)]
    assert len(backup_files) == 0

def test_main_with_large_message(setup_log_file, monkeypatch):
    """Test the main function with a large message."""
    # Mock time.sleep to speed up the test
    def mock_sleep(seconds):
        pass
    monkeypatch.setattr(time, 'sleep', mock_sleep)

    # Write a large message
    write_to_log('a' * (MAX_SIZE_BYTES + 1))

    # Check if a backup file was created
    backup_files = [f for f in os.listdir() if f.startswith(LOG_FILE)]
    assert len(backup_files) == 1

def test_main_with_negative_delay(setup_log_file, monkeypatch):
    """Test the main function with a negative delay."""
    # Mock time.sleep to speed up the test
    def mock_sleep(seconds):
        pass
    monkeypatch.setattr(time, 'sleep', mock_sleep)

    # Set negative delay
    global DELAY_SECONDS
    DELAY_SECONDS = -5

    # Write a message
    write_to_log('Test message')

    # Check if no backup file was created
    backup_files = [f for f in os.listdir() if f.startswith(LOG_FILE)]
    assert len(backup_files) == 0
```