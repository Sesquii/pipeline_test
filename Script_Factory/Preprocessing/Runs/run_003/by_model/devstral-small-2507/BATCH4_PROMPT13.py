import sys
from collections import defaultdict

# Common words that will be exaggerated
COMMON_WORDS = {"the", "a", "an", "and", "or", "but", "is", "are", "was", "were"}

def count_words(file_path):
    """Count occurrences of each word in a text file."""
    word_counts = defaultdict(int)

    with open(file_path, 'r') as file:
        for line in file:
            words = line.strip().split()
            for word in words:
                # Convert to lowercase for consistency
                word = word.lower()
                word_counts[word] += 1

    return word_counts

def exaggerate_common_words(word_counts):
    """Exaggerate counts for common words."""
    exaggerated_counts = {}
    
    for word, count in word_counts.items():
        if word in COMMON_WORDS:
            # Exaggerate by multiplying the actual count by 1000
            exaggerated_counts[word] = count * 1000
        else:
            exaggerated_counts[word] = count

    return exaggerated_counts

def main():
    """Main entry point for the script."""
    if len(sys.argv) != 2:
        print("Usage: python exaggerated_word_counter.py <input_file>")
        sys.exit(1)

    file_path = sys.argv[1]

    # Count words in the file
    word_counts = count_words(file_path)

    # Exaggerate counts for common words
    exaggerated_counts = exaggerate_common_words(word_counts)

    # Print the results
    print("Exaggerated Word Counts:")
    for word, count in exaggerated_counts.items():
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()