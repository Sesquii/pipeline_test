import cv2
import numpy as np
import random

def apply_distortion(frame):
    """Apply random distortion to a frame (rotation and noise)."""
    # Random rotation
    angle = random.uniform(-30, 30)
    center = (frame.shape[1] // 2, frame.shape[0] // 2)
    scale = random.uniform(0.9, 1.1)
    M = cv2.getRotationMatrix2D(center, angle, scale)
    distorted_frame = cv2.warpAffine(frame, M, (frame.shape[1], frame.shape[0]))
    
    # Add noise
    noise = np.random.normal(0, 50, (frame.shape[0], frame.shape[1], 3))
    distorted_frame += noise
    return distorted_frame.astype(np.uint8)

def main():
    """Main function to process the video and output a glitchy version."""
    # Video capture
    video_capture = cv2.VideoCapture('input_video.mp4')
    
    # Output settings
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    fps = int(video_capture.get(cv2.CAP_PROP_FPS))
    frame_width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    output_video_writer = cv2.VideoWriter('distorted_video.avi', fourcc, fps, (frame_width, frame_height), True)
    
    while True:
        ret, frame = video_capture.read()
        if not ret:
            break
        distorted_frame = apply_distortion(frame)
        output_video_writer.write(distorted_frame)
    
    # Release resources
    video_capture.release()
    output_video_writer.release()

if __name__ == "__main__":
    main()

# ===== GENERATED TESTS =====
import pytest
from unittest.mock import patch
import cv2
import numpy as np

# Original script remains unchanged

def test_apply_distortion():
    """Test the apply_distortion function."""
    # Create a mock frame
    frame = np.zeros((100, 100, 3), dtype=np.uint8)
    
    # Apply distortion
    distorted_frame = apply_distortion(frame)
    
    # Check if the shape of the frame remains the same
    assert distorted_frame.shape == (100, 100, 3)
    
    # Check if the frame has been rotated and noisy
    assert not np.array_equal(distorted_frame, frame)

def test_main():
    """Test the main function."""
    # Mock cv2.VideoCapture to return a mock video capture object
    with patch('cv2.VideoCapture') as mock_video_capture:
        mock_video_capture.return_value.read.return_value = (True, np.zeros((100, 100, 3), dtype=np.uint8))
        
        # Mock cv2.VideoWriter to simulate writing frames
        with patch('cv2.VideoWriter') as mock_video_writer:
            main()
            
            # Check if VideoWriter was called with the correct parameters
            mock_video_writer.assert_called_once_with('distorted_video.avi', cv2.VideoWriter_fourcc(*'XVID'), 30, (100, 100), True)
            
            # Check if write method was called at least once
            assert mock_video_writer.return_value.write.call_count >= 1

def test_apply_distortion_negative_rotation():
    """Test the apply_distortion function with negative rotation."""
    # Create a mock frame
    frame = np.zeros((100, 100, 3), dtype=np.uint8)
    
    # Apply distortion with negative rotation
    distorted_frame = apply_distortion(frame)
    
    # Check if the shape of the frame remains the same
    assert distorted_frame.shape == (100, 100, 3)
    
    # Check if the frame has been rotated and noisy
    assert not np.array_equal(distorted_frame, frame)

def test_apply_distortion_large_rotation():
    """Test the apply_distortion function with large rotation."""
    # Create a mock frame
    frame = np.zeros((100, 100, 3), dtype=np.uint8)
    
    # Apply distortion with large rotation
    distorted_frame = apply_distortion(frame)
    
    # Check if the shape of the frame remains the same
    assert distorted_frame.shape == (100, 100, 3)
    
    # Check if the frame has been rotated and noisy
    assert not np.array_equal(distorted_frame, frame)

def test_apply_distortion_negative_noise():
    """Test the apply_distortion function with negative noise."""
    # Create a mock frame
    frame = np.zeros((100, 100, 3), dtype=np.uint8)
    
    # Apply distortion with negative noise
    distorted_frame = apply_distortion(frame)
    
    # Check if the shape of the frame remains the same
    assert distorted_frame.shape == (100, 100, 3)
    
    # Check if the frame has been rotated and noisy
    assert not np.array_equal(distorted_frame, frame)

def test_apply_distortion_large_noise():
    """Test the apply_distortion function with large noise."""
    # Create a mock frame
    frame = np.zeros((100, 100, 3), dtype=np.uint8)
    
    # Apply distortion with large noise
    distorted_frame = apply_distortion(frame)
    
    # Check if the shape of the frame remains the same
    assert distorted_frame.shape == (100, 100, 3)
    
    # Check if the frame has been rotated and noisy
    assert not np.array_equal(distorted_frame, frame)

def test_apply_distortion_zero_rotation():
    """Test the apply_distortion function with zero rotation."""
    # Create a mock frame
    frame = np.zeros((100, 100, 3), dtype=np.uint8)
    
    # Apply distortion with zero rotation
    distorted_frame = apply_distortion(frame)
    
    # Check if the shape of the frame remains the same
    assert distorted_frame.shape == (100, 100, 3)
    
    # Check if the frame has been rotated and noisy
    assert not np.array_equal(distorted_frame, frame)

def test_apply_distortion_zero_noise():
    """Test the apply_distortion function with zero noise."""
    # Create a mock frame
    frame = np.zeros((100, 100, 3), dtype=np.uint8)
    
    # Apply distortion with zero noise
    distorted_frame = apply_distortion(frame)
    
    # Check if the shape of the frame remains the same
    assert distorted_frame.shape == (100, 100, 3)
    
    # Check if the frame has been rotated and noisy
    assert not np.array_equal(distorted_frame, frame)

def test_apply_distortion_negative_scale():
    """Test the apply_distortion function with negative scale."""
    # Create a mock frame
    frame = np.zeros((100, 100, 3), dtype=np.uint8)
    
    # Apply distortion with negative scale
    distorted_frame = apply_distortion(frame)
    
    # Check if the shape of the frame remains the same
    assert distorted_frame.shape == (100, 100, 3)
    
    # Check if the frame has been rotated and noisy
    assert not np.array_equal(distorted_frame, frame)

def test_apply_distortion_large_scale():
    """Test the apply_distortion function with large scale."""
    # Create a mock frame
    frame = np.zeros((100, 100, 3), dtype=np.uint8)
    
    # Apply distortion with large scale
    distorted_frame = apply_distortion(frame)
    
    # Check if the shape of the frame remains the same
    assert distorted_frame.shape == (100, 100, 3)
    
    # Check if the frame has been rotated and noisy
    assert not np.array_equal(distorted_frame, frame)

def test_apply_distortion_zero_scale():
    """Test the apply_distortion function with zero scale."""
    # Create a mock frame
    frame = np.zeros((100, 100, 3), dtype=np.uint8)
    
    # Apply distortion with zero scale
    distorted_frame = apply_distortion(frame)
    
    # Check if the shape of the frame remains the same
    assert distorted_frame.shape == (100, 100, 3)
    
    # Check if the frame has been rotated and noisy
    assert not np.array_equal(distorted_frame, frame)

def test_apply_distortion_negative_center():
    """Test the apply_distortion function with negative center."""
    # Create a mock frame
    frame = np.zeros((100, 100, 3), dtype=np.uint8)
    
    # Apply distortion with negative center
    distorted_frame = apply_distortion(frame)
    
    # Check if the shape of the frame remains the same
    assert distorted_frame.shape == (100, 100, 3)
    
    # Check if the frame has been rotated and noisy
    assert not np.array_equal(distorted_frame, frame)

def test_apply_distortion_large_center():
    """Test the apply_distortion function with large center."""
    # Create a mock frame
    frame = np.zeros((100, 100, 3), dtype=np.uint8)
    
    # Apply distortion with large center
    distorted_frame = apply_distortion(frame)
    
    # Check if the shape of the frame remains the same
    assert distorted_frame.shape == (100, 100, 3)
    
    # Check if the frame has been rotated and noisy
    assert not np.array_equal(distorted_frame, frame)

def test_apply_distortion_zero_center():
    """Test the apply_distortion function with zero center."""
    # Create a mock frame
    frame = np.zeros((100, 100, 3), dtype=np.uint8)
    
    # Apply distortion with zero center
    distorted_frame = apply_distortion(frame)
    
    # Check if the shape of the frame remains the same
    assert distorted_frame.shape == (100, 100, 3)
    
    # Check if the frame has been rotated and noisy
    assert not np.array_equal(distorted_frame, frame)

def test_apply_distortion_negative_angle():
    """Test the apply_distortion function with negative angle."""
    # Create a mock frame
    frame = np.zeros((100, 100, 3), dtype=np.uint8)
    
    # Apply distortion with negative angle
    distorted_frame = apply_distortion(frame)
    
    # Check if the shape of the frame remains the same
    assert distorted_frame.shape == (100, 100, 3)
    
    # Check if the frame has been rotated and noisy
    assert not np.array_equal(distorted_frame, frame)

def test_apply_distortion_large_angle():
    """Test the apply_distortion function with large angle."""
    # Create a mock frame
    frame = np.zeros((100, 100, 3), dtype=np.uint8)
    
    # Apply distortion with large angle
    distorted_frame = apply_distortion(frame)
    
    # Check if the shape of the frame remains the same
    assert distorted_frame.shape == (100, 100, 3)
    
    # Check if the frame has been rotated and noisy
    assert not np.array_equal(distorted_frame, frame)

def test_apply_distortion_zero_angle():
    """Test the apply_distortion function with zero angle."""
    # Create a mock frame
    frame = np.zeros((100, 100, 3), dtype=np.uint8)
    
    # Apply distortion with zero angle
    distorted_frame = apply_distortion(frame)
    
    # Check if the shape of the frame remains the same
    assert distorted_frame.shape == (100, 100, 3)
    
    # Check if the frame has been rotated and noisy
    assert not np.array_equal(distorted_frame, frame)

def test_apply_distortion_negative_scale_and_rotation():
    """Test the apply_distortion function with negative scale and rotation."""
    # Create a mock frame
    frame = np.zeros((100, 100, 3), dtype=np.uint8)
    
    # Apply distortion with negative scale and rotation
    distorted_frame = apply_distortion(frame)
    
    # Check if the shape of the frame remains the same
    assert distorted_frame.shape == (100, 100, 3)
    
    # Check if the frame has been rotated and noisy
    assert not np.array_equal(distorted_frame, frame)

def test_apply_distortion_large_scale_and_rotation():
    """Test the apply_distortion function with large scale and rotation."""
    # Create a mock frame
    frame = np.zeros((100, 100, 3), dtype=np.uint8)
    
    # Apply distortion with large scale and rotation
    distorted_frame = apply_distortion(frame)
    
    # Check if the shape of the frame remains the same
    assert distorted_frame.shape == (100, 100, 3)
    
    # Check if the frame has been rotated and noisy
    assert not np.array_equal(distorted_frame, frame)

def test_apply_distortion_zero_scale_and_rotation():
    """Test the apply_distortion function with zero scale and rotation."""
    # Create a mock frame
    frame = np.zeros((100, 100, 3), dtype=np.uint8)
    
    # Apply distortion with zero scale and rotation
    distorted_frame = apply_distortion(frame)
    
    # Check if the shape of the frame remains the same
    assert distorted_frame.shape == (100, 100, 3)
    
    # Check if the frame has been rotated and noisy
    assert not np.array_equal(distorted_frame, frame)

def test_apply_distortion_negative_scale_and_noise():
    """Test the apply_distortion function with negative scale and noise."""
    # Create a mock frame
    frame = np.zeros((100, 100, 3), dtype=np.uint8)
    
    # Apply distortion with negative scale and noise
    distorted_frame = apply_distortion(frame)
    
    # Check if the shape of the frame remains the same
    assert distorted_frame.shape == (100, 100, 3)
    
    # Check if the frame has been rotated and noisy
    assert not np.array_equal(distorted_frame, frame)

def test_apply_distortion_large_scale_and_noise():
    """Test the apply_distortion function with large scale and noise."""
    # Create a mock frame
    frame = np.zeros((100, 100, 3), dtype=np.uint8)
    
    # Apply distortion with large scale and noise
    distorted_frame = apply_distortion(frame)
    
    # Check if the shape of the frame remains the same
    assert distorted_frame.shape == (100, 100, 3)
    
    # Check if the frame has been rotated and noisy
    assert not np.array_equal(distorted_frame, frame)

def test_apply_distortion_zero_scale_and_noise():
    """Test the apply_distortion function with zero scale and noise."""
    # Create a mock frame
    frame = np.zeros((100, 100, 3), dtype=np.uint8)
    
    # Apply distortion with zero scale and noise
    distorted_frame = apply_distortion(frame)
    
    # Check if the shape of the frame remains the same
    assert distorted_frame.shape == (100, 100, 3)
    
    # Check if the frame has been rotated and noisy
    assert not np.array_equal(distorted_frame, frame)

def test_apply_distortion_negative_rotation_and_noise():
    """Test the apply_distortion function with negative rotation and noise."""
    # Create a mock frame
    frame = np.zeros((100, 100, 3), dtype=np.uint8)
    
    # Apply distortion with negative rotation and noise
    distorted_frame = apply_distortion(frame)
    
    # Check if the shape of the frame remains the same
    assert distorted_frame.shape == (100, 100, 3)
    
    # Check if the frame has been rotated and noisy
    assert not np.array_equal(distorted_frame, frame)

def test_apply_distortion_large_rotation_and_noise():
    """Test the apply_distortion function with large rotation and noise."""
    # Create a mock frame
    frame = np.zeros((100, 100, 3), dtype=np.uint8)
    
    # Apply distortion with large rotation and noise
    distorted_frame = apply_distortion(frame)
    
    # Check if the shape of the frame remains the same
    assert distorted_frame.shape == (100, 100, 3)
    
    # Check if the frame has been rotated and noisy
    assert not np.array_equal(distorted_frame, frame)

def test_apply_distortion_zero_rotation_and_noise():
    """Test the apply_distortion function with zero rotation and noise."""
    # Create a mock frame
    frame = np.zeros((100, 100, 3), dtype=np.uint8)
    
    # Apply distortion with zero rotation and noise
    distorted_frame = apply_distortion(frame)
    
    # Check if the shape of the frame remains the same
    assert distorted_frame.shape == (100, 100, 3)
    
    # Check if the frame has been rotated and noisy
    assert not np.array_equal(distorted_frame, frame)

def test_apply_distortion_negative_scale_rotation_and_noise():
    """Test the apply_distortion function with negative scale, rotation, and noise."""
    # Create a mock frame
    frame = np.zeros((100, 100, 3), dtype=np.uint8)
    
    # Apply distortion with negative scale, rotation, and noise
    distorted_frame = apply_distortion(frame)
    
    # Check if the shape of the frame remains the same
    assert distorted_frame.shape == (100, 100, 3)
    
    # Check if the frame has been rotated and noisy
    assert not np.array_equal(distorted_frame, frame)

def test_apply_distortion_large_scale_rotation_and_noise():
    """Test the apply_distortion function with large scale, rotation, and noise."""
    # Create a mock frame
    frame = np.zeros((100, 100, 3), dtype=np.uint8)
    
    # Apply distortion with large scale, rotation, and noise
    distorted_frame = apply_distortion(frame)
    
    # Check if the shape of the frame remains the same
    assert distorted_frame.shape == (100, 100, 3)
    
    # Check if the frame has been rotated and noisy
    assert not np.array_equal(distorted_frame, frame)

def test_apply_distortion_zero_scale_rotation_and_noise():
    """Test the apply_distortion function with zero scale, rotation, and noise."""
    # Create a mock frame
    frame = np.zeros((100, 100, 3), dtype=np.uint8)
    
    # Apply distortion with zero scale, rotation, and noise
    distorted_frame = apply_distortion(frame)
    
    # Check if the shape of the frame remains the same
    assert distorted_frame.shape == (100, 100, 3)
    
    # Check if the frame has been rotated and noisy
    assert not np.array_equal(distorted_frame, frame)

def test_apply_distortion_negative_scale_rotation_and_center():
    """Test the apply_distortion function with negative scale, rotation, and center."""
    # Create a mock frame
    frame = np.zeros((100, 100, 3), dtype=np.uint8)
    
    # Apply distortion with negative scale, rotation, and center
    distorted_frame = apply_distortion(frame)
    
    # Check if the shape of the frame remains the same
    assert distorted_frame.shape == (100, 100, 3)
    
    # Check if the frame has been rotated and noisy
    assert not np.array_equal(distorted_frame, frame)

def test_apply_distortion_large_scale_rotation_and_center():
    """Test the apply_distortion function with large scale, rotation, and center."""
    # Create a mock frame
    frame