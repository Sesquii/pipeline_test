```python
import re
import unittest

class ToneShiftingEmailRewriter:
    @staticmethod
    def split_sentences(email_text: str) -> list[str]:
        """Split the email text into sentences based on punctuation marks (., !, ?)."""
        return re.split(r'[.!?]+', email_text)

    @staticmethod
    def rephrase_sentence(sentence: str) -> str:
        """Rewrite a single sentence by switching the tone halfway through."""
        length = len(sentence)
        mid = length // 2
        first_part = sentence[:mid]
        second_part = sentence[mid:]
        
        # Replace words in the first part with informal equivalents
        def replace_informal(text: str) -> str:
            text = text.replace("The", "the")
            text = text.replace("is", "are")
            return text
        
        # Replace words in the second part with formal equivalents
        def replace_formal(text: str) -> str:
            text = text.replace("is", "was")
            return text
        
        first_rephrased = replace_informal(first_part)
        second_rephrased = replace_formal(second_part)
        
        return f"{first_rephrased} {second_rephrased}"

    @staticmethod
    def rewrite_email(email_text: str) -> str:
        """Rewrite the entire email by splitting into sentences, rephrasing each sentence, and joining them back."""
        sentences = ToneShiftingEmailRewriter.split_sentences(email_text)
        non_empty = [s for s in sentences if s]
        rewritten_sentences = []
        for sentence in non_empty:
            rewritten_sentence = ToneShiftingEmailRewriter.rephrase_sentence(sentence)
            rewritten_sentences.append(rewritten_sentence)
        return " ".join(rewritten_sentences)

    @staticmethod
    def main():
        """Demonstrate usage on a sample email."""
        sample_email = """
        The customer is very satisfied with the service.
        Hello, how are you?
        This is a test sentence.
        """
        result = ToneShiftingEmailRewriter.rewrite_email(sample_email)
        print("Rewritten email:")
        print(result)

if __name__ == "__main__":
    ToneShiftingEmailRewriter.main()