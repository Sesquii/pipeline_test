import os
from nltk.sentiment import SentimentIntensityAnalyzer


def analyze_sentiment(text):
    """
    Analyze sentiment of given text using NLTK's Vader Sentiment analyzer.

    Returns a dictionary with scores for positive, negative, neutral and compound (overall) sentiment.
    """
    sia = SentimentIntensityAnalyzer()
    return sia.polarity_scores(text)


def rename_file(file_path):
    """
    Read the content of a file, perform sentiment analysis, and rename the file based on its sentiment.

    If compound sentiment score is > 0.5 (more positive), append "_happy" to the filename.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    sentiment_scores = analyze_sentiment(content)
    compound_score = sentiment_scores['compound']

    if compound_score > 0.5:
        new_name = f"{os.path.splitext(file_path)[0]}_happy{os.path.splitext(file_path)[1]}"
        os.rename(file_path, new_name)


if __name__ == "__main__":
    # Specify the file path here
    file_to_rename = 'sample_text.txt'  # Change this to your desired filepath

    rename_file(file_to_rename)
    print(f"Renamed {file_to_rename} to {os.path.basename(file_to_rename)}.")