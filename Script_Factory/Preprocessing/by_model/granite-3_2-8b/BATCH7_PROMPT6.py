# BATCH7_PROMPT6_SpellCheckerBot.py

import random
from spellchecker import SpellCheck

def misspell_words(input_file, output_file):
    with open(input_file, 'r') as f:
        text = f.read()

    words = text.split()
    spell = SpellCheck()

    for i in range(10):  # Misspell 10 random words
        word = random.choice(words)
        misspelled = spell.unknown([word])
        if misspelled:
            words[words.index(word)] = misspelled[0]

    with open(output_file, 'w') as f:
        f.write(' '.join(words))

def correct_spelling(input_file, output_file):
    spell = SpellCheck()

    with open(input_file, 'r') as f:
        text = f.read()

    corrected_text = ''
    for word in text.split():
        if spell.known([word]):
            corrected_text += word + ' '
        else:
            corrections = spell.candidates(word)
            correct_word = corrections[0]  # Using the first suggested correction
            corrected_text += correct_word + ' '

    with open(output_file, 'w') as f:
        f.write(corrected_text)

def log_errors_and_corrections(input_file, output_file):
    spell = SpellCheck()

    errors_found = 0
    corrections_made = 0

    with open(input_file, 'r') as f:
        original_text = f.read()

    words = original_text.split()
    for word in words:
        if not spell.known([word]):
            errors_found += 1

    corrected_words = [spell.correction(word) if not spell.known([word]) else word for word in words]
    corrected_text = ' '.join(corrected_words)
    with open('fixed_text.txt', 'w') as f:
        f.write(corrected_text)

    for word, corr_word in zip(words, corrected_words):
        if word != corr_word and word not in spell.known():
            corrections_made += 1

    with open('log.txt', 'a') as log_file:
        log_file.write(f"Errors Found: {errors_found}\n")
        log_file.write(f"Corrections Made: {corrections_made}\n")

def main():
    input_text = 'sample_input.txt'  # Replace with your input file path
    typos_output = 'typos.txt'
    fixed_output = 'fixed_text.txt'
    log_file = 'log.txt'

    misspell_words(input_text, typos_output)
    correct_spelling(typos_output, fixed_output)
    log_errors_and_corrections(input_text, fixed_output)

if __name__ == "__main__":
    main()