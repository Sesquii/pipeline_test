import requests
from bs4 import BeautifulSoup
import random

def fetch_real_headlines():
    """Fetch real news headlines from BBC News."""
    try:
        response = requests.get("https://www.bbc.com/news", timeout=5)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        headlines = []
        # Look for common headline selectors
        for item in soup.find_all(['h3', 'h2'], class_=['gs-c-promo-heading__title', 'media__title']):
            text = item.get_text(strip=True)
            if text and len(text) > 10:
                headlines.append(text)
        return headlines[:10]  # Return first 10 valid headlines
    except Exception as e:
        print(f"Warning: Failed to fetch real headlines: {e}")
        # Fallback list of hard-coded headlines
        return [
            "Global leaders meet in emergency summit",
            "New study reveals climate change impacts",
            "Tech giant announces major acquisition",
            "Sports stars celebrate championship win",
            "Health experts warn of new virus strain",
            "Economy shows signs of recovery",
            "Scientists discover new species in rainforest",
            "International trade agreement signed",
            "Major film festival opens with star-studded premiere",
            "Renewable energy investment hits record high"
        ]

def generate_fake_fragment():
    """Generate a fake headline fragment."""
    adjectives = ["mysterious", "surprising", "unbelievable", "shocking", "incredible", "strange", "weird", "odd"]
    verbs = ["suddenly", "unexpectedly", "rapidly", "swiftly", "gradually", "incredibly"]
    nouns = ["government", "scientists", "animals", "technology", "population", "economy", "climate", "people"]
    
    fragment = random.choice(adjectives) + " " + random.choice(verbs) + " " + random.choice(nouns)
    return fragment

def create_fictional_headline():
    """Create a completely fictional headline."""
    prefixes = ["Scientists", "Experts", "Researchers", "Government", "World leaders"]
    actions = ["discover", "find", "uncover", "reveal", "confirm"]
    objects = ["new energy source", "ancient artifact", "hidden disease", "secret treaty", "unknown planet"]
    
    prefix = random.choice(prefixes)
    action = random.choice(actions)
    obj = random.choice(objects)
    
    return f"{prefix} {action} {obj}"

def generate_mixed_headlines(real_headlines, count=10):
    """Generate a mix of real, fake, and hybrid headlines."""
    mixed = []
    
    for _ in range(count):
        choice = random.randint(1, 3)
        
        if choice == 1:  # Real headline
            headline = random.choice(real_headlines)
        elif choice == 2:  # Fictional headline
            headline = create_fictional_headline()
        else:  # Hybrid - mix real and fake
            fake = generate_fake_fragment()
            real = random.choice(real_headlines)
            # Combine them in a plausible way
            parts = real.split()
            if len(parts) > 2:
                idx = random.randint(0, len(parts)-1)
                parts[idx] = fake
                headline = " ".join(parts)
            else:
                headline = f"{fake} {real}"
        
        mixed.append(headline)
    
    # Shuffle the headlines to ensure randomness
    random.shuffle(mixed)
    return mixed

def main():
    """Main function to generate and print 10 mixed news headlines."""
    real_headlines = fetch_real_headlines()
    headlines = generate_mixed_headlines(real_headlines, 10)
    
    for i, headline in enumerate(headlines, 1):
        print(f"{i}. {headline}")

if __name__ == "__main__":
    main()
