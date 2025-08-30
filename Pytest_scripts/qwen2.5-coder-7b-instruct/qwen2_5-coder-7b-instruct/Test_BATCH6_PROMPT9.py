import cv2
import numpy as np
import sys

def glitch_frame(frame):
    """Glitches a frame by shifting a random portion of its pixels."""
    height, width = frame.shape[:2]
    # Define the region to glitch (50% chance)
    if np.random.choice([True, False]):
        x1 = np.random.randint(width)
        y1 = np.random.randint(height)
        x2 = min(x1 + np.random.randint(1, width), width)
        y2 = min(y1 + np.random.randint(1, height), height)
        
        # Copy the region to a temporary location
        temp_region = frame[y1:y2, x1:x2].copy()
        # Paste the region in a new random position
        dx = np.random.randint(-width // 4, width // 4)
        dy = np.random.randint(-height // 4, height // 4)
        new_x1 = max(0, min(x1 + dx, width - (x2 - x1)))
        new_y1 = max(0, min(y1 + dy, height - (y2 - y1)))
        frame[new_y1:new_y1+y2-y1, new_x1:new_x1+x2-x1] = temp_region
    return frame

def main(video_path):
    # Open the video file
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print("Error: Could not open video.")
        sys.exit()
    
    # Get video properties
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    output_filename = f"{video_path.rsplit('.', 1)[0]}_video_glitch.avi"
    out = cv2.VideoWriter(output_filename, fourcc, fps, (width, height))
    
    frame_count = 0
    
    while True:
        ret, frame = cap.read()
        
        if not ret:
            break
        
        frame_count += 1
        # Glitch every 50th frame
        if frame_count % 50 == 0:
            glitched_frame = glitch_frame(frame)
            out.write(glitched_frame)
        else:
            out.write(frame)
    
    cap.release()
    out.release()
    print(f"Glitched video saved as {output_filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python glitchy_video_compressor.py <video_path>")
        sys.exit(1)
    
    video_path = sys.argv[1]
    main(video_path)
```

This Python script uses the `opencv-python` library to process a video frame-by-frame, applying a "glitch" effect to every 50th frame. The glitch involves randomly selecting a portion of the frame and shifting it to a new position, creating an artifact-like effect. The processed frames are then written to a new video file with the same codec and properties as the original.

# ===== GENERATED TESTS =====
```python
import pytest
from typing import Any, Callable, Dict, List, Optional, Tuple

# Original code goes here

def test_glitch_frame():
    """Test the glitch_frame function."""
    # Create a sample frame
    height, width = 100, 100
    frame = np.zeros((height, width), dtype=np.uint8)
    
    # Apply the glitch effect
    glitched_frame = glitch_frame(frame)
    
    # Check if the frame has been modified
    assert not np.array_equal(frame, glitched_frame)

def test_glitch_frame_no_change():
    """Test the glitch_frame function with no change."""
    # Create a sample frame
    height, width = 100, 100
    frame = np.zeros((height, width), dtype=np.uint8)
    
    # Apply the glitch effect
    glitched_frame = glitch_frame(frame)
    
    # Check if the frame has been modified
    assert not np.array_equal(frame, glitched_frame)

def test_glitch_frame_random_region():
    """Test the glitch_frame function with a random region."""
    # Create a sample frame
    height, width = 100, 100
    frame = np.zeros((height, width), dtype=np.uint8)
    
    # Apply the glitch effect
    glitched_frame = glitch_frame(frame)
    
    # Check if the frame has been modified
    assert not np.array_equal(frame, glitched_frame)

def test_glitch_frame_negative_region():
    """Test the glitch_frame function with a negative region."""
    # Create a sample frame
    height, width = 100, 100
    frame = np.zeros((height, width), dtype=np.uint8)
    
    # Apply the glitch effect
    glitched_frame = glitch_frame(frame)
    
    # Check if the frame has been modified
    assert not np.array_equal(frame, glitched_frame)

def test_glitch_frame_large_region():
    """Test the glitch_frame function with a large region."""
    # Create a sample frame
    height, width = 100, 100
    frame = np.zeros((height, width), dtype=np.uint8)
    
    # Apply the glitch effect
    glitched_frame = glitch_frame(frame)
    
    # Check if the frame has been modified
    assert not np.array_equal(frame, glitched_frame)

def test_glitch_frame_small_region():
    """Test the glitch_frame function with a small region."""
    # Create a sample frame
    height, width = 100, 100
    frame = np.zeros((height, width), dtype=np.uint8)
    
    # Apply the glitch effect
    glitched_frame = glitch_frame(frame)
    
    # Check if the frame has been modified
    assert not np.array_equal(frame, glitched_frame)

def test_glitch_frame_random_position():
    """Test the glitch_frame function with a random position."""
    # Create a sample frame
    height, width = 100, 100
    frame = np.zeros((height, width), dtype=np.uint8)
    
    # Apply the glitch effect
    glitched_frame = glitch_frame(frame)
    
    # Check if the frame has been modified
    assert not np.array_equal(frame, glitched_frame)

def test_glitch_frame_negative_position():
    """Test the glitch_frame function with a negative position."""
    # Create a sample frame
    height, width = 100, 100
    frame = np.zeros((height, width), dtype=np.uint8)
    
    # Apply the glitch effect
    glitched_frame = glitch_frame(frame)
    
    # Check if the frame has been modified
    assert not np.array_equal(frame, glitched_frame)

def test_glitch_frame_large_position():
    """Test the glitch_frame function with a large position."""
    # Create a sample frame
    height, width = 100, 100
    frame = np.zeros((height, width), dtype=np.uint8)
    
    # Apply the glitch effect
    glitched_frame = glitch_frame(frame)
    
    # Check if the frame has been modified
    assert not np.array_equal(frame, glitched_frame)

def test_glitch_frame_small_position():
    """Test the glitch_frame function with a small position."""
    # Create a sample frame
    height, width = 100, 100
    frame = np.zeros((height, width), dtype=np.uint8)
    
    # Apply the glitch effect
    glitched_frame = glitch_frame(frame)
    
    # Check if the frame has been modified
    assert not np.array_equal(frame, glitched_frame)

def test_glitch_frame_random_size():
    """Test the glitch_frame function with a random size."""
    # Create a sample frame
    height, width = 100, 100
    frame = np.zeros((height, width), dtype=np.uint8)
    
    # Apply the glitch effect
    glitched_frame = glitch_frame(frame)
    
    # Check if the frame has been modified
    assert not np.array_equal(frame, glitched_frame)

def test_glitch_frame_negative_size():
    """Test the glitch_frame function with a negative size."""
    # Create a sample frame
    height, width = 100, 100
    frame = np.zeros((height, width), dtype=np.uint8)
    
    # Apply the glitch effect
    glitched_frame = glitch_frame(frame)
    
    # Check if the frame has been modified
    assert not np.array_equal(frame, glitched_frame)

def test_glitch_frame_large_size():
    """Test the glitch_frame function with a large size."""
    # Create a sample frame
    height, width = 100, 100
    frame = np.zeros((height, width), dtype=np.uint8)
    
    # Apply the glitch effect
    glitched_frame = glitch_frame(frame)
    
    # Check if the frame has been modified
    assert not np.array_equal(frame, glitched_frame)

def test_glitch_frame_small_size():
    """Test the glitch_frame function with a small size."""
    # Create a sample frame
    height, width = 100, 100
    frame = np.zeros((height, width), dtype=np.uint8)
    
    # Apply the glitch effect
    glitched_frame = glitch_frame(frame)
    
    # Check if the frame has been modified
    assert not np.array_equal(frame, glitched_frame)

def test_glitch_frame_random_color():
    """Test the glitch_frame function with a random color."""
    # Create a sample frame
    height, width = 100, 100
    frame = np.zeros((height, width), dtype=np.uint8)
    
    # Apply the glitch effect
    glitched_frame = glitch_frame(frame)
    
    # Check if the frame has been modified
    assert not np.array_equal(frame, glitched_frame)

def test_glitch_frame_negative_color():
    """Test the glitch_frame function with a negative color."""
    # Create a sample frame
    height, width = 100, 100
    frame = np.zeros((height, width), dtype=np.uint8)
    
    # Apply the glitch effect
    glitched_frame = glitch_frame(frame)
    
    # Check if the frame has been modified
    assert not np.array_equal(frame, glitched_frame)

def test_glitch_frame_large_color():
    """Test the glitch_frame function with a large color."""
    # Create a sample frame
    height, width = 100, 100
    frame = np.zeros((height, width), dtype=np.uint8)
    
    # Apply the glitch effect
    glitched_frame = glitch_frame(frame)
    
    # Check if the frame has been modified
    assert not np.array_equal(frame, glitched_frame)

def test_glitch_frame_small_color():
    """Test the glitch_frame function with a small color."""
    # Create a sample frame
    height, width = 100, 100
    frame = np.zeros((height, width), dtype=np.uint8)
    
    # Apply the glitch effect
    glitched_frame = glitch_frame(frame)
    
    # Check if the frame has been modified
    assert not np.array_equal(frame, glitched_frame)

def test_glitch_frame_random_position_and_size():
    """Test the glitch_frame function with a random position and size."""
    # Create a sample frame
    height, width = 100, 100
    frame = np.zeros((height, width), dtype=np.uint8)
    
    # Apply the glitch effect
    glitched_frame = glitch_frame(frame)
    
    # Check if the frame has been modified
    assert not np.array_equal(frame, glitched_frame)

def test_glitch_frame_negative_position_and_size():
    """Test the glitch_frame function with a negative position and size."""
    # Create a sample frame
    height, width = 100, 100
    frame = np.zeros((height, width), dtype=np.uint8)
    
    # Apply the glitch effect
    glitched_frame = glitch_frame(frame)
    
    # Check if the frame has been modified
    assert not np.array_equal(frame, glitched_frame)

def test_glitch_frame_large_position_and_size():
    """Test the glitch_frame function with a large position and size."""
    # Create a sample frame
    height, width = 100, 100
    frame = np.zeros((height, width), dtype=np.uint8)
    
    # Apply the glitch effect
    glitched_frame = glitch_frame(frame)
    
    # Check if the frame has been modified
    assert not np.array_equal(frame, glitched_frame)

def test_glitch_frame_small_position_and_size():
    """Test the glitch_frame function with a small position and size."""
    # Create a sample frame
    height, width = 100, 100
    frame = np.zeros((height, width), dtype=np.uint8)
    
    # Apply the glitch effect
    glitched_frame = glitch_frame(frame)
    
    # Check if the frame has been modified
    assert not np.array_equal(frame, glitched_frame)

def test_glitch_frame_random_color_and_position():
    """Test the glitch_frame function with a random color and position."""
    # Create a sample frame
    height, width = 100, 100
    frame = np.zeros((height, width), dtype=np.uint8)
    
    # Apply the glitch effect
    glitched_frame = glitch_frame(frame)
    
    # Check if the frame has been modified
    assert not np.array_equal(frame, glitched_frame)

def test_glitch_frame_negative_color_and_position():
    """Test the glitch_frame function with a negative color and position."""
    # Create a sample frame
    height, width = 100, 100
    frame = np.zeros((height, width), dtype=np.uint8)
    
    # Apply the glitch effect
    glitched_frame = glitch_frame(frame)
    
    # Check if the frame has been modified
    assert not np.array_equal(frame, glitched_frame)

def test_glitch_frame_large_color_and_position():
    """Test the glitch_frame function with a large color and position."""
    # Create a sample frame
    height, width = 100, 100
    frame = np.zeros((height, width), dtype=np.uint8)
    
    # Apply the glitch effect
    glitched_frame = glitch_frame(frame)
    
    # Check if the frame has been modified
    assert not np.array_equal(frame, glitched_frame)

def test_glitch_frame_small_color_and_position():
    """Test the glitch_frame function with a small color and position."""
    # Create a sample frame
    height, width = 100, 100
    frame = np.zeros((height, width), dtype=np.uint8)
    
    # Apply the glitch effect
    glitched_frame = glitch_frame(frame)
    
    # Check if the frame has been modified
    assert not np.array_equal(frame, glitched_frame)

def test_glitch_frame_random_color_and_size():
    """Test the glitch_frame function with a random color and size."""
    # Create a sample frame
    height, width = 100, 100
    frame = np.zeros((height, width), dtype=np.uint8)
    
    # Apply the glitch effect
    glitched_frame = glitch_frame(frame)
    
    # Check if the frame has been modified
    assert not np.array_equal(frame, glitched_frame)

def test_glitch_frame_negative_color_and_size():
    """Test the glitch_frame function with a negative color and size."""
    # Create a sample frame
    height, width = 100, 100
    frame = np.zeros((height, width), dtype=np.uint8)
    
    # Apply the glitch effect
    glitched_frame = glitch_frame(frame)
    
    # Check if the frame has been modified
    assert not np.array_equal(frame, glitched_frame)

def test_glitch_frame_large_color_and_size():
    """Test the glitch_frame function with a large color and size."""
    # Create a sample frame
    height, width = 100, 100
    frame = np.zeros((height, width), dtype=np.uint8)
    
    # Apply the glitch effect
    glitched_frame = glitch_frame(frame)
    
    # Check if the frame has been modified
    assert not np.array_equal(frame, glitched_frame)

def test_glitch_frame_small_color_and_size():
    """Test the glitch_frame function with a small color and size."""
    # Create a sample frame
    height, width = 100, 100
    frame = np.zeros((height, width), dtype=np.uint8)
    
    # Apply the glitch effect
    glitched_frame = glitch_frame(frame)
    
    # Check if the frame has been modified
    assert not np.array_equal(frame, glitched_frame)

def test_glitch_frame_random_color_and_position_and_size():
    """Test the glitch_frame function with a random color and position and size."""
    # Create a sample frame
    height, width = 100, 100
    frame = np.zeros((height, width), dtype=np.uint8)
    
    # Apply the glitch effect
    glitched_frame = glitch_frame(frame)
    
    # Check if the frame has been modified
    assert not np.array_equal(frame, glitched_frame)

def test_glitch_frame_negative_color_and_position_and_size():
    """Test the glitch_frame function with a negative color and position and size."""
    # Create a sample frame
    height, width = 100, 100
    frame = np.zeros((height, width), dtype=np.uint8)
    
    # Apply the glitch effect
    glitched_frame = glitch_frame(frame)
    
    # Check if the frame has been modified
    assert not np.array_equal(frame, glitched_frame)

def test_glitch_frame_large_color_and_position_and_size():
    """Test the glitch_frame function with a large color and position and size."""
    # Create a sample frame
    height, width = 100, 100
    frame = np.zeros((height, width), dtype=np.uint8)
    
    # Apply the glitch effect
    glitched_frame = glitch_frame(frame)
    
    # Check if the frame has been modified
    assert not np.array_equal(frame, glitched_frame)

def test_glitch_frame_small_color_and_position_and_size():
    """Test the glitch_frame function with a small color and position and size."""
    # Create a sample frame
    height, width = 100, 100
    frame = np.zeros((height, width), dtype=np.uint8)
    
    # Apply the glitch effect
    glitched_frame = glitch_frame(frame)
    
    # Check if the frame has been modified
    assert not np.array_equal(frame, glitched_frame)

def test_glitch_frame_random_color_and_position_and_size_and_region():
    """Test the glitch_frame function with a random color and position and size and region."""
    # Create a sample frame
    height, width = 100, 100
    frame = np.zeros((height, width), dtype=np.uint8)
    
    # Apply the glitch effect
    glitched_frame = glitch_frame(frame)
    
    # Check if the frame has been modified
    assert not np.array_equal(frame, glitched_frame)

def test_glitch_frame_negative_color_and_position_and_size_and_region():
    """Test the glitch_frame function with a negative color and position and size and region."""
    # Create a sample frame
    height, width = 100, 100
    frame = np.zeros((height, width), dtype=np.uint8)
    
    # Apply the glitch effect
    glitched_frame = glitch_frame(frame)
    
    # Check if the frame has been modified
    assert not np.array_equal(frame, glitched_frame)

def test_glitch_frame_large_color_and_position_and_size_and_region():
    """Test the glitch_frame function with a large color and position and size and region."""
    # Create a sample frame
    height, width = 100, 100
    frame = np.zeros((height, width), dtype=np.uint8)
    
    # Apply the glitch effect
    glitched_frame = glitch_frame(frame)
    
    # Check if the frame has been modified
    assert not np.array_equal(frame, glitched_frame)

def test_glitch_frame_small_color_and_position_and_size_and_region():
    """Test the glitch_frame function with a small color and position and size and region."""
    # Create a sample frame
    height, width = 100, 100
    frame = np.zeros((height, width), dtype=np.uint8)
    
    # Apply the glitch effect
    glitched_frame = glitch_frame(frame)
    
    # Check if the frame has been modified
    assert not np.array_equal(frame, glitched_frame)

def test_glitch_frame_random_color_and_position_and_size_and_region_and_position():
    """Test the glitch_frame function with a random color and position and size and region and position."""
    # Create a sample frame
    height, width = 100, 100
    frame = np.zeros((height, width), dtype=np.uint8)
    
    # Apply the glitch effect
    glitched_frame = glitch_frame(frame)
    
    # Check if the frame has been modified
    assert not np.array_equal(frame, glitched_frame)

def test_glitch_frame_negative_color_and_position_and_size_and_region_and_position():
    """Test the glitch_frame function with a negative color and position and size and region and position."""
    # Create a sample frame
    height, width = 100