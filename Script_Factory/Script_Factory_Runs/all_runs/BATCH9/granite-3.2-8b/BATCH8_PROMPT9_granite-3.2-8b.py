# BATCH8_PROMPT9_Granite.py

def count_words(file_path):
    """
    Counts words in a text file, exaggerating counts for words appearing more than 5 times.

    Args:
        file_path (str): Path to the input text file.

    Returns:
        dict: A dictionary with words as keys and their respective counts as values.
              Word counts greater than 5 are exaggerated by a factor of 2.
    """
    word_count = {}
    
    # Open and read the file
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Split the line into words
            words = line.lower().split()
            
            for word in words:
                # Remove punctuation from words
                cleaned_word = ''.join([char if char.isalnum() or char.isspace() else ' ' for char in word])
                
                if cleaned_word:  # Ignore empty strings
                    if cleaned_word not in word_count:
                        word_count[cleaned_word] = 1
                    elif word_count[cleaned_word] < 5:
                        word_count[cleaned_word] += 1
                    else:
                        word_count[cleaned_word] = min(2 * word_count[cleaned_word], 9999)  # Capping at 9999 for exaggeration

    return word_count


def main():
    """
    Entry point of the program. Expects a text file named 'input.txt' in the same directory.
    Prints the word count dictionary to the console.
    """
    file_path = 'input.txt'
    word_counts = count_words(file_path)
    
    print("Word Counts:")
    for word, count in sorted(word_counts.items()):
        print(f"{word}: {count}")


if __name__ == "__main__":
    main()