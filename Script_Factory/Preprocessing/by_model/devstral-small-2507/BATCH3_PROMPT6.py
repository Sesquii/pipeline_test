# BATCH3_PROMPT6_Devstral.py

import random

class DataDrivenPasswordGenerator:
    def __init__(self):
        # Common names and places for password generation
        self.common_names = ["Alice", "Bob", "Charlie", "David", "Eve"]
        self.common_places = ["London", "Paris", "NewYork", "Tokyo", "Berlin"]
        self.common_animals = ["Dog", "Cat", "Bird", "Fish", "Horse"]

    def generate_password(self):
        """Generate a password based on common data"""
        name = random.choice(self.common_names).lower()
        place = random.choice(self.common_places).lower()
        animal = random.choice(self.common_animals).lower()

        # Combine elements with special characters and numbers
        password_elements = [
            name,
            "123",
            place[0].upper() + place[1:],
            "@#$",
            animal.capitalize(),
            str(random.randint(10, 99))
        ]

        # Shuffle the elements to create variety
        random.shuffle(password_elements)

        # Join all elements to form the password
        password = ''.join(password_elements)
        return password

if __name__ == "__main__":
    generator = DataDrivenPasswordGenerator()
    password = generator.generate_password()
    print(f"Generated password: {password}")