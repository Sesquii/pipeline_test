```python
import argparse

def main():
    parser = argparse.ArgumentParser(description='Conversational CLI')
    parser.add_argument('--confirm', action='store_true', help='Trigger chatty confirmation')
    args = parser.parse_args()
    
    if args.confirm:
        print("Confirming... This is a chatty, unhelpful confirmation message.")
        # No further actions
    else:
        print("No confirmation needed.")

if __name__ == "__main__":
    main()