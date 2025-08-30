def loop():
    """
    This function calls itself continuously under a condition that is always true.
    """
    while True:  # The condition 'True' ensures this loop never terminates
        print("Entered self-referential infinite loop.")

if __name__ == "__main__":
    loop()