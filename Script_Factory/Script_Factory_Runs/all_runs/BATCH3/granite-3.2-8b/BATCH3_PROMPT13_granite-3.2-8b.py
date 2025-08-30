import random
import string

def generate_random_word(length=5):
    """Generates a random word of given length."""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def expand_acronym(acronym, depth):
    """Recursively expands an acronym to a certain depth."""
    if depth == 0:
        return acronym

    # Split the current acronym into its components
    parts = [char.title() + generate_random_word(4) for char in acronym]
    
    # Join them back together with spaces
    expanded_acronym = ' '.join(parts)
    return expand_acronym(expanded_acronym, depth - 1)

def main():
    print("Recursive Acronym Expander")
    acronym = input("Enter an acronym: ")
    max_depth = int(input("Enter the maximum depth for expansion: "))

    try:
        expanded_acronym = expand_acronym(acronym, max_depth)
        print(f"Expanded Acronym: {expanded_acronym}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()