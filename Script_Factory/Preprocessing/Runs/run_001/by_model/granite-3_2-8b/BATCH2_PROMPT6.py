import random
from getpass import getuser  # For getting the current username

# Hardcoded list of common names and places
COMMON_NAMES = [
    "alice", "bob", "charlie", "david", "emma", "fred", "grace", "helen", "ian", "jane"
]
COMMON_PLACES = ["newyork", "london", "tokyo", "paris", "sydney", "berlin"]


def generate_password(length=12):
    """Generate a password based on common names and places."""
    # Combine lists for easier random selection
    combined = COMMON_NAMES + COMMON_PLACES
    
    if length < 4:
        raise ValueError("Password length should be at least 4 to ensure complexity.")
    
    # Ensure the password contains at least one character from each category
    while True:
        password = [
            random.choice(combined),  # At least one name/place
            random.choice('0123456789'),  # One digit
            random.choice('!@#$%^&*()'),  # One special character
            ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=length-4))  # Remaining letters
        ]
        
        random.shuffle(password)
        password = ''.join(password)
        
        if any(char in password for char in COMMON_NAMES + COMMON_PLACES):
            return password


def main():
    """Entry point of the program."""
    username = getuser()  # Use current username as a seed
    
    print(f"Welcome, {username}!")
    password = generate_password(12)  # Generate a 12-character password
    print(f"Your generated password is: {password}")


if __name__ == "__main__":
    main()