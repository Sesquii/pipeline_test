import random
from spellchecker import SpellChecker

# Function to misspell words and save to typos.txt
def create_typos(input_file, typo_file):
    spell = SpellChecker()
    with open(input_file, 'r') as file:
        text = file.read()
    
    words = text.split()
    misspelled = spell.unknown(words)
    if len(misspelled) < 10:
        raise ValueError("Not enough unique misspellings found in the input file.")
    
    typo_indices = random.sample(range(len(misspelled)), 10)
    typos = [(words.index(word), word, random.choice(list(spell.known(word)))) for idx, word in enumerate(words) if idx in typo_indices]
    
    with open(typo_file, 'w') as typo:
        typo.write(text)
    
    return typos

# Function to correct typos and save to fixed_text.txt
def fix_typos(typo_file, fixed_file):
    spell = SpellChecker()
    with open(typo_file, 'r') as file:
        text = file.read()
    
    words = text.split()
    for typo in typos:
        word_index = typo[0]
        wrong_word = typo[1]
        corrected_word = typo[2]
        words[word_index] = corrected_word
    
    fixed_text = ' '.join(words)
    with open(fixed_file, 'w') as fixed:
        fixed.write(fixed_text)

# Function to log errors and corrections
def log_errors(typos, log_file):
    with open(log_file, 'w') as log:
        for typo in typos:
            original_word = typo[1]
            corrected_word = typo[2]
            log.write(f"Original: {original_word}, Corrected: {corrected_word}\n")

# Main function
if __name__ == "__main__":
    input_file = 'input.txt'
    typo_file = 'typos.txt'
    fixed_file = 'fixed_text.txt'
    log_file = 'log.txt'
    
    try:
        typos = create_typos(input_file, typo_file)
        fix_typos(typo_file, fixed_file)
        log_errors(typos, log_file)
        print("Spelling corrections have been made and logged.")
    except Exception as e:
        print(f"An error occurred: {e}")

This Python script implements a "Self-Correcting Spelling Bot" with the specified requirements. It uses the `SpellChecker` library from the `spellchecker` package to identify misspellings, randomly selects 10 words to misspell, saves the original text with typos to `typos.txt`, corrects these typos, and logs the corrections in `log.txt`. The main function handles the workflow and error handling.

# ===== GENERATED TESTS =====
import pytest
from spellchecker import SpellChecker

# Test fixture to create a temporary input file for testing
@pytest.fixture
def temp_input_file(tmp_path):
    input_text = "This is a test sentence with some misspellings."
    input_file = tmp_path / 'input.txt'
    with open(input_file, 'w') as file:
        file.write(input_text)
    return input_file

# Test fixture to create temporary files for testing
@pytest.fixture(params=[
    ('typos.txt', 'fixed_text.txt', 'log.txt'),
    ('typos2.txt', 'fixed_text2.txt', 'log2.txt')
])
def temp_files(tmp_path, request):
    typo_file, fixed_file, log_file = [tmp_path / f for f in request.param]
    return typo_file, fixed_file, log_file

# Test function to check if create_typos works correctly
def test_create_typos(temp_input_file, temp_files):
    typo_file, _, _ = temp_files
    typos = create_typos(str(temp_input_file), str(typo_file))
    
    assert len(typos) == 10, "Should select 10 misspellings"
    for typo in typos:
        assert isinstance(typo, tuple), "Each typo should be a tuple"
        assert len(typo) == 3, "Each typo tuple should have 3 elements"

# Test function to check if fix_typos works correctly
def test_fix_typos(temp_files):
    typo_file, fixed_file, _ = temp_files
    
    # Create typos in the typo file
    create_typos('input.txt', str(typo_file))
    
    # Fix typos and save to fixed_file
    fix_typos(str(typo_file), str(fixed_file))
    
    with open(fixed_file, 'r') as file:
        fixed_text = file.read()
    
    assert "This is a test sentence with some misspellings." in fixed_text, "Fixed text should contain the original sentence"

# Test function to check if log_errors works correctly
def test_log_errors(temp_files):
    typo_file, _, log_file = temp_files
    
    # Create typos in the typo file
    create_typos('input.txt', str(typo_file))
    
    # Log errors and corrections
    typos = create_typos('input.txt', str(typo_file))
    log_errors(typos, str(log_file))
    
    with open(log_file, 'r') as file:
        log_content = file.read()
    
    assert "Original:" in log_content and "Corrected:" in log_content, "Log should contain original and corrected words"

# Test function to check if create_typos raises an error when not enough unique misspellings are found
def test_create_typos_not_enough_misspellings(temp_input_file):
    with pytest.raises(ValueError) as exc_info:
        create_typos(str(temp_input_file), 'typos.txt')
    
    assert "Not enough unique misspellings found in the input file." in str(exc_info.value)

# Test function to check if fix_typos handles missing typo file
def test_fix_typos_missing_typo_file(temp_files):
    typo_file, fixed_file, _ = temp_files
    
    with pytest.raises(FileNotFoundError) as exc_info:
        fix_typos(str(typo_file), str(fixed_file))
    
    assert "No such file or directory" in str(exc_info.value)

# Test function to check if log_errors handles missing typo list
def test_log_errors_missing_typo_list(temp_files):
    typo_file, _, log_file = temp_files
    
    with pytest.raises(TypeError) as exc_info:
        log_errors(None, str(log_file))
    
    assert "NoneType object is not iterable" in str(exc_info.value)
