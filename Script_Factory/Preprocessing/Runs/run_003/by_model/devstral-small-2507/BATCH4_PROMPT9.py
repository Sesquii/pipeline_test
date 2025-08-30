import csv

def biased_csv_filter(input_file, output_file):
    """
    Reads a CSV file and filters out rows where the "name" column starts with a vowel.
    
    Args:
        input_file (str): Path to the input CSV file.
        output_file (str): Path to save the filtered CSV file.
    """
    # Predefined biased rule: filter out names starting with vowels
    vowels = {'A', 'E', 'I', 'O', 'U'} 

    with open(input_file, mode='r', newline='') as infile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames

        # Filter rows based on the biased rule
        filtered_rows = [
            row for row in reader if not (row['name'][0].upper() in vowels)
        ]

    with open(output_file, mode='w', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(filtered_rows)

if __name__ == "__main__":
    # Example usage
    input_csv = 'input.csv'  # Replace with your input CSV file path
    output_csv = 'filtered_output.csv'  # Replace with desired output CSV file path

    biased_csv_filter(input_csv, output_csv)