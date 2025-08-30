# BATCH3_PROMPT11_Granite.py

def circle_of_fifths(chord):
    """Converts a chord to its position in the circle of fifths."""
    if chord[0] == 'C':
        return 0
    elif chord[0] == 'G':
        return 1
    elif chord[0] == 'D':
        return 2
    elif chord[0] == 'A':
        return 3
    elif chord[0] == 'E':
        return 4
    elif chord[0] == 'B':
        return 5
    else:
        raise ValueError("Unknown chord")


def sort_chords(chords):
    """Sorts a list of chords based on their positions in the circle of fifths."""
    return sorted(chords, key=circle_of_fifths)


if __name__ == "__main__":
    # Test the function with an example
    chords = ['C', 'G', 'Am', 'F']
    sorted_chords = sort_chords(chords)
    print("Sorted Chords:", sorted_chords)