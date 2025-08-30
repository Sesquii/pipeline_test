# BATCH3_PROMPT11_Devstral.py

"""
Musical Chord Sorter based on Circle of Fifths.

This program takes a list of musical chords and sorts them based on their 
musical proximity in the circle of fifths rather than alphabetically.
"""

def get_circle_of_fifths_order():
    """
    Returns the order of chords in the circle of fifths starting from C.
    
    The circle of fifths is a visual representation of the relationships among
    the 12 tones of the Western musical scale. This function defines this order
    for sorting purposes.
    """
    return [
        'C', 'G', 'D', 'A', 'E', 'B', 'F#/Gb', 'C#/Db', 'G#/Ab',
        'D#/Eb', 'A#/Bb', 'F', 'Bb', 'Eb', 'Ab', 'Db', 'Gb', 'Cb'
    ]

def chord_to_index(chord, circle_order):
    """
    Converts a chord to its index in the circle of fifths order.
    
    Args:
        chord (str): The chord to convert.
        circle_order (list): The list defining the circle of fifths order.
    
    Returns:
        int: The index of the chord in the circle order, or None if not found.
    """
    try:
        return circle_order.index(chord)
    except ValueError:
        # Handle enharmonic equivalents if needed
        enharmonics = {
            'F#': 'Gb',
            'C#': 'Db',
            'G#': 'Ab',
            'D#': 'Eb',
            'A#': 'Bb',
            'Cb': 'B'
        }
        for standard, enh in enharmonics.items():
            if chord == enh:
                return circle_order.index(standard)
        return None

def sort_chords_by_circle_of_fifths(chord_list):
    """
    Sorts a list of chords based on their position in the circle of fifths.
    
    Args:
        chord_list (list): List of chords to be sorted.
    
    Returns:
        list: Sorted list of chords.
    """
    circle_order = get_circle_of_fifths_order()
    # Sort using the custom key function that maps chords to their indices
    return sorted(chord_list, key=lambda chord: chord_to_index(chord, circle_order))

if __name__ == "__main__":
    # Example usage
    chords = ['C', 'G', 'Am', 'F']
    sorted_chords = sort_chords_by_circle_of_fifths(chords)
    print("Original chords:", chords)
    print("Sorted chords:", sorted_chords)

    # Note: The above example doesn't account for minor chords in the circle of fifths.
    # For a complete implementation, you would need to handle minor chords as well,
    # which typically involve parallel or relative major relationships.