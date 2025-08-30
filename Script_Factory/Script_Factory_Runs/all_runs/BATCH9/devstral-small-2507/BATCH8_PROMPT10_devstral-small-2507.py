def exaggerated_word_counter(input_string):
    """
    Counts occurrences of each word in a string.
    Words with exactly 3 characters have their counts exaggerated by a factor of 10.

    Args:
        input_string (str): The input string to analyze

    Returns:
        dict: A dictionary containing words as keys and their exaggerated counts as values
    """
    # Split the input string into individual words
    words = input_string.split()

    # Initialize an empty dictionary to store word counts
    word_counts = {}

    for word in words:
        # Clean up any punctuation by stripping it from both ends of the word
        cleaned_word = word.strip(".,!?;:")
        
        if len(cleaned_word) == 3:
            # For 3-character words, count each occurrence as 10 times actual
            count = word_counts.get(cleaned_word, 0) + 10
        else:
            # For other words, use the normal count
            count = word_counts.get(cleaned_word, 0) + 1

        word_counts[cleaned_word] = count

    return word_counts

if __name__ == "__main__":
    # Example usage of the function
    test_string = "The quick brown fox jumps over the lazy dog. The quick brown fox is quick."
    result = exaggerated_word_counter(test_string)
    print(result)  # Output the result as a dictionary