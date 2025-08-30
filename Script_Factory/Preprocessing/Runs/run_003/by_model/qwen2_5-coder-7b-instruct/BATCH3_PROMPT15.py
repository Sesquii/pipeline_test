import sys

def main():
    print("Welcome to the Chatty Command Line Interface! How can I help you today?")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("I'm sorry to see you go. Have a great day!")
            break
        else:
            print(f"I found that for you, human! The file is now at your fingertips.")
            print(f"That was indeed helpful, wasn't it? {user_input} was just what I needed.")
            print(f"You know, I could've done even more to assist you. Did you see my latest features?")

if __name__ == "__main__":
    main()