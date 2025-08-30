# BATCH6_PROMPT23_Granite.py
import cmd

class ChattyCLI(cmd.Cmd):
    intro = 'Welcome to the Chatty Command Line Interface! Type help or ? to list commands.\n'
    prompt = '(Chatty CLI)>'

    def do_greet(self, arg):
        """Overly verbose greeting command."""
        print("Greetings, human! I perceive you have invoked the 'greet' command. How utterly thrilling!")

    def do_status(self, arg):
        """Unhelpful status check."""
        print("I'm checking... Nope, nothing to report. The universe is ticking along as it always does.")

    def do_quit(self, arg):
        """Exit the program."""
        return True  # Returning True signifies we want to exit

def main():
    ChattyCLI().cmdloop()

if __name__ == "__main__":
    main()