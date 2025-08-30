def loop():
    """
    This function calls itself under a condition that is always true,
    creating a self-referential infinite loop.
    """
    print("Entering self-referential infinite loop...")
    loop()  # Recursive call to the same function

if __name__ == "__main__":
    loop()