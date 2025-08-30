import random

def load_vocabulary(file_path):
    """Load words from a file."""
    with open(file_path, 'r') as file:
        vocabulary = [word.strip() for word in file.readlines()]
    return vocabulary

def transpose_word(word):
    """Transposes two random adjacent letters in the word."""
    if len(word) < 2:
        return word
    pos = random.randint(0, len(word) - 2)
    transposed_word = word[:pos] + word[pos+1] + word[pos] + word[pos+2:]
    return transposed_word

def misspell_words(vocabulary, text):
    """Misspell target words in the text by transposing adjacent letters."""
    misspelled_text = []
    for line in text.split('\n'):
        new_line = ''
        for word in line.split():
            if word.lower() in vocabulary:
                new_line += transpose_word(word) + ' '
            else:
                new_line += word + ' '
        misspelled_text.append(new_line.strip())
    return '\n'.join(misspelled_text)

def correct_words(vocabulary, text):
    """Correct misspelled target words by transposing back adjacent letters."""
    corrected_text = []
    for line in text.split('\n'):
        new_line = ''
        for word in line.split():
            if any(word == transpose_word(target) for target in vocabulary):
                for target in vocabulary:
                    if word == transpose_word(target):
                        new_line += target + ' '
                        break
            else:
                new_line += word + ' '
        corrected_text.append(new_line.strip())
    return '\n'.join(corrected_text)

def main():
    # Load vocabulary from file
    vocabulary = load_vocabulary('vocabulary.txt')
    
    # Read the text file
    with open('input_text.txt', 'r') as file:
        text = file.read()
    
    # Misspell target words in the text
    misspelled_text = misspell_words(vocabulary, text)
    
    # Write misspelled text to a new file
    with open(f'misspelled_text_BATCH7_PROMPT1_{model_name}.txt', 'w') as file:
        file.write(misspelled_text)
    
    # Correct the misspelled words
    corrected_text = correct_words(vocabulary, misspelled_text)
    
    # Write corrected text to a new file
    with open(f'corrected_text_BATCH7_PROMPT1_{model_name}.txt', 'w') as file:
        file.write(corrected_text)

if __name__ == "__main__":
    model_name = "YourModelName"  # Replace with the actual model name or leave empty if not applicable
    main()