import re

def rewrite_tone(sentence):
    """
    Rewrite the tone of a sentence halfway through.
    
    Parameters:
    - sentence: A single sentence as a string.
    
    Returns:
    - The rewritten sentence with changed tone.
    """
    # Simple rule set for tone shift
    formal_words = {'we': 'you', 'us': 'your'}
    informal_words = {'you': 'we', 'your': 'us'}
    
    words = re.findall(r'\b\w+\b', sentence)
    mid_point = len(words) // 2
    
    # Rewrite the second half of the sentence
    for i in range(mid_point, len(words)):
        if words[i] in formal_words:
            words[i] = informal_words[words[i]]
        elif words[i] in informal_words:
            words[i] = formal_words[words[i]]
    
    return ' '.join(words)

def rewrite_email(email_body: str) -> str:
    """
    Rewrite the tone of an entire email body.
    
    Parameters:
    - email_body: The email body as a plain string.
    
    Returns:
    - The fully rewritten email with changed tones in each sentence.
    """
    sentences = re.split(r'(?<=[.!?]) +', email_body)
    rewritten_sentences = [rewrite_tone(sentence) for sentence in sentences]
    return ' '.join(rewritten_sentences)

if __name__ == "__main__":
    sample_email = "We are writing to you today to inform you about the changes we have made."
    print(rewrite_email(sample_email))

import unittest

class TestToneShiftingEmailRewriter(unittest.TestCase):
    def test_rewrite_tone(self):
        self.assertEqual(rewrite_tone("We are going to meet tomorrow."), "We are going to meet tomorrow.")
        self.assertEqual(rewrite_tone("You should come with us."), "We should come with you.")

    def test_rewrite_email(self):
        sample_email = "We are writing to you today to inform you about the changes we have made."
        rewritten_email = rewrite_email(sample_email)
        self.assertTrue('we' in rewritten_email.lower())
        self.assertTrue('you' in rewritten_email.lower())

if __name__ == "__main__":
    unittest.main()