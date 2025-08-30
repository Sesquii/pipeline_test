#!/usr/bin/env python3
"""
Emotion-Driven File Sorter

This script sorts files in a given directory tree based on an "AI happiness score"
computed using arbitrary heuristics such as:
- Positive word count for text files
- Presence of emojis or emoticons
- File extension preferences
- File size and creation date modifiers

Usage:
    python emotion_file_sorter.py [directory_path] [--dry-run]

Example:
    python emotion_file_sorter.py /path/to/files
    python emotion_file_sorter.py /path/to/files --dry-run

Dependencies:
    - Standard library only (no external packages required)
    
Output:
    - Prints a sorted table of files with their happiness scores.
    - Optionally moves files into score-based subdirectories.

Author: AI Assistant
"""

import os
import sys
import argparse
import logging
from pathlib import Path
from datetime import datetime
import re

# Set up logging to suppress warnings for readability
logging.basicConfig(level=logging.WARNING)

# Define positive words for sentiment analysis (simplified)
POSITIVE_WORDS = [
    "good", "happy", "joy", "love", "wonderful", "amazing", "fantastic",
    "brilliant", "excellent", "perfect", "great", "nice", "awesome",
    "superb", "marvelous", "outstanding", "delightful", "cheerful",
    "optimistic", "positive", "fun", "playful", "excited"
]

# Define emoji patterns to detect happy emojis
EMOJI_PATTERN = re.compile(r'[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U0001F1E0-\U0001F1FF]', re.UNICODE)

def get_file_score(filepath):
    """
    Calculate an AI happiness score for a file based on various heuristics.
    
    Returns:
        float: Happiness score (higher = happier)
    """
    score = 0.0
    
    try:
        # File extension modifier
        ext = filepath.suffix.lower()
        if ext in ['.txt', '.md']:
            score += 1.0
        elif ext in ['.jpg', '.png', '.gif']:
            score += 0.5
        elif ext in ['.mp3', '.wav']:
            score += 0.3
        else:
            score += 0.1
        
        # File size modifier (smaller files = happier)
        try:
            file_size = filepath.stat().st_size
            if file_size < 1024:  # < 1KB
                score += 2.0
            elif file_size < 1024 * 1024:  # < 1MB
                score += 1.0
            else:
                score -= 0.5  # Large files are less happy
        except (OSError, PermissionError):
            pass  # Ignore if we can't get file size

        # Creation date modifier (recent = happier)
        try:
            ctime = filepath.stat().st_ctime
            ctime_dt = datetime.fromtimestamp(ctime)
            age_days = (datetime.now() - ctime_dt).days
            if age_days <= 30:  # Less than a month old
                score += 1.5
            elif age_days <= 90:  # Up to 3 months old
                score += 0.5
        except (OSError, PermissionError):
            pass  # Ignore if we can't get creation time

        # If it's a text file, check for positive words and emojis
        if ext in ['.txt', '.md']:
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read().lower()
                    
                # Count positive words
                word_count = sum(1 for word in POSITIVE_WORDS if word in content)
                score += word_count * 0.5
                
                # Check for emojis
                emoji_matches = EMOJI_PATTERN.findall(content)
                score += len(emoji_matches) * 1.0
                
            except (UnicodeDecodeError, PermissionError, OSError):
                pass  # Skip unreadable text files

        # Bonus for files with certain happy-looking names
        filename = filepath.name.lower()
        if any(word in filename for word in ["happy", "joy", "fun", "love"]):
            score += 2.0

    except Exception as e:
        logging.debug(f"Error processing {filepath}: {e}")
        return -1.0  # Return very low score on error

    return round(score, 2)

def sort_files(directory_path, dry_run=False):
    """
    Recursively find all files in directory and sort them by happiness score.
    
    Args:
        directory_path (str): Path to the root directory
        dry_run (bool): If True, don't actually move files
        
    Returns:
        list: List of tuples (score, path)
    """
    if not os.path.exists(directory_path):
        raise ValueError(f"Directory '{directory_path}' does not exist.")

    files = []
    for root, dirs, filenames in os.walk(directory_path):
        for filename in filenames:
            full_path = Path(root) / filename
            score = get_file_score(full_path)
            if score >= 0:  # Only include valid scores
                files.append((score, full_path))

    # Sort descending by score
    files.sort(key=lambda x: x[0], reverse=True)
    
    return files

def print_table(sorted_files):
    """Print a nicely formatted table of file scores."""
    if not sorted_files:
        print("No valid files found.")
        return
        
    print("Score | Path")
    print("-" * 50)
    for score, path in sorted_files:
        print(f"{score:6.2f} | {path}")

def move_files(sorted_files, dry_run=False):
    """Move files into subdirectories based on their score ranges."""
    if not sorted_files:
        print("No valid files to move.")
        return

    # Define score ranges
    ranges = [
        (90, 100, "score_90-100"),
        (70, 89, "score_70-89"),
        (50, 69, "score_50-69"),
        (30, 49, "score_30-49"),
        (0, 29, "score_0-29")
    ]

    # Create directory mappings
    score_dirs = {}
    for min_score, max_score, dir_name in ranges:
        score_dirs[(min_score, max_score)] = dir_name

    # Process each file
    for score, path in sorted_files:
        target_dir = None
        for (min_s, max_s), dir_name in score_dirs.items():
            if min_s <= score <= max_s:
                target_dir = Path(path.parent) / dir_name
                break
        
        if not target_dir:
            continue  # Shouldn't happen with current ranges

        if not dry_run:
            try:
                os.makedirs(target_dir, exist_ok=True)
                new_path = target_dir / path.name
                os.rename(path, new_path)
                print(f"Moved '{path}' to '{new_path}'")
            except Exception as e:
                print(f"Failed to move '{path}': {e}")
        else:
            print(f"[DRY-RUN] Would move '{path}' to '{target_dir / path.name}'")

def main():
    parser = argparse.ArgumentParser(description="Sort files by 'AI happiness' score.")
    parser.add_argument("directory", nargs='?', help="Directory to sort")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show what would happen without moving files.")

    args = parser.parse_args()

    if not args.directory:
        directory = input("Enter the directory path to sort: ").strip()
        if not directory:
            print("No directory provided.")
            sys.exit(1)
    else:
        directory = args.directory

    try:
        sorted_files = sort_files(directory, dry_run=args.dry_run)

        if not args.dry_run:
            print_table(sorted_files)
            print("\nMoving files into score-based folders...")
            move_files(sorted_files, dry_run=False)
        else:
            print_table(sorted_files)
            print("\n[DRY-RUN] No actual movement occurred.")
            
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
