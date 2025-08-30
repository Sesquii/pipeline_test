import os
from nltk.corpus import positive_words
from nltk.tokenize import word_tokenize

# Ensure you have downloaded NLTK's positive words dataset
# nltk.download('positive')

def count_positive_words(text):
    """Count the number of positive words in a given text."""
    positive_set = set(positive_words.words())
    words = word_tokenize(text)
    return sum(1 for word in words if word.lower() in positive_set)

def rename_file(filename, sentiment_score):
    """Rename file based on sentiment score."""
    new_name = f"{os.path.splitext(filename)[0]}_{sentiment_score}.txt"
    os.rename(filename, new_name)

def main():
    # Input and output directory
    input_dir = "path_to_input_directory"  # Replace with your directory
    output_dir = "path_to_output_directory"  # Replace with your directory

    for filename in os.listdir(input_dir):
        if filename.endswith(".txt"):
            input_file = os.path.join(input_dir, filename)
            with open(input_file, 'r', encoding='utf-8') as f:
                text = f.read()
            
            sentiment_score = count_positive_words(text)

            # Define a simple threshold for renaming the file
            if sentiment_score > 10:  # You can adjust this threshold
                new_name = f"{filename}_{sentiment_score}"
                output_file = os.path.join(output_dir, new_name + ".txt")
                
                rename_file(input_file, str(sentiment_score))
                print(f"Renamed '{filename}' to '{new_name}'")

if __name__ == "__main__":
    main()