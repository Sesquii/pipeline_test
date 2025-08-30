import random
from string import ascii_letters, digits

# Hard-coded list of common names and places
COMMON_DATA = [
    "Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace",
    "Hannah", "Ivan", "Judy", "Kevin", "Lisa", "Max", "Nora", 
    "Oliver", "Penelope", "Quentin", "Rachel", "Steve", "Theresa",
    "Uma", "Victor", "Wendy", "Xander", "Yara", "Zoe",
    "New York", "London", "Paris", "Tokyo", "Sydney", "Berlin"
]

def generate_password(length=12):
    """Generate a password using common names and places."""
    # Randomly select elements from the COMMON_DATA list
    password = [random.choice(COMMON_DATA) for _ in range(3)]
    
    # Add random letters and digits to reach desired length
    password += [random.choice(ascii_letters + digits) for _ in range(length - 3)]
    
    # Shuffle to ensure randomness
    random.shuffle(password)
    
    # Join list into string and return
    return ''.join(password)

if __name__ == "__main__":
    print("Welcome to the Data-Driven Password Generator!")
    while True:
        try:
            length = int(input("Enter desired password length (default is 12): ") or 12)
            if length < 3:
                raise ValueError("Password length should be at least 3 characters.")
            break
        except ValueError as e:
            print(e)

    password = generate_password(length)
    print(f"Your generated password is: {password}")