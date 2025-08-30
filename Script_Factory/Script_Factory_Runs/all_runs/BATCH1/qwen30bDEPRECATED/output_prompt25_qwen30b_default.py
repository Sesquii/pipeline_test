import random

class MemoryLossStoryteller:
    """
    A storyteller that generates narratives with memory loss.
    
    The storyteller creates a story with a specific number of sentences.
    In the middle of the story, it "forgets" all previous plot points and 
    begins introducing entirely new, unrelated plot elements.
    This simulates amnesia by maintaining two distinct story segments:
    - First half: builds upon original plot points
    - Second half: starts fresh with new unrelated content
    """
    
    def __init__(self):
        # List of possible story elements for the first half (original plot)
        self.original_elements = [
            "A mysterious stranger arrived in town.",
            "The old lighthouse had been abandoned for decades.",
            "A letter was found tucked under a rock.",
            "The town's annual festival was canceled.",
            "An ancient map was discovered in the attic.",
            "Strange lights appeared in the night sky.",
            "A dog ran into the forest, never to return.",
            "The mayor made an unusual announcement.",
            "A tree in the square began to glow.",
            "Someone heard whispers from the walls."
        ]
        
        # List of possible story elements for the second half (new plot)
        self.new_elements = [
            "A spaceship landed in the backyard.",
            "The ocean turned to glass overnight.",
            "A talking cat appeared on the windowsill.",
            "The clocks all stopped at 3:17.",
            "A rainbow appeared without any rain.",
            "The sky began to sing a lullaby.",
            "A library full of books flew away.",
            "The ground started to taste like chocolate.",
            "A giant sandwich grew in the garden.",
            "The stars began to dance in formation."
        ]
        
        # Common sentence starters for variety
        self.starters = [
            "Suddenly,",
            "In the end,",
            "It was then that",
            "Meanwhile,",
            "Unbeknownst to everyone,",
            "Little did they know,",
            "As if by magic,",
            "One day,",
            "The discovery led to",
            "What followed was"
        ]
    
    def tell_story(self, total_sentences: int) -> str:
        """
        Generate a story with memory loss.
        
        Args:
            total_sentences: Number of sentences in the final story
            
        Returns:
            A string containing the generated story
        """
        # Determine where the midpoint is (integer division)
        midpoint = total_sentences // 2
        
        # Store original plot points for first half
        original_plot = []
        
        # Generate first half of the story (with original plot points)
        for i in range(midpoint):
            # Select a random original element
            element = random.choice(self.original_elements)
            # Add a starter phrase to make it more natural
            starter = random.choice(self.starters)
            sentence = f"{starter} {element}"
            original_plot.append(sentence)
        
        # Generate second half of the story (with new unrelated plot points)
        new_plot = []
        for i in range(midpoint, total_sentences):
            # Select a random new element
            element = random.choice(self.new_elements)
            # Add a starter phrase to make it more natural
            starter = random.choice(self.starters)
            sentence = f"{starter} {element}"
            new_plot.append(sentence)
        
        # Combine both halves to form the complete story
        full_story = original_plot + new_plot
        
        return " ".join(full_story)


# Example usage:
if __name__ == "__main__":
    storyteller = MemoryLossStoryteller()
    story = storyteller.tell_story(10)
    print(story)
