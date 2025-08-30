import hashlib
from datetime import datetime

def generate_password():
    # Get the current timestamp as a string
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    
    # Hash the timestamp using SHA-256 to ensure the password is secure and varied
    hashed_password = hashlib.sha256(timestamp.encode()).hexdigest()
    
    # Return the first 10 characters of the hash as the password
    return hashed_password[:10]

def main():
    # Generate and print a new password every minute
    while True:
        password = generate_password()
        print(f"Current timestamp-based password: {password}")
        # Wait for one minute before generating the next password
        time.sleep(60)

if __name__ == "__main__":
    import time
    main()
```

This Python program uses the `hashlib` library to securely hash the current timestamp, which changes every second. The first 10 characters of the hash are used as the password. The program runs in an infinite loop, generating and printing a new password every minute.