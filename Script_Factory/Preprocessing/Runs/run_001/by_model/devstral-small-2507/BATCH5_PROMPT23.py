import random

class QuantumLogger:
    def __init__(self):
        self.state = None  # This represents the superposition state

    def log(self, message):
        # Collapse the superposition to a definite state (0 or 1)
        self.state = random.choice([True, False])

        if self.state:
            print(f"Logged: {message}")
        else:
            contradictory_message = "CONTRADICTORY_MESSAGE"  # Replace with actual logic
            print(f"Logged: {contradictory_message}")

if __name__ == "__main__":
    logger = QuantumLogger()

    messages = ["First message", "Second message", "Third message"]

    for msg in messages:
        logger.log(msg)