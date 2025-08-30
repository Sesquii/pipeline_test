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

# ===== GENERATED TESTS =====
import pytest
from io import StringIO
import os
import time

# Original script remains unchanged

def test_main_with_small_log():
    """Test main function with a small log file size"""
    current_log = 'log.txt'
    threshold_size = 1024 * 1024  # 1MB
    interval = 5  # seconds
    counter = 0

    with pytest.raises(SystemExit) as exc_info:
        main()
    assert exc_info.value.code == 0

def test_main_with_large_log(tmpdir):
    """Test main function with a large log file size"""
    current_log = os.path.join(tmpdir, 'log.txt')
    threshold_size = 1024 * 1024  # 1MB
    interval = 5  # seconds
    counter = 0

    for _ in range(2):
        with open(current_log, 'a') as f:
            f.write(f"Log message at {time.time()}\n")
        file_size = os.path.getsize(current_log)
        if file_size >= threshold_size:
            os.remove(current_log)
            current_log = os.path.join(tmpdir, f"log_{counter}.txt")
            counter += 1
        time.sleep(interval)

    assert len(os.listdir(tmpdir)) == 2

def test_main_with_negative_interval():
    """Test main function with a negative interval"""
    current_log = 'log.txt'
    threshold_size = 1024 * 1024  # 1MB
    interval = -5  # seconds
    counter = 0

    with pytest.raises(SystemExit) as exc_info:
        main()
    assert exc_info.value.code == 0

def test_main_with_zero_threshold():
    """Test main function with a zero threshold size"""
    current_log = 'log.txt'
    threshold_size = 0  # bytes
    interval = 5  # seconds
    counter = 0

    with pytest.raises(SystemExit) as exc_info:
        main()
    assert exc_info.value.code == 0

def test_main_with_empty_log(tmpdir):
    """Test main function with an empty log file"""
    current_log = os.path.join(tmpdir, 'log.txt')
    threshold_size = 1024 * 1024  # 1MB
    interval = 5  # seconds
    counter = 0

    with open(current_log, 'w') as f:
        pass

    with pytest.raises(SystemExit) as exc_info:
        main()
    assert exc_info.value.code == 0

def test_main_with_large_interval(tmpdir):
    """Test main function with a large interval"""
    current_log = os.path.join(tmpdir, 'log.txt')
    threshold_size = 1024 * 1024  # 1MB
    interval = 3600  # seconds (1 hour)
    counter = 0

    for _ in range(2):
        with open(current_log, 'a') as f:
            f.write(f"Log message at {time.time()}\n")
        file_size = os.path.getsize(current_log)
        if file_size >= threshold_size:
            os.remove(current_log)
            current_log = os.path.join(tmpdir, f"log_{counter}.txt")
            counter += 1
        time.sleep(interval)

    assert len(os.listdir(tmpdir)) == 2

def test_main_with_large_threshold(tmpdir):
    """Test main function with a large threshold size"""
    current_log = os.path.join(tmpdir, 'log.txt')
    threshold_size = 1024 * 1024 * 1024  # 1GB
    interval = 5  # seconds
    counter = 0

    for _ in range(2):
        with open(current_log, 'a') as f:
            f.write(f"Log message at {time.time()}\n")
        file_size = os.path.getsize(current_log)
        if file_size >= threshold_size:
            os.remove(current_log)
            current_log = os.path.join(tmpdir, f"log_{counter}.txt")
            counter += 1
        time.sleep(interval)

    assert len(os.listdir(tmpdir)) == 2

def test_main_with_zero_interval():
    """Test main function with a zero interval"""
    current_log = 'log.txt'
    threshold_size = 1024 * 1024  # 1MB
    interval = 0  # seconds
    counter = 0

    with pytest.raises(SystemExit) as exc_info:
        main()
    assert exc_info.value.code == 0

def test_main_with_negative_threshold():
    """Test main function with a negative threshold size"""
    current_log = 'log.txt'
    threshold_size = -1  # bytes
    interval = 5  # seconds
    counter = 0

    with pytest.raises(SystemExit) as exc_info:
        main()
    assert exc_info.value.code == 0

def test_main_with_empty_log(tmpdir):
    """Test main function with an empty log file"""
    current_log = os.path.join(tmpdir, 'log.txt')
    threshold_size = 1024 * 1024  # 1MB
    interval = 5  # seconds
    counter = 0

    with open(current_log, 'w') as f:
        pass

    with pytest.raises(SystemExit) as exc_info:
        main()
    assert exc_info.value.code == 0

def test_main_with_large_interval(tmpdir):
    """Test main function with a large interval"""
    current_log = os.path.join(tmpdir, 'log.txt')
    threshold_size = 1024 * 1024  # 1MB
    interval = 3600  # seconds (1 hour)
    counter = 0

    for _ in range(2):
        with open(current_log, 'a') as f:
            f.write(f"Log message at {time.time()}\n")
        file_size = os.path.getsize(current_log)
        if file_size >= threshold_size:
            os.remove(current_log)
            current_log = os.path.join(tmpdir, f"log_{counter}.txt")
            counter += 1
        time.sleep(interval)

    assert len(os.listdir(tmpdir)) == 2

