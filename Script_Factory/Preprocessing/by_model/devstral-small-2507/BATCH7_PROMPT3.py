import re

def get_phonetically_similar_vowel(vowel):
    """Return a phonetically similar vowel based on simple rules."""
    similar_vowels = {
        'a': 'e',
        'e': 'i',
        'i': 'o',
        'o': 'u',
        'u': 'a'
    }
    return similar_vowels.get(vowel, vowel)

def misspell_word(word):
    """Purposefully misspell a word by replacing one vowel with a phonetically similar vowel."""
    vowels = "aeiou"
    for char in word:
        if char.lower() in vowels:
            similar_vowel = get_phonetically_similar_vowel(char.lower())
            # Preserve case
            if char.isupper():
                similar_vowel = similar_vowel.upper()
            return word.replace(char, similar_vowel)
    return word  # No vowels to replace

def correct_spelling(word):
    """Attempt to correct spelling using simple phonetic rules."""
    vowels = "aeiou"
    for char in word:
        if char.lower() in vowels:
            corrected_vowel = get_phonetically_similar_vowel(char.lower())
            # Preserve case 
            if char.isupper():
                corrected_vowel = corrected_vowel.upper()
            return word.replace(char, corrected_vowel)
    return word  # No vowels to correct

def process_text(text):
    """Process the input text by misspelling and correcting words."""
    words = re.findall(r'\w+|[^\w\s]', text)  # Split into words and punctuation
    for i in range(len(words)):
        if i % 3 == 2:  # Every third word (0-based index)
            original_word = words[i]
            misspelled_word = misspell_word(original_word)
            corrected_word = correct_spelling(misspelled_word)

            print(f"Original: {original_word}")
            print(f"Misspelled: {misspelled_word}")
            print(f"Corrected: {corrected_word}\n")

            words[i] = misspelled_word  # Replace with misspelled version

    corrected_text = ''.join(words)
    return corrected_text

if __name__ == "__main__":
    input_text = "This is a simple test to demonstrate the self correcting spelling bot."
    print("Original text:")
    print(input_text)

    processed_text = process_text(input_text)
    print("\nProcessed text with misspellings and corrections:")
    print(processed_text)