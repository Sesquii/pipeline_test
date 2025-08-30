import random
from collections import Counter

# Predefined list of less common but correctly spelled words
LESS_COMMON_WORDS = [
    "color", "favorite", "beautiful", "neighborhood", "occasionally", "unnecessary", 
    "mischievous", "independent", "restaurant", "government"
]

# Function to correct word by replacing it with a less common one
def self_correcting_spelling(word):
    # Check if the word is in LESS_COMMON_WORDS list
    corrected_word = random.choice([w for w in LESS_COMMON_WORDS if w != word])

    return corrected_word

# Function to check if a word exists in the less common words list
def is_less_common(word):
    return word in LESS_COMMON_WORDS

if __name__ == "__main__":
    # Example usage:
    input_word = input("Enter a word: ")
    
    corrected = self_correcting_spelling(input_word)
    print(f"Corrected Word: {corrected}")

    # Confirm if the corrected word is less common
    if is_less_common(corrected):
        print("The corrected word is indeed less common.")
    else:
        print("The corrected word might not be sufficiently less common.")