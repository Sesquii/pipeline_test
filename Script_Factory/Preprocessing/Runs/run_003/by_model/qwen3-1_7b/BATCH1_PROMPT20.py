```python
import requests
from bs4 import BeautifulSoup
import random

# Define hardcoded headlines (for fallback)
hardcoded_headlines = [
    "A major earthquake hits Japan, causing widespread damage.",
    "New study reveals surprising findings on climate change impact.",
    "Government announces new policy to address rising inflation."
]

def scrape_real_news():
    try:
        response = requests.get('https://www.bbc.com/news', timeout=10)
        if response.status_code != 200:
            return hardcoded_headlines
        soup = BeautifulSoup(response.text, 'html.parser')
        # Find all h1 elements (or other tags)
        headlines = []
        for item in soup.find_all('h1'):
            headlines.append(item.get_text(strip=True))
        return headlines
    except Exception as e:
        print(f"Error scraping news: {e}")
        return hardcoded_headlines

def generate_fake_headline():
    fake_fragments = ["mysterious", "surprising", "unbelievable", "strange", "fascinating"]
    noun = random.choice(['event', 'story', 'incident', 'report', 'case'])
    verb = random.choice(['revealed', 'reported', 'discovered', 'confirmed', 'unveiled'])
    return f"{random.choice(fake_fragments)} {noun} {verb}"

def generate_fake_headlines(num=10):
    return [generate_fake_headline() for _ in range(num)]

def main():
    real_headlines = scrape_real_news()
    fake_headlines = generate_fake_headlines(10)
    # Now, mix them unpredictably
    for _ in range(10):
        choice = random.choice(['real', 'fake', 'hybrid'])
        if choice == 'real':
            print(random.choice(real_headlines))
        elif choice == 'fake':
            print(random.choice(fake_headlines))
        else:  # hybrid
            real = random.choice(real_headlines)
            fake = random.choice(fake_headlines)
            print(f"{real} {fake}")

if __name__ == "__main__":
    main()