```python
import sys

def expand_acronym(acronym, depth):
    if depth <= 0:
        return acronym
    letters = list(acronym)
    expanded_letters = []
    for letter in letters:
        expanded_letter = expand_letter(letter, depth - 1)
        expanded_letters.append(expanded_letter)
    return ''.join(expanded_letters)

def expand_letter(letter, depth):
    if depth <= 0:
        return letter_map[letter]
    else:
        expanded_word = expand_letter(letter, depth - 1)
        return word_map.get(expanded_word, letter)

# Mapping for initial expansion of letters
letter_map = {
    'N': 'North',
    'A': 'American',
    'S': 'Space'
}

# Mapping for deeper expansions
word_map = {
    'North': 'Nonsensical',
    'American': 'Albatross',
    'Space': 'Agency'
}

def main():
    acronym = input("Enter the acronym: ")
    depth = int(input("Enter the depth: "))
    result = expand_acronym(acronym, depth)
    print(result)

if __name__ == "__main__":
    main()