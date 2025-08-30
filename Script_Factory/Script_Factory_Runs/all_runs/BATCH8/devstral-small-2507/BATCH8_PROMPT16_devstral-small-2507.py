import random

def read_file(file_path):
    """Read the content of a text file and return it as a string."""
    with open(file_path, 'r') as file:
        return file.read()

def count_words(text):
    """Count the occurrences of each word in the given text."""
    words = text.split()
    word_count = {}
    for word in words:
        word = word.lower()  # Make word counting case-insensitive
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

def apply_exaggeration(word_count):
    """Apply a random exaggeration factor to each word count."""
    exaggerated_counts = {}
    for word, count in word_count.items():
        exaggeration_factor = round(random.uniform(1.0, 3.0), 2)
        exaggerated_counts[word] = round(count * exaggeration_factor, 2)
    return exaggerated_counts

def main(file_path):
    """Main function to read a file, count words with exaggeration, and print the result."""
    text = read_file(file_path)
    word_count = count_words(text)
    exaggerated_word_count = apply_exaggeration(word_count)
    print(exaggerated_word_count)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python BATCH8_PROMPT16_Devstral.py <file_path>")
    else:
        file_path = sys.argv[1]
        main(file_path)