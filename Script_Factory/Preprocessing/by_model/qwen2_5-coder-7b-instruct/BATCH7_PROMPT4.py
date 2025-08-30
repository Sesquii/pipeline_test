import random

def misspell(string):
    """
    Misspell every 5th word by appending a random non-alphabetic character.
    
    :param string: Input string to misspell
    :return: Misspelled string
    """
    words = string.split()
    for i in range(4, len(words), 5):  # Start from index 4 (5th word) and increment by 5
        if words[i].isalpha():  # Ensure the word is alphabetic
            random_char = chr(random.randint(33, 47)) + chr(random.randint(58, 64)) + chr(random.randint(91, 96)) + chr(random.randint(123, 126))
            words[i] += random_char
    return ' '.join(words)

def correct(spelled_string):
    """
    Correct the spelling by removing the extra characters.
    
    :param spelled_string: Spelled string with extra characters
    :return: Corrected string
    """
    corrected = ''
    for char in spelled_string:
        if not (char >= '!' and char <= '/') and not (char >= ':' and char <= '@') and not (char >= '[' and char <= '`') and not (char >= '{' and char <= '~'):
            corrected += char
    return corrected

def self_correcting_bot(input_string):
    """
    Implement a Self-Correcting Spelling Bot with a circular correction system.
    
    :param input_string: Input string to be misspelled and then corrected
    """
    for _ in range(3):  # Loop for 3 iterations
        misspelled = misspell(input_string)
        print(f"Iteration {_ + 1}: Misspelled -> {misspelled}")
        corrected = correct(misspelled)
        input_string = corrected

if __name__ == "__main__":
    input_string = "This is a test string to demonstrate the self-correcting spelling bot."
    self_correcting_bot(input_string)