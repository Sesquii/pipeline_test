import random

class MemoryLossStoryteller:
    """
    A storyteller that simulates memory loss by forgetting previous plot points
    halfway through generating a story.
    """

    def __init__(self):
        # List of possible sentence starters for original plot
        self.original_starters = [
            "In the beginning,",
            "Once upon a time,",
            "As the sun set,",
            "Meanwhile, in another part of town,",
            "Years later,"
        ]

        # List of possible sentence starters for new plot after memory loss
        self.new_starters = [
            "Suddenly, something entirely different happened:",
            "In a completely unrelated event,",
            "Meanwhile, in a distant land,",
            "As if starting anew,",
            "Without any connection to before,"
        ]

        # List of possible sentence endings for both plot types
        self.endings = [
            "the adventure began.",
            "a mystery unfolded.",
            "destiny called their name.",
            "unexpected challenges awaited.",
            "new friendships were forged."
        ]

    def _generate_sentence(self, is_original: bool) -> str:
        """
        Generate a single sentence based on whether it's part of the original plot
        or the new plot after memory loss.

        Args:
            is_original (bool): True if this sentence is part of the original plot,
                                False if it's part of the new plot

        Returns:
            str: A generated sentence
        """
        starters = self.original_starters if is_original else self.new_starters
        starter = random.choice(starters)
        ending = random.choice(self.endings)

        # Generate a simple sentence structure
        return f"{starter} {ending}"

    def tell_story(self, total_sentences: int) -> str:
        """
        Generate a story with memory loss effect at the midpoint.

        Args:
            total_sentences (int): Total number of sentences in the story

        Returns:
            str: The complete story as a single string with sentences separated by newlines
        """
        if total_sentences < 1:
            return ""

        # Calculate midpoint where memory loss occurs
        midpoint = total_sentences // 2

        # Generate sentences for the original plot (before memory loss)
        original_plot = [
            self._generate_sentence(is_original=True)
            for _ in range(midpoint)
        ]

        # Generate sentences for the new plot (after memory loss)
        new_plot = [
            self._generate_sentence(is_original=False)
            for _ in range(total_sentences - midpoint)
        ]

        # Combine both plots with a clear indication of memory loss
        story_lines = original_plot + ["\n--- Memory Loss Occurs ---\n"] + new_plot

        # Join all sentences into a single string separated by newlines
        return "\n".join(story_lines)

# Example usage
if __name__ == "__main__":
    storyteller = MemoryLossStoryteller()
    story = storyteller.tell_story(10)
    print("Generated Story:")
    print(story)