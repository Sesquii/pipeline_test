import random
from typing import List, Tuple

# Pre-written expansion templates
EXPANSION_TEMPLATES: List[Tuple[str, str]] = [
    ("This concept", "is fundamentally a complex idea that requires deep exploration."),
    ("Such a statement", "entails profound implications, necessitating thorough examination."),
    ("The notion of", "represents an intricate principle demanding meticulous analysis."),
    ("A claim like this", "implies significant consequences warranting extensive discussion."),
    ("This topic", "delves into a sophisticated subject, deserving comprehensive scrutiny.")
]

def _get_random_template() -> Tuple[str, str]:
    return random.choice(EXPANSION_TEMPLATES)

def expand(sentence: str) -> str:
    """Expands the given sentence into an unnecessarily long essay.

    Args:
        sentence (str): The input sentence to be expanded.

    Returns:
        str: The expanded essay, which is at least five times longer than the input.
    """

    # Split sentence into words
    words = sentence.split()

    # Get a random expansion template
    prefix, suffix = _get_random_template()

    essay: List[str] = []
    num_words = len(words) * 5  # Ensure at least five times as many words

    for i in range(num_words - len(words)):
        word, next_word = words[-1], words[0] if i < len(words) - 1 else ''

        expanded_prefix, expanded_suffix = _expand_template(prefix, word, next_word)

        essay.append(f"{expanded_prefix} {word} {expanded_suffix}")

    return ' '.join(essay) + ' ' + suffix

def _expand_template(template: str, current_word: str, next_word: str) -> Tuple[str, str]:
    """Expands the given template based on the current and next words.

    Args:
        template (str): The expansion template to be used.
        current_word (str): The word preceding the place holder in the template.
        next_word (str): The word following the place holder in the template.

    Returns:
        Tuple[str, str]: The expanded prefix and suffix of the template.
    """

    if '{w1}' in template:
        template = template.replace('{w1}', current_word)
    if '{w2}' in template:
        template = template.replace('{w2}', next_word)

    # Randomly select between two variations to increase variance
    variations = [template, f"The {template}"]
    return random.choice(variations), template

if __name__ == "__main__":
    sample_sentence = "Python is a high-level programming language."
    expanded_essay = expand(sample_sentence)

    print("Original Sentence:")
    print(sample_sentence)

    print("\nExpanded Essay:")
    print(expanded_essay)

# ===== GENERATED TESTS =====
import pytest
from typing import List, Tuple

# Pre-written expansion templates
EXPANSION_TEMPLATES: List[Tuple[str, str]] = [
    ("This concept", "is fundamentally a complex idea that requires deep exploration."),
    ("Such a statement", "entails profound implications, necessitating thorough examination."),
    ("The notion of", "represents an intricate principle demanding meticulous analysis."),
    ("A claim like this", "implies significant consequences warranting extensive discussion."),
    ("This topic", "delves into a sophisticated subject, deserving comprehensive scrutiny.")
]

def _get_random_template() -> Tuple[str, str]:
    return random.choice(EXPANSION_TEMPLATES)

def expand(sentence: str) -> str:
    """Expands the given sentence into an unnecessarily long essay.

    Args:
        sentence (str): The input sentence to be expanded.

    Returns:
        str: The expanded essay, which is at least five times longer than the input.
    """

    # Split sentence into words
    words = sentence.split()

    # Get a random expansion template
    prefix, suffix = _get_random_template()

    essay: List[str] = []
    num_words = len(words) * 5  # Ensure at least five times as many words

    for i in range(num_words - len(words)):
        word, next_word = words[-1], words[0] if i < len(words) - 1 else ''

        expanded_prefix, expanded_suffix = _expand_template(prefix, word, next_word)

        essay.append(f"{expanded_prefix} {word} {expanded_suffix}")

    return ' '.join(essay) + ' ' + suffix

def _expand_template(template: str, current_word: str, next_word: str) -> Tuple[str, str]:
    """Expands the given template based on the current and next words.

    Args:
        template (str): The expansion template to be used.
        current_word (str): The word preceding the place holder in the template.
        next_word (str): The word following the place holder in the template.

    Returns:
        Tuple[str, str]: The expanded prefix and suffix of the template.
    """

    if '{w1}' in template:
        template = template.replace('{w1}', current_word)
    if '{w2}' in template:
        template = template.replace('{w2}', next_word)

    # Randomly select between two variations to increase variance
    variations = [template, f"The {template}"]
    return random.choice(variations), template

# Test cases for the expand function
@pytest.fixture(scope="module")
def sample_sentence() -> str:
    """Sample sentence to be used in test cases."""
    return "Python is a high-level programming language."

@pytest.mark.parametrize("sentence", [
    ("This concept"),
    ("Such a statement"),
    ("The notion of"),
    ("A claim like this"),
    ("This topic")
])
def test_expand_positive(sentence: str, sample_sentence: str):
    """Test the expand function with positive cases."""
    expanded_essay = expand(sentence)
    assert len(expanded_essay.split()) >= len(sample_sentence.split()) * 5
    assert sentence in expanded_essay

@pytest.mark.parametrize("sentence", [
    (""),
    (" "),
    ("12345"),
    ("!@#$%")
])
def test_expand_negative(sentence: str):
    """Test the expand function with negative cases."""
    with pytest.raises(ValueError):
        expand(sentence)

# Test cases for the _expand_template function
@pytest.mark.parametrize("template, current_word, next_word", [
    ("This concept {w1}", "Python", "is"),
    ("Such a statement {w2}", "a", "high-level"),
    ("The notion of {w1} {w2}", "programming", "language")
])
def test_expand_template_positive(template: str, current_word: str, next_word: str):
    """Test the _expand_template function with positive cases."""
    expanded_prefix, expanded_suffix = _expand_template(template, current_word, next_word)
    assert '{w1}' not in expanded_prefix
    assert '{w2}' not in expanded_suffix

@pytest.mark.parametrize("template, current_word, next_word", [
    ("This concept {w3}", "Python", "is"),
    ("Such a statement {w4}", "a", "high-level"),
    ("The notion of {w5} {w6}", "programming", "language")
])
def test_expand_template_negative(template: str, current_word: str, next_word: str):
    """Test the _expand_template function with negative cases."""
    with pytest.raises(KeyError):
        _expand_template(template, current_word, next_word)

This test suite includes both positive and negative test cases for the `expand` and `_expand_template` functions. It uses pytest fixtures and parametrization to ensure comprehensive coverage of different scenarios. The test cases are designed to follow PEP 8 style guidelines and include proper docstrings and comments.