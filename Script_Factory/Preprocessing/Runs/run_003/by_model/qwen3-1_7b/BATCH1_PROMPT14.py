```python
import random
import time

def delayed_chatbot(user_message):
    delay = random.randint(1, 5)
    time.sleep(delay)
    return "Here is your response!"

if __name__ == "__main__":
    print(delayed_chatbot("Hello"))