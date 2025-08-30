import random
from typing import List, Tuple

def expand(sentence: str) -> str:
    """
    Expands a short sentence into an unnecessarily long essay.
    
    Args:
        sentence: A short input sentence to be expanded
        
    Returns:
        An expanded essay that is at least 5 times longer than the input
    """
    # Predefined expansion templates with varying structures
    templates = [
        "The concept of {word} is a fascinating one. In today's world, {word} has become increasingly important. "
        "Many individuals believe that {word} plays a significant role in our daily lives. "
        "This idea can be explored from multiple perspectives. "
        "It is clear that understanding {word} contributes to personal development.",
        
        "When we consider the topic of {word}, several aspects come into play. "
        "{word} has been studied extensively by researchers and scholars. "
        "The significance of {word} cannot be overstated in modern society. "
        "Furthermore, {word} influences various sectors including technology, education, and health. "
        "Therefore, it is crucial to examine {word} thoroughly.",
        
        "One cannot ignore the importance of {word} in contemporary times. "
        "The evolution of {word} over the years has been remarkable. "
        "Various theories have emerged concerning {word}. "
        "People from all walks of life are affected by {word}. "
        "Thus, a comprehensive understanding of {word} is essential for progress.",
        
        "The phenomenon of {word} has captured the attention of many experts. "
        "Research into {word} continues to yield new insights. "
        "It is evident that {word} impacts society in profound ways. "
        "Moreover, {word} has implications for future developments. "
        "As such, studying {word} remains a priority for many researchers.",
        
        "In conclusion, the topic of {word} deserves careful consideration. "
        "The benefits of understanding {word} are numerous and well-documented. "
        "It is important to recognize that {word} affects different groups in unique ways. "
        "With continued study, {word} will continue to evolve. "
        "Ultimately, {word} represents a vital area of exploration."
    ]
    
    # Extract the main word from the sentence (first word)
    words = sentence.strip().split()
    if not words:
        return sentence
    
    main_word = words[0].rstrip('.,!?;:"()[]{}')
    
    # Select a random template
    template = random.choice(templates)
    
    # Expand the sentence using the selected template
    expanded_text = template.format(word=main_word)
    
    # Split into sentences and process further to meet word count requirement
    sentences = [s.strip() for s in expanded_text.split('.') if s.strip()]
    
    # Add more variations to reach at least 5x word count
    target_words = len(words) * 5
    current_words = len(expanded_text.split())
    
    # Continue expanding by repeating and modifying content
    while current_words < target_words:
        # Create additional sentences with variations
        additional_sentences = [
            f"Additionally, {main_word} demonstrates remarkable characteristics that are worth examining.",
            f"It is interesting to note how {main_word} interacts with other related concepts.",
            f"Various experts have highlighted the importance of understanding {main_word}.",
            f"The study of {main_word} reveals intricate details about its nature.",
            f"{main_word} serves as a cornerstone in many academic disciplines."
        ]
        
        # Add random sentences
        for _ in range(2):
            if current_words >= target_words:
                break
            sentence = random.choice(additional_sentences)
            sentences.append(sentence)
            current_words += len(sentence.split())
    
    # Join all sentences into a paragraph, ensuring each sentence is <= 25 words
    final_sentences = []
    for sent in sentences:
        words_in_sent = sent.split()
        if len(words_in_sent) > 25:
            # Truncate to 25 words and add ellipsis if needed
            truncated = ' '.join(words_in_sent[:25])
            final_sentences.append(truncated + "...")
        else:
            final_sentences.append(sent)
    
    # Combine sentences into a single essay
    result = ". ".join(final_sentences) + "."
    
    return result

if __name__ == "__main__":
    # Test example
    original = "Technology is important."
    expanded = expand(original)
    print("Original:", original)
    print("Expanded:", expanded)
    print("Word count - Original:", len(original.split()), "Expanded:", len(expanded.split()))
