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