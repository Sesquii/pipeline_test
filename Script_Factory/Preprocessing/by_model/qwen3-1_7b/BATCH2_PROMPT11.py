```python
import sys

def get_position(note):
    circle = ['C', 'G', 'D', 'A', 'E', 'B', 'F#', 'C#', 'G#', 'D#', 'A#', 'E#']
    return circle.index(note)

def sort_chords(chords):
    # Map each chord to its position in the circle of fifths
    positions = [get_position(c) for c in chords]
    
    # Sort by their position (alphabetical order)
    sorted_chords = sorted(chords, key=lambda x: get_position(x))
    return sorted_chords

def main():
    if __name__ == "__main__":
        input_list = sys.argv[1:]
        sorted_list = sort_chords(input_list)
        print(' '.join(sorted_list))

if __name__ == "__main__":
    main()