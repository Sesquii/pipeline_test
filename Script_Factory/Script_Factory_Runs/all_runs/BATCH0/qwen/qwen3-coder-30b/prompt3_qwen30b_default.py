#!/usr/bin/env python3
"""
Emotion-Driven File Sorter

This script sorts files in a given directory based on an "AI happiness score" derived from:
- Text content: positive word count
- Emojis and emoticons (if present)
- File extension (with arbitrary weights)
- File size (smaller files = happier)
- Creation date (newer files = happier)

Usage:
    python emotion_file_sorter.py [directory_path] [--dry-run]

Options:
    directory_path   : Path to the directory to scan. If not provided, prompts user.
    --dry-run        : Only show what would happen without moving files.

Dependencies:
    None (uses only Python standard library)

Example:
    $ python emotion_file_sorter.py /home/user/documents
    $ python emotion_file_sorter.py --dry-run

Output:
    A table showing scores and paths, or moves files into score-based folders.
"""

import os
import sys
import argparse
import logging
from pathlib import Path
from datetime import datetime
import re

# Set up logging
logging.basicConfig(level=logging.WARNING, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Positive words for text analysis
POSITIVE_WORDS = [
    "good", "happy", "joy", "love", "amazing", "wonderful", "fantastic", "excellent",
    "brilliant", "outstanding", "perfect", "delighted", "thrilled", "pleased", "satisfied",
    "cheerful", "optimistic", "glad", "content", "peaceful", "serene"
]

# Emojis and emoticons that increase happiness
EMOJIS = [
    "😀", "😃", "😄", "😁", "😆", "😅", "😂", "🤣", "😊", "😇", "🙂", "🙃", "😉", "😌",
    "😍", "🥰", "😘", "😗", "😙", "😚", "😋", "😛", "😝", "😜", "🤪", "🤨", "🧐", "🤓",
    "😎", "🤩", "🥳", "😏", "😒", "😞", "😔", "😟", "😕", "🙁", "☹️", "😣", "😖", "😫",
    "😩", "🥺", "😢", "😭", "😤", "😠", "😡", "🤬", "🤯", "😳", "🥵", "🥶", "😱", "😨",
    "😰", "😥", "😓", "🤗", "🤔", "🤭", "🤫", "🤥", "😶", "😐", "😑", "😬", "🙄", "😯",
    "😦", "😧", "😮", "😲", "🥱", "😴", "🤤", "😪", "😵", "🤐", "🥴", "🤢", "🤮", "🤧",
    "😷", "🤒", "🤕", "🤑", "🤠", "😈", "👿", "👹", "👺", "🤡", "💩", "👻", "💀", "☠️",
    "👽", "👾", "🤖", "🎃", "😺", "😸", "😹", "😻", "😼", "😽", "🙀", "😿", "😾"
]

# File extension weights
EXT_WEIGHTS = {
    ".txt": 10,
    ".md": 8,
    ".py": 5,
    ".json": 3,
    ".csv": 2,
    ".html": 4,
    ".css": 1,
    ".js": 1,
    ".jpg": 0,
    ".jpeg": 0,
    ".png": 0,
    ".gif": 0,
    ".mp4": 0,
    ".avi": 0,
    ".pdf": 2,
    ".doc": 1,
    ".docx": 1,
    ".xls": 1,
    ".xlsx": 1,
    ".ppt": 1,
    ".pptx": 1,
    ".zip": -1,
    ".exe": -3,
    ".tmp": -5,
    ".log": -2
}

def get_file_score(file_path):
    """
    Calculate happiness score for a file based on multiple criteria.
    Returns a float.
    """
    score = 0.0

    try:
        # Extension weight
        ext = file_path.suffix.lower()
        if ext in EXT_WEIGHTS:
            score += EXT_WEIGHTS[ext]
        else:
            score += 0  # Default neutral value

        # File size (smaller is happier)
        size = file_path.stat().st_size
        if size > 0:
            score += max(0, 1000 - size) / 100  # Normalize to ~10 points max

        # Creation date (newer is happier)
        ctime = file_path.stat().st_ctime
        age_days = (datetime.now().timestamp() - ctime) / (24 * 3600)
        score += max(0, 10 - age_days/30)  # Max 10 points for recent files

        # Read content if it's a text file
        if ext in [".txt", ".md", ".py", ".json", ".csv", ".html", ".css", ".js"]:
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
            except Exception as e:
                logger.warning(f"Could not read {file_path}: {e}")
                return score

            # Positive words
            content_lower = content.lower()
            for word in POSITIVE_WORDS:
                count = content_lower.count(word)
                score += count * 2.0

            # Emojis and emoticons
            for emoji in EMOJIS:
                count = content.count(emoji)
                score += count * 3.0

        return round(score, 2)

    except Exception as e:
        logger.warning(f"Error processing {file_path}: {e}")
        return -100  # Penalize unreadable files heavily


def sort_files(directory):
    """
    Find all files in directory recursively and return them with scores.
    Returns list of tuples: (score, file_path)
    """
    files = []
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            file_path = Path(root) / filename
            try:
                score = get_file_score(file_path)
                files.append((score, file_path))
            except Exception as e:
                logger.warning(f"Skipping {file_path}: {e}")
    return sorted(files, key=lambda x: x[0], reverse=True)


def print_table(sorted_files):
    """
    Print a formatted table of scores and paths.
    """
    print(f"{'Score':>8} | {'Path'}")
    print("-" * 70)
    for score, path in sorted_files:
        print(f"{score:>8.2f} | {path}")


def move_files(sorted_files, dry_run=False):
    """
    Move files into folders based on their happiness score ranges.
    """
    score_ranges = [
        (90, 100, "score_90-100"),
        (70, 89, "score_70-89"),
        (50, 69, "score_50-69"),
        (30, 49, "score_30-49"),
        (0, 29, "score_0-29")
    ]

    for score, path in sorted_files:
        folder_name = None
        for low, high, name in score_ranges:
            if low <= score <= high:
                folder_name = name
                break

        if not folder_name:
            folder_name = "score_negative"

        target_dir = path.parent / folder_name
        if not dry_run:
            try:
                target_dir.mkdir(exist_ok=True)
                new_path = target_dir / path.name
                path.rename(new_path)
                print(f"Moved: {path} -> {new_path}")
            except Exception as e:
                logger.error(f"Failed to move {path}: {e}")
        else:
            print(f"[DRY RUN] Would move: {path} -> {target_dir / path.name}")


def main():
    parser = argparse.ArgumentParser(description="Sort files by AI happiness score.")
    parser.add_argument("directory", nargs='?', help="Directory to scan")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show what would happen without actually moving files.")

    args = parser.parse_args()

    # Prompt for directory if not provided
    if not args.directory:
        print("No directory provided.")
        args.directory = input("Please enter the directory path to scan: ").strip()
        if not args.directory:
            print("No directory entered. Exiting.")
            sys.exit(1)

    try:
        directory = Path(args.directory)
        if not directory.exists():
            raise FileNotFoundError(f"Directory '{directory}' does not exist.")
        if not directory.is_dir():
            raise NotADirectoryError(f"'{directory}' is not a directory.")

        print(f"Scanning directory: {directory}")
        sorted_files = sort_files(directory)

        if not sorted_files:
            print("No files found or all files had errors.")
            return

        if args.dry_run:
            print("[DRY RUN MODE] Files would be moved as follows:")
            move_files(sorted_files, dry_run=True)
        else:
            print("Sorting by happiness score...")
            print_table(sorted_files)
            print("\nMoving files to score-based folders...")
            move_files(sorted_files)

    except Exception as e:
        logger.error(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
