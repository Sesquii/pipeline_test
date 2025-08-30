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

# ===== GENERATED TESTS =====
import os
import datetime
import time
from typing import Any

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

# Test suite for the provided script

import pytest

def test_main_with_small_file():
    """Test that the log file is not rotated when it's smaller than the threshold."""
    filename = 'log_test.txt'
    threshold_size = 1024 * 1024  # 1MB
    with open(filename, 'w') as f:
        f.write("Log entry at " + str(datetime.datetime.now()) + "\n")
    
    main()
    
    assert os.path.exists(filename)
    assert os.path.getsize(filename) < threshold_size
    
    os.remove(filename)

def test_main_with_large_file():
    """Test that the log file is rotated when it's larger than the threshold."""
    filename = 'log_test.txt'
    threshold_size = 1024 * 1024  # 1MB
    with open(filename, 'w') as f:
        for _ in range(1000):
            f.write("Log entry at " + str(datetime.datetime.now()) + "\n")
    
    main()
    
    assert not os.path.exists(filename)
    new_filename = f"log_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
    assert os.path.exists(new_filename)
    assert os.path.getsize(new_filename) < threshold_size
    
    os.remove(new_filename)

def test_main_with_empty_file():
    """Test that the log file is not rotated when it's empty."""
    filename = 'log_test.txt'
    threshold_size = 1024 * 1024  # 1MB
    with open(filename, 'w') as f:
        pass
    
    main()
    
    assert os.path.exists(filename)
    assert os.path.getsize(filename) == 0
    
    os.remove(filename)

def test_main_with_negative_threshold():
    """Test that the script handles a negative threshold size gracefully."""
    filename = 'log_test.txt'
    threshold_size = -1  # Negative threshold
    with open(filename, 'w') as f:
        f.write("Log entry at " + str(datetime.datetime.now()) + "\n")
    
    main()
    
    assert os.path.exists(filename)
    assert os.path.getsize(filename) > 0
    
    os.remove(filename)

def test_main_with_zero_threshold():
    """Test that the script handles a zero threshold size gracefully."""
    filename = 'log_test.txt'
    threshold_size = 0  # Zero threshold
    with open(filename, 'w') as f:
        f.write("Log entry at " + str(datetime.datetime.now()) + "\n")
    
    main()
    
    assert os.path.exists(filename)
    assert os.path.getsize(filename) > 0
    
    os.remove(filename)

def test_main_with_large_threshold():
    """Test that the script handles a large threshold size gracefully."""
    filename = 'log_test.txt'
    threshold_size = 1024 * 1024 * 1024  # 1GB
    with open(filename, 'w') as f:
        f.write("Log entry at " + str(datetime.datetime.now()) + "\n")
    
    main()
    
    assert os.path.exists(filename)
    assert os.path.getsize(filename) > 0
    
    os.remove(filename)

def test_main_with_multiple_entries():
    """Test that the script handles multiple log entries gracefully."""
    filename = 'log_test.txt'
    threshold_size = 1024 * 1024  # 1MB
    with open(filename, 'w') as f:
        for _ in range(10):
            f.write("Log entry at " + str(datetime.datetime.now()) + "\n")
    
    main()
    
    assert os.path.exists(filename)
    assert os.path.getsize(filename) < threshold_size
    
    os.remove(filename)

def test_main_with_large_multiple_entries():
    """Test that the script handles large multiple log entries gracefully."""
    filename = 'log_test.txt'
    threshold_size = 1024 * 1024  # 1MB
    with open(filename, 'w') as f:
        for _ in range(1000):
            f.write("Log entry at " + str(datetime.datetime.now()) + "\n")
    
    main()
    
    assert not os.path.exists(filename)
    new_filename = f"log_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
    assert os.path.exists(new_filename)
    assert os.path.getsize(new_filename) < threshold_size
    
    os.remove(new_filename)

def test_main_with_no_entries():
    """Test that the script handles no log entries gracefully."""
    filename = 'log_test.txt'
    threshold_size = 1024 * 1024  # 1MB
    with open(filename, 'w') as f:
        pass
    
    main()
    
    assert os.path.exists(filename)
    assert os.path.getsize(filename) == 0
    
    os.remove(filename)

def test_main_with_existing_log_file():
    """Test that the script handles an existing log file gracefully."""
    filename = 'log_test.txt'
    threshold_size = 1024 * 1024  # 1MB
    with open(filename, 'w') as f:
        f.write("Log entry at " + str(datetime.datetime.now()) + "\n")
    
    main()
    
    assert os.path.exists(filename)
    assert os.path.getsize(filename) < threshold_size
    
    os.remove(filename)

