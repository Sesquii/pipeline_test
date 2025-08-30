import random
import string

def misspell(s):
    """Misspell every 5th word by appending a random non-alphabetic character."""
    words = s.split()
    for i, word in enumerate(words):
        if (i + 1) % 5 == 0:
            words[i] += random.choice(string.punctuation)
    return ' '.join(words)

def correct_spelling(s, iterations=3):
    """Correct the spelling recursively by removing extra characters."""
    if iterations > 0:
        # Misspell the string again
        misspelled = misspell(s)
        print(f"Iteration {iterations}: {misspelled}")
        
        # Correct it by finding and removing non-alphabetic characters at every 5th position
        corrected = ''.join([word[:-1] if (i+1) % 5 == 0 else word for i, word in enumerate(misspelled.split())])
        return correct_spelling(corrected, iterations - 1)
    else:
        return s

if __name__ == "__main__":
    original_string = "This is a test string to demonstrate the self-correcting spell bot."
    corrected_string = correct_spelling(original_string)
    print("Final Corrected String:", corrected_string)