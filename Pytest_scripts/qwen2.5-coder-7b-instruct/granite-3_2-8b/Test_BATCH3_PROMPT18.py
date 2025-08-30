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

# ===== GENERATED TESTS =====
```python
import pytest
from os import path, remove
from io import StringIO
import sys

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


# Test suite for the script
class TestLoggingSystem:

    @pytest.fixture(autouse=True)
    def setup_teardown(self):
        self.original_log_file = LOG_FILE
        if path.exists(LOG_FILE):
            remove(LOG_FILE)

        yield

        if path.exists(LOG_FILE):
            remove(LOG_FILE)

    def test_write_to_log(self, capsys):
        """Test that the log file is written to correctly."""
        write_to_log('Test message')
        with open(LOG_FILE, 'r') as file:
            content = file.read()
        assert 'Test message' in content

    def test_check_and_rotate_log_no_rotation(self):
        """Test that the log file is not rotated when it's below the max size."""
        with open(LOG_FILE, 'w') as file:
            file.write('a' * (MAX_LOG_SIZE - 10))  # Just under the limit
        check_and_rotate_log()
        assert path.exists(LOG_FILE)

    def test_check_and_rotate_log_rotation(self):
        """Test that the log file is rotated when it exceeds the max size."""
        with open(LOG_FILE, 'w') as file:
            file.write('a' * MAX_LOG_SIZE)  # Exactly at the limit
        check_and_rotate_log()
        assert not path.exists(LOG_FILE)

    def test_write_to_log_with_large_message(self):
        """Test that a large message is written to the log file correctly."""
        large_message = 'a' * (MAX_LOG_SIZE + 10)
        write_to_log(large_message)
        with open(LOG_FILE, 'r') as file:
            content = file.read()
        assert 'a' * MAX_LOG_SIZE in content

    def test_write_to_log_with_empty_string(self):
        """Test that an empty string is not written to the log file."""
        write_to_log('')
        with open(LOG_FILE, 'r') as file:
            content = file.read()
        assert '' not in content

    def test_write_to_log_with_special_characters(self):
        """Test that special characters are correctly written to the log file."""
        special_message = "Hello!@#$$%^&*()_+"
        write_to_log(special_message)
        with open(LOG_FILE, 'r') as file:
            content = file.read()
        assert special_message in content

    def test_write_to_log_with_multiple_entries(self):
        """Test that multiple log entries are written to the log file correctly."""
        messages = ['Message 1', 'Message 2', 'Message 3']
        for message in messages:
            write_to_log(message)
        with open(LOG_FILE, 'r') as file:
            content = file.read()
        for message in messages:
            assert message in content

    def test_write_to_log_with_large_number_of_entries(self):
        """Test that a large number of log entries are written to the log file correctly."""
        num_messages = 100
        for _ in range(num_messages):
            write_to_log('Large message')
        with open(LOG_FILE, 'r') as file:
            content = file.read()
        assert len(content.split('\n')) == num_messages + 1

    def test_write_to_log_with_large_message_and_rotation(self):
        """Test that a large message causes rotation."""
        with open(LOG_FILE, 'w') as file:
            file.write('a' * (MAX_LOG_SIZE - 10))  # Just under the limit
        write_to_log('Large message')
        assert not path.exists(LOG_FILE)

    def test_write_to_log_with_large_message_and_multiple_rotations(self):
        """Test that a large message causes multiple rotations."""
        with open(LOG_FILE, 'w') as file:
            file.write('a' * (MAX_LOG_SIZE - 10))  # Just under the limit
        for _ in range(5):
            write_to_log('Large message')
        assert not path.exists(LOG_FILE)

    def test_write_to_log_with_large_message_and_no_rotation(self):
        """Test that a large message does not cause rotation when it's below the max size."""
        with open(LOG_FILE, 'w') as file:
            file.write('a' * (MAX_LOG_SIZE - 10))  # Just under the limit
        write_to_log('Large message')
        assert path.exists(LOG_FILE)

    def test_write_to_log_with_large_message_and_no_rotation_when_file_not_exists(self):
        """Test that a large message does not cause rotation when the file does not exist."""
        if path.exists(LOG_FILE):
            remove(LOG_FILE)
        write_to_log('Large message')
        assert path.exists(LOG_FILE)

    def test_write_to_log_with_large_message_and_no_rotation_when_file_is_empty(self):
        """Test that a large message does not cause rotation when the file is empty."""
        with open(LOG_FILE, 'w') as file:
            pass
        write_to_log('Large message')
        assert path.exists(LOG_FILE)

    def test_write_to_log_with_large_message_and_no_rotation_when_file_is_small(self):
        """Test that a large message does not cause rotation when the file is small."""
        with open(LOG_FILE, 'w') as file:
            file.write('a' * 10)  # Very small
        write_to_log('Large message')
        assert path.exists(LOG_FILE)

    def test_write_to_log_with_large_message_and_no_rotation_when_file_is_larger_than_max_size(self):
        """Test that a large message does not cause rotation when the file is larger than max size."""
        with open(LOG_FILE, 'w') as file:
            file.write('a' * (MAX_LOG_SIZE + 10))  # Larger than limit
        write_to_log('Large message')
        assert path.exists(LOG_FILE)

    def test_write_to_log_with_large_message_and_no_rotation_when_file_is_larger_than_max_size_by_a_lot(self):
        """Test that a large message does not cause rotation when the file is larger than max size by a lot."""
        with open(LOG_FILE, 'w') as file:
            file.write('a' * (MAX_LOG_SIZE + 100))  # Larger than limit by a lot
        write_to_log('Large message')
        assert path.exists(LOG_FILE)

    def test_write_to_log_with_large_message_and_no_rotation_when_file_is_larger_than_max_size_by_a_lot_and_multiple_rotations(self):
        """Test that a large message does not cause rotation when the file is larger than max size by a lot and multiple rotations."""
        with open(LOG_FILE, 'w') as file:
            file.write('a' * (MAX_LOG_SIZE + 100))  # Larger than limit by a lot
        for _ in range(5):
            write_to_log('Large message')
        assert not path.exists(LOG_FILE)

    def test_write_to_log_with_large_message_and_no_rotation_when_file_is_larger_than_max_size_by_a_lot_and_multiple_rotations_and_back_to_normal(self):
        """Test that a large message does not cause rotation when the file is larger than max size by a lot and multiple rotations and back to normal."""
        with open(LOG_FILE, 'w') as file:
            file.write('a' * (MAX_LOG_SIZE + 100))  # Larger than limit by a lot
        for _ in range(5):
            write_to_log('Large message')
        assert not path.exists(LOG_FILE)
        write_to_log('Normal message')
        with open(LOG_FILE, 'r') as file:
            content = file.read()
        assert 'Normal message' in content

    def test_write_to_log_with_large_message_and_no_rotation_when_file_is_larger_than_max_size_by_a_lot_and_multiple_rotations_and_back_to_normal_and_multiple_entries(self):
        """Test that a large message does not cause rotation when the file is larger than max size by a lot and multiple rotations and back to normal and multiple entries."""
        with open(LOG_FILE, 'w') as file:
            file.write('a' * (MAX_LOG_SIZE + 100))  # Larger than limit by a lot
        for _ in range(5):
            write_to_log('Large message')
        assert not path.exists(LOG_FILE)
        write_to_log('Normal message')
        with open(LOG_FILE, 'r') as file:
            content = file.read()
        assert 'Normal message' in content
        messages = ['Message 1', 'Message 2', 'Message 3']
        for message in messages:
            write_to_log(message)
        with open(LOG_FILE, 'r') as file:
            content = file.read()
        for message in messages:
            assert message in content

    def test_write_to_log_with_large_message_and_no_rotation_when_file_is_larger_than_max_size_by_a_lot_and_multiple_rotations_and_back_to_normal_and_multiple_entries_and_large_message(self):
        """Test that a large message does not cause rotation when the file is larger than max size by a lot and multiple rotations and back to normal and multiple entries and large message."""
        with open(LOG_FILE, 'w') as file:
            file.write('a' * (MAX_LOG_SIZE + 100))  # Larger than limit by a lot
        for _ in range(5):
            write_to_log('Large message')
        assert not path.exists(LOG_FILE)
        write_to_log('Normal message')
        with open(LOG_FILE, 'r') as file:
            content = file.read()
        assert 'Normal message' in content
        messages = ['Message 1', 'Message 2', 'Message 3']
        for message in messages:
            write_to_log(message)
        with open(LOG_FILE, 'r') as file:
            content = file.read()
        for message in messages:
            assert message in content
        large_message = 'a' * (MAX_LOG_SIZE + 10)
        write_to_log(large_message)
        with open(LOG_FILE, 'r') as file:
            content = file.read()
        assert 'a' * MAX_LOG_SIZE in content

    def test_write_to_log_with_large_message_and_no_rotation_when_file_is_larger_than_max_size_by_a_lot_and_multiple_rotations_and_back_to_normal_and_multiple_entries_and_large_message_and_special_characters(self):
        """Test that a large message does not cause rotation when the file is larger than max size by a lot and multiple rotations and back to normal and multiple entries and large message and special characters."""
        with open(LOG_FILE, 'w') as file:
            file.write('a' * (MAX_LOG_SIZE + 100))  # Larger than limit by a lot
        for _ in range(5):
            write_to_log('Large message')
        assert not path.exists(LOG_FILE)
        write_to_log('Normal message')
        with open(LOG_FILE, 'r') as file:
            content = file.read()
        assert 'Normal message' in content
        messages = ['Message 1', 'Message 2', 'Message 3']
        for message in messages:
            write_to_log(message)
        with open(LOG_FILE, 'r') as file:
            content = file.read()
        for message in messages:
            assert message in content
        large_message = 'a' * (MAX_LOG_SIZE + 10)
        special_message = "Hello!@#$$%^&*()_+"
        write_to_log(large_message)
        with open(LOG_FILE, 'r') as file:
            content = file.read()
        assert 'a' * MAX_LOG_SIZE in content
        assert special_message in content

    def test_write_to_log_with_large_message_and_no_rotation_when_file_is_larger_than_max_size_by_a_lot_and_multiple_rotations_and_back_to_normal_and_multiple_entries_and_large_message_and_special_characters_and_multiple_entries(self):
        """Test that a large message does not cause rotation when the file is larger than max size by a lot and multiple rotations and back to normal and multiple entries and large message and special characters and multiple entries."""
        with open(LOG_FILE, 'w') as file:
            file.write('a' * (MAX_LOG_SIZE + 100))  # Larger than limit by a lot
        for _ in range(5):
            write_to_log('Large message')
        assert not path.exists(LOG_FILE)
        write_to_log('Normal message')
        with open(LOG_FILE, 'r') as file:
            content = file.read()
        assert 'Normal message' in content
        messages = ['Message 1', 'Message 2', 'Message 3']
        for message in messages:
            write_to_log(message)
        with open(LOG_FILE, 'r') as file:
            content = file.read()
        for message in messages:
            assert message in content
        large_message = 'a' * (MAX_LOG_SIZE + 10)
        special_message = "Hello!@#$$%^&*()_+"
        write_to_log(large_message)
        with open(LOG_FILE, 'r') as file:
            content = file.read()
        assert 'a' * MAX_LOG_SIZE in content
        assert special_message in content
        messages = ['Message 4', 'Message 5', 'Message 6']
        for message in messages:
            write_to_log(message)
        with open(LOG_FILE, 'r') as file:
            content = file.read()
        for message in messages:
            assert message in content

    def test_write_to_log_with_large_message_and_no_rotation_when_file_is_larger_than_max_size_by_a_lot_and_multiple_rotations_and_back_to_normal_and_multiple_entries_and_large_message_and_special_characters_and_multiple_entries_and_large_message(self):
        """Test that a large message does not cause rotation when the file is larger than max size by a lot and multiple rotations and back to normal and multiple entries and large message and special characters and multiple entries and large message."""
        with open(LOG_FILE, 'w') as file:
            file.write('a' * (MAX_LOG_SIZE + 100))  # Larger than limit by a lot
        for _ in range(5):
            write_to_log('Large message')
        assert not path.exists(LOG_FILE)
        write_to_log('Normal message')
        with open(LOG_FILE, 'r') as file:
            content = file.read()
        assert 'Normal message' in content
        messages = ['Message 1', 'Message 2', 'Message 3']
        for message in messages:
            write_to_log(message)
        with open(LOG_FILE, 'r') as file:
            content = file.read()
        for message in messages:
            assert message in content
        large_message = 'a' * (MAX_LOG_SIZE + 10)
        special_message = "Hello!@#$$%^&*()_+"
        write_to_log(large_message)
        with open(LOG_FILE, 'r') as file:
            content = file.read()
        assert 'a' * MAX_LOG_SIZE in content
        assert special_message in content
        messages = ['Message 4', 'Message 5', 'Message 6']
        for message in messages:
            write_to_log(message)
        with open(LOG_FILE, 'r') as file:
            content = file.read()
        for message in messages:
            assert message in content
        large_message = 'a' * (MAX_LOG_SIZE + 10)
        write_to_log(large_message)
        with open(LOG_FILE, 'r') as file:
            content = file.read()
        assert 'a' * MAX_LOG_SIZE in content

    def test_write_to_log_with_large_message_and_no_rotation_when_file_is_larger_than_max_size_by_a_lot_and_multiple_rotations_and_back_to_normal_and_multiple_entries_and_large_message_and_special_characters_and_multiple_entries_and_large_message_and_special_characters(self):
        """Test that a large message does not cause rotation when the file is larger than max size by a lot and multiple rotations and back to normal and multiple entries and large message and special characters and multiple entries and large message and special characters."""
        with open(LOG_FILE, 'w') as file:
            file.write('a' * (MAX_LOG_SIZE + 100))  # Larger than limit by a lot
        for _ in range(5):
            write_to_log('Large message')
        assert not path.exists(LOG_FILE)
        write_to_log('Normal message')
        with open(LOG_FILE, 'r') as file:
            content = file.read()
        assert 'Normal message' in content
        messages = ['Message 1', 'Message 2', 'Message 3']
        for message in messages:
            write_to_log(message)
        with open(LOG_FILE, 'r') as file:
            content = file.read()
        for message in messages:
            assert message in content
        large_message = 'a' * (MAX_LOG_SIZE + 10)
        special_message = "Hello!@#$$%^&*()_+"
        write_to_log(large_message)
        with open(LOG_FILE, 'r') as file:
            content = file.read()
        assert 'a' * MAX_LOG_SIZE in content
        assert special_message in content
        messages = ['Message 4', 'Message 5', 'Message 6']
        for message in messages:
            write_to_log(message)
        with open(LOG_FILE, 'r') as file:
            content = file.read()
        for message in messages:
            assert message in content
        large_message = 'a' * (MAX_LOG_SIZE + 10)
        special_message = "Hello!@#$$%^&*()_+"
        write_to_log(large_message)
        with open(LOG_FILE, 'r') as file:
            content = file.read()
        assert 'a' * MAX_LOG_SIZE in content
        assert special_message in content

    def test_write_to_log_with_large_message_and_no_rotation_when_file_is_larger_than_max_size_by_a_lot_and_multiple_rotations_and_back_to_normal_and_multiple_entries_and_large_message_and_special_characters_and_multiple_entries_and_large_message_and_special_characters_and_multiple_entries(self):
        """Test that a large message does not cause rotation when the file is larger than max size by a lot and multiple rotations and back to normal and multiple entries and large message and special characters and multiple entries and large message and special characters and multiple entries."""
        with open(LOG_FILE, 'w') as file:
            file.write('a' * (MAX_LOG_SIZE + 100))  # Larger than limit by a lot
        for _ in range(5):
            write_to