```python
def loop():
    while True:
        print("Entering self-referential infinite loop")
        loop()

if __name__ == "__main__":
    loop()