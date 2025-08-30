# BATCH2_PROMPT11_Granite.py

from typing import List


def circle_of_fifths_sort(chords: List[str]) -> List[str]:
    """
    Sort a list of musical chords based on their proximity in the circle of fifths.

    The circle of fifths is a geometric representation of relationships among the 12 tones of the chromatic scale,
    arranged so that notes with common qualities are positioned near each other. 
    This function sorts chords by moving to the nearest note clockwise in the circle.
    
    :param chords: List of musical chord names (e.g., ['C', 'G', 'Am', 'F'])
    :return: Sorted list of chords
    """

    # Mapping of chord roots to their position in the circle of fifths, starting from C
    chord_positions = {
        'C': 0, 'C#': 1, 'Db': 2, 'D': 3, 'D#': 4, 'Eb': 5, 'E': 6, 'F': 7,
        'F#': 8, 'Gb': 9, 'G': 10, 'G#': 11, 'Ab': 12
    }

    # Convert all chords to their respective positions in the circle of fifths
    position_map = {chord: chord_positions[chord.lower()] for chord in chords}
    
    # Sort chords by their positions, wrapping around at the end of the circle
    sorted_chords = sorted(position_map.keys(), key=lambda c: (position_map[c] + 1) % len(position_map))

    return sorted_chords


if __name__ == "__main__":
    # Example usage
    chords = ['C', 'G', 'Am', 'F']
    print("Original Chords:", chords)
    sorted_chords = circle_of_fifths_sort(chords)
    print("Sorted Chords based on Circle of Fifths:", sorted_chords)