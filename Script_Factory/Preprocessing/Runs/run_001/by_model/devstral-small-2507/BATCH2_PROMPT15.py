# BATCH2_PROMPT15_Devstral.py

import os

def find_file(filename):
    """Search for a file in the current directory and return its path if found."""
    try:
        # Check if file exists in current directory
        if os.path.isfile(filename):
            return os.path.abspath(filename)
        else:
            raise FileNotFoundError(f"File '{filename}' not found in current directory.")
    except Exception as e:
        raise e

def main():
    """Main function to handle user interaction."""
    print("Welcome to the overly chatty file finder! I'm here to help you locate files.")
    while True:
        try:
            # Get filename from user
            filename = input("\nPlease enter the name of the file you're looking for (or 'exit' to quit): ").strip()

            if filename.lower() == 'exit':
                print("Goodbye! Have a fantastic day!")
                break

            # Find the file
            file_path = find_file(filename)
            print(f"\nOh, what a joyous occasion! I've found the file you were looking for: {file_path}")
            print("I'm so happy to have been of service, human!")

        except FileNotFoundError as e:
            print(f"\nOh dear me! It seems that {e}. Let's try again, shall we?")
        except Exception as e:
            print(f"\nOh my goodness! Something went horribly wrong: {e}. But don't worry, I'm here to help!")

if __name__ == "__main__":
    main()