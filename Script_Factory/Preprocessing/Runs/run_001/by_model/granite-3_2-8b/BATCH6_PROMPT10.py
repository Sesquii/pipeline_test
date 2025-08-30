from PIL import Image
import random

def dither_image(input_path):
    # Open image file
    img = Image.open(input_path)

    # Convert image to RGB (in case it's not)
    img = img.convert("RGB")

    # Get image size
    width, height = img.size

    # Reduce color palette to 3 colors using a simple quantization method
    def reduce_palette(image):
        colors = image.getcolors(image.size[0] * image.size[1])
        total_pixels = sum([count for count, color in colors[:3]])

        reduced_img = Image.new("RGB", (width, height))
        pixels = reduced_img.load()

        # Sort colors by quantity and choose top 3
        colors.sort(key=lambda x: x[0], reverse=True)[:3]

        for count, color in colors:
            for _ in range(count):
                x, y = random.randint(0, width - 1), random.randint(0, height - 1)
                pixels[x, y] = color

        return reduced_img

    # Apply reduction and dithering
    dithered_img = reduce_palette(img)

    # Save the dithered image with a new filename
    output_path = f"{input_path.split('/')[-1].rsplit('.', 1)[0]}_dithered.png"
    dithered_img.save(output_path)

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python glitchy_compressor.py <path_to_image>")
    else:
        input_file = sys.argv[1]
        dither_image(input_file)
        print(f"Dithered image saved as {input_file.rsplit('.', 1)[0]}_dithered.png")