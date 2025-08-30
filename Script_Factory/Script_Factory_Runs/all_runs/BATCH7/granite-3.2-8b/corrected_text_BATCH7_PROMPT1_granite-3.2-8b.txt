import random
from difflib import get_close_matches

# Hard-coded list of target words
TARGET_WORDS = ["necessary", "accommodate", "rhythm"]

def transpose_letters(word):
    """Transposes two adjacent letters in a word."""
    list_word = list(word)
    i, j = random.sample(range(len(list_word) - 1), 2)
    list_word[i], list_word[j] = list_word[j], list_word[i]
    return ''.join(list_word)

def misspell(text):
    """Misspells each target word in the text."""
    words = text.split()
    for i, word in enumerate(words):
        if word in TARGET_WORDS:
            words[i] = transpose_letters(word)
    return ' '.join(words)

def correct_misspellings(text):
    """Corrects misspelled target words using get_close_matches."""
    words = text.split()
    corrected_words = []

    for word in words:
        matches = get_close_matches(word, TARGET_WORDS, n=1, cutoff=0.6)
        if matches:
            corrected_words.append(matches[0])
        else:
            corrected_words.append(word)  # Keep the word unchanged if no close match found

    return ' '.join(corrected_words)

def main():
    input_file = "input_text.txt"
    output_file = f"corrected_text_BATCH7_PROMPT1_{__file__.split('/')[-1]}.txt"

    with open(input_file, 'r') as file:
        text = file.read()

    # Misspell target words
    misspelled_text = misspell(text)

    # Correct misspelled target words
    corrected_text = correct_misspellings(misspelled_text)

    with open(output_file, 'w') as file:
        file.write(corrected_text)

if __name__ == "__main__":
    main()