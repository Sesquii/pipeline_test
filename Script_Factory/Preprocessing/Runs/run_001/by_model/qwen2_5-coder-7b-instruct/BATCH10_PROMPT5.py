# BATCH10_PROMPT5_python_emoji_palindromes.py

def is_palindrome(word):
    """
    Check if a given word is a palindrome.
    
    :param word: str - The word to check.
    :return: bool - True if the word is a palindrome, False otherwise.
    """
    return word == word[::-1]

def translate_to_emoji(word):
    """
    Translate an English word into its emoji representation.
    
    :param word: str - The word to translate.
    :return: str - The emoji representation of the word.
    """
    # Mapping of letters to their corresponding emojis
    letter_to_emoji = {
        'a': '😊', 'b': '👍', 'c': '🎉', 'd': 'DOMContentLoaded',
        'e': '➡️', 'f': '❌', 'g': '🍇', 'h': '🐎', 'i': '😉',
        'j': 'jpeg', 'k': 'keyup', 'l': 'localStorage', 'm': 'mousedown',
        'n': 'mouseover', 'o': 'onclick', 'p': 'parent', 'q': 'querySelector',
        'r': 'removeEventListener', 's': 'submit', 't': 'target', 'u': 'undefined',
        'v': 'valueOf', 'w': 'window', 'x': 'xmlhttprequest', 'y': 'youtube',
        'z': 'zero'
    }
    
    # Translate each letter in the word to its corresponding emoji
    return ''.join(letter_to_emoji.get(char, char) for char in word)

def main():
    """
    Entry point of the program.
    """
    input_text = "madam"
    if is_palindrome(input_text):
        print(translate_to_emoji(input_text))
    else:
        print("The word is not a palindrome.")

if __name__ == "__main__":
    main()