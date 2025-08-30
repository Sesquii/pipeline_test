import sys

def is_palindrome(word):
    """Check if a word is a palindrome."""
    return word == word[::-1]

def translate_to_emoji(word):
    """Translate each character of a palindromic word to an emoji."""
    char_to_emoji = {
        'a': '🍎', 'b': '🐦', 'c': '🌈', 'd': '🐶', 'e': '🐧',
        'f': '🍃', 'g': '🦄', 'h': '🍭', 'i': '🌺', 'j': '🐬',
        'k': '🐯', 'l': '🌴', 'm': '🍃', 'n': '🐢', 'o': '🍊',
        'p': '🦋', 'q': '🦅', 'r': '🌹', 's': '🌟', 't': '🍄',
        'u': '🌈', 'v': '🦋', 'w': '🐋', 'x': '✨', 'y': '🦄',
        'z': '🌺'
    }
    return ''.join(char_to_emoji.get(c.lower(), c) for c in word)

def translate_text(text):
    """Translate palindromic words in text to emojis."""
    words = text.split()
    translated_words = [
        translate_to_emoji(word) if is_palindrome(word) else word
        for word in words
    ]
    return ' '.join(translated_words)

if __name__ == "__main__":
    # Example usage
    input_text = "madam racecar level hello world"
    output_text = translate_text(input_text)
    print(output_text)