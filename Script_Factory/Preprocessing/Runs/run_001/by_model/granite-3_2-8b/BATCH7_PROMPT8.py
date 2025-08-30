import random
import string
from typing import List


def misspell_capitalized(word: str) -> str:
    """Misspells a word starting with an uppercase letter by randomly changing one of its vowels to a consonant."""
    if not word[0].isupper():
        raise ValueError("The word does not start with an uppercase letter.")

    vowels = 'aeiou'
    consonants = ''.join(c for c in string.ascii_lowercase if c not in vowels)
    random_vowel_index = random.randint(0, len(word) - 1)

    if word[random_vowel_index] in vowels:
        new_char = random.choice(consonants)
    else:
        new_char = word[random_vowel_index]

    return word[:random_vowel_index] + new_char + word[random_vowel_index+1:]


def correct_case(word: str) -> str:
    """Corrects the case of a given word."""
    if word.isupper():
        return word.capitalize()
    elif word.istitle():
        return word.title()
    else:
        return word


def read_and_process_file(input_filename: str, output_filename: str) -> None:
    """Reads a file, misspells capitalized words, and writes the result to an output file."""
    with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
        for line in infile:
            words = line.split()
            new_words = []
            for word in words:
                if word[0].isupper():
                    misspelled = misspell_capitalized(word)
                    corrected = correct_case(misspelled)
                    new_words.append(corrected)
                else:
                    new_words.append(word)

            outfile.write(' '.join(new_words) + '\n')


if __name__ == "__main__":
    input_file = 'input_text.txt'  # Replace with your input file name
    output_file = 'misspelled_corrected.txt'

    read_and_process_file(input_file, output_file)