# BATCH10_PROMPT12_Granite.py
import os
import random
import time
from moviepy.editor import VideoFileClip

def distort_video(input_file, output_file):
    """
    Distort the video file by randomly adding glitches.

    Parameters:
    input_file (str): Path to the input video file.
    output_file (str): Path for the output distorted video file.
    """
    clip = VideoFileClip(input_file)
    
    width, height = clip.size
    duration = len(clip) / clip.fps

    # Glitch parameters
    glitch_prob = 0.1  # Probability of a glitch occurring in a second
    glitch_duration = 0.2  # Average duration of each glitch in seconds
    glitch_intensity = 50  # Intensity of the glitch effect

    for t in range(int(duration)):
        if random.random() < glitch_prob:
            # Randomly choose a position and duration for the glitch
            start_time = random.uniform(t, t + glitch_duration)
            end_time = min(start_time + glitch_duration, duration)

            # Create a glitch effect (simple intensity change in this example)
            intensity_change = random.randint(-glitch_intensity, glitch_intensity)
            color = (abs(intensity_change), abs(intensity_change), abs(intensity_change))

            clip.subclip(start_time, end_time).fx(vfx.colorx, all=True).effect_attrs(color=color)

    # Save the distorted video
    clip.write_videofile(output_file, codec='libx264')


def main():
    """Entry point for the program."""
    if len(sys.argv) != 3:
        print("Usage: python BATCH10_PROMPT12_Granite.py <input_video> <output_video>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.isfile(input_file):
        print("Error: Input file does not exist.")
        sys.exit(1)

    distort_video(input_file, output_file)
    print(f"Distorted video saved to {output_file}")


if __name__ == "__main__":
    main()