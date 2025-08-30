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