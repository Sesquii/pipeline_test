import sys
import time
import random
from unittest.mock import patch, MagicMock
import pytest
import sys, os

# Import the functions to test
from Script_Factory.Script_Factory_Runs.all_runs.prompt17_qwen30b_default import (

from Script_Factory.Script_Factory_Runs.all_runs.prompt17_qwen30b_default import (
    generate_target_price,
    get_stock_price,
    main,
    play_alarm_sound
)

    get_stock_price,
    generate_target_price,
    play_alarm_sound,
    main
)

def test_get_stock_price_valid_ticker():
    """Test fetching stock price with a valid ticker symbol"""
    # Mock yfinance functionality
    with patch('Script_Factory.Script_Factory_runs.all_runs.recipe.yf') as mock_yf:
        mock_ticker = MagicMock()
        mock_ticker.info = {'regularMarketPrice': 150.0}
        mock_yf.Ticker.return_value = mock_ticker
        
        result = get_stock_price("AAPL")
        assert result == 150.0

def test_get_stock_price_no_regular_market_price():
    """Test fetching stock price when regularMarketPrice is not available"""
    # Mock yfinance functionality
    with patch('Script_Factory.Script_Factory_runs.all_runs.recipe.yf') as mock_yf:
        mock_ticker = MagicMock()
        mock_ticker.info = {'previousClose': 145.0}
        mock_yf.Ticker.return_value = mock_ticker
        
        result = get_stock_price("AAPL")
        assert result == 145.0

def test_get_stock_price_error_handling():
    """Test error handling when fetching stock price fails"""
    # Mock yfinance to raise an exception
    with patch('Script_Factory.Script_Factory_runs.all_runs.recipe.yf') as mock_yf:
        mock_yf.Ticker.side_effect = Exception("Network error")
        
        result = get_stock_price("AAPL")
        assert result is None

def test_generate_target_price_normal_case():
    """Test generating target price with normal input"""
    current_price = 100.0
    result = generate_target_price(current_price)
    
    # Should be within Â±10% of the current price
    assert 90.0 <= result <= 110.0

def test_generate_target_price_edge_case_zero():
    """Test generating target price with zero as input"""
    current_price = 0.0
    result = generate_target_price(current_price)
    
    # Should be exactly 0 since 0 * 0.10 = 0
    assert result == 0.0

def test_generate_target_price_negative_price():
    """Test generating target price with negative input"""
    current_price = -100.0
    result = generate_target_price(current_price)
    
    # Should be within Â±10% of the current price
    assert -110.0 <= result <= -90.0

def test_play_alarm_sound_has_playsound():
    """Test playing alarm sound when playsound is available"""
    # Mock that playsound is available
    with patch('Script_Factory.Script_Factory_runs.all_runs.recipe.HAS_PLAYSOUND', True):
        with patch('Script_Factory.Script_Factory_runs.all_runs.recipe.playsound') as mock_playsound:
            play_alarm_sound()
            # Should call playsound function
            mock_playsound.assert_called_once()

def test_play_alarm_sound_no_playsound():
    """Test playing alarm sound when playsound is not available"""
    # Mock that playsound is not available
    with patch('Script_Factory.Script_Factory_runs.all_runs.recipe.HAS_PLAYSOUND', False):
        # Capture print output
        with patch('sys.stdout') as mock_stdout:
            play_alarm_sound()
            # Should print "BOOM!" to console
            mock_stdout.write.assert_called()

def test_main_valid_inputs():
    """Test main function with valid inputs"""
    # Mock all external dependencies
    with patch('Script_Factory.Script_Factory_runs.all_runs.recipe.get_stock_price') as mock_get_price, \
         patch('Script_Factory.Script_Factory_runs.all_runs.recipe.generate_target_price') as mock_gen_target, \
         patch('Script_Factory.Script_Factory_runs.all_runs.recipe.play_alarm_sound') as mock_play_sound:
        
        # Setup mocks
        mock_get_price.return_value = 150.0
        mock_gen_target.return_value = 160.0
        
        # Mock time.sleep to avoid actual delays in tests
        with patch('Script_Factory.Script_Factory_runs.all_runs.recipe.time.sleep'):
            # Mock datetime to return a fixed value
            with patch('Script_Factory.Script_Factory_runs.all_runs.recipe.datetime') as mock_datetime:
                mock_datetime.now.return_value.strftime.return_value = "2023-01-01 12:00:00"
                
                # Test with ticker and interval
                main("AAPL", 5)
                
                # Verify the calls were made
                mock_get_price.assert_called()
                mock_gen_target.assert_called()

def test_main_no_stock_data():
    """Test main function when stock data cannot be fetched"""
    # Mock get_stock_price to return None
    with patch('Script_Factory.Script_Factory_runs.all_runs.recipe.get_stock_price') as mock_get_price:
        mock_get_price.return_value = None
        
        # Capture print output
        with patch('sys.stdout') as mock_stdout:
            main("AAPL", 5)
            
            # Should print error message and exit
            assert "Could not fetch stock data" in str(mock_stdout.write.call_args)

def test_main_keyboard_interrupt():
    """Test main function handling of keyboard interrupt"""
    # Mock all external dependencies
    with patch('Script_Factory.Script_Factory_runs.all_runs.recipe.get_stock_price') as mock_get_price, \
         patch('Script_Factory.Script_Factory_runs.all_runs.recipe.generate_target_price') as mock_gen_target:
        
        # Setup mocks to raise KeyboardInterrupt after first call
        mock_get_price.side_effect = [150.0, 155.0]  # First call returns price, second raises exception
        mock_gen_target.return_value = 160.0
        
        # Mock time.sleep to avoid actual delays in tests
        with patch('Script_Factory.Script_Factory_runs.all_runs.recipe.time.sleep'):
            with patch('Script_Factory.Script_Factory_runs.all_runs.recipe.datetime') as mock_datetime:
                mock_datetime.now.return_value.strftime.return_value = "2023-01-01 12:00:00"
                
                # Test with keyboard interrupt
                with pytest.raises(KeyboardInterrupt):
                    main("AAPL", 5)
