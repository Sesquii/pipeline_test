# BATCH2_PROMPT13_Granite.py

def recursive_acronym(acronym, depth=5):
    """Recursively expands an acronym into nonsensical terms until a specified depth."""

    # A dictionary with common English words categorized for easy access
    categories = {
        "NASA": ["North", "American", "Space", "Agency"],
        "FBI": ["Federal", "Bureau", "Investigation"],
        "CIA": ["Central", "Intelligence", "Agency"]
    }

    # If the acronym is in our dictionary, expand it
    if acronym.upper() in categories:
        return _expand_acronym(categories[acronym.upper()], depth)

    # If not in dictionary, just append random words from different categories
    else:
        all_words = [word for category in categories.values() for word in category]
        return ' '.join([random.choice(all_words) for _ in range(depth)])


def _expand_acronym(acronym_list, depth):
    """Recursively expands an acronym list until the desired depth."""

    if depth == 1:
        return random.choice(acronym_list)

    expanded = []
    for term in acronym_list:
        expanded.extend(_expand_acronym(term.split(), depth - 1))
    return ' '.join(expanded)


if __name__ == "__main__":
    import random

    # Example usage:
    acronym = "NASA"
    depth = 3
    print(recursive_acronym(acronym, depth))