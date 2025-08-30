```python
import random

def misspell_word(word):
    """Misspells a word starting with uppercase by replacing one vowel with a consonant."""
    if not word[0].isupper():
        return word
    
    vowels = [c for c in word if c in 'aeiou']
    if not vowels:
        return word  # No vowels to replace, leave as is
    
    selected_vowel = random.choice(vowels)
    indices = [i for i, c in enumerate(word) if c == selected_vowel]
    idx = random.choice(indices)
    
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    replaced_char = random.choice(consonants)
    
    new_word = word[:idx] + replaced_char + word[idx+1:]
    return new_word

def correct_case(word):
    """Corrects the case of a word, making the first letter uppercase."""
    return word[0].upper() + word[1:]

def main():
    """Main function to process input and output files."""
    import sys
    if len(sys.argv) != 3:
        print("Usage: python BATCH7_PROMPT8_{{model_name}}.py <input_file> <output_file>")
        return
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    with open(input_file, 'r') as infile:
        lines = infile.readlines()
    
    with open(output_file, 'w') as outfile:
        for line in lines:
            words = line.strip().split()
            processed_words = []
            
            for word in words:
                if word and word[0].isupper():
                    processed_word = misspell_word(word)
                    corrected = correct_case(processed_word)
                    processed_words.append(corrected)
                else:
                    processed_words.append(word)
            
            outfile.write(' '.join(processed_words) + '\n')

if __name__ == "__main__":
    main()

# ===== GENERATED TESTS =====
```python
import pytest

# Original script code remains unchanged above this line

def test_misspell_word():
    """Test the misspell_word function."""
    assert misspell_word("Apple") == "Applc"  # Vowel replaced with consonant
    assert misspell_word("Banana") == "Bnna"  # Vowel replaced with consonant
    assert misspell_word("Cherry") == "Chrry"  # No vowels, should remain unchanged
    assert misspell_word("Dog") == "Dg"  # No vowels, should remain unchanged

def test_correct_case():
    """Test the correct_case function."""
    assert correct_case("apple") == "Apple"
    assert correct_case("banana") == "Banana"
    assert correct_case("cherry") == "Cherry"

def test_main(tmp_path):
    """Test the main function with a temporary file."""
    input_file = tmp_path / 'input.txt'
    output_file = tmp_path / 'output.txt'

    # Create input file
    input_content = "apple banana cherry\n"
    input_file.write_text(input_content)

    # Run main function
    import subprocess
    subprocess.run(['python', str(__file__), str(input_file), str(output_file)], check=True)

    # Check output file
    expected_output = "Applc Bnna Chrry\n"
    assert output_file.read_text() == expected_output

# Add more test cases as needed
```