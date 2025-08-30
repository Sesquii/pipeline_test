import re
import unittest
from typing import List, Tuple

def split_into_sentences(text: str) -> List[str]:
    """
    Split text into sentences, handling punctuation, abbreviations, and quoted speech.
    
    Args:
        text (str): The input text to split
        
    Returns:
        List[str]: A list of sentences
    """
    # Split on sentence endings, but preserve the ending punctuation
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|!)\s', text)
    
    # Filter out empty strings and strip whitespace
    return [s.strip() for s in sentences if s.strip()]

def is_formal_word(word: str) -> bool:
    """
    Check if a word is typically used in formal contexts.
    
    Args:
        word (str): The word to check
        
    Returns:
        bool: True if the word is formal, False otherwise
    """
    formal_words = {
        'utilize', 'implement', 'consider', 'endeavor', 'commence', 
        'terminate', 'subsequently', 'therefore', 'nevertheless', 
        'additionally', 'furthermore', 'consequently', 'henceforth',
        'whereas', 'notwithstanding', 'regarding', 'concerning'
    }
    return word.lower() in formal_words

def is_informal_word(word: str) -> bool:
    """
    Check if a word is typically used in informal contexts.
    
    Args:
        word (str): The word to check
        
    Returns:
        bool: True if the word is informal, False otherwise
    """
    informal_words = {
        'gonna', 'wanna', 'gotta', 'kinda', 'sorta', 'hafta',
        'wicked', 'awesome', 'cool', 'neat', 'dude', 'bro'
    }
    return word.lower() in informal_words

def replace_formal_with_informal(word: str) -> str:
    """
    Replace formal words with informal equivalents.
    
    Args:
        word (str): The formal word to replace
        
    Returns:
        str: The informal equivalent or original word if not found
    """
    replacements = {
        'utilize': 'use',
        'implement': 'do',
        'consider': 'think about',
        'endeavor': 'try',
        'commence': 'start',
        'terminate': 'stop',
        'subsequently': 'then',
        'therefore': 'so',
        'nevertheless': 'but',
        'additionally': 'also',
        'furthermore': 'and',
        'consequently': 'because',
        'henceforth': 'from now on',
        'whereas': 'while',
        'notwithstanding': 'even though',
        'regarding': 'about',
        'concerning': 'about'
    }
    return replacements.get(word.lower(), word)

def replace_informal_with_formal(word: str) -> str:
    """
    Replace informal words with formal equivalents.
    
    Args:
        word (str): The informal word to replace
        
    Returns:
        str: The formal equivalent or original word if not found
    """
    replacements = {
        'gonna': 'going to',
        'wanna': 'want to',
        'gotta': 'got to',
        'kinda': 'kind of',
        'sorta': 'sort of',
        'hafta': 'have to',
        'wicked': 'excellent',
        'awesome': 'excellent',
        'cool': 'acceptable',
        'neat': 'tidy',
        'dude': 'friend',
        'bro': 'friend'
    }
    return replacements.get(word.lower(), word)

def rewrite_sentence_tone(sentence: str, target_tone: str = "informal") -> str:
    """
    Rewrite a sentence by shifting its tone.
    
    Args:
        sentence (str): The sentence to rewrite
        target_tone (str): Either 'formal' or 'informal'
        
    Returns:
        str: The rewritten sentence with shifted tone
    """
    if not sentence:
        return sentence
        
    # Split into words while preserving punctuation
    words = re.findall(r'\b\w+\b|[^\w\s]', sentence)
    
    # Determine current tone and target tone
    current_tone = "formal" if any(is_formal_word(w) for w in words if w.isalpha()) else "informal"
    
    # If already in target tone, return as is
    if current_tone == target_tone:
        return sentence
    
    # Process each word
    rewritten_words = []
    for word in words:
        if not word.isalpha():
            rewritten_words.append(word)
            continue
            
        if target_tone == "informal":
            # Convert formal to informal
            if is_formal_word(word):
                rewritten_words.append(replace_formal_with_informal(word))
            elif is_informal_word(word):
                rewritten_words.append(word)
            else:
                # Replace some common formal words with informal equivalents
                if word.lower() in ['we', 'our', 'us']:
                    rewritten_words.append('I')
                elif word.lower() in ['you', 'your']:
                    rewritten_words.append('you')
                else:
                    rewritten_words.append(word)
        else:  # target_tone == "formal"
            # Convert informal to formal
            if is_informal_word(word):
                rewritten_words.append(replace_informal_with_formal(word))
            elif is_formal_word(word):
                rewritten_words.append(word)
            else:
                # Replace some common informal words with formal equivalents
                if word.lower() in ['i', 'me']:
                    rewritten_words.append('we')
                elif word.lower() in ['you']:
                    rewritten_words.append('you')
                else:
                    rewritten_words.append(word)
    
    return ''.join(rewritten_words)

def shift_tone_in_sentence(sentence: str, midpoint: int = None) -> str:
    """
    Shift the tone of a sentence by splitting it at midpoint and applying different tones.
    
    Args:
        sentence (str): The sentence to rewrite
        midpoint (int): Position to split the sentence. If None, splits at half point.
        
    Returns:
        str: The sentence with tone shifted
    """
    if not sentence:
        return sentence
        
    # Simple approach: split into two parts and apply different tones
    words = sentence.split()
    
    if not words:
        return sentence
        
    # Default midpoint is halfway through the sentence
    if midpoint is None:
        midpoint = len(words) // 2
    
    # Ensure midpoint is within bounds
    midpoint = max(0, min(midpoint, len(words)))
    
    # Split the sentence
    first_part = ' '.join(words[:midpoint])
    second_part = ' '.join(words[midpoint:])
    
    # Rewrite each part with different tone
    first_rewritten = rewrite_sentence_tone(first_part, "formal")
    second_rewritten = rewrite_sentence_tone(second_part, "informal")
    
    return f"{first_rewritten} {second_rewritten}".strip()

def rewrite_email_body(email_body: str) -> str:
    """
    Rewrite an email body by shifting the tone of each sentence.
    
    Args:
        email_body (str): The original email body
        
    Returns:
        str: The rewritten email body with tone shifted
    """
    if not email_body:
        return email_body
    
    sentences = split_into_sentences(email_body)
    rewritten_sentences = []
    
    for sentence in sentences:
        # Apply tone shift to each sentence
        rewritten_sentence = shift_tone_in_sentence(sentence)
        rewritten_sentences.append(rewritten_sentence)
    
    return ' '.join(rewritten_sentences)

class TestToneShiftingEmailRewriter(unittest.TestCase):
    def test_split_into_sentences(self):
        text = "Hello world. How are you? I am fine!"
        expected = ["Hello world.", "How are you?", "I am fine!"]
        self.assertEqual(split_into_sentences(text), expected)
        
    def test_rewrite_sentence_tone(self):
        # Test formal to informal conversion
        sentence = "We consider this matter carefully."
        result = rewrite_sentence_tone(sentence, "informal")
        self.assertIn("think about", result)
        
        # Test informal to formal conversion
        sentence = "I wanna know what's up."
        result = rewrite_sentence_tone(sentence, "formal")
        self.assertIn("want to", result)

if __name__ == "__main__":
    # Example usage
    sample_email = (
        "We are pleased to inform you that the project has been completed. "
        "You should review the final report and provide feedback. "
        "Please note that this is a significant milestone for our company."
    )
    
    print("Original email:")
    print(sample_email)
    print("\nRewritten email:")
    print(rewrite_email_body(sample_email))
    
    # Run tests
    unittest.main()
