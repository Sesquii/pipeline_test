import random

def read_file(file_path):
    """Reads the content of a text file and returns it as a string."""
    with open(file_path, 'r') as file:
        return file.read()

def count_words(text):
    """Counts the occurrences of each word in the given text."""
    words = text.split()
    word_count = {}
    for word in words:
        cleaned_word = word.strip('.,!?()[]{}:;\"\'').lower()
        if cleaned_word:
            if cleaned_word in word_count:
                word_count[cleaned_word] += 1
            else:
                word_count[cleaned_word] = 1
    return word_count

def add_fabricated_words(word_count):
    """Adds three fabricated words with random high counts to the word count dictionary."""
    fabricated_words = ['flibberjib', 'gobbledygook', 'supercalifragilisticexpialidocious']
    for word in fabricated_words:
        word_count[word] = random.randint(1000, 5000)
    return word_count

def main():
    """Main function to execute the Exaggerated Word Counter."""
    file_path = 'input.txt'  # Replace with your text file path
    text = read_file(file_path)
    word_count = count_words(text)
    word_count_with_fabrications = add_fabricated_words(word_count.copy())
    print(word_count_with_fabrications)

if __name__ == "__main__":
    main()