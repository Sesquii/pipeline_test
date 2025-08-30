def exaggerated_word_counter(input_string):
    """
    Counts occurrences of each word in a string.
    Words with length exactly 3 characters have their count exaggerated by a factor of 10.

    Args:
        input_string (str): The input string to analyze

    Returns:
        dict: A dictionary containing words as keys and their counts as values
    """
    # Initialize an empty dictionary to store word counts
    word_counts = {}

    # Split the input string into individual words
    words = input_string.split()

    # Iterate through each word in the list
    for word in words:
        # Check if the word is already in the dictionary
        if word in word_counts:
            # Increment the count (exaggerated by 10x for length-3 words)
            word_counts[word] += 10 if len(word) == 3 else 1
        else:
            # Add new word with initial count (exaggerated by 10x for length-3 words)
            word_counts[word] = 10 if len(word) == 3 else 1

    return word_counts

if __name__ == "__main__":
    # Example usage
    input_text = "the cat in the hat sat on the mat"
    result = exaggerated_word_counter(input_text)
    print(result)