import re
from typing import List

def split_into_sentences(text: str) -> List[str]:
    """
    Split text into sentences handling punctuation and quoted speech.

    Args:
        text (str): The email body as a plain string.

    Returns:
        List[str]: List of sentences.
    """
    # Regular expression to match sentence endings, considering quoted speech
    sentence_endings = re.compile(r'(?<=[.!?]) +(?=[\'"“])|(?<=[.!?]) +|(?<=\")[.!?] ')
    return sentence_endings.split(text)

def rewrite_sentence(sentence: str) -> str:
    """
    Rewrite a sentence to change tone halfway through.

    Args:
        sentence (str): A single sentence from the email.

    Returns:
        str: The rewritten sentence with shifted tone.
    """
    words = sentence.split()
    midpoint = len(words) // 2

    # Formal to informal shift
    formal_to_informal = {
        'we': 'you',
        'our': 'your',
        'please': '',
        'kindly': '',
        'request': 'ask',
        'inquire': 'ask',
        'investigate': 'check out'
    }

    # Informal to formal shift
    informal_to_formal = {
        'u': 'you',
        'ur': 'your',
        'ya': 'yes',
        'nah': 'no',
        'gonna': 'going to',
        'wanna': 'want to',
        'lol': '',
        'heh': ''
    }

    if len(words) > 4:
        if any(word in formal_to_informal for word in words[:midpoint]):
            # Shift from formal to informal
            new_words = [
                formal_to_informal.get(word, word) if i < midpoint else word
                for i, word in enumerate(words)
            ]
        elif any(word in informal_to_formal for word in words[:midpoint]):
            # Shift from informal to formal
            new_words = [
                informal_to_formal.get(word, word) if i < midpoint else word
                for i, word in enumerate(words)
            ]
        else:
            new_words = words
    else:
        new_words = words

    return ' '.join(new_words)

def rewrite_email(email_body: str) -> str:
    """
    Rewrite an email body to change tone halfway through each sentence.

    Args:
        email_body (str): The email body as a plain string.

    Returns:
        str: The fully rewritten email as a single string.
    """
    sentences = split_into_sentences(email_body)
    rewritten_sentences = [rewrite_sentence(sentence) for sentence in sentences]
    return ' '.join(rewritten_sentences)

if __name__ == "__main__":
    sample_email = """Dear Customer,

We have received your inquiry and are currently investigating the issue. Please allow us 24 hours to resolve this matter.

Thank you for your patience.
Best regards,
Support Team"""

    rewritten_email = rewrite_email(sample_email)
    print("Original Email:")
    print(sample_email)
    print("\nRewritten Email:")
    print(rewritten_email)

import unittest

class TestToneShiftingEmailRewriter(unittest.TestCase):
    def test_rewrite_formal_to_informal(self):
        input_text = "We are pleased to inform you that your request has been processed."
        expected_output = "you are pleased to inform you that your request has been processed."
        self.assertEqual(rewrite_sentence(input_text), expected_output)

    def test_rewrite_informal_to_formal(self):
        input_text = "hey man, ur stuff is ready, come pick it up"
        expected_output = "hey man, your stuff is ready, come pick it up"
        self.assertEqual(rewrite_sentence(input_text), expected_output)

if __name__ == "__main__":
    unittest.main()