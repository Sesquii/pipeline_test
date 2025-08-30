import re
import random

def misspell(word):
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    
    # Find all words starting with a capital letter
    if word[0].isupper():
        for vowel in vowels:
            if vowel in word:
                # Randomly replace one vowel with a consonant
                new_word = re.sub(vowel, random.choice(consonants), word, count=1)
                return new_word.upper()
    
    return word

def correct_case(word):
    # Only correct the case of the word
    return word.upper()

def process_file(input_path, output_path):
    with open(input_path, 'r') as file:
        lines = file.readlines()
    
    misspelled_lines = [misspell(line.strip()) + '\n' for line in lines]
    corrected_case_lines = [correct_case(line) + '\n' for line in misspelled_lines]
    
    with open(output_path, 'w') as file:
        file.writelines(corrected_case_lines)

if __name__ == "__main__":
    input_file = 'input.txt'
    output_file = 'output.txt'
    process_file(input_file, output_file)
```

This Python script reads a text file line by line, misspells words that start with a capital letter by randomly changing one of its vowels to a consonant, and then corrects only the case of these misspelled words. The final output is written to a new text file.