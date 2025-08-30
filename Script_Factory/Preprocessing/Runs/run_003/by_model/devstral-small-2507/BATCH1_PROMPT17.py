Here's a complete Python script that implements an Arbitrary Alarm Clock for stock prices:

```python
import time
import random
import sys
from yahoo_finance_api2 import share
import yfinance as yf

def get_live_price(ticker):
    """Get the live price of a given ticker symbol using yfinance."""
    try:
        stock = yf.Ticker(ticker)
        historical_data = stock.history(period="1d", interval="1m")
        if not historical_data.empty:
            return historical_data['Close'].iloc[-1]
        else:
            raise ValueError(f"Could not retrieve price data for {ticker}")
    except Exception as e:
        print(f"Error retrieving price for {ticker}: {e}")
        sys.exit(1)

def generate_target_price(current_price):
    """Generate a random target price by adding or subtracting up to ±10% of the current price."""
    percentage_change = random.uniform(-0.1, 0.1)
    return current_price * (1 + percentage_change)

def trigger_alarm():
    """Trigger an alarm by printing a message and optionally playing a sound."""
    print("BOOM! Target price reached!")
    # Uncomment the following line if you have playsound installed and want to play a sound
    # from playsound import playsound
    # playsound('alarm_sound.mp3')

def main():
    """Main function to run the Arbitrary Alarm Clock for stock prices."""
    if len(sys.argv) > 1:
        ticker = sys.argv[1]
    else:
        ticker = "AAPL"  # Default ticker symbol

    interval = 30  # Default polling interval in seconds
    if len(sys.argv) > 2:
        try:
            interval = int(sys.argv[2])
        except ValueError:
            print("Invalid interval. Using default value of 30 seconds.")
    
    print(f"Monitoring {ticker} for price changes...")
    current_price = get_live_price(ticker)
    print(f"Current price: ${current_price:.2f}")

    target_price = generate_target_price(current_price)
    print(f"Target price set to: ${target_price:.2f}")

    while True:
        live_price = get_live_price(ticker)
        print(f"Live price: ${live_price:.2f}")
        
        if live_price >= target_price:
            trigger_alarm()
            break

        time.sleep(interval)

if __name__ == "__main__":
    main()
```

### Usage Example:
```bash
# Run with default ticker (AAPL) and 30-second interval
python arbitrary_alarm_clock.py

# Run with custom ticker (MSFT) and 60-second interval
python arbitrary_alarm_clock.py MSFT 60
```

### Notes:
1. This script uses the `yfinance` library to fetch live stock prices.
2. It generates a random target price by adding or subtracting up to ±10% of the current price.
3. The script continuously polls the ticker at user-configurable intervals (default: 30 seconds).
4. When the live price reaches or exceeds the target price, it triggers an alarm by printing "BOOM!" and optionally playing a sound file if `playsound` is available.

### Dependencies:
- Install required packages with:
```bash
pip install yfinance playsound
```

The script includes clear comments explaining each step and provides a brief usage example in the comments.