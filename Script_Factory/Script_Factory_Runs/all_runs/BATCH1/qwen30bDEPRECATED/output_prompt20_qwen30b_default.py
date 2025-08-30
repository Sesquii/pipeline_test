import requests
from bs4 import BeautifulSoup
import random

def scrape_news_headlines():
    """Scrape headlines from BBC News."""
    try:
        url = "https://www.bbc.com/news"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find headline elements (adjust selectors as needed)
        headlines = []
        for item in soup.find_all('h3'):
            text = item.get_text(strip=True)
            if len(text) > 10:  # Filter out very short texts
                headlines.append(text)
                
        # If not enough headlines, fallback to hardcoded list
        if len(headlines) < 5:
            raise Exception("Not enough headlines found")
            
        return headlines[:10]  # Return first 10
        
    except Exception as e:
        # Fallback to hardcoded headlines in case of scraping failure
        return [
            "Global leaders meet in emergency summit",
            "New study reveals health benefits of chocolate",
            "Tech giant announces major breakthrough in AI",
            "Weather forecast predicts unusual conditions",
            "Local school wins national competition"
        ]

def generate_fake_headline():
    """Generate a fictional headline using fake fragments."""
    adjectives = ["mysterious", "surprising", "unbelievable", "shocking", "extraordinary", "bizarre"]
    verbs = ["discovered", "uncovered", "revealed", "found", "identified", "developed"]
    nouns = ["phenomenon", "secret", "truth", "evidence", "solution", "mystery"]
    
    adj = random.choice(adjectives)
    verb = random.choice(verbs)
    noun = random.choice(nouns)
    
    # Create a fake headline using structure: "Adjective Noun Verb"
    return f"{adj.capitalize()} {noun} {verb} in latest study"

def mix_headlines(real_headlines, fake_headline_func):
    """Mix real and fake headlines randomly."""
    mixed = []
    
    for _ in range(10):
        choice = random.randint(1, 3)
        
        if choice == 1:
            # Real headline
            if real_headlines:
                mixed.append(random.choice(real_headlines))
            else:
                mixed.append("Breaking: Unexpected event occurs")
        elif choice == 2:
            # Fake headline
            mixed.append(fake_headline_func())
        else:
            # Hybrid (combine real and fake parts)
            real = random.choice(real_headlines) if real_headlines else "News"
            fake_part = fake_headline_func().split()[0]  # Get first word of fake
            mixed.append(f"{fake_part} {real}")
    
    return mixed

def main():
    """Main function to generate and print 10 mixed headlines."""
    real_headlines = scrape_news_headlines()
    fake_headline_func = generate_fake_headline
    
    mixed_headlines = mix_headlines(real_headlines, fake_headline_func)
    
    for i, headline in enumerate(mixed_headlines, 1):
        print(f"{i}. {headline}")

if __name__ == "__main__":
    main()
