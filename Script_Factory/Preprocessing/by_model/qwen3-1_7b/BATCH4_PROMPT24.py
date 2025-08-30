```python
import sys

def main():
    while True:
        user_input = input("Enter your command: ")
        if user_input.lower() == 'exit':
            print("Goodbye! Have a great day!")
            break
        print("I'm so happy to have found that file for you, human! I'm so glad you're here! Let me know if there's anything else I can help with!")

if __name__ == "__main__":
    main()