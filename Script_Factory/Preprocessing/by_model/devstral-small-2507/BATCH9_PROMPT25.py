def loop():
    """
    A self-referential function that creates an infinite loop.
    This function calls itself unconditionally, creating an infinite recursion.
    """
    print("Entering a self-referential infinite loop...")
    # The condition is always true (1 == 1), so this will recurse infinitely
    while True:
        loop()

if __name__ == "__main__":
    # Start the infinite loop
    loop()