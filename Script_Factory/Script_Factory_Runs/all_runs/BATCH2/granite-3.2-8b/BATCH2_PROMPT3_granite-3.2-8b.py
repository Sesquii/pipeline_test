import re
from collections import Counter

def misspell_word(word):
    """Randomly misspell a word by swapping two letters."""
    word = list(word)
    swap_indices = sorted(random.sample(range(len(word)), 2))
    word[swap_indices[0]], word[swap_indices[1]] = word[swap_indices[1]], word[swap_indices[0]]
    return "".join(word)

def correct_spelling(word, words):
    """Correct the spelling of a word by finding its closest match in the list of words."""
    min_distance = float('inf')
    corrected_word = None
    for w in words:
        distance = sum(1 for a, b in zip(word, w) if a != b)
        if distance < min_distance:
            min_distance = distance
            corrected_word = w
    return corrected_word

def process_file(filename):
    """Read file, misspell every tenth word and correct the next occurrence."""
    
    # Read file content
    with open(filename, 'r') as f:
        text = f.read()

    words = re.findall(r'\b\w+\b', text.lower())  # Extract all words, ignoring case

    word_counter = Counter(words)
    misspelled_words = set()

    # Misspell every tenth word
    for i, word in enumerate(words):
        if (i + 1) % 10 == 0:
            misspelled_word = misspell_word(word)
            misspelled_words.add(misspelled_word)
            text = text.replace(word, f"MISSPELLED_{misspelled_word}")

    # Correct the next occurrence of each misspelled word
    for i, word in enumerate(words):
        if word in misspelled_words:
            corrected_word = correct_spelling(word, words)
            text = re.sub(r'\b' + re.escape(word) + r'\b', corrected_word, text)

    return text

if __name__ == "__main__":
    filename = 'input.txt'  # Replace with your text file path
    new_text = process_file(filename)

    print("Misspelled Words:")
    for misspelled in set(re.findall(r"MISSPELLED_\w+", new_text)):
        print(misspelled)

    print("\nCorrected Text:")
    print(new_text)