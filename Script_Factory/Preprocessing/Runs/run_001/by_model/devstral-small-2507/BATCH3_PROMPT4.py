import os
import re

# Simple positive and negative word lists for sentiment analysis
POSITIVE_WORDS = {'happy', 'joy', 'love', 'excellent', 'great', 'fantastic'}
NEGATIVE_WORDS = {'sad', 'angry', 'hate', 'terrible', 'bad', 'awful'}

def analyze_sentiment(text):
    """Analyze the sentiment of a given text based on word counts."""
    words = re.findall(r'\b\w+\b', text.lower())
    positive_count = sum(1 for word in words if word in POSITIVE_WORDS)
    negative_count = sum(1 for word in words if word in NEGATIVE_WORDS)

    if positive_count > negative_count:
        return 'positive'
    elif negative_count > positive_count:
        return 'negative'
    else:
        return 'neutral'

def rename_file_based_on_sentiment(filepath):
    """Rename a file based on its sentiment analysis."""
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
        
        sentiment = analyze_sentiment(content)
        
        if sentiment == 'positive':
            new_name = os.path.splitext(filepath)[0] + '_happy' + os.path.splitext(filepath)[1]
        elif sentiment == 'negative':
            new_name = os.path.splitext(filepath)[0] + '_sad' + os.path.splitext(filepath)[1]
        else:
            new_name = filepath  # No change for neutral sentiment

        if new_name != filepath:
            os.rename(filepath, new_name)
            print(f"Renamed '{filepath}' to '{new_name}' based on {sentiment} sentiment")
        else:
            print(f"No rename needed for '{filepath}' (neutral sentiment)")

    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Example usage
    test_file = 'test_sentiment.txt'  # Replace with your actual file path

    # Create a sample file for testing (remove this in production)
    sample_content_positive = "I feel happy and joyful today. Everything is fantastic!"
    sample_content_negative = "I am so angry and sad about everything. This is terrible."
    sample_content_neutral = "The weather is nice. I went to the store."

    # Write test files
    with open('test_happy.txt', 'w') as f:
        f.write(sample_content_positive)
    with open('test_sad.txt', 'w') as f:
        f.write(sample_content_negative)
    with open('test_neutral.txt', 'w') as f:
        f.write(sample_content_neutral)

    # Test the renaming function
    rename_file_based_on_sentiment('test_happy.txt')
    rename_file_based_on_sentiment('test_sad.txt')
    rename_file_based_on_sentiment('test_neutral.txt')

    # Clean up test files (optional)
    for f in ['test_happy_happy.txt', 'test_sad_sad.txt', 'test_neutral.txt']:
        if os.path.exists(f):
            os.remove(f)