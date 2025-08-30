#!/usr/bin/env python3
"""
Distracted Image Labeler

This script takes an image, simulates object detections with bounding boxes,
randomly corrupts 40% of the labels to simulate human error in labeling,
and saves an annotated image with visual indicators for correct vs incorrect labels.
"""

import sys
import random
from PIL import Image, ImageDraw, ImageFont

# Set seed for reproducibility
random.seed(42)

def load_image(image_path):
    """Load an image from the specified path."""
    try:
        img = Image.open(image_path)
        return img
    except Exception as e:
        print(f"Error loading image: {e}")
        sys.exit(1)

def get_random_label(label_pool, exclude=None):
    """Select a random label from the pool, excluding a given label if provided."""
    available_labels = [label for label in label_pool if label != exclude]
    return random.choice(available_labels)

def simulate_detections():
    """
    Simulate object detections with bounding boxes and true labels.
    Returns a list of tuples: (top_left, bottom_right, correct_label)
    """
    # Hard-coded detections - each tuple is (top_left, bottom_right, correct_label)
    detections = [
        ((50, 80), (200, 250), "cat"),
        ((300, 120), (450, 280), "dog"),
        ((100, 300), (250, 450), "car"),
        ((350, 350), (500, 500), "person"),
        ((200, 100), (300, 200), "tree"),
        ((50, 400), (150, 500), "bicycle"),
        ((400, 50), (500, 150), "cat"),
        ((150, 200), (250, 300), "dog")
    ]
    return detections

def corrupt_labels(detections, label_pool, corruption_rate=0.4):
    """
    Randomly corrupts a percentage of labels in detections.
    
    Args:
        detections: List of tuples (top_left, bottom_right, correct_label)
        label_pool: List of possible incorrect labels
        corruption_rate: Fraction of labels to corrupt (default 0.4 for 40%)
    
    Returns:
        List of tuples with potentially corrupted labels
    """
    # Create a copy of detections to avoid modifying the original
    corrupted_detections = []
    
    for top_left, bottom_right, correct_label in detections:
        if random.random() < corruption_rate:
            # Corrupt the label
            incorrect_label = get_random_label(label_pool, exclude=correct_label)
            corrupted_detections.append((top_left, bottom_right, incorrect_label))
        else:
            # Keep the correct label
            corrupted_detections.append((top_left, bottom_right, correct_label))
    
    return corrupted_detections

def draw_annotations(img, detections, label_pool):
    """
    Draw bounding boxes and labels on the image.
    
    Args:
        img: PIL Image object
        detections: List of tuples (top_left, bottom_right, label)
        label_pool: List of possible incorrect labels
    """
    draw = ImageDraw.Draw(img)
    
    # Define colors for correct (green) and incorrect (red) labels
    correct_color = "green"
    incorrect_color = "red"
    
    # Try to use a default font; if that fails, use a basic one
    try:
        font = ImageFont.truetype("arial.ttf", 16)
    except:
        font = ImageFont.load_default()
    
    for top_left, bottom_right, label in detections:
        # Draw bounding box
        draw.rectangle([top_left, bottom_right], outline=correct_color if label in [det[2] for det in simulate_detections() if det[2] == label] else incorrect_color, width=3)
        
        # Determine color based on whether the label is correct or not
        color = correct_color if label in [det[2] for det in simulate_detections()] else incorrect_color
        
        # Draw label text
        draw.text(top_left, label, fill=color, font=font)

def main():
    # Define the image path (can be changed or passed via command-line argument)
    image_path = "input.jpg"  # Change this to your input image path
    
    # Predefined pool of incorrect labels
    incorrect_labels = ["car", "tree", "person", "bicycle"]
    
    # Load the image
    img = load_image(image_path)
    
    # Simulate object detections
    original_detections = simulate_detections()
    
    # Corrupt 40% of the labels
    corrupted_detections = corrupt_labels(original_detections, incorrect_labels, corruption_rate=0.4)
    
    # Draw annotations on image
    draw_annotations(img, corrupted_detections, incorrect_labels)
    
    # Save the annotated image
    img.save("output.png")
    print("Annotated image saved as output.png")

if __name__ == "__main__":
    main()
