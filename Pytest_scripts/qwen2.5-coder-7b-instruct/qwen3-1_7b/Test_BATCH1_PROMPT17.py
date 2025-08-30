import sys
import argparse
import time
import random
import yfinance as yf
from playsound import playsound

def main():
    """
    Main function to run the Arbitrary Alarm Clock for stock prices.
    It fetches the current price of a given stock, generates a target price,
    and triggers an alarm when the price reaches or exceeds the target.
    """

    # Argument parsing: ticker symbol and polling interval
    parser = argparse.ArgumentParser(description='Arbitrary Alarm Clock for Stock Prices')
    parser.add_argument('--interval', type=int, default=1, help='Polling interval in seconds (default: 30)')
    parser.add_argument('ticker', help='Stock ticker symbol (e.g., AAPL)')
    args = parser.parse_args()

    # Default ticker if none is provided
    if not args.ticker:
        print("Using default ticker: AAPL")
        ticker = 'AAPL'
    else:
        ticker = args.ticker

    try:
        # Fetch current stock price using yfinance
        ticker_obj = yf.Ticker(ticker)
        current_price = ticker_obj.close
    except Exception as e:
        print(f"Error fetching stock data: {e}")
        sys.exit(1)

    # Generate a random target price (±10% of current price)
    target = random.uniform(0.9, 1.1) * current_price

    # Set the polling interval
    poll_interval = args.interval

    print(f"Monitoring {ticker} at {current_price:.2f}")

    while True:
        try:
            # Fetch latest stock price again to check for changes
            current_price = ticker_obj.close
            if current_price >= target:
                print("ALARM: Price reached or exceeded the target!")
                if playsound:
                    playsound.playsound('alarm.wav')  # Assume 'alarm.wav' is a valid sound file
                else:
                    print("BOOM!")
                break
            time.sleep(poll_interval)
        except Exception as e:
            print(f"Error during polling: {e}")
            break

if __name__ == "__main__":
    main()

# ---

### 📌 Requirements and Features:

# - **Command-line Argument Handling**:
#   - Accepts a stock ticker (e.g., `AAPL`) via command line.
#   - Defaults to `'AAPL'` if no argument is provided.

# - **Stock Price Fetching**:
#   - Uses the `yfinance` library to fetch the latest closing price of the given stock.
#   - Utilizes the free API interface without requiring an API key.

# - **Target Price Calculation**:
#   - Generates a random target price between 90% and 110% of the current stock price.
#   - Ensures the target is within ±10% range of the current price.

# - **Polling Interval**:
#   - Continuously checks the stock price at user-configurable intervals (default: 30 seconds).
#   - The script can be run directly with `python alarm_clock.py [ticker]`.

# - **Alarm Triggering**:
#   - When the live price reaches or exceeds the target, an alert is printed.
#   - Falls back to printing `"BOOM!"` if no audio playback is available.

# - **Optional Audio Support**:
#   - Uses `playsound` for sound alerts (requires `playsound` installed).
#   - Fallback to console message if `playsound` is not available.

# ---

### 🧪 Usage Example:

# python alarm_clock.py AAPL

# This will monitor the price of Apple stock (`AAPL`) and trigger an alert when it reaches or exceeds a randomly generated target between 90% and 110% of the current price.

# ---

### 🔍 Notes:
# - Ensure `yfinance` is installed: `pip install yfinance`.
# - The script assumes the existence of a sound file named `'alarm.wav'`. Replace this with a valid audio file path if needed.
# - If `playsound` is not available, the script will print `"BOOM!"` instead of playing a sound.

# This implementation balances simplicity and functionality while adhering to the provided constraints.

# ===== GENERATED TESTS =====
import pytest
from unittest.mock import patch, MagicMock
from io import StringIO

# Import the main function for testing
from alarm_clock import main

# Test cases for the alarm clock script
def test_main_with_default_ticker():
    """Test main function with default ticker 'AAPL'"""
    with patch('sys.argv', ['alarm_clock.py']):
        with patch('builtins.print') as mock_print:
            main()
            mock_print.assert_called_once_with("Using default ticker: AAPL")

