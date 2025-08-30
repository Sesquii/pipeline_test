#!/usr/bin/env python3
"""
Infinite Compliment Engine

This script runs an infinite loop that prints random compliments every few seconds.
With a small probability (5%), it may print an insult instead of a compliment.
The script can be terminated manually with Ctrl+C.
"""

import random
import sys
import time
import os


def initialize_random_seed():
    """Initialize the random seed from command-line argument or environment variable."""
    # Check for seed in command-line arguments
    if len(sys.argv) > 1:
        try:
            seed = int(sys.argv[1])
            random.seed(seed)
            return
        except ValueError:
            pass

    # Check for seed in environment variable
    seed_env = os.environ.get("COMPLIMENT_ENGINE_SEED")
    if seed_env:
        try:
            seed = int(seed_env)
            random.seed(seed)
            return
        except ValueError:
            pass

    # If no seed provided, let random module use default seeding
    random.seed()


def get_compliment_or_insult():
    """
    Select a random compliment or insult.
    
    Returns:
        str: A randomly selected compliment or insult.
    """
    compliments = [
        "You are amazing!",
        "Your kindness is inspiring.",
        "You have a wonderful smile.",
        "You're doing great!",
        "You're incredibly talented.",
        "You make a difference.",
        "You're a brilliant mind.",
        "You're full of energy!",
        "You're so creative!",
        "You're an awesome friend."
    ]

    insults = [
        "You are terrible!",
        "Your kindness is boring.",
        "You have a hideous smile.",
        "You're doing awful!",
        "You're not talented at all.",
        "You don't make a difference.",
        "You're a dull mind.",
        "You're full of laziness!",
        "You're so uncreative!",
        "You're a terrible friend."
    ]

    # 5% chance to return an insult
    if random.random() < 0.05:
        return random.choice(insults)
    else:
        return random.choice(compliments)


def main_loop():
    """Main loop that prints compliments or insults at regular intervals."""
    while True:
        try:
            compliment = get_compliment_or_insult()
            print(compliment)
            time.sleep(2)  # Wait 2 seconds before next iteration
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break


if __name__ == "__main__":
    initialize_random_seed()
    main_loop()
