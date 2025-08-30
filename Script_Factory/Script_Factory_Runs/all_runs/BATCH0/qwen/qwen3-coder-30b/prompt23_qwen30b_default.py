import re
from typing import List, Tuple

def split_sentences(text: str) -> List[str]:
    """
    Split text into sentences, handling punctuation and quoted speech.
    
    Args:
        text (str): Input text to split
        
    Returns:
        List[str]: List of sentences
    """
    # Split on sentence-ending punctuation, but not within quotes or abbreviations
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\!|\?)\s', text)
    return [s.strip() for s in sentences if s.strip()]

def replace_formal_words(sentence: str) -> str:
    """
    Replace formal words with more colloquial equivalents.
    
    Args:
        sentence (str): Input sentence
        
    Returns:
        str: Sentence with formal words replaced
    """
    replacements = {
        'utilize': 'use',
        'commence': 'start',
        'endeavor': 'try',
        'subsequently': 'then',
        'furthermore': 'and',
        'nevertheless': 'but',
        'consequently': 'so',
        'additionally': 'also',
        'considerably': 'a lot',
        'exceedingly': 'very',
        'inasmuch as': 'because',
        'nonetheless': 'still',
        'regarding': 'about',
        'therefore': 'so',
        'whereas': 'while'
    }
    
    result = sentence
    for formal, colloquial in replacements.items():
        # Use word boundaries to avoid partial matches
        pattern = r'\b' + re.escape(formal) + r'\b'
        result = re.sub(pattern, colloquial, result, flags=re.IGNORECASE)
    
    return result

def replace_colloquial_words(sentence: str) -> str:
    """
    Replace colloquial words with more formal equivalents.
    
    Args:
        sentence (str): Input sentence
        
    Returns:
        str: Sentence with colloquial words replaced
    """
    replacements = {
        'use': 'utilize',
        'start': 'commence',
        'try': 'endeavor',
        'then': 'subsequently',
        'and': 'furthermore',
        'but': 'nevertheless',
        'so': 'consequently',
        'also': 'additionally',
        'a lot': 'considerably',
        'very': 'exceedingly',
        'because': 'inasmuch as',
        'still': 'nonetheless',
        'about': 'regarding',
        'therefore': 'therefore',
        'while': 'whereas'
    }
    
    result = sentence
    for colloquial, formal in replacements.items():
        pattern = r'\b' + re.escape(colloquial) + r'\b'
        result = re.sub(pattern, formal, result, flags=re.IGNORECASE)
    
    return result

def switch_tone(sentence: str, is_formal: bool = True) -> str:
    """
    Switch the tone of a sentence from formal to informal or vice versa.
    
    Args:
        sentence (str): Input sentence
        is_formal (bool): If True, make informal; if False, make formal
        
    Returns:
        str: Sentence with switched tone
    """
    if is_formal:
        # Convert to informal by replacing formal words
        return replace_formal_words(sentence)
    else:
        # Convert to formal by replacing colloquial words
        return replace_colloquial_words(sentence)

def rewrite_email_tone(email_body: str, start_formal: bool = True) -> str:
    """
    Rewrite an email body with tone shifting halfway through each sentence.
    
    Args:
        email_body (str): The original email text
        start_formal (bool): If True, sentences start formal and become informal;
                            if False, they start informal and become formal
        
    Returns:
        str: Email with tone-shifted sentences
    """
    sentences = split_sentences(email_body)
    
    # Process each sentence to shift tone halfway through
    rewritten_sentences = []
    for i, sentence in enumerate(sentences):
        if not sentence:
            continue
            
        # Determine whether to make it formal or informal based on position and start_formal flag
        is_formal = (i % 2 == 0) ^ (not start_formal)
        
        # Apply tone shift
        rewritten_sentence = switch_tone(sentence, is_formal)
        rewritten_sentences.append(rewritten_sentence)
    
    return ' '.join(rewritten_sentences)

def main():
    """Demonstrate usage of the tone-shifting email rewriter."""
    sample_email = (
        "We would like to inform you that the project has been completed. "
        "Please note that this is a formal notice regarding the matter. "
        "The team has worked diligently to ensure quality standards are met. "
        "Furthermore, we appreciate your cooperation in this regard."
    )
    
    print("Original Email:")
    print(sample_email)
    print("\nRewritten Email (starting formal):")
    print(rewrite_email_tone(sample_email, start_formal=True))
    print("\nRewritten Email (starting informal):")
    print(rewrite_email_tone(sample_email, start_formal=False))

if __name__ == "__main__":
    main()
