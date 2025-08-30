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
        word = word.strip('.,!?()[]{}"\'').lower()  # Basic cleaning
        if word:
            word_count[word] = word_count.get(word, 0) + 1
    return word_count

def add_fabricated_words(word_count):
    """Adds three fabricated words with random absurdly high counts."""
    fabricated_words = ['flibberjib', 'gobbledygook', 'hocuspocus']
    for word in fabricated_words:
        count = random.randint(1000, 9999)
        word_count[word] = count
    return word_count

def main():
    """Main function to execute the exaggerated word counter."""
    file_path = input("Enter the path of the text file: ")
    try:
        text = read_file(file_path)
        word_count = count_words(text)
        word_count = add_fabricated_words(word_count)

        print("\nWord Counts (including fabricated words):")
        for word, count in sorted(word_count.items(), key=lambda item: item[1], reverse=True):
            print(f"{word}: {count}")

    except FileNotFoundError:
        print("Error: The specified file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()