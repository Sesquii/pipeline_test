import csv
import random

def generate_broken_csv(filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        
        # Generate data for CSV rows
        for _ in range(10):
            row = []
            for _ in range(5):
                data = random.choice([
                    'Field {}'.format(i),  # Valid field with numbering
                    random.randint(-100, 100),  # Random integer (could cause issues if negative)
                    "Field {} with special chars: !@#$%^&*()".format(i),  # Field with special characters
                    random.choice(['True', 'False']),  # Boolean value
                ])
                row.append(data)
            
            # Intentionally break CSV format in this row
            if random.random() < 0.5:  # 50% chance to introduce an error
                row = ['Error'] * len(row)
            
            writer.writerow(row)

if __name__ == "__main__":
    generate_broken_csv('broken_data.csv')