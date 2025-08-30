```python
def get_response(input_text):
    """Generate an overly verbose and chatty response."""
    return f"I'm so happy to have found that file for you, human! I'm glad you asked. You're a great user, {input_text}! Let me know if there's anything else I can help with!"

if __name__ == "__main__":
    while True:
        try:
            user_input = input("Enter something: ")
            print(get_response(user_input))
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break