import random
import string

def randomize_password(password, remove_chars=2):
    """
    Strengthens a password by ensuring it meets certain criteria and then deliberately weakens it.

    Args:
        password (str): The initial plaintext password.
        remove_chars (int, optional): Number of characters to randomly remove from the strengthened password. Defaults to 2.

    Returns:
        str: The final weakened password.
    """

    # Ensure password is at least 12 characters long
    if len(password) < 12:
        password += ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=12 - len(password)))

    # Check and add required character types if missing
    while not (any(c.islower() for c in password) and any(c.isupper() for c in password) and
               any(c.isdigit() for c in password) and any(c in string.punctuation for c in password)):
        password += random.choice(string.ascii_letters + string.digits + string.punctuation)

    # Randomly shuffle the strengthened password
    password = ''.join(random.sample(password, len(password)))

    # Deliberately weaken the password by removing characters
    for _ in range(remove_chars):
        # Try to remove a character without losing a required category
        if any(c.islower() for c in password) and any(c.isupper() for c in password) and \
           any(c.isdigit() for c in password) and any(c in string.punctuation for c in password):
            remove_pos = random.randint(0, len(password) - 1)
            password = password[:remove_pos] + password[remove_pos+1:]
        else:
            # If can't remove without losing a required category, just pick a random char and hope for the best
            remove_pos = random.randint(0, len(password) - 1)

    return password

if __name__ == "__main__":
    # Demonstrate usage
    original_password = input("Enter your initial password: ")
    final_password = randomize_password(original_password)
    print(f"Weakened Password: {final_password}")