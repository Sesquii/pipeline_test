import os
import time
import random
from moviepy.editor import VideoFileClip

def glitch_video(video_path):
    # Load the video file
    clip = VideoFileClip(video_path)
    
    # Get the duration of the video
    duration = clip.duration
    
    # Define a list of glitch effects
    glitches = [
        lambda t: clip.set_start(t + random.uniform(-0.1, 0.1)),
        lambda t: clip.set_end(t + random.uniform(-0.1, 0.1)),
        lambda t: clip.fx(lambda x: x[::random.randint(2, 4)]),
        lambda t: clip.fx(lambda x: x[::-1]),
    ]
    
    # Apply glitches randomly
    glitched_clip = clip
    for _ in range(5):  # Number of glitches to apply
        glitch = random.choice(glitches)
        glitched_clip = glitch(0)  # Apply the glitch at the beginning
    
    # Write the result to a new file
    output_path = "glitched_" + os.path.basename(video_path)
    glitched_clip.write_videofile(output_path, codec='libx264')
    
    return output_path

if __name__ == "__main__":
    video_path = input("Enter the path to your video file: ")
    if not os.path.isfile(video_path):
        print("File does not exist.")
    else:
        glitched_video_path = glitch_video(video_path)
        print(f"Glitched video saved as {glitched_video_path}")