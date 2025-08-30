Here's a Python script that meets your requirements:

```python
# Import necessary libraries
import sys
import time
import random
from yfinance import Ticker
from playsound import playsound

# If using playsound, ensure it's installed via pip install playsound

def get_stock_price(ticker):
    """Function to fetch the most recent price of a stock ticker"""
    try:
        stock = Ticker(ticker)
        latest_price = float(stock.info['regularMarketPrice'])
        return latest_price
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
        return None

def set_alarm(target_price, current_price):
    """Function to check if the current price meets the target and trigger alarm"""
    if current_price >= target_price:
        print("\nALARM! Target price reached!")
        if hasattr(sys, 'argv'):  # Check if running from command line
            playsound('alarm.wav')  # If playsound is installed, play a sound
        else:
            print("BOOM!")  # Fallback to console message

def main():
    """Main function"""

    # Set default interval and ticker (can be overridden by command-line args)
    interval = 30  # in seconds
    ticker = "AAPL"  # Hardcoded for this example, can be replaced with command line argument

    if len(sys.argv) > 1:
        ticker = sys.argv[1]  # Use first command line argument as ticker

    while True:
        current_price = get_stock_price(ticker)
        
        if current_price is None:
            continue  # Skip this iteration if there was an error fetching data

        # Generate random target price (between ±10% of the current price)
        target_percentage = random.uniform(-0.1, 0.1)
        target_price = current_price * (1 + target_percentage)
        
        set_alarm(target_price, current_price)

        # Wait for configured interval before next check
        time.sleep(interval)

if __name__ == "__main__":
    main()
```

Usage example:

To run the script and listen for alarms on Apple Inc. (AAPL):

1. Save this code in a file, e.g., `stock_alarm.py`.
2. Make sure you have `yfinance` and optionally `playsound` installed (`pip install yfinance playsound`).
3. Run the script with Python: `python stock_alarm.py AAPL` (or omit `AAPL` if you want to use the default).
4. The script will continuously check the price of AAPL every 30 seconds and sound an alarm when the price reaches or exceeds a randomly chosen target price (within ±10% of the current price). If `playsound` is installed, it'll play an audio alarm; otherwise, it will print "BOOM!" in the console.

**Note:** This script does not handle exceptions for non-existent tickers or network issues gracefully. For a production-ready application, you'd want to add more robust error handling and possibly a user interface for configuration.