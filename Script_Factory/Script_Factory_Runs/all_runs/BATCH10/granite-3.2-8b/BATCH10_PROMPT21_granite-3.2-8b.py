import time
from datetime import datetime
import os
import getpass

def generate_password(length=12):
    """Generate a random password of specified length."""
    all_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+"
    return ''.join(random.choice(all_characters) for _ in range(length))

def save_password_to_file(password):
    """Save password to a secure file."""
    if not os.path.exists("passwords"):
        os.makedirs("passwords")
    timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
    filename = f"passwords/password_{timestamp}.txt"
    with open(filename, 'w') as f:
        f.write(password)

def load_latest_password():
    """Load the latest password from file."""
    if not os.path.exists("passwords"):
        return None

    latest_file = max([f for f in os.listdir('passwords') if f.startswith('password_')], key=lambda x: os.path.getctime(os.path.join('passwords', x)))
    return open(os.path.join('passwords', latest_file), 'r').read().strip()

if __name__ == "__main__":
    last_password = load_latest_password()

    while True:
        current_password = generate_password()

        if last_password != current_password:
            print(f"New password generated: {current_password}")
            save_password_to_file(current_password)
            last_password = current_password

        time.sleep(60)  # Wait for a minute