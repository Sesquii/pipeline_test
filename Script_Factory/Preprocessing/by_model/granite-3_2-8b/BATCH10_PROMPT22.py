import random
import time

def generate_story():
    """Generates a simple story with plot twists."""

    plot_twists = [
        "Suddenly, the protagonist discovers an old letter hidden in the attic.",
        "The seemingly ordinary object turns out to be a magical artifact.",
        "It was revealed that the friend was actually an undercover agent.",
        "A mysterious stranger offers them a deal they can't refuse.",
        "They stumble upon a secret passage leading to an unknown part of the house."
    ]

    story = f"Once upon a time, there was a person named Alex. They lived in a big old house. One day, while cleaning the attic, " \
            f"Alex found {random.choice(plot_twists)}. This event changed their life forever.\n\n"
    return story

def memory_loss_storyteller():
    """Storyteller that forgets its plot every five sentences."""

    stories = []  # Keep track of told stories to avoid repetition

    while True:
        new_story = generate_story()

        for _ in range(5):
            print(new_story, end='')
            time.sleep(1)  # Slow down the narration

            if _ < 4:
                new_story = generate_story()  # Add a new twist to keep the story going

        # Forgetting the plot after five sentences
        stories.append(new_story)

        print("\n--- New Story ---\n")

if __name__ == "__main__":
    memory_loss_storyteller()