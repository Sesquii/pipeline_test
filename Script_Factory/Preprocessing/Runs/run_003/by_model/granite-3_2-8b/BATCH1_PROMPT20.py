import requests
from bs4 import BeautifulSoup
import random
import time

# List of real news sites for scraping
NEWS_SITES = ['https://www.bbc.com/', 'https://edition.cnn.com/', 'https://www.reuters.com/']

# Hard-coded list of real headlines as fallback
FALLBACK_HEADLINES = [
    "Scientists Discover New Planet",
    "Historical Agreement Signed Between Nations",
    "Tech Giant Unveils Revolutionary Product",
    "Unprecedented Natural Phenomenon Observed",
    "Legendary Athlete Retires After Decades of Success"
]

# Lists for generating fake headlines
ADJECTIVES = ["mysterious", "surprising", "unbelievable", "shocking", "remarkable"]
NOUNS = ["discovery", "phenomenon", "agreement", "product", "retirement", "event", "crime", "victory"]
VERBS = ["reveals", "unfolds", "announces", "debuts", "ends", "sparks", "investigates", "achieves"]

def get_real_headlines(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        soup = BeautifulSoup(response.text, 'html.parser')
        headlines = [h3.text for h3 in soup.find_all('h3', class_=lambda x: x and 'gs-c-promo-heading__title' in x)]
        return headlines
    except requests.RequestException as e:
        print(f"Error fetching headlines from {url}: {e}")
        return []

def generate_fake_headline():
    adjective = random.choice(ADJECTIVES)
    noun = random.choice(NOUNS)
    verb = random.choice(VERBS)
    return f"{adjective} {noun} {verb}."

def mix_headlines(real_headlines, fake_headlines):
    mixed_headlines = []
    for _ in range(10):
        if not real_headlines:
            mixed_headlines.append(generate_fake_headline())
        else:
            choice = random.choice([True, False])  # Randomly decide to use a real or fake headline
            if choice and real_headlines:
                mixed_headlines.append(random.choice(real_headlines))
            elif not choice:
                mixed_headlines.append(generate_fake_headline())
    return mixed_headlines

def main():
    all_headlines = []
    
    for site in NEWS_SITES:
        headlines = get_real_headlines(site)
        if headlines:
            all_headlines.extend(headlines)
    
    # Fallback to hard-coded headlines if no real ones were fetched
    if not all_headlines:
        all_headlines = FALLBACK_HEADLINES

    mixed_headlines = mix_headlines(all_headlines, [])  # No fake headlines needed in this case

    for headline in mixed_headlines:
        print(headline)
    
    time.sleep(2)  # Avoid rapid-fire printing

if __name__ == "__main__":
    main()