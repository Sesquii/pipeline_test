```python
def main():
    original_text = input("Enter text: ")
    words = original_text.split()
    
    # First replacement mapping for misspellings (i→e, o→u)
    replacements1 = {
        'i': 'e',
        'o': 'u'
    }
    
    # Second replacement mapping for correction (e→i, i→o, o→u, u→i)
    replacements2 = {
        'e': 'i',
        'i': 'o',
        'o': 'u',
        'u': 'i'
    }
    
    # Process first misspellings
    misspelled_words = []
    for i in range(len(words)):
        if i % 3 == 2:
            current_word = words[i]
            new_word = []
            for char in current_word:
                if char in replacements1:
                    new_char = replacements1[char]
                    new_word.append(new_char)
                else:
                    new_word.append(char)
            misspelled_words.append(''.join(new_word))
        else:
            misspelled_words.append(words[i])
    
    # Apply correction to all words
    corrected_words = []
    for word in misspelled_words:
        new_word = []
        for char in word:
            if char in replacements2:
                new_char = replacements2[char]
                new_word.append(new_char)
            else:
                new_word.append(char)
        corrected_words.append(''.join(new_word))
    
    # Print original and corrected texts with highlighting
    print("Original Text:")
    print(' '.join(words))
    print("\nCorrected Text:")
    print(' '.join(corrected_words))

if __name__ == "__main__":
    main()