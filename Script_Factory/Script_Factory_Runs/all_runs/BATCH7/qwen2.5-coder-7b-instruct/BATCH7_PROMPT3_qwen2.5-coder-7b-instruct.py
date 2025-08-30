def phonetic_spelling_bot(text):
    # Define a mapping of vowels to phonetically similar vowels
    vowel_mapping = {'i': 'e', 'o': 'u', 'a': 'e'}
    
    words = text.split()
    corrected_words = []
    
    for i, word in enumerate(words):
        if (i + 1) % 3 == 0:
            # Misspell the word by replacing a vowel with a phonetically similar one
            misspelled_word = ''.join(vowel_mapping.get(char, char) if char.lower() in vowel_mapping else char for char in word)
            corrected_words.append(misspelled_word)
        else:
            corrected_words.append(word)
    
    # Join the words back into a single string
    corrected_text = ' '.join(corrected_words)
    
    return text, corrected_text

def main():
    input_text = "This is an example sentence with some misspellings"
    original_text, corrected_text = phonetic_spelling_bot(input_text)
    
    print("Original Text:", original_text)
    print("Corrected Text:", corrected_text)

if __name__ == "__main__":
    main()