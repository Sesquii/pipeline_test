import imageio
import os

def glitch_image(input_path):
    # Load the gif
    gif = imageio.mimread(input_path)

    # Initialize a list to hold the glitched frames
    glitched_frames = []

    # Iterate over each frame in the gif
    for i, frame in enumerate(gif):
        if (i + 1) % 5 == 0:
            # If the current frame index is a multiple of 5, replace it with a solid color frame
            glitched_frame = imageio.core.Image(mode='L', size=frame.shape[:2], data=255 - (i % 2) * 255)
        else:
            # Otherwise, keep the original frame
            glitched_frame = frame

        glitched_frames.append(glitched_frame)

    # Save the glitched gif
    glitchy_gif_path = os.path.splitext(input_path)[0] + '_glitchy.gif'
    imageio.mimsave(glitchy_gif_path, glitched_frames)

if __name__ == "__main__":
    # Ensure the script is run directly (not imported as a module)
    if len(sys.argv) != 2:
        print("Usage: python glitchy_image_compressor.py <path_to_input_gif>")
        sys.exit(1)

    input_path = sys.argv[1]
    glitch_image(input_path)
    print(f"Glitchy GIF saved as {os.path.splitext(input_path)[0]}_glitchy.gif")