import random

# List of words to use for generating acronyms
WORD_LIST = [
    "Nonsensical", "Albatross", "Space", "Agency", "North", "American",
    "Recursive", "Acronym", "Expander", "Meaningless", "Random", "Words",
    "Python", "Programming", "Code", "Script", "Development", "Software",
    "Technology", "Innovation", "Artificial", "Intelligence", "Machine",
    "Learning", "Data", "Science", "Engineering", "Research"
]

def generate_acronym(acronym, depth):
    """
    Recursively generates a meaningless acronym from the given acronym
    until the specified depth is reached.

    Args:
        acronym (str): The initial acronym to expand.
        depth (int): The number of times to recursively expand the acronym.

    Returns:
        str: The final expanded acronym after reaching the specified depth.
    """
    if depth <= 0:
        return acronym

    # Get the first letter of each word in the current acronym
    words = [word.strip() for word in acronym.split()]
    initials = [word[0] for word in words]

    # Generate a new meaningless phrase using random words from WORD_LIST
    new_phrase = []
    for initial in initials:
        new_word = random.choice(WORD_LIST)
        while new_word.startswith(initial):
            new_word = random.choice(WORD_LIST)  # Ensure the first letter matches the initial
        new_phrase.append(new_word)

    # Join the new words into a phrase and create an acronym from it
    new_acronym = " ".join([word[0] for word in new_phrase])
    return generate_acronym(new_acronym, depth - 1)

def main():
    """
    Main function to execute the Recursive Acronym Expander.
    Takes user input for initial acronym and expansion depth.
    """
    print("Recursive Acronym Expander")
    print("--------------------------")

    # Get user input
    initial_acronym = input("Enter an acronym (e.g., NASA): ").upper()
    try:
        max_depth = int(input("Enter the maximum depth for recursion: "))
    except ValueError:
        print("Invalid depth. Please enter a valid integer.")
        return

    if max_depth < 0:
        print("Depth must be a non-negative integer.")
        return

    # Generate and display the final expanded acronym
    result = generate_acronym(initial_acronym, max_depth)
    print(f"\nFinal Expanded Acronym: {result}")

if __name__ == "__main__":
    main()