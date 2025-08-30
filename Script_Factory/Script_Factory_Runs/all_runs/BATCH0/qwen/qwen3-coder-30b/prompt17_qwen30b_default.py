import sys
import time
import random
import argparse
from datetime import datetime

# Try to import yfinance and playsound
try:
    import yfinance as yf
except ImportError:
    print("Error: yfinance module is required. Please install it with 'pip install yfinance'")
    sys.exit(1)

try:
    from playsound import playsound
    HAS_PLAYSOUND = True
except ImportError:
    HAS_PLAYSOUND = False
    print("Warning: playsound module not found. Using console alarm instead.")

def get_stock_price(ticker):
    """
    Fetch the current price of a stock using yfinance.
    
    Args:
        ticker (str): Stock ticker symbol (e.g., 'AAPL')
        
    Returns:
        float: Current stock price or None if error
    """
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        # Get the current price from the info dictionary
        # If regularMarketPrice is not available, try previousClose
        price = info.get('regularMarketPrice') or info.get('previousClose')
        return price
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
        return None

def generate_target_price(current_price):
    """
    Generate a random target price within ±10% of the current price.
    
    Args:
        current_price (float): The current stock price
        
    Returns:
        float: A random target price
    """
    # Calculate 10% of the current price
    ten_percent = current_price * 0.10
    
    # Generate a random value between -10% and +10%
    random_change = random.uniform(-ten_percent, ten_percent)
    
    # Return the target price
    return current_price + random_change

def play_alarm_sound():
    """
    Play an alarm sound if playsound is available.
    Otherwise, print a console message.
    """
    if HAS_PLAYSOUND:
        try:
            # You can change this to point to your own sound file
            # For now, we'll use a simple approach that tries to play a sound
            # If no sound file is found, it will raise an exception
            playsound('alarm.mp3')  # This will fail if the file doesn't exist
        except:
            print("BOOM! (No alarm sound file found)")
    else:
        print("BOOM!")

def main(ticker, interval=30):
    """
    Main function to run the stock alarm clock.
    
    Args:
        ticker (str): Stock ticker symbol
        interval (int): Polling interval in seconds (default: 30)
    """
    print(f"Starting arbitrary alarm clock for {ticker}")
    print(f"Polling every {interval} seconds")
    print("Press Ctrl+C to stop")
    
    # Get the current price
    current_price = get_stock_price(ticker)
    if current_price is None:
        print("Could not fetch stock data. Exiting.")
        return
    
    print(f"Current price: ${current_price:.2f}")
    
    # Generate a random target price
    target_price = generate_target_price(current_price)
    print(f"Target price: ${target_price:.2f}")
    
    # Loop until the price hits or exceeds the target
    while True:
        try:
            # Get the live price
            live_price = get_stock_price(ticker)
            
            if live_price is None:
                print("Could not fetch live price. Retrying...")
                time.sleep(interval)
                continue
            
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Live price: ${live_price:.2f}")
            
            # Check if the target has been reached
            if live_price >= target_price:
                print("\nTarget price reached!")
                play_alarm_sound()
                break
                
            # Wait for the next check
            time.sleep(interval)
            
        except KeyboardInterrupt:
            print("\nProgram interrupted by user.")
            break
        except Exception as e:
            print(f"Unexpected error: {e}")
            time.sleep(interval)

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Arbitrary Stock Alarm Clock")
    parser.add_argument("ticker", nargs='?', default="AAPL",
                       help="Stock ticker symbol (default: AAPL)")
    parser.add_argument("--interval", "-i", type=int, default=30,
                       help="Polling interval in seconds (default: 30)")
    
    # Parse arguments
    args = parser.parse_args()
    
    # Run the main program
    main(args.ticker, args.interval)
