import imageio
import numpy as np

def glitchy_image_compressor(input_path):
    # Read the GIF file
    reader = imageio.get_reader(input_path)
    
    # Initialize a list to store frames
    frames = []
    
    # Iterate over each frame in the GIF
    for index, frame in enumerate(reader):
        # Every fifth frame, create a solid color frame
        if (index + 1) % 5 == 0:
            # Create a black or white frame based on the index
            solid_color = np.zeros_like(frame)
            solid_color[:, :, 0] = 255 * ((index // 3) % 2)  # Red channel
            solid_color[:, :, 1] = 255 * ((index // 3) % 2)  # Green channel
            solid_color[:, :, 2] = 255 * ((index // 3) % 2)  # Blue channel
            frames.append(solid_color)
        else:
            # Append the original frame
            frames.append(frame)
    
    # Save the new GIF with glitchy frames
    output_path = f"{input_path.rsplit('.', 1)[0]}_glitchy.gif"
    imageio.mimsave(output_path, frames, duration=reader.get_meta_data()['duration'])

# Example usage
if __name__ == "__main__":
    input_path = "example.gif"  # Replace with your GIF file path
    glitchy_image_compressor(input_path)
```

This Python script uses the `imageio` library to read a GIF file and create a new GIF where every fifth frame is replaced with a solid-color frame. The output file will be saved as `<input_filename>_glitchy.gif`.