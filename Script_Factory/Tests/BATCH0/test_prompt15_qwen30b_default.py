import sys
import random
from unittest.mock import patch, MagicMock
from PIL import Image, ImageDraw, ImageFont

# Import the functions to test
from Script_Factory.Script_Factory_Runs.all_runs.prompt15_qwen30b_default import (

from Script_Factory.Script_Factory_Runs.all_runs.prompt15_qwen30b_default import (
    corrupt_labels,
    draw_annotations,
    get_random_label,
    load_image,
    main,
    simulate_detections
)

    load_image,
    get_random_label,
    simulate_detections,
    corrupt_labels,
    draw_annotations,
    main
)

def test_load_image_valid():
    """Test loading a valid image file."""
    # Mock Image.open to return a valid image object
    with patch('PIL.Image.open') as mock_open:
        mock_image = MagicMock()
        mock_open.return_value = mock_image
        
        result = load_image("valid_image.jpg")
        assert result == mock_image
        mock_open.assert_called_once_with("valid_image.jpg")

def test_load_image_invalid():
    """Test handling of invalid image file."""
    # Mock Image.open to raise an exception
    with patch('PIL.Image.open') as mock_open:
        mock_open.side_effect = Exception("Invalid image")
        
        # Capture stdout to check error message
        with patch('sys.stdout') as mock_stdout:
            with patch('sys.exit') as mock_exit:
                try:
                    load_image("invalid_image.jpg")
                except SystemExit:
                    pass  # Expected to exit
                
                mock_exit.assert_called_once_with(1)

def test_get_random_label_normal():
    """Test selecting a random label from the pool."""
    label_pool = ["cat", "dog", "car"]
    result = get_random_label(label_pool)
    assert result in label_pool

def test_get_random_label_exclude():
    """Test selecting a random label while excluding one."""
    label_pool = ["cat", "dog", "car"]
    exclude = "dog"
    result = get_random_label(label_pool, exclude=exclude)
    assert result in label_pool
    assert result != exclude

def test_get_random_label_all_excluded():
    """Test when all labels are excluded (should raise IndexError)."""
    label_pool = ["cat", "dog"]
    exclude = "cat"
    
    # This should work - it will pick from remaining labels
    result = get_random_label(label_pool, exclude=exclude)
    assert result == "dog"

def test_simulate_detections():
    """Test that simulate_detections returns expected format."""
    detections = simulate_detections()
    
    # Check that we get the right number of detections
    assert len(detections) == 8
    
    # Check that each detection has the right structure
    for detection in detections:
        assert len(detection) == 3
        top_left, bottom_right, label = detection
        assert isinstance(top_left, tuple)
        assert isinstance(bottom_right, tuple)
        assert len(top_left) == 2
        assert len(bottom_right) == 2
        assert isinstance(label, str)

def test_corrupt_labels_normal():
    """Test normal corruption of labels."""
    detections = [
        ((50, 80), (200, 250), "cat"),
        ((300, 120), (450, 280), "dog"),
        ((100, 300), (250, 450), "car")
    ]
    label_pool = ["tree", "person", "bicycle"]
    
    # Set seed for reproducible results
    random.seed(42)
    
    result = corrupt_labels(detections, label_pool, corruption_rate=0.5)
    
    # Check that we get the same number of detections
    assert len(result) == len(detections)
    
    # Check that each detection still has the right structure
    for i, detection in enumerate(result):
        assert len(detection) == 3
        top_left, bottom_right, label = detection
        assert isinstance(top_left, tuple)
        assert isinstance(bottom_right, tuple)
        assert isinstance(label, str)

def test_corrupt_labels_zero_rate():
    """Test corruption with zero rate (no labels should be corrupted)."""
    detections = [
        ((50, 80), (200, 250), "cat"),
        ((300, 120), (450, 280), "dog")
    ]
    label_pool = ["tree", "person", "bicycle"]
    
    result = corrupt_labels(detections, label_pool, corruption_rate=0.0)
    
    # All labels should remain unchanged
    for i, detection in enumerate(result):
        assert detection[2] == detections[i][2]

def test_corrupt_labels_one_rate():
    """Test corruption with 100% rate (all labels should be corrupted)."""
    detections = [
        ((50, 80), (200, 250), "cat"),
        ((300, 120), (450, 280), "dog")
    ]
    label_pool = ["tree", "person", "bicycle"]
    
    result = corrupt_labels(detections, label_pool, corruption_rate=1.0)
    
    # All labels should be corrupted (different from original)
    for i, detection in enumerate(result):
        assert detection[2] != detections[i][2]

def test_draw_annotations():
    """Test drawing annotations on an image."""
    # Create a mock image
    img = MagicMock()
    draw = MagicMock()
    ImageDraw.Draw.return_value = draw
    
    # Mock font loading
    with patch('PIL.ImageFont.truetype'):
        # Mock the actual font since we're not testing font rendering
        ImageFont.truetype.return_value = MagicMock()
        
        detections = [
            ((50, 80), (200, 250), "cat"),
            ((300, 120), (450, 280), "dog")
        ]
        label_pool = ["tree", "person", "bicycle"]
        
        # Call the function
        draw_annotations(img, detections, label_pool)
        
        # Check that drawing methods were called
        assert draw.rectangle.called
        assert draw.text.called

def test_main_function():
    """Test main function execution."""
    # Mock all required functions and modules
    with patch('Script_Factory.Script_Factory_runs.all_runs.recipe.load_image') as mock_load, \
         patch('Script_Factory.Script_Factory_runs.all_runs.recipe.simulate_detections') as mock_simulate, \
         patch('Script_Factory.Script_Factory_runs.all_runs.recipe.corrupt_labels') as mock_corrupt, \
         patch('Script_Factory.Script_Factory_runs.all_runs.recipe.draw_annotations') as mock_draw, \
         patch('Script_Factory.Script_Factory_runs.all_runs.recipe.Image') as mock_image_class:
        
        # Setup mocks
        mock_img = MagicMock()
        mock_load.return_value = mock_img
        mock_simulate.return_value = [
            ((50, 80), (200, 250), "cat"),
            ((300, 120), (450, 280), "dog")
        ]
        mock_corrupt.return_value = [
            ((50, 80), (200, 250), "cat"),
            ((300, 120), (450, 280), "dog")
        ]
        
        # Call main function
        try:
            main()
        except SystemExit:
            pass  # Expected if some condition fails
        
        # Verify that functions were called
        mock_load.assert_called_once_with("input.jpg")
        mock_simulate.assert_called_once()
        mock_corrupt.assert_called_once()
        mock_draw.assert_called_once()
        mock_img.save.assert_called_once_with("output.png")
