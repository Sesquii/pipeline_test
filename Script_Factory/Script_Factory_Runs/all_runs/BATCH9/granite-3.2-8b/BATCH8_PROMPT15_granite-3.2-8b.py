# BATCH8_PROMPT15_Granite.py

def count_words(file_path):
    """
    This function reads a text file and counts each word, exaggerating the count for words with more than three 'e's.

    Args:
        file_path (str): Path to the input text file.

    Returns:
        dict: A dictionary where keys are words and values are their exaggerated counts.
    """
    word_count = {}

    # Open and read the file
    with open(file_path, 'r') as file:
        for line in file:
            # Split the line into words
            words = line.split()

            for word in words:
                # Remove punctuation from the word and convert to lowercase
                cleaned_word = ''.join(char.lower() for char in word if char.isalnum())

                # Count 'e's in the word
                e_count = cleaned_word.count('e')

                # Decide whether to exaggerate or not
                if e_count > 3:
                    exaggerated_count = 3 * (1 + e_count)
                else:
                    exaggerated_count = 1 + e_count
                
                # Update the word count dictionary
                if cleaned_word in word_count:
                    word_count[cleaned_word] += exaggerated_count
                else:
                    word_count[cleaned_word] = exaggerated_count

    return word_count

def main():
    """Entry point for the script."""
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python BATCH8_PROMPT15_Granite.py <path_to_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    word_counts = count_words(file_path)
    
    # Print the results
    for word, count in word_counts.items():
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()