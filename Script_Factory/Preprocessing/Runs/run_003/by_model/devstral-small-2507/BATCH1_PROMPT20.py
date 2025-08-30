import requests
from bs4 import BeautifulSoup
import random

def scrape_real_headlines():
    """Scrape real news headlines from BBC front page"""
    url = "https://www.bbc.com/news"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        headlines = []
        for item in soup.find_all('h3'):
            text = item.get_text(strip=True)
            if text and len(text) > 5:
                headlines.append(text)
        return headlines[:10]  # Return top 10 headlines
    except Exception as e:
        print(f"Error scraping headlines: {e}")
        return [
            "Breaking: Unusual weather patterns continue",
            "Local community comes together for charity event",
            "New technology promises to revolutionize industry",
            "Political leaders meet for historic summit",
            "Economic trends show signs of improvement"
        ]

def generate_fake_fragments():
    """Generate fake headline fragments"""
    adjectives = ["mysterious", "surprising", "unbelievable", "shocking", "incredible"]
    nouns = ["discovery", "event", "phenomenon", "development", "situation"]
    verbs = ["occurs", "happens", "takes place", "emerges", "unfolds"]

    fake_adjectives = [f"In {adj.capitalize()}" for adj in adjectives]
    fake_nouns = [f"{noun.capitalize()} Stuns Experts" for noun in nouns]
    fake_verbs = [f"What Happens When It {verb.capitalize()}?" for verb in verbs]

    return {
        "adjectives": fake_adjectives,
        "nouns": fake_nouns,
        "verbs": fake_verbs
    }

def generate_fake_headline(fragments):
    """Generate a completely fake headline"""
    fragment_type = random.choice(["adjective", "noun", "verb"])
    return random.choice(fragments[fragment_type])

def mix_headlines(real_headlines, fake_fragments):
    """Mix real and fake headlines unpredictably"""
    mixed = []
    for i in range(10):
        if i % 3 == 0:
            # Real headline
            mixed.append(random.choice(real_headlines))
        elif i % 3 == 1:
            # Fake headline  
            mixed.append(generate_fake_headline(fake_fragments))
        else:
            # Hybrid headline (blend real and fake)
            real = random.choice(real_headlines)
            fake = generate_fake_headline(fake_fragments)
            if random.choice([True, False]):
                mixed.append(f"{fake} - {real}")
            else:
                mixed.append(f"{real} | {fake}")

    # Shuffle to remove any predictable pattern
    random.shuffle(mixed)
    return mixed

def main():
    """Main function to generate and print mixed headlines"""
    real_headlines = scrape_real_headlines()
    fake_fragments = generate_fake_fragments()
    mixed_headlines = mix_headlines(real_headlines, fake_fragments)

    for headline in mixed_headlines:
        print(headline)
    
if __name__ == "__main__":
    main()