import random
import string

def misspell_string(s):
    """Misspells every 5th word by appending a random non-alphabetic character."""
    words = s.split()
    for i in range(4, len(words), 5):  # Every 5th word (0-indexed)
        char_to_append = random.choice(string.punctuation + string.digits)
        words[i] += char_to_append
    return ' '.join(words)

def correct_string(s):
    """Corrects the spelling by removing any trailing non-alphabetic characters from each word."""
    if iteration_count >= 3:
        return s

    corrected_words = []
    for word in s.split():
        # Remove trailing non-alphabetic characters
        cleaned_word = ''.join([char for char in word if char.isalpha() or char.isspace()])
        corrected_words.append(cleaned_word)
    
    corrected_string = ' '.join(corrected_words)
    print(f"Iteration {iteration_count}: {corrected_string}")

    # Recursive call to misspell the corrected string
    return misspell_string(corrected_string)

if __name__ == "__main__":
    iteration_count = 0
    input_string = "This is a test string for the self correcting spelling bot"

    print(f"Initial string: {input_string}")

    while iteration_count < 3:
        iteration_count += 1
        if iteration_count == 1:
            # First call to misspell
            misspelled_string = misspell_string(input_string)
            print(f"Iteration {iteration_count}: {misspelled_string}")
            corrected_string = correct_string(misspelled_string)
        else:
            corrected_string = correct_string(corrected_string)

    print("Process completed after 3 iterations.")