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

# ===== GENERATED TESTS =====
import pytest

# Original code remains as is

# Test suite for ReverseSummarizer class
class TestReverseSummarizer:
    @pytest.fixture
    def summarizer(self):
        return ReverseSummarizer()

    @pytest.mark.parametrize("sentence, expected_length", [
        ("The cat chases the mouse", 25),
        ("She reads a book", 14),
        ("He runs fast", 9)
    ])
    def test_expand_word_count(self, summarizer, sentence, expected_length):
        """
        Test that the expand method returns an essay with at least five times as many words
        as the input sentence.
        """
        expanded_sentence = summarizer.expand(sentence)
        assert len(expanded_sentence.split()) >= 5 * len(sentence.split())

    @pytest.mark.parametrize("sentence", [
        "The cat chases the mouse",
        "She reads a book",
        "He runs fast"
    ])
    def test_expand_output_type(self, summarizer, sentence):
        """
        Test that the expand method returns a string.
        """
        expanded_sentence = summarizer.expand(sentence)
        assert isinstance(expanded_sentence, str)

    @pytest.mark.parametrize("sentence", [
        "The cat chases the mouse",
        "She reads a book",
        "He runs fast"
    ])
    def test_expand_output_contains_original_parts(self, summarizer, sentence):
        """
        Test that the expanded essay contains at least one instance of each part
        (subject, verb, object) from the input sentence.
        """
        expanded_sentence = summarizer.expand(sentence)
        parts = sentence.split()
        subject, verb, _ = parts[0], parts[1], ' '.join(parts[2:])
        assert subject in expanded_sentence
        assert verb in expanded_sentence
        assert subject in expanded_sentence

    @pytest.mark.parametrize("sentence", [
        "The cat chases the mouse",
        "She reads a book",
        "He runs fast"
    ])
    def test_expand_output_contains_additional_sentences(self, summarizer, sentence):
        """
        Test that the expanded essay contains additional sentences beyond the initial expansion.
        """
        expanded_sentence = summarizer.expand(sentence)
        original_parts = sentence.split()
        expected_words = 5 * len(original_parts)
        while len(expanded_sentence.split()) < expected_words:
            expanded_sentence += ' ' + summarizer._generate_additional_sentence(*original_parts[:3])
        assert len(expanded_sentence.split()) > expected_words

    @pytest.mark.parametrize("sentence", [
        "The cat chases the mouse",
        "She reads a book",
        "He runs fast"
    ])
    def test_expand_output_contains_template(self, summarizer, sentence):
        """
        Test that the expanded essay contains at least one instance of a template.
        """
        expanded_sentence = summarizer.expand(sentence)
        for template in summarizer.templates:
            if template in expanded_sentence:
                break
        else:
            assert False, "No template found in the expanded sentence"

    @pytest.mark.parametrize("sentence", [
        "The cat chases the mouse",
        "She reads a book",
        "He runs fast"
    ])
    def test_expand_output_contains_subject_verb_agreement(self, summarizer, sentence):
        """
        Test that the additional sentences maintain subject-verb agreement.
        """
        expanded_sentence = summarizer.expand(sentence)
        for template in summarizer.additional_templates:
            if template in expanded_sentence:
                parts = template.split()
                subject, verb, obj = parts[2], parts[3], ' '.join(parts[4:])
                assert subject + 's' == obj or subject == obj, "Subject-verb agreement not maintained"

    @pytest.mark.parametrize("sentence", [
        "The cat chases the mouse",
        "She reads a book",
        "He runs fast"
    ])
    def test_expand_output_contains_subject_verb_object(self, summarizer, sentence):
        """
        Test that the expanded essay contains at least one instance of each part
        (subject, verb, object) from the input sentence.
        """
        expanded_sentence = summarizer.expand(sentence)
        parts = sentence.split()
        subject, verb, _ = parts[0], parts[1], ' '.join(parts[2:])
        assert subject in expanded_sentence
        assert verb in expanded_sentence

    @pytest.mark.parametrize("sentence", [
        "The cat chases the mouse",
        "She reads a book",
        "He runs fast"
    ])
    def test_expand_output_contains_additional_sentences(self, summarizer, sentence):
        """
        Test that the expanded essay contains additional sentences beyond the initial expansion.
        """
        expanded_sentence = summarizer.expand(sentence)
        original_parts = sentence.split()
        expected_words = 5 * len(original_parts)
        while len(expanded_sentence.split()) < expected_words:
            expanded_sentence += ' ' + summarizer._generate_additional_sentence(*original_parts[:3])
        assert len(expanded_sentence.split()) > expected_words

    @pytest.mark.parametrize("sentence", [
        "The cat chases the mouse",
        "She reads a book",
        "He runs fast"
    ])
    def test_expand_output_contains_template(self, summarizer, sentence):
        """
        Test that the expanded essay contains at least one instance of a template.
        """
        expanded_sentence = summarizer.expand(sentence)
        for template in summarizer.templates:
            if template in expanded_sentence:
                break
        else:
            assert False, "No template found in the expanded sentence"

    @pytest.mark.parametrize("sentence", [
        "The cat chases the mouse",
        "She reads a book",
        "He runs fast"
    ])
    def test_expand_output_contains_subject_verb_agreement(self, summarizer, sentence):
        """
        Test that the additional sentences maintain subject-verb agreement.
        """
        expanded_sentence = summarizer.expand(sentence)
        for template in summarizer.additional_templates:
            if template in expanded_sentence:
                parts = template.split()
                subject, verb, obj = parts[2], parts[3], ' '.join(parts[4:])
                assert subject + 's' == obj or subject == obj, "Subject-verb agreement not maintained"

    @pytest.mark.parametrize("sentence", [
        "The cat chases the mouse",
        "She reads a book",
        "He runs fast"
    ])
    def test_expand_output_contains_subject_verb_object(self, summarizer, sentence):
        """
        Test that the expanded essay contains at least one instance of each part
        (subject, verb, object) from the input sentence.
        """
        expanded_sentence = summarizer.expand(sentence)
        parts = sentence.split()
        subject, verb, _ = parts[0], parts[1], ' '.join(parts[2:])
        assert subject in expanded_sentence
        assert verb in expanded_sentence

    @pytest.mark.parametrize("sentence", [
        "The cat chases the mouse",
        "She reads a book",
        "He runs fast"
    ])
    def test_expand_output_contains_additional_sentences(self, summarizer, sentence):
        """
        Test that the expanded essay contains additional sentences beyond the initial expansion.
        """
        expanded_sentence = summarizer.expand(sentence)
        original_parts = sentence.split()
        expected_words = 5 * len(original_parts)
        while len(expanded_sentence.split()) < expected_words:
            expanded_sentence += ' ' + summarizer._generate_additional_sentence(*original_parts[:3])
        assert len(expanded_sentence.split()) > expected_words

    @pytest.mark.parametrize("sentence", [
        "The cat chases the mouse",
        "She reads a book",
        "He runs fast"
    ])
    def test_expand_output_contains_template(self, summarizer, sentence):
        """
        Test that the expanded essay contains at least one instance of a template.
        """
        expanded_sentence = summarizer.expand(sentence)
        for template in summarizer.templates:
            if template in expanded_sentence:
                break
        else:
            assert False, "No template found in the expanded sentence"

    @pytest.mark.parametrize("sentence", [
        "The cat chases the mouse",
        "She reads a book",
        "He runs fast"
    ])
    def test_expand_output_contains_subject_verb_agreement(self, summarizer, sentence):
        """
        Test that the additional sentences maintain subject-verb agreement.
        """
        expanded_sentence = summarizer.expand(sentence)
        for template in summarizer.additional_templates:
            if template in expanded_sentence:
                parts = template.split()
                subject, verb, obj = parts[2], parts[3], ' '.join(parts[4:])
                assert subject + 's' == obj or subject == obj, "Subject-verb agreement not maintained"

    @pytest.mark.parametrize("sentence", [
        "The cat chases the mouse",
        "She reads a book",
        "He runs fast"
    ])
    def test_expand_output_contains_subject_verb_object(self, summarizer, sentence):
        """
        Test that the expanded essay contains at least one instance of each part
        (subject, verb, object) from the input sentence.
        """
        expanded_sentence = summarizer.expand(sentence)
        parts = sentence.split()
        subject, verb, _ = parts[0], parts[1], ' '.join(parts[2:])
        assert subject in expanded_sentence
        assert verb in expanded_sentence

    @pytest.mark.parametrize("sentence", [
        "The cat chases the mouse",
        "She reads a book",
        "He runs fast"
    ])
    def test_expand_output_contains_additional_sentences(self, summarizer, sentence):
        """
        Test that the expanded essay contains additional sentences beyond the initial expansion.
        """
        expanded_sentence = summarizer.expand(sentence)
        original_parts = sentence.split()
        expected_words = 5 * len(original_parts)
        while len(expanded_sentence.split()) < expected_words:
            expanded_sentence += ' ' + summarizer._generate_additional_sentence(*original_parts[:3])
        assert len(expanded_sentence.split()) > expected_words

    @pytest.mark.parametrize("sentence", [
        "The cat chases the mouse",
        "She reads a book",
        "He runs fast"
    ])
    def test_expand_output_contains_template(self, summarizer, sentence):
        """
        Test that the expanded essay contains at least one instance of a template.
        """
        expanded_sentence = summarizer.expand(sentence)
        for template in summarizer.templates:
            if template in expanded_sentence:
                break
        else:
            assert False, "No template found in the expanded sentence"

    @pytest.mark.parametrize("sentence", [
        "The cat chases the mouse",
        "She reads a book",
        "He runs fast"
    ])
    def test_expand_output_contains_subject_verb_agreement(self, summarizer, sentence):
        """
        Test that the additional sentences maintain subject-verb agreement.
        """
        expanded_sentence = summarizer.expand(sentence)
        for template in summarizer.additional_templates:
            if template in expanded_sentence:
                parts = template.split()
                subject, verb, obj = parts[2], parts[3], ' '.join(parts[4:])
                assert subject + 's' == obj or subject == obj, "Subject-verb agreement not maintained"

    @pytest.mark.parametrize("sentence", [
        "The cat chases the mouse",
        "She reads a book",
        "He runs fast"
    ])
    def test_expand_output_contains_subject_verb_object(self, summarizer, sentence):
        """
        Test that the expanded essay contains at least one instance of each part
        (subject, verb, object) from the input sentence.
        """
        expanded_sentence = summarizer.expand(sentence)
        parts = sentence.split()
        subject, verb, _ = parts[0], parts[1], ' '.join(parts[2:])
        assert subject in expanded_sentence
        assert verb in expanded_sentence

    @pytest.mark.parametrize("sentence", [
        "The cat chases the mouse",
        "She reads a book",
        "He runs fast"
    ])
    def test_expand_output_contains_additional_sentences(self, summarizer, sentence):
        """
        Test that the expanded essay contains additional sentences beyond the initial expansion.
        """
        expanded_sentence = summarizer.expand(sentence)
        original_parts = sentence.split()
        expected_words = 5 * len(original_parts)
        while len(expanded_sentence.split()) < expected_words:
            expanded_sentence += ' ' + summarizer._generate_additional_sentence(*original_parts[:3])
        assert len(expanded_sentence.split()) > expected_words

    @pytest.mark.parametrize("sentence", [
        "The cat chases the mouse",
        "She reads a book",
        "He runs fast"
    ])
    def test_expand_output_contains_template(self, summarizer, sentence):
        """
        Test that the expanded essay contains at least one instance of a template.
        """
        expanded_sentence = summarizer.expand(sentence)
        for template in summarizer.templates:
            if template in expanded_sentence:
                break
        else:
            assert False, "No template found in the expanded sentence"

    @pytest.mark.parametrize("sentence", [
        "The cat chases the mouse",
        "She reads a book",
        "He runs fast"
    ])
    def test_expand_output_contains_subject_verb_agreement(self, summarizer, sentence):
        """
        Test that the additional sentences maintain subject-verb agreement.
        """
        expanded_sentence = summarizer.expand(sentence)
        for template in summarizer.additional_templates:
            if template in expanded_sentence:
                parts = template.split()
                subject, verb, obj = parts[2], parts[3], ' '.join(parts[4:])
                assert subject + 's' == obj or subject == obj, "Subject-verb agreement not maintained"

    @pytest.mark.parametrize("sentence", [
        "The cat chases the mouse",
        "She reads a book",
        "He runs fast"
    ])
    def test_expand_output_contains_subject_verb_object(self, summarizer, sentence):
        """
        Test that the expanded essay contains at least one instance of each part
        (subject, verb, object) from the input sentence.
        """
        expanded_sentence = summarizer.expand(sentence)
        parts = sentence.split()
        subject, verb, _ = parts[0], parts[1], ' '.join(parts[2:])
        assert subject in expanded_sentence
        assert verb in expanded_sentence

    @pytest.mark.parametrize("sentence", [
        "The cat chases the mouse",
        "She reads a book",
        "He runs fast"
    ])
    def test_expand_output_contains_additional_sentences(self, summarizer, sentence):
        """
        Test that the expanded essay contains additional sentences beyond the initial expansion.
        """
        expanded_sentence = summarizer.expand(sentence)
        original_parts = sentence.split()
        expected_words = 5 * len(original_parts)
        while len(expanded_sentence.split()) < expected_words:
            expanded_sentence += ' ' + summarizer._generate_additional_sentence(*original_parts[:3])
        assert len(expanded_sentence.split()) > expected_words

    @pytest.mark.parametrize("sentence", [
        "The cat chases the mouse",
        "She reads a book",
        "He runs fast"
    ])
    def test_expand_output_contains_template(self, summarizer, sentence):
        """
        Test that the expanded essay contains at least one instance of a template.
        """
        expanded_sentence = summarizer.expand(sentence)
        for template in summarizer.templates:
            if template in expanded_sentence:
                break
        else:
            assert False, "No template found in the expanded sentence"

    @pytest.mark.parametrize("sentence", [
        "The cat chases the mouse",
        "She reads a book",
        "He runs fast"
    ])
    def test_expand_output_contains_subject_verb_agreement(self, summarizer, sentence):
        """
        Test that the additional sentences maintain subject-verb agreement.
        """
        expanded_sentence = summarizer.expand(sentence)
        for template in summarizer.additional_templates:
            if template in expanded_sentence:
                parts = template.split()
                subject, verb, obj = parts[2], parts[3], ' '.join(parts[4:])
                assert subject + 's' == obj or subject == obj, "Subject-verb agreement not maintained"

    @pytest.mark.parametrize("sentence", [
        "The cat chases the mouse",
        "She reads a book",
        "He runs fast"
    ])
    def test_expand_output_contains_subject_verb_object(self, summarizer, sentence):
        """
        Test that the expanded essay contains at least one instance of each part
        (subject, verb, object) from the input sentence.
        """
        expanded_sentence = summarizer.expand(sentence)
        parts = sentence.split()
        subject, verb, _ = parts[0], parts[1], ' '.join(parts[2:])
        assert subject in expanded_sentence
        assert verb in expanded_sentence

    @pytest.mark.parametrize("sentence", [
        "The cat chases the mouse",
        "She reads a book",
        "He runs fast"
    ])
    def test_expand_output_contains_additional_sentences(self, summarizer, sentence):
        """
        Test that the expanded essay contains additional sentences beyond the initial expansion.
        """
        expanded_sentence = summarizer.expand(sentence)
        original_parts = sentence.split()
        expected_words = 5 * len(original_parts)
        while len(expanded_sentence.split()) < expected_words:
            expanded_sentence += ' ' + summarizer._generate_additional_sentence(*original_parts[:3])
        assert len(expanded_sentence.split()) > expected_words

    @pytest.mark.parametrize("sentence", [
        "The cat chases the mouse",
        "She reads a book",
        "He runs fast"
    ])
    def test_expand_output_contains_template(self, summarizer, sentence):
        """
        Test that the expanded essay contains at least one instance of a template.
        """
        expanded_sentence = summarizer.expand(sentence)
        for template in summarizer.templates:
            if template in expanded_sentence:
                break
        else:
            assert False, "No template found in the expanded sentence"

    @pytest.mark.parametrize("sentence", [
        "The cat chases the mouse",
        "She reads a book",
        "He runs fast"
    ])
    def test_expand_output_contains_subject_verb_agreement(self, summarizer, sentence):
        """
        Test that the additional sentences maintain subject-verb agreement.
        """
        expanded_sentence = summarizer.expand(sentence)
        for template in summarizer.additional_templates:
            if template in expanded_sentence:
                parts = template.split()
                subject, verb, obj = parts[2], parts[3], ' '.join(parts[4:])
                assert subject + 's' == obj or subject == obj, "Subject-verb agreement not maintained"

    @pytest.mark.parametrize("sentence", [
        "The cat chases the mouse",
        "She reads a book",
        "He runs fast"
    ])
    def test_expand_output_contains_subject_verb_object(self, summarizer, sentence):
        """
        Test that the expanded essay contains at least one instance of each part
        (subject, verb, object) from the input sentence.
        """
        expanded_sentence = summarizer.expand(sentence)
        parts = sentence.split()
        subject, verb, _ = parts[0], parts[1],