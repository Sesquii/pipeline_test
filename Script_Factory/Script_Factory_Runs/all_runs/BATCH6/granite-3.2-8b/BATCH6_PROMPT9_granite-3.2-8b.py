import cv2
import sys
import numpy as np
import random

def glitch_frame(frame):
    height, width, _ = frame.shape
    shift_x, shift_y = random.randint(0, height), random.randint(0, width)
    return frame[shift_y:height, shift_x:width]

def process_video(input_path, output_path):
    cap = cv2.VideoCapture(input_path)
    
    if not cap.isOpened():
        print("Error opening video file")
        sys.exit()

    fps = cap.get(cv2.CAP_PROP_FPS)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')

    out = cv2.VideoWriter(output_path, fourcc, fps, (int(cap.get(3)), int(cap.get(4))))
    
    frame_count = 0
    glitch_frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if frame_count % 50 == 0:
            frame = glitch_frame(frame)
        
        out.write(frame)
        
        frame_count += 1
    
    cap.release()
    out.release()

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <video_file_path>")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = f"{input_path[:-4]}_video_glitch.avi"
    
    process_video(input_path, output_path)
    print(f"Glitch video saved as {output_path}")

if __name__ == "__main__":
    main()