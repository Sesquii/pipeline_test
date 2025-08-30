# BATCH10_PROMPT5_Text2Emoji.py

import emoji
from collections import defaultdict


def word_to_emoji(word):
    """Map palindromic words to their corresponding emojis."""
    # This is a placeholder function for the actual emoji mapping logic.
    # In a real scenario, you'd have a comprehensive dictionary of palindromes and their emoji equivalents.
    return ''.join([emoji.emojize(char) if char in emoji.UNICODE_EMOJI else char for char in word])


def translate_palindromic(text):
    """Translate palindromic words in the given text to emojis."""
    # Split the text into words, process each one and join back.
    words = text.split()
    translated_words = [word_to_emoji(word) if word == word[::-1] else word for word in words]
    return ' '.join(translated_words)


def main():
    """Entry point of the program."""
    input_text = "A man, a plan, a canal, Panama! Level, Madam. Radar."

    # Translate palindromic words to emojis
    translated_text = translate_palindromic(input_text)

    print("Translated Text:")
    print(translated_text)


if __name__ == "__main__":
    main()