def test_main_with_new_log_file():
    """Test that the script handles a new log file gracefully."""
    filename = 'log_test.txt'
    threshold_size = 1024 * 1024  # 1MB
    with open(filename, 'w') as f:
        pass
    
    main()
    
    assert os.path.exists(filename)
    assert os.path.getsize(filename) == 0
    
    os.remove(filename)

def test_main_with_rotated_log_file():
    """Test that the script handles a rotated log file gracefully."""
    filename = 'log_test.txt'
    threshold_size = 1024 * 1024  # 1MB
    with open(filename, 'w') as f:
        for _ in range(10):
            f.write("Log entry at " + str(datetime.datetime.now()) + "\n")
    
    main()
    
    assert not os.path.exists(filename)
    new_filename = f"log_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
    assert os.path.exists(new_filename)
    assert os.path.getsize(new_filename) < threshold_size
    
    os.remove(new_filename)

def test_main_with_rotated_log_file_and_new_entries():
    """Test that the script handles a rotated log file and new entries gracefully."""
    filename = 'log_test.txt'
    threshold_size = 1024 * 1024  # 1MB
    with open(filename, 'w') as f:
        for _ in range(10):
            f.write("Log entry at " + str(datetime.datetime.now()) + "\n")
    
    main()
    
    assert not os.path.exists(filename)
    new_filename = f"log_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
    assert os.path.exists(new_filename)
    assert os.path.getsize(new_filename) < threshold_size
    
    with open(new_filename, 'a') as f:
        for _ in range(10):
            f.write("Log entry at " + str(datetime.datetime.now()) + "\n")
    
    main()
    
    assert not os.path.exists(new_filename)
    new_new_filename = f"log_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
    assert os.path.exists(new_new_filename)
    assert os.path.getsize(new_new_filename) < threshold_size
    
    os.remove(new_new_filename)

def test_main_with_rotated_log_file_and_large_entries():
    """Test that the script handles a rotated log file and large entries gracefully."""
    filename = 'log_test.txt'
    threshold_size = 1024 * 1024  # 1MB
    with open(filename, 'w') as f:
        for _ in range(10):
            f.write("Log entry at " + str(datetime.datetime.now()) + "\n")
    
    main()
    
    assert not os.path.exists(filename)
    new_filename = f"log_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
    assert os.path.exists(new_filename)
    assert os.path.getsize(new_filename) < threshold_size
    
    with open(new_filename, 'a') as f:
        for _ in range(1000):
            f.write("Log entry at " + str(datetime.datetime.now()) + "\n")
    
    main()
    
    assert not os.path.exists(new_filename)
    new_new_filename = f"log_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
    assert os.path.exists(new_new_filename)
    assert os.path.getsize(new_new_filename) < threshold_size
    
    os.remove(new_new_filename)

def test_main_with_rotated_log_file_and_no_entries():
    """Test that the script handles a rotated log file and no entries gracefully."""
    filename = 'log_test.txt'
    threshold_size = 1024 * 1024  # 1MB
    with open(filename, 'w') as f:
        for _ in range(10):
            f.write("Log entry at " + str(datetime.datetime.now()) + "\n")
    
    main()
    
    assert not os.path.exists(filename)
    new_filename = f"log_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
    assert os.path.exists(new_filename)
    assert os.path.getsize(new_filename) < threshold_size
    
    with open(new_filename, 'w') as f:
        pass
    
    main()
    
    assert not os.path.exists(new_filename)
    new_new_filename = f"log_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
    assert os.path.exists(new_new_filename)
    assert os.path.getsize(new_new_filename) == 0
    
    os.remove(new_new_filename)

def test_main_with_rotated_log_file_and_existing_entries():
    """Test that the script handles a rotated log file and existing entries gracefully."""
    filename = 'log_test.txt'
    threshold_size = 1024 * 1024  # 1MB
    with open(filename, 'w') as f:
        for _ in range(10):
            f.write("Log entry at " + str(datetime.datetime.now()) + "\n")
    
    main()
    
    assert not os.path.exists(filename)
    new_filename = f"log_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
    assert os.path.exists(new_filename)
    assert os.path.getsize(new_filename) < threshold_size
    
    with open(new_filename, 'a') as f:
        for _ in range(10):
            f.write("Log entry at " + str(datetime.datetime.now()) + "\n")
    
    main()
    
    assert not os.path.exists(new_filename)
    new_new_filename = f"log_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
    assert os.path.exists(new_new_filename)
    assert os.path.getsize(new_new_filename) < threshold_size
    
    with open(new_new_filename, 'a') as f:
        for _ in range(10):
            f.write("Log entry at " + str(datetime.datetime.now()) + "\n")
    
    main()
    
    assert not os.path.exists(new_new_filename)
    new_new_new_filename = f"log_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
    assert os.path.exists(new_new_new_filename)
    assert os.path.getsize(new_new_new_filename) < threshold_size
    
    os.remove(new_new_new_filename)

