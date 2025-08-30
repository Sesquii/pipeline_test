import random

class DataDrivenPasswordGenerator:
    def __init__(self):
        # Hard-coded list of common names and places for password generation
        self.common_names = [
            'Alice', 'Bob', 'Charlie', 'David', 'Eve',
            'Frank', 'Grace', 'Heidi', 'Ivan', 'Judy'
        ]
        self.common_places = [
            'London', 'Paris', 'NewYork', 'Tokyo', 'Sydney',
            'Berlin', 'Rome', 'Moscow', 'Cairo', 'RioDeJaneiro'
        ]

    def generate_password(self):
        # Randomly select a name and place
        name = random.choice(self.common_names)
        place = random.choice(self.common_places)

        # Create password by combining name, place and some numbers
        number_part = str(random.randint(1000, 9999))
        special_char = random.choice(['!', '@', '#', '$', '%'])

        # Format the password as: NamePlaceNumberSpecialChar
        password = f"{name}{place}{number_part}{special_char}"

        return password

if __name__ == "__main__":
    generator = DataDrivenPasswordGenerator()
    password = generator.generate_password()
    print(f"Generated Password: {password}")