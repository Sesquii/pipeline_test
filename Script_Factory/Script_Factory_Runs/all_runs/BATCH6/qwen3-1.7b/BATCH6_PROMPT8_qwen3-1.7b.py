```python
import imageio
import numpy as np
import sys

def glitchy_compress(input_path):
    frames = imageio.imread(input_path)
    modified_frames = []
    for i, frame in enumerate(frames):
        if i % 5 == 0:
            # Replace with a solid black color
            modified_frame = np.zeros_like(frame)
            modified_frames.append(modified_frame)
        else:
            modified_frames.append(frame)
    output_path = input_path.replace('.gif', '_glitchy.gif')
    imageio.mimsave(output_path, modified_frames, duration=0.2)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python glitchy_compressor.py <input_file>")
        sys.exit(1)
    input_path = sys.argv[1]
    glitchy_compress(input_path)