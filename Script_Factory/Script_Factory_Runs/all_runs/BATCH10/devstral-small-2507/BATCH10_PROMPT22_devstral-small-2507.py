# BATCH10_PROMPT22_{{model_name}}.py

import random

class MemoryLossStoryteller:
    def __init__(self):
        self.sentence_count = 0
        self.story_segments = []
        self.plot_elements = [
            "In a distant galaxy",
            "Once upon a time in a mystical forest",
            "Deep within the ocean's abyss",
            "High above the clouds in a floating city",
            "In the heart of a bustling medieval town"
        ]

    def generate_sentence(self):
        """Generate a random sentence based on current plot."""
        if self.sentence_count == 0:
            # Start a new story segment
            return random.choice(self.plot_elements) + ", "

        # Add some story progression
        progressions = [
            "a brave hero emerged.",
            "mysterious creatures appeared.",
            "ancient secrets were revealed.",
            "dangerous adventures began.",
            "unexpected alliances formed."
        ]
        return random.choice(progressions)

    def tell_story(self):
        """Tell a story that forgets the plot every 5 sentences."""
        while True:
            if self.sentence_count >= 5:
                # Forget the plot and start fresh
                print("\n(Forgetting the previous story...)")
                self.sentence_count = 0

            sentence = self.generate_sentence()
            print(sentence, end=" ")
            self.sentence_count += 1

            if "." in sentence:
                # Wait for user input after each complete sentence
                input("\nPress Enter to continue...")
                print()  # New line for next segment

if __name__ == "__main__":
    storyteller = MemoryLossStoryteller()
    print("Welcome to the Memory-Loss Storyteller!")
    print("The story will reset every 5 sentences.")
    input("Press Enter to begin...")

    try:
        storyteller.tell_story()
    except KeyboardInterrupt:
        print("\nStorytelling stopped. Goodbye!")