import random

# Function to introduce typos by misspelling words
def introduce_typos(text, num_typos=10):
    words = text.split()
    typo_indices = random.sample(range(len(words)), min(num_typos, len(words)))

    for index in typo_indices:
        word = words[index]
        if len(word) > 2:  # Don't mess with short words
            typo_word = word[:random.randint(1, len(word)-1)] + ''.join(random.sample(word[random.randint(1, len(word)-1):], len(word)-random.randint(1, len(word)-1)))
            words[index] = typo_word

    return ' '.join(words)

# Function to correct typos (simple implementation - just revert changes)
def correct_typos(text):
    # In a real scenario, this would use spell-checking libraries
    # For simplicity, we'll assume the original text is available and use it as reference
    with open('original_text.txt', 'r') as f:
        original_text = f.read()

    original_words = set(original_text.split())
    words = text.split()
    corrected_words = []

    for word in words:
        if word not in original_words:  # If word is misspelled (not in original)
            # Simple correction: find the closest match from original
            correct_word = min(original_words, key=lambda x: (len(x) == len(word), sum(a != b for a, b in zip(x, word))))
            corrected_words.append(correct_word)
        else:
            corrected_words.append(word)

    return ' '.join(corrected_words)

def main():
    # Read original text
    with open('original_text.txt', 'r') as f:
        original_text = f.read()

    # Introduce typos and save to typos.txt
    typo_text = introduce_typos(original_text)
    with open('typos.txt', 'w') as f:
        f.write(typo_text)

    # Correct typos and save to fixed_text.txt
    corrected_text = correct_typos(typo_text)
    with open('fixed_text.txt', 'w') as f:
        f.write(corrected_text)

    # Log the number of errors found and corrected
    error_count = sum(1 for a, b in zip(original_text.split(), typo_text.split()) if a != b)
    with open('log.txt', 'w') as f:
        f.write(f'Errors found and corrected: {error_count}\n')

if __name__ == "__main__":
    main()