# Define the function loop that calls itself under an always true condition
def loop():
    # Print a message indicating the start of the infinite loop
    print("Entered self-referential infinite loop.")
    # Call the loop function again, creating an infinite recursion
    loop()

# Entry point of the program
if __name__ == "__main__":
    # Start the infinite loop by calling the loop function
    loop()