import pytest
from unittest.mock import patch, mock_open
import sys
from io import StringIO
from PIL import Image
import os

# Import the function to test
from Script_Factory.Script_Factory_Runs.all_runs.prompt19_qwen30b_default import main



from Script_Factory.Script_Factory_Runs.all_runs.prompt19_qwen30b_default import (
    main
)

def test_main_normal_case():
    """Test normal case with valid image file and parameters."""
    # Mock Image.open to return a mock image
    with patch('Script_Factory.Script_Factory_runs.all_runs.recipe.Image.open') as mock_image_open:
        # Create a mock image
        mock_img = mock_image_open.return_value.__enter__.return_value
        mock_img.width = 100
        mock_img.height = 50
        mock_img.convert.return_value = mock_img
        mock_img.resize.return_value = mock_img
        
        # Mock getpixel to return consistent values for testing
        def mock_getpixel(pos):
            x, y = pos
            # Create a pattern that will produce predictable ASCII output
            if (x + y) % 2 == 0:
                return 128  # Mid-gray
            else:
                return 0    # Black
        
        mock_img.getpixel.side_effect = mock_getpixel
        
        # Mock file operations
        with patch('builtins.open', new_callable=mock_open) as mock_file:
            # Capture stdout
            captured_output = StringIO()
            with patch('sys.stdout', captured_output):
                # Mock sys.argv to simulate command line arguments
                original_argv = sys.argv
                sys.argv = ['glitchy_ascii.py', '--input', 'test.jpg', '--width', '80']
                
                try:
                    main()
                finally:
                    sys.argv = original_argv
                
            # Verify output was written to file
            mock_file.assert_called_once_with('output.txt', 'w')
            
            # Verify some ASCII characters were written
            output_content = captured_output.getvalue()
            assert len(output_content) > 0
            assert '@' in output_content or '#' in output_content or '*' in output_content


def test_main_empty_image():
    """Test with an empty image (edge case)."""
    with patch('Script_Factory.Script_Factory_runs.all_runs.recipe.Image.open') as mock_image_open:
        mock_img = mock_image_open.return_value.__enter__.return_value
        mock_img.width = 0
        mock_img.height = 0
        mock_img.convert.return_value = mock_img
        
        # Mock getpixel to avoid errors
        mock_img.getpixel.return_value = 0
        
        with patch('builtins.open', new_callable=mock_open) as mock_file:
            captured_output = StringIO()
            with patch('sys.stdout', captured_output):
                original_argv = sys.argv
                sys.argv = ['glitchy_ascii.py', '--input', 'test.jpg']
                try:
                    main()
                finally:
                    sys.argv = original_argv
                
            output_content = captured_output.getvalue()
            # Should produce empty string for 0x0 image
            assert output_content == ""


def test_main_file_not_found():
    """Test error handling when input file doesn't exist."""
    with patch('Script_Factory.Script_Factory_runs.all_runs.recipe.Image.open') as mock_image_open:
        mock_image_open.side_effect = FileNotFoundError("No such file")
        
        captured_output = StringIO()
        with patch('sys.stderr', captured_output):
            original_argv = sys.argv
            sys.argv = ['glitchy_ascii.py', '--input', 'nonexistent.jpg']
            
            # Should exit with code 1 due to exception
            with pytest.raises(SystemExit) as exc_info:
                try:
                    main()
                finally:
                    sys.argv = original_argv
            
            assert exc_info.value.code == 1
            error_output = captured_output.getvalue()
            assert "not found" in error_output


def test_main_invalid_image():
    """Test error handling when image file is invalid."""
    with patch('Script_Factory.Script_Factory_runs.all_runs.recipe.Image.open') as mock_image_open:
        mock_image_open.side_effect = Exception("Invalid image format")
        
        captured_output = StringIO()
        with patch('sys.stderr', captured_output):
            original_argv = sys.argv
            sys.argv = ['glitchy_ascii.py', '--input', 'invalid.jpg']
            
            with pytest.raises(SystemExit) as exc_info:
                try:
                    main()
                finally:
                    sys.argv = original_argv
            
            assert exc_info.value.code == 1
            error_output = captured_output.getvalue()
            assert "Error processing image" in error_output


def test_main_width_zero():
    """Test with width parameter set to zero (edge case)."""
    with patch('Script_Factory.Script_Factory_runs.all_runs.recipe.Image.open') as mock_image_open:
        mock_img = mock_image_open.return_value.__enter__.return_value
        mock_img.width = 100
        mock_img.height = 50
        mock_img.convert.return_value = mock_img
        
        # Mock getpixel to return consistent values
        def mock_getpixel(pos):
            return 128  # Mid-gray
        
        mock_img.getpixel.side_effect = mock_getpixel
        
        with patch('builtins.open', new_callable=mock_open) as mock_file:
            captured_output = StringIO()
            with patch('sys.stdout', captured_output):
                original_argv = sys.argv
                sys.argv = ['glitchy_ascii.py', '--input', 'test.jpg', '--width', '0']
                
                try:
                    main()
                finally:
                    sys.argv = original_argv
                
            output_content = captured_output.getvalue()
            # Should still produce output, but with width 0
            assert len(output_content) > 0


def test_main_no_width_parameter():
    """Test when no width parameter is provided."""
    with patch('Script_Factory.Script_Factory_runs.all_runs.recipe.Image.open') as mock_image_open:
        mock_img = mock_image_open.return_value.__enter__.return_value
        mock_img.width = 100
        mock_img.height = 50
        mock_img.convert.return_value = mock_img
        
        # Mock getpixel to return consistent values
        def mock_getpixel(pos):
            return 128  # Mid-gray
        
        mock_img.getpixel.side_effect = mock_getpixel
        
        with patch('builtins.open', new_callable=mock_open) as mock_file:
            captured_output = StringIO()
            with patch('sys.stdout', captured_output):
                original_argv = sys.argv
                sys.argv = ['glitchy_ascii.py', '--input', 'test.jpg']
                
                try:
                    main()
                finally:
                    sys.argv = original_argv
                
            output_content = captured_output.getvalue()
            assert len(output_content) > 0


def test_main_custom_output_file():
    """Test with custom output file parameter."""
    with patch('Script_Factory.Script_Factory_runs.all_runs.recipe.Image.open') as mock_image_open:
        mock_img = mock_image_open.return_value.__enter__.return_value
        mock_img.width = 100
        mock_img.height = 50
        mock_img.convert.return_value = mock_img
        
        # Mock getpixel to return consistent values
        def mock_getpixel(pos):
            return 128  # Mid-gray
        
        mock_img.getpixel.side_effect = mock_getpixel
        
        with patch('builtins.open', new_callable=mock_open) as mock_file:
            captured_output = StringIO()
            with patch('sys.stdout', captured_output):
                original_argv = sys.argv
                sys.argv = ['glitchy_ascii.py', '--input', 'test.jpg', '--output', 'custom_output.txt']
                
                try:
                    main()
                finally:
                    sys.argv = original_argv
                
            # Verify custom output file was used
            mock_file.assert_called_once_with('custom_output.txt', 'w')
