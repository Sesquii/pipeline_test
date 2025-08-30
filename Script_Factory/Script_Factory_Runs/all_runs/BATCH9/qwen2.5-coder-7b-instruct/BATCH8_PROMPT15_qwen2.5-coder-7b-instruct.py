# BATCH8_PROMPT15_gpt4.py

def count_words(file_path):
    """
    Counts words in a file, exaggerating counts for words with more than three 'e's.
    
    Args:
    file_path (str): The path to the text file to read.
    
    Returns:
    dict: A dictionary of word counts, with exaggerated counts for certain words.
    """
    word_count = {}
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                # Remove punctuation and convert to lowercase
                cleaned_word = ''.join(char.lower() for char in word if char.isalpha())
                if cleaned_word in word_count:
                    word_count[cleaned_word] += 1
                else:
                    word_count[cleaned_word] = 1
    
    # Exaggerate counts for words with more than three 'e's
    for word, count in list(word_count.items()):
        if word.count('e') > 3:
            word_count[word] *= 3
    
    return word_count

if __name__ == "__main__":
    file_path = input("Enter the path to the text file: ")
    result = count_words(file_path)
    print(result)