import re
from typing import Dict, Tuple
import unittest


def shift_tone(sentence: str) -> Tuple[str, str]:
    """
    Shifts tone halfway through a sentence.

    Args:
        sentence (str): The input sentence to rewrite.

    Returns:
        Tuple[str, str]: A tuple containing the formal and informal parts of the rewritten sentence.
    """
    # Define simple rules for tone shifting
    formality_dict: Dict[str, str] = {
        "you": "u",  # Informal
        "we": "us",  # Formal
        "Mr.": "dude",  # Informal
        "Ms.": "lady",  # Informal
        "Dr.": "doc",  # Informal
    }

    # Split sentence into words
    words = re.findall(r'\b\w+\b', sentence)

    formal_part, informal_part = [], []

    for word in words:
        if len(formal_part) <= len(words) // 2:
            formal_part.append(formality_dict.get(word, word))
        else:
            informal_part.append(formality_dict.get(word, word))

    return ' '.join(formal_part), ' '.join(informal_part)


def rewrite_email(body: str) -> str:
    """
    Rewrites an email body with tone shifts in each sentence.

    Args:
        body (str): The input email body as a plain string.

    Returns:
        str: The fully rewritten email body.
    """
    sentences = re.split('(?<=[.!?]) +', body)
    rewritten_sentences = []

    for sentence in sentences:
        if not sentence.strip():
            continue

        formal, informal = shift_tone(sentence)
        rewritten_sentences.append(f"{formal} {informal}")

    return ' '.join(rewritten_sentences)


if __name__ == "__main__":
    sample_email = """
    Dear Mr. Smith,

    We are writing to inform you about the upcoming changes in our policy. This is a significant update that we believe will greatly benefit your experience with us.

    Best regards,
    The Management Team.
    """
    print(rewrite_email(sample_email))


class TestRewriteEmail(unittest.TestCase):

    def test_shift_tone(self):
        formal, informal = shift_tone("Dr. Smith is a renowned expert.")
        self.assertIn("doc", informal)

        formal, informal = shift_tone("You are invited to our event.")
        self.assertIn("u", informal)

    def test_rewrite_email(self):
        email = "Dear Dr. Johnson,\nWe're happy to invite you to our meeting today.\nBest regards,\nThe Team."
        rewritten = rewrite_email(email)
        self.assertIn("doc is a renowned expert", rewritten)
        self.assertIn("u are invited to our meeting", rewritten)

if __name__ == '__main__':
    unittest.main()