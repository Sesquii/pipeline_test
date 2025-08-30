import re
import random

def read_file(file_path):
    """Reads the content of a file."""
    with open(file_path, 'r') as file:
        return file.read()

def write_file(file_path, content):
    """Writes content to a file."""
    with open(file_path, 'w') as file:
        file.write(content)

def get_words(text):
    """Extracts words from text."""
    return re.findall(r'\b\w+\b', text)

def misspell_word(word):
    """Purposefully misspells a word."""
    if len(word) > 1:
        index = random.randint(0, len(word) - 2)
        return word[:index] + 'x' + word[index+1:]
    return word + 'x'

def correct_misspelling(misspelled_word):
    """Corrects a misspelled word."""
    if misspelled_word.endswith('x'):
        return misspelled_word[:-1]
    pattern = re.compile(re.escape(misspelled_word) + r'x')
    return re.sub(pattern, 'x', misspelled_word)

def process_text(text):
    """Processes text to purposefully misspell every tenth word and correct the next occurrence."""
    words = get_words(text)
    misspelled_words = {}
    
    for i in range(len(words)):
        if (i + 1) % 10 == 0:
            original_word = words[i]
            misspelled_word = misspell_word(original_word)
            misspelled_words[original_word] = misspelled_word
            words[i] = misspelled_word
    
    for i in range(len(words)):
        word = words[i]
        if word in misspelled_words.values():
            corrected_word = correct_misspelling(word)
            if corrected_word != word:
                words[i] = corrected_word
    
    return ' '.join(words)

def main(input_file, output_file):
    """Main function to process the input file and write to output file."""
    text = read_file(input_file)
    processed_text = process_text(text)
    write_file(output_file, processed_text)

if __name__ == "__main__":
    input_file = 'input.txt'
    output_file = 'output.txt'
    main(input_file, output_file)