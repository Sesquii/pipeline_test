import requests
from bs4 import BeautifulSoup
import random

# Function to collect real news headlines from BBC
def collect_real_headlines():
    url = "https://www.bbc.com/news"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        headlines = [item.text.strip() for item in soup.find_all('h3')]
        return headlines
    else:
        # Fallback to hard-coded real headlines
        return ["Breaking News: Earthquake Shakes World",
                "Tech Giant Launches Revolutionary Product",
                "New Study Reveals Shocking Health Discovery"]

# Function to generate fake headline fragments
def generate_fake_headlines():
    adjectives = ["mysterious", "surprising", "unbelievable"]
    nouns = ["event", "discovery", "phenomenon", "occurrence", "incident"]
    verbs = ["happened", "took place", "transpired", "unfolded", "revealed"]
    fake_headlines = [f"A {random.choice(adjectives)} {noun} that {random.choice(verbs)}" for _ in range(5)]
    return fake_headlines

# Function to mix real and fake headlines
def mix_headlines(real_headlines, fake_headlines):
    all_headlines = real_headlines + fake_headlines
    random.shuffle(all_headlines)
    return all_headlines

# Main function to print mixed headlines
def main():
    real_headlines = collect_real_headlines()
    fake_headlines = generate_fake_headlines()
    mixed_headlines = mix_headlines(real_headlines, fake_headlines)
    
    for headline in mixed_headlines[:10]:
        print(headline)

# Execute the main function if the script is run directly
if __name__ == "__main__":
    main()