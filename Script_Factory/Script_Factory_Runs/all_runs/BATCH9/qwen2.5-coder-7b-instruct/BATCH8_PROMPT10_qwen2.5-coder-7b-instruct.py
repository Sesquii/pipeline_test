def exaggerated_word_counter(input_string):
    """
    This function takes a string as input and counts the occurrences of each word.
    For words with exactly 3 characters, it reports a count that is 10 times the actual number.
    
    Args:
    input_string (str): The string to be analyzed.
    
    Returns:
    dict: A dictionary with words as keys and their exaggerated or actual counts as values.
    """
    # Splitting the input string into words
    words = input_string.split()
    
    # Dictionary to store word counts
    word_counts = {}
    
    for word in words:
        if len(word) == 3:
            # Exaggerating count by multiplying with 10 for 3-character words
            word_counts[word] = words.count(word) * 10
        else:
            # Using actual count for other words
            word_counts[word] = words.count(word)
    
    return word_counts

# Entry point of the script
if __name__ == "__main__":
    # Example input string
    example_input = "hello world this is a test test hello"
    
    # Calling the function with the example input
    result = exaggerated_word_counter(example_input)
    
    # Printing the result
    print(result)
```

This Python script defines a function `exaggerated_word_counter` that processes an input string to count the occurrences of each word, exaggerating the count by a factor of 10 for words with exactly three characters. The main part of the script demonstrates how to use this function with a sample input and prints the resulting dictionary of word counts.