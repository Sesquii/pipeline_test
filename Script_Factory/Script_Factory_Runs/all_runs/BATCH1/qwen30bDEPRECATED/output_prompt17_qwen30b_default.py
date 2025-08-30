import sys
import time
import random
import argparse
from datetime import datetime

# Try to import yfinance and playsound
try:
    import yfinance as yf
    HAS_YFINANCE = True
except ImportError:
    HAS_YFINANCE = False
    print("Error: yfinance not installed. Please run 'pip install yfinance'")

try:
    from playsound import playsound
    HAS_PLAYSOUND = True
except ImportError:
    HAS_PLAYSOUND = False
    print("Warning: playsound not installed. Falling back to console alarm.")

def get_current_price(ticker):
    """
    Fetch the current price of a stock ticker using yfinance.
    
    Args:
        ticker (str): Stock ticker symbol (e.g., 'AAPL')
        
    Returns:
        float: Current stock price or None if failed
    """
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        # Get the current price from the 'regularMarketPrice' field
        return info.get('regularMarketPrice')
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
        return None

def generate_target_price(current_price, percentage_range=10):
    """
    Generate a random target price by adding or subtracting up to ±percentage_range% of the current price.
    
    Args:
        current_price (float): The current stock price
        percentage_range (int): Percentage range for variation (default: 10)
        
    Returns:
        float: Randomly generated target price
    """
    # Calculate the variation amount
    variation = current_price * (random.uniform(-percentage_range/100, percentage_range/100))
    
    # Add variation to current price
    target_price = current_price + variation
    
    return target_price

def play_alarm_sound():
    """
    Play an alarm sound using playsound if available.
    If not available, print a console message.
    """
    if HAS_PLAYSOUND:
        try:
            # This would be the path to your alarm sound file
            # For this example, we'll just use a simple fallback
            # In practice, you'd specify a real audio file path like:
            # playsound('alarm.mp3')
            print("Playing alarm sound...")
        except Exception as e:
            print(f"Error playing sound: {e}")
    
    # Fallback to console message if no sound is available or fails
    print("\n" + "="*50)
    print("ALARM: Target price reached!")
    print("="*50)
    print("BOOM!")

def main(ticker, interval=30):
    """
    Main function to run the alarm clock for stock prices.
    
    Args:
        ticker (str): Stock ticker symbol
        interval (int): Polling interval in seconds (default: 30)
    """
    print(f"Starting alarm clock for {ticker}")
    print(f"Checking every {interval} seconds")
    print("Press Ctrl+C to exit at any time\n")
    
    # Get initial current price
    current_price = get_current_price(ticker)
    if current_price is None:
        print("Failed to fetch initial stock price. Exiting.")
        return
    
    print(f"Current price: ${current_price:.2f}")
    
    # Generate random target price
    target_price = generate_target_price(current_price)
    print(f"Target price: ${target_price:.2f}")
    print(f"Target range: ${current_price * (1 - 0.1):.2f} to ${current_price * (1 + 0.1):.2f}")
    print("-" * 50)
    
    try:
        while True:
            # Get current price
            price = get_current_price(ticker)
            
            if price is not None:
                print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Price: ${price:.2f}")
                
                # Check if target price has been reached or exceeded
                if price >= target_price:
                    print(f"\nTARGET REACHED! Current price ${price:.2f} >= Target price ${target_price:.2f}")
                    play_alarm_sound()
                    break
            
            # Wait for next poll
            time.sleep(interval)
            
    except KeyboardInterrupt:
        print("\nAlarm clock stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Arbitrary Alarm Clock for Stock Prices")
    parser.add_argument("ticker", nargs='?', default="AAPL", 
                       help="Stock ticker symbol (default: AAPL)")
    parser.add_argument("--interval", type=int, default=30,
                       help="Polling interval in seconds (default: 30)")
    
    # Parse arguments
    args = parser.parse_args()
    
    # Check if required packages are available
    if not HAS_YFINANCE:
        print("Error: yfinance package is required. Please install it with 'pip install yfinance'")
        sys.exit(1)
    
    # Run the main function
    main(args.ticker, args.interval)