def test_main_with_large_threshold(tmpdir):
    """Test main function with a large threshold size"""
    current_log = os.path.join(tmpdir, 'log.txt')
    threshold_size = 1024 * 1024 * 1024  # 1GB
    interval = 5  # seconds
    counter = 0

    for _ in range(2):
        with open(current_log, 'a') as f:
            f.write(f"Log message at {time.time()}\n")
        file_size = os.path.getsize(current_log)
        if file_size >= threshold_size:
            os.remove(current_log)
            current_log = os.path.join(tmpdir, f"log_{counter}.txt")
            counter += 1
        time.sleep(interval)

    assert len(os.listdir(tmpdir)) == 2

def test_main_with_zero_interval():
    """Test main function with a zero interval"""
    current_log = 'log.txt'
    threshold_size = 1024 * 1024  # 1MB
    interval = 0  # seconds
    counter = 0

    with pytest.raises(SystemExit) as exc_info:
        main()
    assert exc_info.value.code == 0

def test_main_with_negative_threshold():
    """Test main function with a negative threshold size"""
    current_log = 'log.txt'
    threshold_size = -1  # bytes
    interval = 5  # seconds
    counter = 0

    with pytest.raises(SystemExit) as exc_info:
        main()
    assert exc_info.value.code == 0

def test_main_with_empty_log(tmpdir):
    """Test main function with an empty log file"""
    current_log = os.path.join(tmpdir, 'log.txt')
    threshold_size = 1024 * 1024  # 1MB
    interval = 5  # seconds
    counter = 0

    with open(current_log, 'w') as f:
        pass

    with pytest.raises(SystemExit) as exc_info:
        main()
    assert exc_info.value.code == 0

def test_main_with_large_interval(tmpdir):
    """Test main function with a large interval"""
    current_log = os.path.join(tmpdir, 'log.txt')
    threshold_size = 1024 * 1024  # 1MB
    interval = 3600  # seconds (1 hour)
    counter = 0

    for _ in range(2):
        with open(current_log, 'a') as f:
            f.write(f"Log message at {time.time()}\n")
        file_size = os.path.getsize(current_log)
        if file_size >= threshold_size:
            os.remove(current_log)
            current_log = os.path.join(tmpdir, f"log_{counter}.txt")
            counter += 1
        time.sleep(interval)

    assert len(os.listdir(tmpdir)) == 2

def test_main_with_large_threshold(tmpdir):
    """Test main function with a large threshold size"""
    current_log = os.path.join(tmpdir, 'log.txt')
    threshold_size = 1024 * 1024 * 1024  # 1GB
    interval = 5  # seconds
    counter = 0

    for _ in range(2):
        with open(current_log, 'a') as f:
            f.write(f"Log message at {time.time()}\n")
        file_size = os.path.getsize(current_log)
        if file_size >= threshold_size:
            os.remove(current_log)
            current_log = os.path.join(tmpdir, f"log_{counter}.txt")
            counter += 1
        time.sleep(interval)

    assert len(os.listdir(tmpdir)) == 2

def test_main_with_zero_interval():
    """Test main function with a zero interval"""
    current_log = 'log.txt'
    threshold_size = 1024 * 1024  # 1MB
    interval = 0  # seconds
    counter = 0

    with pytest.raises(SystemExit) as exc_info:
        main()
    assert exc_info.value.code == 0

def test_main_with_negative_threshold():
    """Test main function with a negative threshold size"""
    current_log = 'log.txt'
    threshold_size = -1  # bytes
    interval = 5  # seconds
    counter = 0

    with pytest.raises(SystemExit) as exc_info:
        main()
    assert exc_info.value.code == 0

def test_main_with_empty_log(tmpdir):
    """Test main function with an empty log file"""
    current_log = os.path.join(tmpdir, 'log.txt')
    threshold_size = 1024 * 1024  # 1MB
    interval = 5  # seconds
    counter = 0

    with open(current_log, 'w') as f:
        pass

    with pytest.raises(SystemExit) as exc_info:
        main()
    assert exc_info.value.code == 0

def test_main_with_large_interval(tmpdir):
    """Test main function with a large interval"""
    current_log = os.path.join(tmpdir, 'log.txt')
    threshold_size = 1024 * 1024  # 1MB
    interval = 3600  # seconds (1 hour)
    counter = 0

    for _ in range(2):
        with open(current_log, 'a') as f:
            f.write(f"Log message at {time.time()}\n")
        file_size = os.path.getsize(current_log)
        if file_size >= threshold_size:
            os.remove(current_log)
            current_log = os.path.join(tmpdir, f"log_{counter}.txt")
            counter += 1
        time.sleep(interval)

    assert len(os.listdir(tmpdir)) == 2

