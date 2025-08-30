import requests
from bs4 import BeautifulSoup
import random

# Define hardcoded headlines (for fallback)
# hardcoded_headlines = [
#     "A major earthquake hits Japan, causing widespread damage.",
#     "New study reveals surprising findings on climate change impact.",
#     "Government announces new policy to address rising inflation."
# ]

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

# ===== GENERATED TESTS =====
import pytest
from unittest.mock import patch, MagicMock

# Original script code
import requests
from bs4 import BeautifulSoup
import random

# hardcoded_headlines = [
#     "A major earthquake hits Japan, causing widespread damage.",
#     "New study reveals surprising findings on climate change impact.",
#     "Government announces new policy to address rising inflation."
# ]

def scrape_real_news():
    try:
        response = requests.get('https://www.bbc.com/news', timeout=10)
        if response.status_code != 200:
            return hardcoded_headlines
        soup = BeautifulSoup(response.text, 'html.parser')
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

# Test cases
def test_scrape_real_news_success(mocker):
#     """Test successful scraping of news."""
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.text = "<html><body><h1>Headline 1</h1><h1>Headline 2</h1></body></html>"
    mocker.patch('requests.get', return_value=mock_response)
    headlines = scrape_real_news()
    assert len(headlines) == 2
    assert "Headline 1" in headlines and "Headline 2" in headlines

def test_scrape_real_news_failure(mocker):
#     """Test failure to scrape news."""
    mock_response = MagicMock()
    mock_response.status_code = 404
    mocker.patch('requests.get', return_value=mock_response)
    headlines = scrape_real_news()
    assert len(headlines) == 3
    assert all(h in hardcoded_headlines for h in headlines)

def test_generate_fake_headline():
#     """Test generation of fake headline."""
    fake_headline = generate_fake_headline()
    assert isinstance(fake_headline, str)
    assert any(fragment in fake_headline for fragment in ["mysterious", "surprising", "unbelievable", "strange", "fascinating"])
    assert any(noun in fake_headline for noun in ["event", "story", "incident", "report", "case"])
    assert any(verb in fake_headline for verb in ["revealed", "reported", "discovered", "confirmed", "unveiled"])

def test_generate_fake_headlines():
#     """Test generation of multiple fake headlines."""
    fake_headlines = generate_fake_headlines(5)
    assert len(fake_headlines) == 5
    assert all(isinstance(h, str) for h in fake_headlines)

if __name__ == "__main__":
    pytest.main()
