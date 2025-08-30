# BATCH10_PROMPT18_Devstral.py

import random

def generate_seven_word_sentences(num_sentences):
    """
    Generates a list of sentences where each sentence contains exactly seven words.

    Args:
        num_sentences (int): The number of sentences to generate

    Returns:
        list: A list containing the generated sentences
    """
    # Define word categories with example words
    subjects = ["The cat", "A boy", "She", "They", "He", "We", "The dog"]
    verbs = ["ran", "jumped", "sang", "danced", "laughed", "cried", "whispered"]
    objects = ["quickly", "happily", "sadly", "quietly", "loudly", "softly", "bravely"]
    prepositions = ["to", "from", "with", "without", "over", "under", "through"]
    nouns = ["the house", "a tree", "the moon", "a river", "mountains", "stars", "friends"]
    conjunctions = ["and", "but", "or", "yet", "so", "for", "nor"]
    adverbs = ["happily", "sadly", "quietly", "loudly", "bravely", "softly", "quickly"]

    sentences = []
    for _ in range(num_sentences):
        # Construct a sentence with exactly 7 words
        subject = random.choice(subjects)
        verb = random.choice(verbs)
        obj1 = random.choice(objects)
        prep = random.choice(prepositions)
        noun = random.choice(nouns)
        conj = random.choice(conjunctions)
        adv = random.choice(adverbs)

        sentence = f"{subject} {verb} {obj1} {prep} {noun} {conj} {adv}."
        sentences.append(sentence)

    return sentences

def main():
    # Number of sentences to generate
    num_sentences = 10

    # Generate the sentences
    story = generate_seven_word_sentences(num_sentences)

    # Print the story
    print("Short Story with Seven-Word Sentences:")
    for sentence in story:
        print(sentence)

if __name__ == "__main__":
    main()