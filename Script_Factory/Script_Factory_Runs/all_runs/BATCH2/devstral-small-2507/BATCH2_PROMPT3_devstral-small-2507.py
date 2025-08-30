import re

def read_file(file_path):
    """Read the content of a file."""
    with open(file_path, 'r') as file:
        return file.read()

def write_file(file_path, content):
    """Write content to a file."""
    with open(file_path, 'w') as file:
        file.write(content)

def misspell_word(word):
    """Purposefully misspell a word by adding a random character."""
    import random
    import string

    if len(word) == 0:
        return word

    random_char = random.choice(string.ascii_lowercase)
    position = random.randint(0, len(word))
    return word[:position] + random_char + word[position:]

def correct_spelling(text, word_to_correct):
    """Correct the spelling of a specific word in the text."""
    pattern = re.compile(r'\b' + re.escape(word_to_correct) + r'\b')
    return pattern.sub(word_to_correct, text)

def process_text(text):
    """Process the text to misspell every tenth word and correct the next occurrence."""
    words = text.split()
    processed_words = []
    word_count = 0

    for i, word in enumerate(words):
        if (i + 1) % 10 == 0:
            original_word = word
            misspelled_word = misspell_word(word)
            processed_words.append(misspelled_word)

            # Correct the next occurrence of this word
            for j in range(i + 1, len(words)):
                if words[j].lower() == original_word.lower():
                    processed_words.append(original_word)
                    break
            else:
                # If no next occurrence is found, just append the original word
                processed_words.append(original_word)

        else:
            processed_words.append(word)

    return ' '.join(processed_words)

def main(input_file_path, output_file_path):
    """Main function to read, process, and write the file."""
    text = read_file(input_file_path)
    processed_text = process_text(text)
    write_file(output_file_path, processed_text)
    print(f"Processed text has been written to {output_file_path}")

if __name__ == "__main__":
    input_file = "input.txt"
    output_file = "output.txt"

    main(input_file, output_file)