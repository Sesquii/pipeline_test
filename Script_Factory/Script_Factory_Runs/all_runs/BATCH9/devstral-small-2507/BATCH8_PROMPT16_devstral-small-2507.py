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
        word = word.lower()  # Normalize to lowercase
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

def apply_exaggeration(word_count):
    """Applies a random exaggeration factor (1.0 to 3.0) to each word count."""
    exaggerated_counts = {}
    for word, count in word_count.items():
        exaggeration_factor = round(random.uniform(1.0, 3.0), 2)
        exaggerated_counts[word] = count * exaggeration_factor
    return exaggerated_counts

def main(file_path):
    """Main function to execute the Exaggerated Word Counter."""
    text = read_file(file_path)
    word_count = count_words(text)
    exaggerated_word_count = apply_exaggeration(word_count)
    print(exaggerated_word_count)

if __name__ == "__main__":
    # Example usage
    file_path = 'sample.txt'  # Replace with your text file path
    main(file_path)