import imageio
import os

def create_glitchy_gif(input_path):
    """
    Creates a glitchy version of a GIF by replacing every fifth frame with a solid color frame.
    
    Args:
        input_path (str): Path to the input GIF file.
    """
    # Load the input GIF
    gif = imageio.mimread(input_path)
    
    # Create output filename
    base, ext = os.path.splitext(input_path)
    output_path = f"{base}_glitchy{ext}"
    
    # Define glitch frame (solid black)
    glitch_frame = [0] * len(gif[0].data)  # Black frame data
    
    # Process frames
    glitchy_frames = []
    for i, frame in enumerate(gif):
        if (i + 1) % 5 == 0:
            # Replace every fifth frame with the glitch frame
            glitchy_frames.append(glitch_frame)
        else:
            glitchy_frames.append(frame.data)
    
    # Save the new GIF
    imageio.mimsave(output_path, glitchy_frames, format='GIF')
    
    print(f"Glitchy GIF saved as {output_path}")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Create a glitchy version of a GIF")
    parser.add_argument("input_gif", help="Path to input GIF file")
    
    args = parser.parse_args()
    
    create_glitchy_gif(args.input_gif)