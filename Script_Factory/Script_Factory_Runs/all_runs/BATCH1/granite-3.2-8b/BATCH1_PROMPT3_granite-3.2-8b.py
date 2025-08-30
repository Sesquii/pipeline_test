#!/usr/bin/env python3
import os
import pathlib
import re
from argparse import ArgumentParser, RawDescriptionHelpFormatter
from typing import List, Tuple

# External packages (optional)
# pip install emoji nltk
# For emoji detection: from emoji import UNICODE_EMOJI
# For text processing: from nltk.tokenize import word_tokenize

# Define positive words for happiness score
POSITIVE_WORDS = ["good", "happy", "joy"]

def get_happiness_score(file_path: pathlib.Path) -> Tuple[float, str]:
    """Determine the AI's happiness score for a given file."""
    
    score = 0.0
    file_extension = file_path.suffix.lower()

    # Add points based on file extension
    if file_extension == ".txt":
        score += 1

    # Read file content and count positive words
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read().lower()

            # Count positive words
            for word in POSITIVE_WORDS:
                if re.search(r'\b' + word + r'\b', text):
                    score += 0.5
    except Exception as e:
        logging.warning(f"Error reading file {file_path}: {e}")

    return score, str(file_path)

def sort_files(directory: pathlib.Path, dry_run: bool = False) -> List[Tuple[float, str]]:
    """Sort files in a given directory by happiness score."""
    
    scores_and_paths: List[Tuple[float, str]] = []

    for file_path in directory.rglob('*'):
        if file_path.is_file():
            try:
                score, path_str = get_happiness_score(file_path)
                scores_and_paths.append((score, path_str))
            except Exception as e:
                logging.warning(f"Skipping file {file_path}: {e}")

    # Sort files by happiness score in descending order
    sorted_files = sorted(scores_and_paths, key=lambda x: x[0], reverse=True)
    
    if not dry_run:
        for score, path_str in sorted_files:
            create_score_folder(pathlib.Path(directory), score)
            shutil.move(file_path, pathlib.Path(f"{score}_folder/{os.path.basename(path_str)}"))
    
    return sorted_files

def create_score_folder(base_dir: pathlib.Path, score: str) -> None:
    """Create a folder for files based on their happiness score."""
    
    score_folder = base_dir / f"score_{score}"
    if not score_folder.exists():
        score_folder.mkdir()

def main():
    parser = ArgumentParser(description=__doc__, formatter_class=RawDescriptionHelpFormatter)
    parser.add_argument("directory", type=pathlib.Path, help="Directory to process (recursively)")
    parser.add_argument("--dry-run", action='store_true', default=False,
                        help="Show what would happen without moving files")

    args = parser.parse_args()

    directory = args.directory
    dry_run = args.dry_run
    
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        return

    sorted_files = sort_files(directory, dry_run)

    print("Score | Path")
    for score, path_str in sorted_files:
        print(f"{score:.1f} | {path_str}")

if __name__ == "__main__":
    main()
```

### README Snippet 

To run the script, first install the required libraries (optional):

```bash
# For emoji detection and text processing:
pip install emoji nltk
```

Then execute:

```bash
python emotion_file_sorter.py /path/to/your/directory --dry-run
```

Replace `/path/to/your/directory` with the path to your directory. The `--dry-run` flag shows what would happen without moving files. 

### Example Output:

Given a simple test directory structure like this:

```
test_dir/
    - file1.txt (Content: "I feel good today!")
    - file2.jpg (No content)
    - file3.txt (Content: "This is a sad day.")
    - subfolder/
        - file4.txt (Content: "Finding joy in little things.")
```

The script's output might look like this:

```
Score | Path
1.5  | test_dir/file1.txt
0.5  | test_dir/subfolder/file4.txt
0    | test_dir/file2.jpg
-0.5 | test_dir/file3.txt
```

Files would be moved into folders named `score_15-20/`, `score_5-10/`, and `score_-5-0/` respectively, based on the happiness score calculation in the script.