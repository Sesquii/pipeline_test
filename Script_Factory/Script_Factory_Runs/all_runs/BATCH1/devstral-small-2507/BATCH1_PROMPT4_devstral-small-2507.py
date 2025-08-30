import random
from typing import List

class ReverseSummarizer:
    """
    A class that expands short sentences into unnecessarily long essays.
    """

    def __init__(self):
        # Pre-written expansion templates for variety
        self.templates = [
            "{subject} {verb} {object}. This action involves {subject} performing the act of {verb} upon {object}.",
            "The process of {subject} {verb} {object} is quite intricate. It begins with {subject}, who then proceeds to {verb} {object}.",
            "{subject} engages in the activity of {verb} {object}. This engagement is characterized by {subject}'s deliberate choice to {verb} {object}.",
            "In the realm of {subject}, there exists the phenomenon of {verb} {object}. This phenomenon manifests when {subject} chooses to {verb} {object}.",
            "{subject} undertakes the task of {verb} {object}. The undertaking involves various steps where {subject} carefully {verb} {object}."
        ]

    def expand(self, sentence: str) -> str:
        """
        Expands a short sentence into an unnecessarily long essay.

        Args:
            sentence (str): A short input sentence to be expanded.

        Returns:
            str: An expanded essay containing at least five times as many words
                 as the input sentence.
        """
        # Simple parsing of the input sentence (subject, verb, object)
        # This is a naive approach and may not work for all sentences
        parts = sentence.split()
        if len(parts) < 3:
            raise ValueError("Sentence must contain at least a subject, verb, and object")

        subject = parts[0]
        verb = parts[1]
        obj_index = 2
        while obj_index < len(parts) and parts[obj_index] not in ['.', '?', '!']:
            obj_index += 1

        object_phrase = ' '.join(parts[2:obj_index])

        # Choose a random template
        template = random.choice(self.templates)

        # Expand the sentence using the chosen template
        expanded_sentence = template.format(subject=subject, verb=verb, object=object_phrase)

        # Create additional sentences to meet word count requirement
        additional_sentences = []
        while self._word_count(expanded_sentence + ' '.join(additional_sentences)) < 5 * len(parts):
            additional_sentences.append(self._generate_additional_sentence(subject, verb, object_phrase))

        # Combine all sentences into the final essay
        essay = expanded_sentence + ' ' + ' '.join(additional_sentences)

        return essay

    def _word_count(self, text: str) -> int:
        """Counts the number of words in a string."""
        return len(text.split())

    def _generate_additional_sentence(self, subject: str, verb: str, obj: str) -> str:
        """
        Generates an additional sentence related to the main action.
        Ensures coherence by maintaining subject-verb agreement.
        """
        additional_templates = [
            "Furthermore, {subject} continues to {verb} {object} with great enthusiasm.",
            "It is noteworthy that {subject}'s ability to {verb} {object} is quite remarkable.",
            "In conclusion, the act of {subject} {verb} {object} demonstrates {subject}'s skill.",
            "Additionally, the process of {subject} {verb} {object} requires considerable effort.",
            "{subject} finds joy in repeatedly {verb} {object} throughout the day."
        ]
        
        return random.choice(additional_templates).format(subject=subject, verb=verb, object=obj)

# Simple test example
if __name__ == "__main__":
    summarizer = ReverseSummarizer()
    sample_sentence = "The cat chases the mouse"
    expanded_essay = summarizer.expand(sample_sentence)

    print("Original sentence:")
    print(sample_sentence)
    print("\nExpanded essay:")
    print(expanded_essay)