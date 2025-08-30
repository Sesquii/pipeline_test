import random
from spellchecker import SpellChecker

# Function to misspell words and save to typos.txt
def create_typos(input_file, typo_file):
    spell = SpellChecker()
    with open(input_file, 'r') as file:
        text = file.read()
    
    words = text.split()
    misspelled = spell.unknown(words)
    if len(misspelled) < 10:
        raise ValueError("Not enough unique misspellings found in the input file.")
    
    typo_indices = random.sample(range(len(misspelled)), 10)
    typos = [(words.index(word), word, random.choice(list(spell.known(word)))) for idx, word in enumerate(words) if idx in typo_indices]
    
    with open(typo_file, 'w') as typo:
        typo.write(text)
    
    return typos

# Function to correct typos and save to fixed_text.txt
def fix_typos(typo_file, fixed_file):
    spell = SpellChecker()
    with open(typo_file, 'r') as file:
        text = file.read()
    
    words = text.split()
    for typo in typos:
        word_index = typo[0]
        wrong_word = typo[1]
        corrected_word = typo[2]
        words[word_index] = corrected_word
    
    fixed_text = ' '.join(words)
    with open(fixed_file, 'w') as fixed:
        fixed.write(fixed_text)

# Function to log errors and corrections
def log_errors(typos, log_file):
    with open(log_file, 'w') as log:
        for typo in typos:
            original_word = typo[1]
            corrected_word = typo[2]
            log.write(f"Original: {original_word}, Corrected: {corrected_word}\n")

# Main function
if __name__ == "__main__":
    input_file = 'input.txt'
    typo_file = 'typos.txt'
    fixed_file = 'fixed_text.txt'
    log_file = 'log.txt'
    
    try:
        typos = create_typos(input_file, typo_file)
        fix_typos(typo_file, fixed_file)
        log_errors(typos, log_file)
        print("Spelling corrections have been made and logged.")
    except Exception as e:
        print(f"An error occurred: {e}")
```

This Python script implements a "Self-Correcting Spelling Bot" with the specified requirements. It uses the `SpellChecker` library from the `spellchecker` package to identify misspellings, randomly selects 10 words to misspell, saves the original text with typos to `typos.txt`, corrects these typos, and logs the corrections in `log.txt`. The main function handles the workflow and error handling.