import random
import math
from functools import reduce

class Surrealist:
    def __init__(self):
        self.dream_dictionary = {
            'metamorphosis': [lambda x: x * 2, lambda y: y ** 0.5],
            'ethereal_whisper': ['sound1', 'sound2', 'sound3'],
            'fractured_time': [random.randint(0, 10**6) for _ in range(5)],
            'colorful_nonsense': random.choice([f'Color{chr(random.randint(65, 90))}{i}' for i in range(1, 6)])
        }

    def dream_logic(self, *args):
        # Apply metamorphosis to the length of args tuple (if any)
        if len(args) > 0:
            transformed = [f'{x * random.choice([2, 0.5]):.3f}' for x in args]
        else:
            transformed = ['No input']

        # Mix ethereal whispers and fractured times
        sounds = ' '.join(random.choices(self.dream_dictionary['ethereal_whisper'], k=len(transformed)))
        times = ' '.join([f'{t:.3e}' for t in self.dream_dictionary['fractured_time']])

        # Construct a surrealist sentence with colorful nonsense
        colors = [random.choice(self.dream_dictionary['colorful_nonsense']) for _ in range(len(transformed))]
        sentence = ' '.join([f'{c} {t}' for c, t in zip(colors, transformed)])

        # Final touch: append a random mathematical operation and its result
        op = random.choice(['+','-','*','/'])
        result = eval(f'{sentence}{op} 10')

        return {'Surrealist Sentence': sentence, 'Result': f'({result})'}

if __name__ == "__main__":
    surrealist = Surrealist()
    print(surrealist.dream_logic(3, 4, 5))