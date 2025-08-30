import random

class MemoryLossStoryteller:
    def __init__(self):
        self.plot_points = []

    def _generate_original_plot(self, count):
        plot_elements = [
            "In a quaint village nestled between rolling hills",
            "A mysterious old mansion stood alone on the outskirts",
            "An ancient artifact was discovered in a local archaeological site",
            "Rumors of ghosts haunting the nearby forest began to circulate",
            "A renowned scientist moved into town with an unusual interest in local legends"
        ]
        return [random.choice(plot_elements) for _ in range(count)]

    def _generate_random_sentence(self):
        sentences = [
            "Suddenly, everything changed.",
            "No one could have predicted this turn of events.",
            "It was as if time itself had been rewritten.",
            "The world seemed to shift on its axis.",
            "A new chapter began with an unexpected twist."
        ]
        return random.choice(sentences)

    def tell_story(self, total_sentences: int) -> str:
        story = []

        # Generate original plot points
        original_plot = self._generate_original_plot(min(total_sentences // 2, len([
            "In a small town, a peculiar antique shop opened",
            "A secret society was rumored to meet in the old library",
            "Strange occurrences started happening after midnight",
            "An unexpected inheritance brought two strangers together",
            "A forgotten diary revealed shocking family secrets"
        ]))
        story.extend(original_plot)

        # Simulate amnesia by forgetting initial plot points and generating new unrelated sentences
        for _ in range(total_sentences // 2, total_sentences):
            story.append(self._generate_random_sentence())
        
        return ' '.join(story)

# Example usage:
if __name__ == "__main__":
    teller = MemoryLossStoryteller()
    print(teller.tell_story(10))