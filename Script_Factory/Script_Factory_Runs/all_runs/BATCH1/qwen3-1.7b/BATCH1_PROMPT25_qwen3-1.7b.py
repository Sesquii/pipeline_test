```python
class MemoryLossStoryteller:
    """
    A memory-loss storyteller that generates stories with a midpoint where
    it forgets all previous plot points and starts introducing new ones.
    
    Attributes:
        None
        
    Methods:
        tell_story(total_sentences: int) -> str:
            Generates exactly total_sentences sentences.
            The first half are original, then the second half are new,
            with new sentences being unrelated to previous ones.
    """
    def tell_story(self, total_sentences: int) -> str:
        """
        Generate a story with memory loss.
        
        Args:
            total_sentences (int): Number of sentences to generate.
            
        Returns:
            str: The generated story as a string.
        """
        mid = total_sentences // 2
        original_sentences = []
        for i in range(mid):
            original_sentences.append(f"Original sentence {i + 1}")
        
        new_sentences = []
        for i in range(mid, total_sentences):
            new_sentences.append(f"New sentence {i - mid + 1}")
        
        return " ".join(original_sentences + new_sentences)