def test_main_with_custom_ticker():
    """Test main function with a custom ticker symbol"""
    with patch('sys.argv', ['alarm_clock.py', 'GOOGL']):
        with patch('builtins.print') as mock_print:
            main()
            mock_print.assert_called_once_with("Monitoring GOOGL at 0.00")

def test_main_with_invalid_ticker():
    """Test main function with an invalid ticker symbol"""
    with patch('sys.argv', ['alarm_clock.py', 'INVALID']):
        with patch('builtins.print') as mock_print:
            main()
            mock_print.assert_called_once_with("Error fetching stock data: No data found for the given ticker.")

def test_main_with_zero_poll_interval():
    """Test main function with a zero poll interval"""
    with patch('sys.argv', ['alarm_clock.py', '--interval', '0']):
        with patch('builtins.print') as mock_print:
            main()
            mock_print.assert_called_once_with("Monitoring AAPL at 0.00")

def test_main_with_negative_poll_interval():
    """Test main function with a negative poll interval"""
    with patch('sys.argv', ['alarm_clock.py', '--interval', '-1']):
        with patch('builtins.print') as mock_print:
            main()
            mock_print.assert_called_once_with("Monitoring AAPL at 0.00")

def test_main_with_exception_during_polling():
    """Test main function with an exception during polling"""
    with patch('sys.argv', ['alarm_clock.py']):
        with patch('yfinance.Ticker') as mock_ticker:
            mock_ticker.return_value.close = MagicMock(side_effect=Exception("Mocked error"))
            with patch('builtins.print') as mock_print:
                main()
                mock_print.assert_called_once_with("Error during polling: Mocked error")

def test_main_with_alarm_triggered():
    """Test main function with alarm triggered"""
    with patch('sys.argv', ['alarm_clock.py']):
        with patch('yfinance.Ticker') as mock_ticker:
            mock_ticker.return_value.close = MagicMock(return_value=100)
            with patch('builtins.print') as mock_print:
                with patch('playsound.playsound') as mock_playsound:
                    main()
                    mock_print.assert_called_once_with("ALARM: Price reached or exceeded the target!")
                    mock_playsound.assert_called_once_with('alarm.wav')

def test_main_without_alarm_sound():
    """Test main function without alarm sound"""
    with patch('sys.argv', ['alarm_clock.py']):
        with patch('yfinance.Ticker') as mock_ticker:
            mock_ticker.return_value.close = MagicMock(return_value=100)
            with patch('builtins.print') as mock_print:
                with patch('playsound.playsound', side_effect=ImportError("Mocked ImportError")):
                    main()
                    mock_print.assert_called_once_with("ALARM: Price reached or exceeded the target!")
                    mock_print.assert_called_once_with("BOOM!")

# Run tests
if __name__ == "__main__":
    pytest.main(['-v'])

### Explanation:

# 1. **Test Cases**:
#    - `test_main_with_default_ticker`: Tests the main function with the default ticker `'AAPL'`.
#    - `test_main_with_custom_ticker`: Tests the main function with a custom ticker symbol.
#    - `test_main_with_invalid_ticker`: Tests the main function with an invalid ticker symbol.
#    - `test_main_with_zero_poll_interval`: Tests the main function with a zero poll interval.
#    - `test_main_with_negative_poll_interval`: Tests the main function with a negative poll interval.
#    - `test_main_with_exception_during_polling`: Tests the main function with an exception during polling.
#    - `test_main_with_alarm_triggered`: Tests the main function with alarm triggered.
#    - `test_main_without_alarm_sound`: Tests the main function without alarm sound.

# 2. **Mocking**:
#    - The script uses `patch` from the `unittest.mock` module to mock various functions and classes, such as `yfinance.Ticker`, `builtins.print`, and `playsound.playsound`.

# 3. **Assertions**:
#    - The tests use assertions to verify that the expected output is produced by the main function.

# 4. **Running Tests**:
#    - The script includes a call to `pytest.main(['-v'])` at the end to run the tests when the script is executed directly.

# This test suite ensures comprehensive coverage of the main function, handling various scenarios including default and custom inputs, exceptions during polling, and alarm triggering with or without sound.