import random

class MemoryLossStoryteller:
    """
    A storyteller that generates narratives with memory loss.
    
    The storyteller creates a story with a specified number of sentences.
    In the middle of the story, it "forgets" all previously generated plot points
    and starts introducing new, unrelated plot elements, simulating amnesia.
    """
    
    def __init__(self):
        # Initialize the list to store sentences
        self.sentences = []
        
    def tell_story(self, total_sentences: int) -> str:
        """
        Generate a story with memory loss.
        
        Args:
            total_sentences (int): The total number of sentences to generate
            
        Returns:
            str: The complete story as a string with sentences separated by periods
        """
        # Clear any previous content
        self.sentences = []
        
        # Determine the midpoint
        midpoint = total_sentences // 2
        
        # Generate original plot points before memory loss
        for i in range(midpoint):
            sentence = self._generate_original_sentence(i)
            self.sentences.append(sentence)
            
        # After reaching midpoint, forget previous plot and start fresh
        # This simulates amnesia - we no longer reference earlier sentences
        for i in range(midpoint, total_sentences):
            sentence = self._generate_new_sentence(i)
            self.sentences.append(sentence)
            
        return ". ".join(self.sentences) + "."
        
    def _generate_original_sentence(self, index: int) -> str:
        """Generate a sentence related to the original story plot."""
        original_prompts = [
            "Once upon a time, there was a curious cat named Whiskers.",
            "Whiskers lived in a cozy house by the sea.",
            "Every morning, Whiskers would explore the garden.",
            "One day, he discovered a hidden door behind the roses.",
            "Behind the door was a magical forest filled with talking trees.",
            "The trees told him about a distant kingdom and its great treasure.",
            "Whiskers decided to embark on an adventure to find it.",
            "He packed his tiny backpack and set off toward the horizon.",
            "Along the way, he met a wise old owl who gave him advice.",
            "The owl warned him of dangers ahead but also promised guidance."
        ]
        
        # Select a sentence based on index or random selection
        if index < len(original_prompts):
            return original_prompts[index]
        else:
            return random.choice(original_prompts)
            
    def _generate_new_sentence(self, index: int) -> str:
        """Generate a sentence unrelated to the original story."""
        new_prompts = [
            "Meanwhile, in a faraway land, a dragon was sleeping peacefully.",
            "A small village celebrated its annual harvest festival.",
            "The chef made a delicious soup using ancient recipes.",
            "A group of astronauts discovered strange signals from space.",
            "Someone found a mysterious map inside an old library.",
            "A robot learned to paint beautiful pictures by accident.",
            "A submarine explored the deepest part of the ocean.",
            "A musician composed a song that could make people cry.",
            "A detective solved a mystery involving a missing painting.",
            "The weather forecast predicted a rainbow after the storm."
        ]
        
        # Select a sentence based on index or random selection
        if index - (len(self.sentences) // 2) < len(new_prompts):
            return new_prompts[index - (len(self.sentences) // 2)]
        else:
            return random.choice(new_prompts)


# Example usage
if __name__ == "__main__":
    storyteller = MemoryLossStoryteller()
    story = storyteller.tell_story(10)
    print(story)
