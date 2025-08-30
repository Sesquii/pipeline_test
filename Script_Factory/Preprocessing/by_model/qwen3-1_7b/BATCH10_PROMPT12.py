```python
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