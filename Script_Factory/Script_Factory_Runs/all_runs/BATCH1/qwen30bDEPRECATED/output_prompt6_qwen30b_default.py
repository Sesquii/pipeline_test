import random
import string


def randomized_password_crippler(password):
    """
    Strengthen and then weaken a password according to specified rules.

    Args:
        password (str): The input plaintext password.

    Returns:
        str: The final weakened password.
    """
    # Step 1: Ensure the password is at least 12 characters long
    min_length = 12
    if len(password) < min_length:
        # Pad with random characters from all character sets
        padding_needed = min_length - len(password)
        all_chars = string.ascii_letters + string.digits + "!@#$%^&*()-_=+[]{};:,.<>?"
        password += ''.join(random.choices(all_chars, k=padding_needed))

    # Step 2: Ensure at least one character from each required category
    required_chars = {
        'uppercase': string.ascii_uppercase,
        'lowercase': string.ascii_lowercase,
        'digit': string.digits,
        'special': "!@#$%^&*()-_=+[]{};:,.<>?"
    }

    # Check if we already have at least one character from each category
    has_upper = any(c in required_chars['uppercase'] for c in password)
    has_lower = any(c in required_chars['lowercase'] for c in password)
    has_digit = any(c in required_chars['digit'] for c in password)
    has_special = any(c in required_chars['special'] for c in password)

    # If not, add one character from each missing category
    if not has_upper:
        password += random.choice(required_chars['uppercase'])
    if not has_lower:
        password += random.choice(required_chars['lowercase'])
    if not has_digit:
        password += random.choice(required_chars['digit'])
    if not has_special:
        password += random.choice(required_chars['special'])

    # Step 3: Shuffle the password string
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    # Step 4: Deliberately weaken the password by removing characters
    # Default number of characters to remove
    chars_to_remove = 2

    # Convert password to list for easier manipulation
    password_chars = list(password)

    # Identify positions of characters from each required category
    categories = {
        'uppercase': [i for i, c in enumerate(password_chars) if c in string.ascii_uppercase],
        'lowercase': [i for i, c in enumerate(password_chars) if c in string.ascii_lowercase],
        'digit': [i for i, c in enumerate(password_chars) if c in string.digits],
        'special': [i for i, c in enumerate(password_chars) if c in "!@#$%^&*()-_=+[]{};:,.<>?"]
    }

    # Ensure we can remove characters while preserving at least one from each category
    removable_positions = list(range(len(password_chars)))
    for cat_positions in categories.values():
        if cat_positions:
            # Remove one position from each category to ensure we keep at least one
            removable_positions.remove(cat_positions[0])

    # If we still have enough positions to remove, do so
    if len(removable_positions) >= chars_to_remove:
        # Select random positions to remove
        positions_to_remove = random.sample(removable_positions, chars_to_remove)
        # Remove characters at those positions (in reverse order to maintain indices)
        for pos in sorted(positions_to_remove, reverse=True):
            password_chars.pop(pos)
    else:
        # If not enough removable positions, just remove the specified number of random positions
        positions_to_remove = random.sample(range(len(password_chars)), chars_to_remove)
        for pos in sorted(positions_to_remove, reverse=True):
            password_chars.pop(pos)

    # Return final weakened password
    return ''.join(password_chars)


if __name__ == "__main__":
    # Get user input
    user_password = input("Enter a plaintext password: ")

    # Process the password
    result = randomized_password_crippler(user_password)

    # Output the result
    print(f"Final weakened password: {result}")
