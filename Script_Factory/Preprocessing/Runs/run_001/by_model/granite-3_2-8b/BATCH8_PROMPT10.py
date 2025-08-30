# BATCH8_PROMPT10_Granite.py

def exaggerated_word_counter(text):
    """
    This function takes a string of text as input and returns a dictionary
    with word counts. For any word of length 3, the count is exaggerated by a factor of 10.
    
    :param text: A string containing words to be counted.
    :return: A dictionary where keys are words and values are their (exaggerated) counts.
    """
    # Split the input text into individual words
    words = text.split()

    word_count = {}

    for word in words:
        # Normalize the word: convert to lowercase, remove punctuation and strip whitespace
        normalized_word = word.lower().strip('.,!?()-_;:')

        if len(normalized_word) == 3:
            # If the word length is exactly 3, exaggerate its count by a factor of 10
            word_count[normalized_word] = 10 * (word_count.get(normalized_word, 0))
        else:
            # For words of other lengths, count them normally
            word_count[normalized_word] = word_count.get(normalized_word, 0) + 1

    return word_count

if __name__ == "__main__":
    # Example usage:
    text = "Hello world! This is a test; this is only a simple test."
    result = exaggerated_word_counter(text)
    for word, count in result.items():
        print(f"{word}: {count}")