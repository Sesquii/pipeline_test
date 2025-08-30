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