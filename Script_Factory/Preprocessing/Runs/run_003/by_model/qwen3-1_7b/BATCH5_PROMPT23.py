```python
import random

class QuantumLogger:
    def __init__(self):
        pass  # No state needed

    def log(self, message):
        if random.random() < 0.5:
            with open('logger.log', 'a') as f:
                f.write(f"{message}\n")
            return message
        else:
            contradict = "Contradict: " + message
            with open('logger.log', 'a') as f:
                f.write(f"{contradict}\n")
            return contradict

if __name__ == "__main__":
    logger = QuantumLogger()
    logger.log("Hello")
    logger.log("World")