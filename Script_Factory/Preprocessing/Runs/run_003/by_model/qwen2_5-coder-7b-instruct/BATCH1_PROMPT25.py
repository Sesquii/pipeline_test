import random

class MemoryLossStoryteller:
    def tell_story(self, total_sentences: int) -> str:
        if total_sentences <= 0:
            raise ValueError("Total sentences must be greater than zero")
        
        story = []
        original_sentences = floor(total_sentences / 2)
        
        # Generate original plot points
        for i in range(1, original_sentences + 1):
            sentence = self.generate_original_sentence(i)
            story.append(sentence)
            
        # Simulate amnesia and generate new sentences
        for i in range(original_sentences + 1, total_sentences + 1):
            sentence = self.generate_new_sentence()
            story.append(sentence)
            
        return ' '.join(story)

    def generate_original_sentence(self, index: int) -> str:
        """Generate a sentence that represents an original plot point."""
        themes = ["A young hero on a quest", "A mysterious artifact", "An ancient prophecy"]
        actions = ["travels to the enchanted forest", "discovers hidden ruins", "receives guidance from an old sage"]
        return f"In part {index}, {random.choice(themes)} {random.choice(actions)}."
    
    def generate_new_sentence(self) -> str:
        """Generate a sentence that is unrelated to earlier plot points."""
        topics = ["The weather changes unexpectedly", "A random person appears", "An interesting coincidence"]
        descriptions = ["becoming increasingly foggy outside", "striking up a conversation with an unfamiliar stranger", "discovering a hidden treasure"]
        return f"In the latter half, {random.choice(topics)} {random.choice(descriptions)}."
        
# Example usage
storyteller = MemoryLossStoryteller()
print(storyteller.tell_story(10))