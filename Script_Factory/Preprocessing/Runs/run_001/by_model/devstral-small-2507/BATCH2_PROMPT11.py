# BATCH2_PROMPT11_Devstral.py

import sys

def circle_of_fifths_order():
    """Return a dictionary mapping chord names to their position in the circle of fifths."""
    # Sharps (clockwise from C)
    sharp_order = {
        'C': 0, 'G': 1, 'D': 2, 'A': 3, 'E': 4,
        'B': 5, 'F#': 6, 'C#': 7, 'G#': 8, 'D#': 9,
        'A#': 10, 'E#': 11
    }

    # Flats (counter-clockwise from C)
    flat_order = {
        'C': 0, 'F': 1, 'Bb': 2, 'Eb': 3, 'Ab': 4,
        'Db': 5, 'Gb': 6, 'Cb': 7, 'Fb': 8, 'Bbb': 9,
        'Ebb': 10, 'Abb': 11
    }

    # Combine both systems (sharp and flat)
    order = {}
    for chord in sharp_order:
        if chord not in flat_order:
            order[chord] = sharp_order[chord]
        else:
            # Average the positions for chords that appear in both systems
            order[chord] = (sharp_order[chord] + flat_order[chord]) / 2

    return order

def sort_chords_by_proximity(chords):
    """Sort a list of chords based on their musical proximity in the circle of fifths."""
    order = circle_of_fifths_order()

    # Handle minor chords by converting them to their major equivalent for ordering
    normalized_chords = []
    for chord in chords:
        if len(chord) > 1 and chord[1] == 'm':
            # Convert minor to major (e.g., 'Am' -> 'A')
            root = chord[0]
            if root in order:
                normalized_chords.append((chord, root))
        else:
            if chord in order:
                normalized_chords.append((chord, chord))

    # Sort based on the circle of fifths position
    sorted_chords = sorted(normalized_chords, key=lambda x: (order.get(x[1], sys.maxsize), x[0]))

    return [chord[0] for chord in sorted_chords]

def main():
    """Main entry point for the Musical Chord Sorter."""
    # Example list of chords
    chords = ['C', 'G', 'Am', 'F']

    print("Original chords:", chords)
    sorted_chords = sort_chords_by_proximity(chords)
    print("Sorted by musical proximity:", sorted_chords)

if __name__ == "__main__":
    main()