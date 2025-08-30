# BATCH10_PROMPT18_gpt_4.py

# Importing the required module for random selection of words
import random

# List of short words to form sentences
words = ["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]

def create_sentence():
    # Selecting seven random words from the list
    sentence_words = random.sample(words, 7)
    # Joining the selected words to form a sentence
    return ' '.join(sentence_words) + '.'

# Main function to execute the program
if __name__ == "__main__":
    # Printing three sentences each containing exactly seven words
    for _ in range(3):
        print(create_sentence())