import random
import string

# Hard-coded dictionary of English words and their "translated" made-up equivalents
TRANSLATION_DICT = {
    'hello': 'zorp', 'world': 'lyth', 'is': 'es', 'a': 'ix', 'program': 'xibro', 
    'python': 'yzonp', 'bot': 'kobt', 'self-correcting': 'xesl-cexorcti'
}

def introduce_spelling_errors(sentence):
    """Introduce spelling errors by randomly swapping a letter in each "translated" word."""
    words = sentence.split()
    erroneous_words = []

    for word in words:
        if word in TRANSLATION_DICT.values():
            new_word = list(word)
            for i in range(len(new_word)):
                # Randomly select two different letters (including the current one) to swap
                swap_with = random.choice([c for c in string.ascii_lowercase if c != new_word[i]])
                while swap_with == new_word[i]:
                    swap_with = random.choice([c for c in string.ascii_lowercase if c != new_word[i]]):
                
                new_word[i], new_word[random.randint(0, len(new_word) - 1)] = new_word[random.randint(0, len(new_word) - 1)], new_word[i]
            erroneous_words.append(''.join(new_word))
        else:
            erroneous_words.append(word)
    
    return ' '.join(erroneous_words)

def correct_spelling(erroneous_sentence):
    """Correct spelling errors by replacing corrupted "translated" words with their correct equivalents."""
    words = erroneous_sentence.split()
    corrected_words = []

    for word in words:
        if word in TRANSLATION_DICT and word not in TRANSLATION_DICT[word]:
            corrected_words.append(TRANSLATION_DICT[word])
        else:
            corrected_words.append(word)
    
    return ' '.join(corrected_words)

def main():
    # Get user input
    sentence = input("Enter an English sentence: ")

    # Translate to made-up language
    translated_sentence = ' '.join([TRANSLATION_DICT[word] if word in TRANSLATION_DICT else word for word in sentence.split()])
    
    print(f"Translated Sentence: {translated_sentence}")

    # Introduce spelling errors
    erroneous_sentence = introduce_spelling_errors(translated_sentence)
    print(f"Sentence with Introduced Errors: {erroneous_sentence}")

    # Correct spelling errors
    corrected_sentence = correct_spelling(erroneous_sentence)
    print(f"Corrected Sentence: {corrected_sentence}")

if __name__ == "__main__":
    main()