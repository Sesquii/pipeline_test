def exaggerated_word_counter(input_string):
    """
    Counts the occurrences of each word in the input string. If a word has a length of exactly 3 characters,
    its count is reported as 10 times the actual number.
    
    :param input_string: A string containing words separated by spaces.
    :return: A dictionary with words as keys and their exaggerated counts as values.
    """
    # Split the input string into words
    words = input_string.split()
    
    # Initialize an empty dictionary to store word counts
    word_counts = {}
    
    # Count occurrences of each word, applying exaggeration for 3-character words
    for word in words:
        if len(word) == 3:
            count = words.count(word)
            word_counts[word] = count * 10
        else:
            word_counts[word] = words.count(word)
    
    return word_counts

if __name__ == "__main__":
    # Example input string
    input_string = "hello world hi hello"
    # Call the function and print the result
    result = exaggerated_word_counter(input_string)
    print(result)
```

This Python script defines a function `exaggerated_word_counter` that processes an input string to count word occurrences, applying a 10x exaggeration for words of exactly 3 characters. The main block demonstrates how to use this function with an example input string.