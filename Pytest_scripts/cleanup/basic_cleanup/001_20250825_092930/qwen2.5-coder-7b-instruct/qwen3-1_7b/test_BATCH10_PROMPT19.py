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

# ===== GENERATED TESTS =====
import pytest

# Original script remains unchanged

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

# Test suite starts here

def test_correct_word_positive():
    """Test case for correct_word with a known correction"""
    assert correct_word('run') == 'rung'
    assert correct_word('spill') == 'sailed'
    assert correct_word('sail') == 'sails'

def test_correct_word_negative():
    """Test case for correct_word with a non-existent word"""
    assert correct_word('unknown') == 'unknown'

def test_correct_word_empty_string():
    """Test case for correct_word with an empty string"""
    assert correct_word('') == ''

def test_correct_word_none_input():
    """Test case for correct_word with None input"""
    with pytest.raises(TypeError):
        correct_word(None)

# Using fixtures and parametrization

@pytest.fixture(params=['run', 'spill', 'sail'])
def word(request):
    return request.param

@pytest.mark.parametrize("correction", ['rung', 'sailed', 'sails'])
def test_correct_word_with_fixture(word, correction):
    """Test case for correct_word using fixture and parametrization"""
    assert correct_word(word) == correction
