import cv2
import numpy as np
import sys
import os

def glitch_frame(frame):
    """Apply a random pixel shift glitch effect to the frame."""
    height, width = frame.shape[:2]

    # Randomly select parameters for the glitch effect
    shift_x = np.random.randint(0, width // 4)
    shift_y = np.random.randint(0, height // 4)
    glitch_width = np.random.randint(width // 8, width // 4)
    glitch_height = np.random.randint(height // 8, height // 4)

    # Randomly select the region to glitch
    x_start = np.random.randint(0, width - glitch_width)
    y_start = np.random.randint(0, height - glitch_height)

    # Create a copy of the frame for glitching
    glitched_frame = frame.copy()

    # Shift the selected region
    if shift_x > 0:
        shifted_region = frame[y_start:y_start+glitch_height, x_start+shift_x:x_start+glitch_width+shift_x]
    else:
        shifted_region = frame[y_start:y_start+glitch_height, x_start-shift_x:x_start+glitch_width-shift_x]

    if shift_y > 0:
        glitched_frame[y_start+shift_y:y_start+glitch_height+shift_y, x_start:x_start+glitch_width] = shifted_region
    else:
        glitched_frame[y_start-shift_y:y_start+glitch_height-shift_y, x_start:x_start+glitch_width] = shifted_region

    return glitched_frame

def process_video(input_path):
    """Process the video frame-by-frame and apply glitch effect to every 50th frame."""
    # Open the input video file
    cap = cv2.VideoCapture(input_path)
    if not cap.isOpened():
        print(f"Error: Could not open video {input_path}")
        return

    # Get video properties
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Define the output file name
    base_name, ext = os.path.splitext(input_path)
    output_path = f"{base_name}_video_glitch.avi"

    # Create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    frame_num = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Apply glitch effect to every 50th frame
        if frame_num % 50 == 0 and frame_num > 0:
            frame = glitch_frame(frame)

        # Write the frame to output video
        out.write(frame)
        frame_num += 1

    # Release resources
    cap.release()
    out.release()
    print(f"Processed video saved as: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python glitchy_image_compressor.py <video_file_path>")
    else:
        input_video = sys.argv[1]
        process_video(input_video)

# ===== GENERATED TESTS =====
import pytest
from pathlib import Path
import numpy as np

# Original code remains unchanged

# Test suite starts here

@pytest.fixture
def test_frame():
    """Create a test frame for glitch effect."""
    return np.zeros((100, 100, 3), dtype=np.uint8)

def test_glitch_frame(test_frame):
    """Test the glitch_frame function with a test frame."""
    original_frame = test_frame.copy()
    glitched_frame = glitch_frame(original_frame)
    
    # Check if the frame has changed
    assert not np.array_equal(original_frame, glitched_frame), "The frame should have been changed by the glitch effect."

def test_process_video(tmp_path):
    """Test the process_video function with a sample video."""
    input_video = tmp_path / "test_video.avi"
    output_video = tmp_path / "test_video_glitch.avi"

    # Create a sample video
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(str(input_video), fourcc, 10.0, (100, 100))
    for _ in range(50):
        frame = np.zeros((100, 100, 3), dtype=np.uint8)
        out.write(frame)
    out.release()

    # Process the video
    process_video(str(input_video))

    # Check if the output video exists
    assert output_video.exists(), "The output video should have been created."

def test_process_video_no_input():
    """Test the process_video function with no input."""
    with pytest.raises(SystemExit) as exc_info:
        process_video(None)
    
    assert exc_info.value.code == 1, "The program should exit with code 1 if no input is provided."

def test_process_video_invalid_input(tmp_path):
    """Test the process_video function with an invalid input file."""
    invalid_input = tmp_path / "invalid_video.avi"
    with open(invalid_input, 'w') as f:
        f.write("Invalid video data")

    with pytest.raises(SystemExit) as exc_info:
        process_video(str(invalid_input))
    
    assert exc_info.value.code == 1, "The program should exit with code 1 if the input file is invalid."

# Run the tests
if __name__ == "__main__":
    pytest.main()

This test suite includes comprehensive test cases for both the `glitch_frame` and `process_video` functions. It uses pytest fixtures to create a test frame and a sample video, and it includes positive and negative test cases. The test suite follows PEP 8 style guidelines and includes proper docstrings and comments.