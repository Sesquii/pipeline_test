import hashlib
import time

def generate_time_based_password(secret_key):
    """
    Generate a time-based password using the current timestamp and a secret key.

    Args:
        secret_key (str): A secret key to add security to the password generation process.

    Returns:
        str: The generated time-based password.
    """
    # Get the current timestamp in seconds since epoch
    current_timestamp = int(time.time())

    # Create a hash using the secret key and current timestamp
    hash_object = hashlib.sha256((secret_key + str(current_timestamp)).encode())
    password_hash = hash_object.hexdigest()

    # Return the first 8 characters of the hash as the password (can be adjusted)
    return password_hash[:8]

if __name__ == "__main__":
    # Define a secret key for the password generation
    SECRET_KEY = "my_secret_key"

    while True:
        # Generate and print the time-based password
        password = generate_time_based_password(SECRET_KEY)
        print(f"Current Time-Based Password: {password}")

        # Wait for 60 seconds before generating the next password
        time.sleep(60)

# ===== GENERATED TESTS =====
```python
import hashlib
import time
from typing import Any

def generate_time_based_password(secret_key: str) -> str:
    """
    Generate a time-based password using the current timestamp and a secret key.

    Args:
        secret_key (str): A secret key to add security to the password generation process.

    Returns:
        str: The generated time-based password.
    """
    # Get the current timestamp in seconds since epoch
    current_timestamp = int(time.time())

    # Create a hash using the secret key and current timestamp
    hash_object = hashlib.sha256((secret_key + str(current_timestamp)).encode())
    password_hash = hash_object.hexdigest()

    # Return the first 8 characters of the hash as the password (can be adjusted)
    return password_hash[:8]

# Test cases for generate_time_based_password function

def test_generate_time_based_password_with_valid_secret_key():
    """Test generate_time_based_password with a valid secret key."""
    secret_key = "my_secret_key"
    password = generate_time_based_password(secret_key)
    assert isinstance(password, str)
    assert len(password) == 8
    # Ensure the password changes over time
    time.sleep(1)
    new_password = generate_time_based_password(secret_key)
    assert password != new_password

def test_generate_time_based_password_with_empty_secret_key():
    """Test generate_time_based_password with an empty secret key."""
    secret_key = ""
    password = generate_time_based_password(secret_key)
    assert isinstance(password, str)
    assert len(password) == 8
    # Ensure the password changes over time
    time.sleep(1)
    new_password = generate_time_based_password(secret_key)
    assert password != new_password

def test_generate_time_based_password_with_long_secret_key():
    """Test generate_time_based_password with a long secret key."""
    secret_key = "a" * 1024
    password = generate_time_based_password(secret_key)
    assert isinstance(password, str)
    assert len(password) == 8
    # Ensure the password changes over time
    time.sleep(1)
    new_password = generate_time_based_password(secret_key)
    assert password != new_password

def test_generate_time_based_password_with_special_characters_secret_key():
    """Test generate_time_based_password with a secret key containing special characters."""
    secret_key = "my-secret@key"
    password = generate_time_based_password(secret_key)
    assert isinstance(password, str)
    assert len(password) == 8
    # Ensure the password changes over time
    time.sleep(1)
    new_password = generate_time_based_password(secret_key)
    assert password != new_password

def test_generate_time_based_password_with_numeric_secret_key():
    """Test generate_time_based_password with a numeric secret key."""
    secret_key = "1234567890"
    password = generate_time_based_password(secret_key)
    assert isinstance(password, str)
    assert len(password) == 8
    # Ensure the password changes over time
    time.sleep(1)
    new_password = generate_time_based_password(secret_key)
    assert password != new_password

def test_generate_time_based_password_with_unicode_secret_key():
    """Test generate_time_based_password with a unicode secret key."""
    secret_key = "你好世界"
    password = generate_time_based_password(secret_key)
    assert isinstance(password, str)
    assert len(password) == 8
    # Ensure the password changes over time
    time.sleep(1)
    new_password = generate_time_based_password(secret_key)
    assert password != new_password

# Test cases for the entire script

def test_script_output():
    """Test the output of the script."""
    secret_key = "my_secret_key"
    original_password = generate_time_based_password(secret_key)
    time.sleep(1)
    new_password = generate_time_based_password(secret_key)
    assert original_password != new_password
```