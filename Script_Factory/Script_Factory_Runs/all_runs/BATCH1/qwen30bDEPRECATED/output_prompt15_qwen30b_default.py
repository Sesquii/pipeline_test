#!/usr/bin/env python3
"""
Distracted Image Labeler

This script loads an image, simulates object detections with bounding boxes,
randomly corrupts 40% of the labels, and saves an annotated image with
correct (green) and incorrect (red) labels.
"""

import sys
import random
from PIL import Image, ImageDraw, ImageFont

# Set seed for reproducibility
random.seed(42)

def load_image(image_path):
    """Load an image from the specified path."""
    try:
        return Image.open(image_path)
    except Exception as e:
        print(f"Error loading image: {e}")
        sys.exit(1)

def get_label_pool():
    """Return a list of possible incorrect labels."""
    return ["car", "tree", "person", "bicycle"]

def simulate_detections():
    """
    Simulate object detections with bounding boxes and true labels.
    Each detection is a tuple: (top_left, bottom_right, correct_label)
    """
    return [
        ((50, 80), (200, 250), "cat"),
        ((300, 120), (450, 280), "dog"),
        ((100, 300), (250, 400), "bird"),
        ((350, 50), (500, 200), "car"),
        ((200, 150), (320, 270), "person"),
        ((50, 350), (180, 450), "tree")
    ]

def corrupt_labels(detections, incorrect_labels):
    """
    Randomly corrupt 40% of the labels.
    Returns a list of tuples: (top_left, bottom_right, label_type, label)
    where label_type is 'correct' or 'incorrect'
    """
    # Shuffle detections to randomize which ones get corrupted
    shuffled_detections = detections.copy()
    random.shuffle(shuffled_detections)
    
    # Calculate number of detections to corrupt (40%)
    num_corrupt = int(len(detections) * 0.4)
    
    # Create a list to store results
    result = []
    
    for i, detection in enumerate(shuffled_detections):
        top_left, bottom_right, correct_label = detection
        
        if i < num_corrupt:
            # Corrupt this label
            incorrect_label = random.choice(incorrect_labels)
            result.append((top_left, bottom_right, "incorrect", incorrect_label))
        else:
            # Keep the correct label
            result.append((top_left, bottom_right, "correct", correct_label))
    
    return result

def draw_boxes_and_labels(image, detections):
    """
    Draw bounding boxes and labels on the image.
    Correct labels in green, incorrect labels in red.
    """
    draw = ImageDraw.Draw(image)
    
    # Define colors
    correct_color = (0, 255, 0)  # Green
    incorrect_color = (255, 0, 0)  # Red
    
    for top_left, bottom_right, label_type, label in detections:
        # Draw bounding box
        draw.rectangle([top_left, bottom_right], outline=correct_color if label_type == "correct" else incorrect_color, width=3)
        
        # Add label text
        try:
            # Try to use a default font with size 20
            font = ImageFont.load_default(size=20)
        except:
            # Fallback in case of error
            font = ImageFont.load_default()
        
        # Get text size to position it properly
        text_bbox = draw.textbbox((0, 0), label, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
        
        # Position label at top-left of bounding box
        label_position = (top_left[0], top_left[1] - text_height - 5)
        
        # Draw background rectangle for better visibility
        draw.rectangle(
            [label_position[0], label_position[1], 
             label_position[0] + text_width, label_position[1] + text_height],
            fill=(255, 255, 255)  # White background
        )
        
        # Draw the actual text
        draw.text(label_position, label, fill=correct_color if label_type == "correct" else incorrect_color, font=font)

def main():
    """Main function to run the image labeler."""
    # Define image path (can be changed or made command-line argument)
    image_path = "input.png"  # Change this to your image path
    
    # Load the image
    print("Loading image...")
    image = load_image(image_path)
    
    # Get incorrect labels
    incorrect_labels = get_label_pool()
    
    # Simulate detections
    print("Simulating object detections...")
    detections = simulate_detections()
    
    # Corrupt 40% of labels
    print("Corrupting labels...")
    corrupted_detections = corrupt_labels(detections, incorrect_labels)
    
    # Draw bounding boxes and labels on the image
    print("Drawing annotations...")
    draw_boxes_and_labels(image, corrupted_detections)
    
    # Save the annotated image
    output_path = "output.png"
    print(f"Saving annotated image to {output_path}...")
    image.save(output_path)
    print("Done!")

if __name__ == "__main__":
    main()
