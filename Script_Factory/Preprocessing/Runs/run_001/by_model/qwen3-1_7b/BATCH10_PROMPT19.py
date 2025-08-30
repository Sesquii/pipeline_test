```python
import sys

corrections = {
    'run': ['rung'],
    'spill': ['sailed'],
    'sail': ['sails']
}

def correct_word(word):
    if word in corrections:
        return corrections[word][0]
    else:
        return word

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python BATCH10_PROMPT19_{{model_name}}.py <word>")
        sys.exit(1)
    word = sys.argv[1]
    corrected_word = correct_word(word)
    print(corrected_word)