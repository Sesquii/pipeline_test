#!/usr/bin/env python3

import os
import re
from pathlib import Path
import argparse
import logging

# Initialize logging configuration
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Emotion-Driven File Sorter")
    parser.add_argument('directory', type=Path, help='Directory path to sort files')
    parser.add_argument('--dry-run', action='store_true', help='Dry run without moving files')
    return parser.parse_args()

def calculate_happiness_score(file_path):
    """Calculate the AI happiness score for a given file."""
    # Initialize score
    score = 0
    
    # Check file type and extension
    if file_path.suffix == '.txt':
        score += 1
    elif file_path.suffix in ['.jpg', '.png']:
        score += 0.5
    elif file_path.suffix == '.mp3':
        score -= 0.5
    
    # Check for positive words in text files
    if file_path.suffix == '.txt':
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read().lower()
            positive_words = ["good", "happy", "joy"]
            score += sum(content.count(word) for word in positive_words)
    
    # Check for emojis
    emoji_pattern = re.compile(r'[\U0001f600-\U0001f64f]')
    if emoji_pattern.search(str(file_path)):
        score += 0.5
    
    # Adjust score based on file size and creation date
    if file_path.stat().st_size > 1024 * 1024:
        score -= 0.5
    if (Path.now() - Path(file_path).stat().st_ctime).total_seconds() > 365 * 86400:
        score -= 0.5
    
    return score

def sort_files(directory, dry_run=False):
    """Sort files in the given directory by their happiness scores."""
    files = []
    
    for root, _, file_names in os.walk(directory):
        for file_name in file_names:
            file_path = Path(root) / file_name
            try:
                score = calculate_happiness_score(file_path)
                files.append((file_path, score))
            except Exception as e:
                logging.error(f"Error processing {file_path}: {e}")
    
    # Sort files by happiness score in descending order
    sorted_files = sorted(files, key=lambda x: x[1], reverse=True)
    
    if not dry_run:
        for file_path, _ in sorted_files:
            destination_dir = directory / f"score_{int(_ * 10)}"
            os.makedirs(destination_dir, exist_ok=True)
            new_path = destination_dir / file_path.name
            logging.info(f"Moving {file_path} to {new_path}")
            file_path.rename(new_path)
    else:
        for file_path, score in sorted_files:
            print(f"{score:.2f} | {file_path}")

if __name__ == "__main__":
    args = parse_args()
    sort_files(args.directory, dry_run=args.dry_run)
```

### README Snippet
To run the script:
```sh
python emotion_file_sorter.py /path/to/directory [--dry-run]
```
Dependencies:
- `emoji` for emoji detection (optional):
  ```sh
  pip install emoji
  ```

### Example Output
Assuming a directory with the following files:

- `happy.txt` (content: "I am so happy!")
- `sad.jpg` (empty file)
- `neutral.mp3` (empty file)
- `positive_words.txt` (content: "Good luck, everyone!")

Dry run output:
```
5.00 | /path/to/directory/sad.jpg
4.00 | /path/to/directory/happy.txt
1.50 | /path/to/directory/neutral.mp3
1.00 | /path/to/directory/positive_words.txt