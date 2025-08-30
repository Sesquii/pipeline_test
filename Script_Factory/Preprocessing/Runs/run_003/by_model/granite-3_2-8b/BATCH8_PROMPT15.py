# BATCH8_PROMPT15_Granite.py

def count_words(file_path):
    """
    Counts words from a file and exaggerates counts for words with 'e' appearing more than 3 times.

    Args:
    - file_path (str): Path to the text file to be read.

    Returns:
    - dict: A dictionary where keys are words and values are their exaggerated/actual counts.
    """
    
    # Initialize an empty dictionary for word counts
    word_counts = {}
    
    # Open and read the file
    with open(file_path, 'r') as file:
        for line in file:
            # Split the line into words
            words = line.split()
            
            # Process each word
            for word in words:
                # Remove punctuation and convert to lowercase for case-insensitive comparison
                cleaned_word = ''.join(e for e in word if e.isalnum()).lower()
                
                # Count the 'e' occurrences in the word
                e_count = sum(1 for letter in cleaned_word if letter == 'e')
                
                # If the word has more than 3 'e's, exaggerate its count
                if e_count > 3:
                    word_counts[cleaned_word] = word_counts.get(cleaned_word, 0) * 3
                else:
                    word_counts[cleaned_word] = word_counts.get(cleaned_word, 0) + 1
    
    return word_counts


def main():
    """
    Entry point of the program - reads a file and prints exaggerated word counts.
    """
    # Replace 'your_text_file.txt' with the path to your text file
    file_path = 'your_text_file.txt'
    
    try:
        # Get word counts
        word_counts = count_words(file_path)
        
        # Print results
        for word, count in sorted(word_counts.items()):
            print(f"{word}: {count}")
    except FileNotFoundError:
        print("File not found. Please check the file path.")


if __name__ == "__main__":
    main()