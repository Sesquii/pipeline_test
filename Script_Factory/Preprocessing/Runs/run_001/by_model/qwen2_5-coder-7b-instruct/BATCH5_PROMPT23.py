import random

class QuantumLogger:
    def __init__(self):
        self.state = None

    def collapse(self):
        if self.state is None:
            self.state = random.choice([True, False])

    def log(self, message):
        self.collapse()
        if self.state:
            with open('log.txt', 'a') as file:
                file.write(message + '\n')
        else:
            with open('contra_log.txt', 'a') as file:
                file.write("Contradictory: " + message + '\n')

if __name__ == "__main__":
    logger = QuantumLogger()
    messages = ["State is collapsed", "Superposition rules"]
    for msg in messages:
        logger.log(msg)