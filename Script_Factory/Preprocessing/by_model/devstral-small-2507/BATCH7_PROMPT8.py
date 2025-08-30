import random

def misspell_word(word):
    """Randomly change one vowel in a capitalized word to a consonant."""
    vowels = 'AEIOU'
    consonants = 'BCDFGHJKLMNPQRSTVWXYZ'
    
    # Find all vowels in the word
    vowel_positions = [i for i, char in enumerate(word) if char in vowels]
    
    if not vowel_positions:
        return word  # No vowels to change

    # Randomly select one vowel position
    selected_position = random.choice(vowel_positions)
    original_char = word[selected_position]

    # Find a consonant that's different from the original character
    possible_consonants = [c for c in consonants if c != original_char]
    if not possible_consonants:
        return word  # No different consonant available

    new_char = random.choice(possible_consonants)
    misspelled_word = word[:selected_position] + new_char + word[selected_position+1:]

    return misspelled_word

def correct_case(word):
    """Convert all letters to uppercase if the original word was capitalized."""
    if word[0].isupper():
        return word.upper()
    return word

def process_file(input_filename, output_filename):
    """Read input file, process each word, and write to output file."""
    with open(input_filename, 'r') as infile:
        content = infile.read()

    words = content.split()
    processed_words = []

    for word in words:
        # Only process words that start with a capital letter
        if word[0].isupper():
            misspelled = misspell_word(word)
            corrected_case = correct_case(misspelled)
            processed_words.append(corrected_case)
        else:
            processed_words.append(word)

    output_content = ' '.join(processed_words)

    with open(output_filename, 'w') as outfile:
        outfile.write(output_content)

if __name__ == "__main__":
    input_file = "input.txt"  # Replace with your actual input file name
    output_file = "output.txt"  # Replace with your desired output file name

    process_file(input_file, output_file)