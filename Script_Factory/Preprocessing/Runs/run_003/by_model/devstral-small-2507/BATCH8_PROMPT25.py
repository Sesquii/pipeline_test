def loop():
    """
    This function creates a self-referential infinite loop.
    It calls itself repeatedly under a condition that is always true,
    resulting in an infinite recursion.
    """
    print("Entered self-referential infinite loop")
    # Call itself with a condition that is always true
    while True:
        loop()

if __name__ == "__main__":
    loop()