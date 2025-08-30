import random

def read_file(file_path):
    """Reads a text file and returns its content as a string."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def count_words(text):
    """Counts the occurrences of each word in the given text."""
    words = text.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

def add_fabricated_words(word_count):
    """Adds three fabricated words with random counts to the dictionary."""
    fabricated_words = [f"word{random.randint(100, 999)}" for _ in range(3)]
    fabricated_counts = [random.randint(1000, 10000) for _ in range(3)]
    
    for word, count in zip(fabricated_words, fabricated_counts):
        word_count[word] = count
    
    return word_count

def main():
    file_path = 'input.txt'  # Replace with the path to your text file
    text = read_file(file_path)
    word_count = count_words(text)
    word_count = add_fabricated_words(word_count)
    
    print(word_count)

if __name__ == "__main__":
    main()
```

Please note that you need to replace `'input.txt'` with the actual path to your text file when running this script.