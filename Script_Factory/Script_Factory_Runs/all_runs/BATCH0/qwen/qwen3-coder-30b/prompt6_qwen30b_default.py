import random
import string


def randomized_password_crippler(password, remove_count=2):
    """
    Strengthen and then weaken a password according to specified rules.

    :param password: The input plaintext password string.
    :param remove_count: Number of characters to remove (default is 2).
    :return: The final weakened password string.
    """
    # Step 1: Ensure minimum length of 12 characters by padding with random characters
    if len(password) < 12:
        # Generate random characters from all categories to pad the password
        all_chars = string.ascii_letters + string.digits + "!@#$%^&*()-_=+[]{};:,.<>?"
        padding_length = 12 - len(password)
        for _ in range(padding_length):
            password += random.choice(all_chars)

    # Step 2: Ensure at least one character from each required category
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*()-_=+[]{};:,.<>?" for c in password)

    # If any category is missing, add a random character from that category
    if not has_upper:
        password += random.choice(string.ascii_uppercase)
    if not has_lower:
        password += random.choice(string.ascii_lowercase)
    if not has_digit:
        password += random.choice(string.digits)
    if not has_special:
        password += random.choice("!@#$%^&*()-_=+[]{};:,.<>?")

    # Step 3: Shuffle the entire password string to randomize character positions
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    # Step 4: Deliberately weaken the password by removing specified number of characters
    if remove_count <= 0:
        return password

    # Identify indices of characters from each required category
    upper_indices = [i for i, c in enumerate(password) if c.isupper()]
    lower_indices = [i for i, c in enumerate(password) if c.islower()]
    digit_indices = [i for i, c in enumerate(password) if c.isdigit()]
    special_indices = [i for i, c in enumerate(password) if c in "!@#$%^&*()-_=+[]{};:,.<>?"]

    # Ensure we keep at least one character from each category if possible
    to_remove = []
    categories = [upper_indices, lower_indices, digit_indices, special_indices]
    remaining_chars = list(password)

    # Remove characters one by one, ensuring at least one from each category remains
    for _ in range(remove_count):
        if len(remaining_chars) <= 4:
            break  # Can't remove more without violating constraints

        # Find a random index that is not from the last remaining character of any category
        valid_indices = []
        for i, char in enumerate(remaining_chars):
            # Check if removing this character would leave us with no character from its category
            category_has_more = False
            if char.isupper():
                category_has_more = any(i != j for j in upper_indices if j < len(remaining_chars) and remaining_chars[j] == char)
            elif char.islower():
                category_has_more = any(i != j for j in lower_indices if j < len(remaining_chars) and remaining_chars[j] == char)
            elif char.isdigit():
                category_has_more = any(i != j for j in digit_indices if j < len(remaining_chars) and remaining_chars[j] == char)
            else:
                category_has_more = any(i != j for j in special_indices if j < len(remaining_chars) and remaining_chars[j] == char)

            # Only remove if it's not the last character of a category
            if category_has_more or (len(upper_indices) + len(lower_indices) + len(digit_indices) + len(special_indices)) > 4:
                valid_indices.append(i)

        # If we have no valid indices, just remove any random character
        if not valid_indices:
            valid_indices = list(range(len(remaining_chars)))

        # Pick a random index to remove
        index_to_remove = random.choice(valid_indices)
        to_remove.append(index_to_remove)

    # Sort indices in descending order to avoid index shifting issues when removing
    to_remove.sort(reverse=True)
    for idx in to_remove:
        remaining_chars.pop(idx)

    # Return the final weakened password
    return ''.join(remaining_chars)


if __name__ == "__main__":
    # Example usage of the randomized_password_crippler function
    user_input = input("Enter a plaintext password: ")
    result = randomized_password_crippler(user_input)
    print(f"Final weakened password: {result}")
