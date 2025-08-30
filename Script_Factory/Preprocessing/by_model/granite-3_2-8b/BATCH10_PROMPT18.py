# BATCH10_PROMPT18_Granite.py

# Importing necessary libraries
import random

# List of short phrases for story generation
phrases = [
    "In a quiet town lived a young boy.",
    "He found an old, mysterious book.",
    "Under the waning moonlight it opened.",
    "Strange symbols filled its pages.",
    "A map appeared on the next page.",
    "It hinted at a hidden treasure.",
    "The boy made a secret plan.",
    "In the dead of night, he set out.",
    "Through dense forests, he journeyed.",
    "Over towering mountains, he climbed.",
    "Finally, he reached an ancient cave.",
    "Inside, glowing crystals illuminated.",
    "There lay the treasure, waiting to be claimed.",
    "Unexpectedly, the ground began to shake.",
    "A trap! He narrowly escaped.",
    "Back home, he kept his secret tale.",
    "Years later, he'd tell it to his grandchildren."
]

def generate_story():
    story = []
    for phrase in phrases:
        sentence = ' '.join(phrase.split()[:7]) + '.'  # Ensuring each sentence has exactly seven words
        story.append(sentence)
    return '\n'.join(story)

# Main function to run the program
def main():
    story = generate_story()
    print(story)

if __name__ == "__main__":
    main()