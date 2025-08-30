import re

# Phonetic rules for vowel substitution and correction
VOWEL_SUBSTITUTIONS = {'i': 'e', 'a': 'e', 'o': 'u'}
VOWEL_CORRECTIONS = {'ee': 'i', 'eu': 'o'}

def misspell(text):
    """Misspells every third word in the text using phonetic substitution."""
    words = re.findall(r'\b\w+\b', text)  # Split text into words
    for i, word in enumerate(words):
        if (i + 1) % 3 == 0:  # Every third word
            new_word = ''.join([VOWEL_SUBSTITUTIONS.get(c, c) for c in word])
            words[i] = new_word
    return ' '.join(words)

def correct_spelling(text):
    """Attemps to correct the spelling using phonetic rules."""
    words = re.findall(r'\b\w+\b', text)  # Split text into words
    corrected_words = []

    for word in words:
        new_word = word
        for vowel, sound in VOWEL_SUBSTITUTIONS.items():
            new_word = new_word.replace(vowel, sound)

        if new_word in VOWEL_CORRECTIONS.values():  # Check if correction matches a known phonetic rule
            corrected_words.append(list(VOWEL_CORRECTIONS.keys())[list(VOWEL_CORRECTIONS.values()).index(new_word)])
        else:
            corrected_words.append(new_word)

    return ' '.join(corrected_words)

def print_changes(original, corrected):
    """Prints the original and corrected texts, highlighting changes."""
    changed = list(set(original.split()) - set(corrected.split()))  # Find misspelled words
    if changed:
        print("Original: ", original)
        print("Changes: ", ' '.join(changed))
        print("Corrected: ", corrected)
    else:
        print("No changes detected.")

def main():
    user_input = input("Enter a sentence: ")
    misspelled = misspell(user_input)
    corrected = correct_spelling(misspelled)
    print_changes(user_input, corrected)

if __name__ == "__main__":
    main()