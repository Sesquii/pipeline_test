import hashlib

def generate_password(data):
    """
    Generates a password based on user's publicly available data.
    
    Args:
        data (str): The public data to base the password on.
        
    Returns:
        str: A generated password.
    """
    # Hash the data using SHA-256
    hashed_data = hashlib.sha256(data.encode()).hexdigest()
    
    # Convert the first 8 characters of the hash into a readable format
    password = hashed_data[:8]
    
    return password

if __name__ == "__main__":
    # Example public data (replace this with actual user data)
    public_data = "JohnDoe123"  # Replace with actual data
    
    # Generate and print the password
    generated_password = generate_password(public_data)
    print(f"Generated Password: {generated_password}")