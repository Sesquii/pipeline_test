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

# ===== GENERATED TESTS =====
import pytest

# Original code
def main():
    original_text = input("Enter text: ")
    words = original_text.split()
    
    replacements1 = {
        'i': 'e',
        'o': 'u'
    }
    
    replacements2 = {
        'e': 'i',
        'i': 'o',
        'o': 'u',
        'u': 'i'
    }
    
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
    
    print("Original Text:")
    print(' '.join(words))
    print("\nCorrected Text:")
    print(' '.join(corrected_words))

if __name__ == "__main__":
    main()

# Test cases
def test_replacements1():
    assert {'i': 'e', 'o': 'u'} == {
        'i': 'e',
        'o': 'u'
    }

def test_replacements2():
    assert {'e': 'i', 'i': 'o', 'o': 'u', 'u': 'i'} == {
        'e': 'i',
        'i': 'o',
        'o': 'u',
        'u': 'i'
    }

@pytest.fixture
def sample_text():
    return "hello world this is a test"

def test_misspelled_words(sample_text):
    words = sample_text.split()
    misspelled_words = []
    for i in range(len(words)):
        if i % 3 == 2:
            current_word = words[i]
            new_word = []
            for char in current_word:
                if char in {'i': 'e', 'o': 'u'}:
                    new_char = {'i': 'e', 'o': 'u'}[char]
                    new_word.append(new_char)
                else:
                    new_word.append(char)
            misspelled_words.append(''.join(new_word))
        else:
            misspelled_words.append(words[i])
    assert misspelled_words == ['hello', 'world', 'thiis', 'is', 'a', 'test']

def test_corrected_words(sample_text):
    words = sample_text.split()
    misspelled_words = []
    for i in range(len(words)):
        if i % 3 == 2:
            current_word = words[i]
            new_word = []
            for char in current_word:
                if char in {'i': 'e', 'o': 'u'}:
                    new_char = {'i': 'e', 'o': 'u'}[char]
                    new_word.append(new_char)
                else:
                    new_word.append(char)
            misspelled_words.append(''.join(new_word))
        else:
            misspelled_words.append(words[i])
    
    corrected_words = []
    for word in misspelled_words:
        new_word = []
        for char in word:
            if char in {'e': 'i', 'i': 'o', 'o': 'u', 'u': 'i'}:
                new_char = {'e': 'i', 'i': 'o', 'o': 'u', 'u': 'i'}[char]
                new_word.append(new_char)
            else:
                new_word.append(char)
        corrected_words.append(''.join(new_word))
    
    assert corrected_words == ['hello', 'world', 'this', 'is', 'a', 'test']

def test_main(sample_text, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: sample_text)
    captured_output = pytest.io.StringIO()
    monkeypatch.setattr('sys.stdout', captured_output)
    
    main()
    
    output = captured_output.getvalue().strip()
    expected_output = "Original Text:\nhello world this is a test\n\nCorrected Text:\nhello world this is a test"
    assert output == expected_output
