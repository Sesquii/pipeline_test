import csv
import random

def generate_broken_csv(filename):
    """
    Generates a CSV file with intentional formatting errors.

    Args:
        filename (str): The name of the CSV file to create.
    """
    # Define some sample data - 10 rows with 5 columns each
    data = [
        ["Name", "Age", "Email", "City", "Country"],
        ['John Doe', '29', 'john.doe@example.com', 'New York', 'USA'],
        ['Jane Smith', '34', 'jane.smith@example.com', 'London', 'UK'],
        ['Bob Johnson', 45, 'bob.johnson@example.com', 'Toronto', 'Canada'],
        ['Alice Brown', '28', 'alice.brown@example.com', 'Sydney', 'Australia'],
        ['Charlie Davis', '31', 'charlie.davis@example.com', 'Berlin', 'Germany'],
        ['Eve Wilson', 40, 'eve.wilson@example.com', 'Paris', 'France'],
        ['Frank Miller', '25', 'frank.miller@example.com', 'Tokyo', 'Japan'],
        ['Grace Lee', 37, 'grace.lee@example.com', 'Seoul', 'South Korea'],
        ['Henry Clark', '29', 'henry.clark@example.com', 'Mexico City', 'Mexico']
    ]

    # Introduce errors
    data[2][1] = 34  # Mixing quotes and no quotes in Age column
    data[7][3] = "Berlin, Germany"  # Inconsistent number of columns - extra field
    data[8].append("Extra field with quotes")  # Another inconsistent row length

    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        for row in data:
            if random.random() < 0.3:  # 30% chance of introducing an error
                # Randomly skip quotes or add extra commas
                if random.random() < 0.5:
                    row[random.randint(0, len(row)-1)] = str(row[random.randint(0, len(row)-1)]) + ",extra"
                else:
                    row.pop(random.randint(0, len(row)-1))  # Remove a field to create inconsistent columns

            writer.writerow(row)

if __name__ == "__main__":
    generate_broken_csv("broken_data.csv")
    print("Broken CSV file 'broken_data.csv' has been generated with intentional errors.")