# BATCH8_PROMPT10_Granite.py

def exaggerated_word_counter(text):
    """
    Counts words in a given string, with special handling for 3-character words.

    Args:
        text (str): The input text to be analyzed.

    Returns:
        dict: A dictionary where keys are words and values are their counts.
              Words of length 3 are exaggerated by being counted as if they're 10 times more frequent.
    """

    # Split the text into words
    words = text.split()

    word_count = {}

    for word in words:
        # If the word is exactly 3 characters long, count it 10 times
        if len(word) == 3:
            word_count[word] = word_count.get(word, 0) + 10
        else:
            word_count[word] = word_count.get(word, 0) + 1

    return word_count


if __name__ == "__main__":
    # Test the function with a sample text
    input_text = "This is an example sentence with some short words like 'is' and longer ones."
    result = exaggerated_word_counter(input_text)
    print(result)