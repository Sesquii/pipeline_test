import random

# Hard-coded dictionary of English words and their made-up equivalents
TRANSLATION_DICT = {
    'hello': 'zorp',
    'world': 'flurb',
    'programming': 'klatch',
    'is': 'gork',
    'fun': 'bliv',
    'python': 'pytho',
    'code': 'kode',
    'development': 'devel',
    'software': 'softa',
    'engineer': 'enjin',
    'computer': 'compy',
    'science': 'scien',
    'technology': 'techno',
    'algorithm': 'algor',
    'data': 'datum',
    'structure': 'struct',
    'network': 'networ',
    'system': 'syso',
    'design': 'desig',
    'analysis': 'analy'
}

def translate_sentence(sentence):
    """Translate an English sentence into the made-up language."""
    words = sentence.split()
    translated_words = []

    for word in words:
        # Remove punctuation from the end of the word
        cleaned_word = word.strip('.,!?')
        if cleaned_word.lower() in TRANSLATION_DICT:
            translated_words.append(TRANSLATION_DICT[cleaned_word.lower()])
        else:
            translated_words.append(word)

    return ' '.join(translated_words)

def introduce_spelling_errors(word):
    """Introduce random spelling errors by swapping letters."""
    if len(word) < 2:
        return word

    # Create a copy of the word to modify
    error_word = list(word)
    
    # Randomly choose two different positions in the word
    pos1, pos2 = random.sample(range(len(word)), 2)
    
    # Swap the characters at these positions
    error_word[pos1], error_word[pos2] = error_word[pos2], error_word[pos1]
    
    return ''.join(error_word)

def correct_spelling(erroneous_sentence):
    """Correct spelling errors by replacing corrupted words with correct translations."""
    words = erroneous_sentence.split()
    corrected_words = []

    for word in words:
        # Check if the word with any single letter swapped matches a translation
        found_match = False
        for original_word, translated_word in TRANSLATION_DICT.items():
            if len(word) == len(translated_word):
                # Count how many letters match
                matches = sum(1 for w1, w2 in zip(word, translated_word) if w1 == w2)
                if matches >= len(word) - 1:  # Allow for one letter to be wrong
                    corrected_words.append(translated_word)
                    found_match = True
                    break

        if not found_match:
            corrected_words.append(word)

    return ' '.join(corrected_words)

def main():
    """Main entry point for the Self-Correcting Spelling Bot."""
    # Example input sentence
    english_sentence = "Hello world! Programming is fun with Python."

    # Step 1: Translate the sentence into the made-up language
    translated_sentence = translate_sentence(english_sentence)
    print(f"Translated Sentence: {translated_sentence}")

    # Step 2: Introduce spelling errors
    words = translated_sentence.split()
    erroneous_words = [introduce_spelling_errors(word) for word in words]
    erroneous_sentence = ' '.join(erroneous_words)
    print(f"Erroneous Sentence: {erroneous_sentence}")

    # Step 3: Correct the spelling errors
    corrected_sentence = correct_spelling(erroneous_sentence)
    print(f"Corrected Sentence: {corrected_sentence}")

if __name__ == "__main__":
    main()