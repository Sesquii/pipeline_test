```python
import random

insults = [
    "You're so... *insert insult*...",
    "What's next?",
    "Why are you here?",
    "I'm done with this.",
    "You're a idiot.",
    "Don't even try to talk to me."
]

while True:
    user_input = input("Enter something: ")
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break
    print(random.choice(insults))