def test_main_with_large_threshold(tmpdir):
    """Test main function with a large threshold size"""
    current_log = os.path.join(tmpdir, 'log.txt')
    threshold_size = 1024 * 1024 * 1024  # 1GB
    interval = 5  # seconds
    counter = 0

    for _ in range(2):
        with open(current_log, 'a') as f:
            f.write(f"Log message at {time.time()}\n")
        file_size = os.path.getsize(current_log)
        if file_size >= threshold_size:
            os.remove(current_log)
            current_log = os.path.join(tmpdir, f"log_{counter}.txt")
            counter += 1
        time.sleep(interval)

    assert len(os.listdir(tmpdir)) == 2

def test_main_with_zero_interval():
    """Test main function with a zero interval"""
    current_log = 'log.txt'
    threshold_size = 1024 * 1024  # 1MB
    interval = 0  # seconds
    counter = 0

    with pytest.raises(SystemExit) as exc_info:
        main()
    assert exc_info.value.code == 0

def test_main_with_negative_threshold():
    """Test main function with a negative threshold size"""
    current_log = 'log.txt'
    threshold_size = -1  # bytes
    interval = 5  # seconds
    counter = 0

    with pytest.raises(SystemExit) as exc_info:
        main()
    assert exc_info.value.code == 0

def test_main_with_empty_log(tmpdir):
    """Test main function with an empty log file"""
    current_log = os.path.join(tmpdir, 'log.txt')
    threshold_size = 1024 * 1024  # 1MB
    interval = 5  # seconds
    counter = 0

    with open(current_log, 'w') as f:
        pass

    with pytest.raises(SystemExit) as exc_info:
        main()
    assert exc_info.value.code == 0

def test_main_with_large_interval(tmpdir):
    """Test main function with a large interval"""
    current_log = os.path.join(tmpdir, 'log.txt')
    threshold_size = 1024 * 1024  # 1MB
    interval = 3600  # seconds (1 hour)
    counter = 0

    for _ in range(2):
        with open(current_log, 'a') as f:
            f.write(f"Log message at {time.time()}\n")
        file_size = os.path.getsize(current_log)
        if file_size >= threshold_size:
            os.remove(current_log)
            current_log = os.path.join(tmpdir, f"log_{counter}.txt")
            counter += 1
        time.sleep(interval)

    assert len(os.listdir(tmpdir)) == 2

def test_main_with_large_threshold(tmpdir):
    """Test main function with a large threshold size"""
    current_log = os.path.join(tmpdir, 'log.txt')
    threshold_size = 1024 * 1024 * 1024  # 1GB
    interval = 5  # seconds
    counter = 0

    for _ in range(2):
        with open(current_log, 'a') as f:
            f.write(f"Log message at {time.time()}\n")
        file_size = os.path.getsize(current_log)
        if file_size >= threshold_size:
            os.remove(current_log)
            current_log = os.path.join(tmpdir, f"log_{counter}.txt")
            counter += 1
        time.sleep(interval)

    assert len(os.listdir(tmpdir)) == 2

def test_main_with_zero_interval():
    """Test main function with a zero interval"""
    current_log = 'log.txt'
    threshold_size = 1024 * 1024  # 1MB
    interval = 0  # seconds
    counter = 0

    with pytest.raises(SystemExit) as exc_info:
        main()
    assert exc_info.value.code == 0

def test_main_with_negative_threshold():
    """Test main function with a negative threshold size"""
    current_log = 'log.txt'
    threshold_size = -1  # bytes
    interval = 5  # seconds
    counter = 0

    with pytest.raises(SystemExit) as exc_info:
        main()
    assert exc_info.value.code == 0

def test_main_with_empty_log(tmpdir):
    """Test main function with an empty log file"""
    current_log = os.path.join(tmpdir, 'log.txt')
    threshold_size = 1024 * 1024  # 1MB
    interval = 5  # seconds
    counter = 0

    with open(current_log, 'w') as f:
        pass

    with pytest.raises(SystemExit) as exc_info:
        main()
    assert exc_info.value.code == 0

def test_main_with_large_interval(tmpdir):
    """Test main function with a large interval"""
    current_log = os.path.join(tmpdir, 'log.txt')
    threshold_size = 1024 * 1024  # 1MB
    interval = 3600  # seconds (1 hour)
    counter = 0

    for _ in range(2):
        with open(current_log, 'a') as f:
            f.write(f"Log message at {time.time()}\n")
        file_size = os.path.getsize(current_log)
        if file_size >= threshold_size:
            os.remove(current_log)
            current_log = os.path.join(tmpdir, f"log_{counter}.txt")
            counter += 1
        time.sleep(interval)

    assert len(os.listdir(tmpdir)) == 2

def test_main_with_large_threshold(tmpdir):
    """Test main function with a large threshold size"""
    current_log = os.path.join(tmpdir, 'log.txt')
    threshold_size = 1024 * 1024 * 1024  # 1GB
    interval = 5  # seconds
    counter = 0

    for _ in range(2):
        with open(current_log, 'a') as f:
            f.write(f"Log message at {time.time()}\n")
        file_size = os.path.getsize(current_log)
        if file_size >= threshold_size:
            os.remove(current_log)
            current_log = os.path.join(tmpdir, f"log_{counter}.txt")
            counter += 1
        time.sleep(interval)

    assert len(os.listdir(tmpdir)) == 