# BATCH2_PROMPT13_Devstral.py

import random

# List of meaningless words to create new acronyms
MEANINGLESS_WORDS = [
    "Nonsensical", "Albatross", "Bumblebee", "Cucumber", "Dandelion",
    "Ephemeral", "Frolicsome", "Gargantuan", "Harmonious", "Ineffable",
    "Jubilant", "Kaleidoscopic", "Luminous", "Mysterious", "Nebulous",
    "Oblivion", "Peculiar", "Quirky", "Radiant", "Sublime", "Tranquil",
    "Unpredictable", "Vibrant", "Whimsical", "Xenial", "Youthful",
    "Zealous"
]

def expand_acronym(acronym, depth):
    """
    Recursively expands an acronym into a meaningless acronym.

    Args:
        acronym (str): The original acronym to expand.
        depth (int): The recursion depth to reach.

    Returns:
        str: The expanded acronym after reaching the specified depth.
    """
    if depth == 0:
        return acronym

    # Split the acronym into words
    words = acronym.split()

    # If it's not already an acronym (first expansion), create one
    if len(words) > 1 and all(word.isalpha() for word in words):
        new_acronym = ''.join([word[0] for word in words])
    else:
        new_acronym = acronym

    # Create a new meaningless phrase
    meaningful_words_count = random.randint(2, 4)
    meaningful_part = ' '.join(words[:meaningful_words_count])
    meaningless_part = ' '.join(random.sample(MEANINGLESS_WORDS, len(words) - meaningful_words_count))

    new_meaningful_phrase = f"{meaningful_part} {meaningless_part}"
    return expand_acronym(new_meaningful_phrase, depth - 1)

def main():
    """Main entry point for the acronym expander."""
    # Example usage
    original_acronym = "NASA"
    expansion_depth = 3

    print(f"Original Acronym: {original_acronym}")
    expanded_acronym = expand_acronym(original_acronym, expansion_depth)
    print(f"Expanded Acronym after {expansion_depth} levels: {expanded_acronym}")

if __name__ == "__main__":
    main()