def test_main_with_rotated_log_file_and_large_existing_entries():
    """Test that the script handles a rotated log file and large existing entries gracefully."""
    filename = 'log_test.txt'
    threshold_size = 1024 * 1024  # 1MB
    with open(filename, 'w') as f:
        for _ in range(10):
            f.write("Log entry at " + str(datetime.datetime.now()) + "\n")
    
    main()
    
    assert not os.path.exists(filename)
    new_filename = f"log_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
    assert os.path.exists(new_filename)
    assert os.path.getsize(new_filename) < threshold_size
    
    with open(new_filename, 'a') as f:
        for _ in range(1000):
            f.write("Log entry at " + str(datetime.datetime.now()) + "\n")
    
    main()
    
    assert not os.path.exists(new_filename)
    new_new_filename = f"log_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
    assert os.path.exists(new_new_filename)
    assert os.path.getsize(new_new_filename) < threshold_size
    
    with open(new_new_filename, 'a') as f:
        for _ in range(10):
            f.write("Log entry at " + str(datetime.datetime.now()) + "\n")
    
    main()
    
    assert not os.path.exists(new_new_filename)
    new_new_new_filename = f"log_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
    assert os.path.exists(new_new_new_filename)
    assert os.path.getsize(new_new_new_filename) < threshold_size
    
    with open(new_new_new_filename, 'a') as f:
        for _ in range(1000):
            f.write("Log entry at " + str(datetime.datetime.now()) + "\n")
    
    main()
    
    assert not os.path.exists(new_new_new_filename)
    new_new_new_new_filename = f"log_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
    assert os.path.exists(new_new_new_new_filename)
    assert os.path.getsize(new_new_new_new_filename) < threshold_size
    
    os.remove(new_new_new_new_filename)

def test_main_with_rotated_log_file_and_no_existing_entries():
    """Test that the script handles a rotated log file and no existing entries gracefully."""
    filename = 'log_test.txt'
    threshold_size = 1024 * 1024  # 1MB
    with open(filename, 'w') as f:
        for _ in range(10):
            f.write("Log entry at " + str(datetime.datetime.now()) + "\n")
    
    main()
    
    assert not os.path.exists(filename)
    new_filename = f"log_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
    assert os.path.exists(new_filename)
    assert os.path.getsize(new_filename) < threshold_size
    
    with open(new_filename, 'w') as f:
        pass
    
    main()
    
    assert not os.path.exists(new_filename)
    new_new_filename = f"log_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
    assert os.path.exists(new_new_filename)
    assert os.path.getsize(new_new_filename) == 0
    
    with open(new_new_filename, 'a') as f:
        for _ in range(10):
            f.write("Log entry at " + str(datetime.datetime.now()) + "\n")
    
    main()
    
    assert not os.path.exists(new_new_filename)
    new_new_new_filename = f"log_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
    assert os.path.exists(new_new_new_filename)
    assert os.path.getsize(new_new_new_filename) < threshold_size
    
    with open(new_new_new_filename, 'a') as f:
        for _ in range(10):
            f.write("Log entry at " + str(datetime.datetime.now()) + "\n")
    
    main()
    
    assert not os.path.exists(new_new_new_filename)
    new_new_new_new_filename = f"log_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
    assert os.path.exists(new_new_new_new_filename)
    assert os.path.getsize(new_new_new_new_filename) < threshold_size
    
    with open(new_new_new_new_filename, 'a') as f:
        for _ in range(10):
            f.write("Log entry at " + str(datetime.datetime.now()) + "\n")
    
    main()
    
    assert not os.path.exists(new_new_new_new_filename)
    new_new_new_new_new_filename = f"log_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
    assert os.path.exists(new_new_new_new_new_filename)
    assert os.path.getsize(new_new_new_new_new_filename) < threshold_size
    
    os.remove(new_new_new_new_new_filename)

def test_main_with_rotated_log_file_and_large_no_existing_entries():
    """Test that the script handles a rotated log file and large no existing entries gracefully."""
    filename = 'log_test.txt'
    threshold_size = 1024 * 1024  # 1MB
    with open(filename, 'w') as f:
        for _ in range(10):
            f.write("Log entry at " + str(datetime.datetime.now()) + "\n")
    
    main()
    
    assert not os.path.exists(filename)
    new_filename = f"log_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
    assert os.path.exists(new_filename)
    assert os.path.getsize(new_filename) < threshold_size
    
    with open(new_filename,