import random
from typing import List, Tuple

def expand(sentence: str) -> str:
    """
    Expands a short sentence into an unnecessarily long essay.
    
    Args:
        sentence (str): The input sentence to expand
        
    Returns:
        str: An expanded essay that is at least 5 times longer than the input
    """
    # Initialize the summarizer class and return its result
    summarizer = ReverseSummarizer()
    return summarizer.expand(sentence)

class ReverseSummarizer:
    """A class that expands short sentences into unnecessarily long essays."""
    
    def __init__(self):
        """Initialize the ReverseSummarizer with expansion templates."""
        self.templates = [
            "The concept of {topic} has been a subject of intense scrutiny and contemplation for scholars and thinkers throughout history. In contemporary discourse, it is essential to understand that {topic} represents a fundamental principle that underpins much of modern thought. When examining the intricacies of {topic}, one cannot help but notice its profound implications on various aspects of human experience.",
            "In recent years, there has been significant interest in exploring how {topic} manifests itself in our daily lives. The phenomenon of {topic} is not merely an abstract concept but rather a tangible element that influences countless decisions and behaviors. It is evident that {topic} serves as a cornerstone for understanding broader societal trends.",
            "The significance of {topic} cannot be overstated when considering its impact on individual development and collective progress. Various studies have shown that {topic} plays a crucial role in shaping attitudes, beliefs, and practices across different communities. Furthermore, it is clear that {topic} continues to evolve and adapt to changing circumstances.",
            "It is important to recognize that {topic} operates on multiple levels, from the personal to the global. The complexity of {topic} means that its effects are often subtle yet far-reaching. Scholars have dedicated considerable effort to unraveling the mysteries surrounding {topic}, leading to new insights and perspectives.",
            "The exploration of {topic} reveals fascinating connections between seemingly unrelated domains. As we delve deeper into understanding {topic}, we find that it encompasses a wide range of ideas and concepts that interconnect in unexpected ways. This interconnectedness makes {topic} a particularly rich area for further investigation."
        ]
        
        self.conjunctions = ["Furthermore", "Additionally", "Moreover", "Similarly", "In addition", "Also", "Notably", "Importantly", "Crucially"]
        self.adverbs = ["significantly", "dramatically", "profoundly", "substantially", "considerably", "markedly", "noticeably", "distinctively"]
        self.qualifiers = ["certainly", "undoubtedly", "without question", "without doubt", "clearly", "obviously", "evidently"]
        
    def expand(self, sentence: str) -> str:
        """
        Expands a short sentence into an unnecessarily long essay.
        
        Args:
            sentence (str): The input sentence to expand
            
        Returns:
            str: An expanded essay that is at least 5 times longer than the input
        """
        # Clean and process the input sentence
        cleaned_sentence = sentence.strip()
        if not cleaned_sentence:
            return ""
            
        # Extract key topic from the sentence (simplified approach)
        words = cleaned_sentence.split()
        topic = " ".join(words[:min(3, len(words))])  # Use first 1-3 words as topic
        
        # Generate initial paragraphs using templates
        paragraphs = []
        for i in range(3):  # Create 3 paragraphs
            template = random.choice(self.templates)
            expanded_text = template.format(topic=topic)
            
            # Add some variation with conjunctions and qualifiers
            if i > 0:
                conjunction = random.choice(self.conjunctions)
                expanded_text += f" {conjunction}, {random.choice(self.qualifiers)} {topic} demonstrates itself in {self._get_random_phrase()}."
                
            paragraphs.append(expanded_text)
            
        # Combine paragraphs and add more sentences for length
        essay = " ".join(paragraphs)
        
        # Add more sentences to meet the minimum word requirement
        additional_sentences = []
        for _ in range(10):  # Add 10 more sentences
            sentence = self._generate_expanded_sentence(topic)
            additional_sentences.append(sentence)
            
        essay += " " + " ".join(additional_sentences)
        
        # Ensure minimum word count and readability
        words_needed = max(20, len(cleaned_sentence.split()) * 5)  # At least 5x longer
        current_words = len(essay.split())
        
        # If needed, add more content
        while current_words < words_needed:
            sentence = self._generate_expanded_sentence(topic)
            essay += " " + sentence
            current_words = len(essay.split())
            
        return self._format_essay(essay)
        
    def _get_random_phrase(self) -> str:
        """Generate a random descriptive phrase."""
        phrases = [
            "numerous aspects of modern society",
            "the evolution of contemporary thought",
            "the foundations of human understanding",
            "the progression of scientific knowledge",
            "the development of cultural norms"
        ]
        return random.choice(phrases)
        
    def _generate_expanded_sentence(self, topic: str) -> str:
        """Generate a single expanded sentence."""
        # Create variations of sentences about the topic
        templates = [
            f"{topic} is {random.choice(self.adverbs)} {random.choice(['influential', 'important', 'significant'])} in shaping our understanding.",
            f"The {random.choice(['impact', 'influence', 'role'])} of {topic} on modern society is {random.choice(self.qualifiers)}.",
            f"Research has shown that {topic} has a {random.choice(['profound', 'considerable', 'substantial'])} effect on individual behavior.",
            f"One cannot overlook the fact that {topic} plays a {random.choice(['crucial', 'significant', 'essential'])} role in today's world.",
            f"From multiple perspectives, it is evident that {topic} holds {random.choice(['great', 'considerable', 'important'])} significance."
        ]
        
        sentence = random.choice(templates)
        return sentence
        
    def _format_essay(self, essay: str) -> str:
        """Format the essay to ensure readability and proper sentence structure."""
        # Split into sentences and reassemble with proper punctuation
        words = essay.split()
        formatted_sentences = []
        
        current_sentence = []
        word_count = 0
        
        for word in words:
            current_sentence.append(word)
            word_count += 1
            
            # Start a new sentence if we've reached the limit or hit a period
            if word_count >= 25 or (word.endswith('.') and word_count >= 10):
                formatted_sentences.append(" ".join(current_sentence))
                current_sentence = []
                word_count = 0
                
        # Add any remaining words to a final sentence
        if current_sentence:
            formatted_sentences.append(" ".join(current_sentence))
            
        # Join sentences with proper spacing and ensure each is under 25 words
        result = ""
        for sentence in formatted_sentences:
            # Ensure no sentence exceeds 25 words
            sentence_words = sentence.split()
            if len(sentence_words) > 25:
                # Truncate to 25 words
                truncated = " ".join(sentence_words[:25])
                result += truncated + ". "
            else:
                result += sentence + ". "
                
        return result.strip()

# Example usage and testing
if __name__ == "__main__":
    # Test with a simple sentence
    original = "Technology is important."
    expanded = expand(original)
    
    print("Original:", original)
    print("Expanded:")
    print(expanded)
    print()
    
    # Show word counts
    original_words = len(original.split())
    expanded_words = len(expanded.split())
    print(f"Original word count: {original_words}")
    print(f"Expanded word count: {expanded_words}")
    print(f"Expansion factor: {expanded_words / original_words:.1f}x")
