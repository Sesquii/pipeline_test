def tesseract_string(input_string):
    def ascii_to_4d(coord):
        return (coord % 2, (coord // 2) % 3, (coord // 6) % 5, (coord // 30))

    def rotate_4d_point(p):
        x, y, z, w = p
        return (
            y - x + z - w,
            z - y + w - x,
            w - z + x - y,
            x - w + y - z
        )

    def rotate_string(s):
        rotated_chars = []
        for i, char in enumerate(s):
            ascii_val = ord(char)
            p = ascii_to_4d(ascii_val)
            rotated_p = rotate_4d_point(p)

            # Convert back to ASCII value and character
            new_ascii = (rotated_p[0] +
                         3 * rotated_p[1] +
                         5 * rotated_p[2] +
                         7 * rotated_p[3])
            new_char = chr(new_ascii % 128)  # Keep within printable ASCII range
            rotated_chars.append(new_char)

        return ''.join(rotated_chars)

    result = rotate_string(input_string)
    return result

if __name__ == "__main__":
    input_str = "Non-Euclidean String Manipulator"
    output_str = tesseract_string(input_str)
    print(f"Input: {input_str}")
    print(f"Output: {output_str}")

# ===== GENERATED TESTS =====
```python
import pytest

# Original code remains unchanged

def tesseract_string(input_string):
    def ascii_to_4d(coord):
        return (coord % 2, (coord // 2) % 3, (coord // 6) % 5, (coord // 30))

    def rotate_4d_point(p):
        x, y, z, w = p
        return (
            y - x + z - w,
            z - y + w - x,
            w - z + x - y,
            x - w + y - z
        )

    def rotate_string(s):
        rotated_chars = []
        for i, char in enumerate(s):
            ascii_val = ord(char)
            p = ascii_to_4d(ascii_val)
            rotated_p = rotate_4d_point(p)

            # Convert back to ASCII value and character
            new_ascii = (rotated_p[0] +
                         3 * rotated_p[1] +
                         5 * rotated_p[2] +
                         7 * rotated_p[3])
            new_char = chr(new_ascii % 128)  # Keep within printable ASCII range
            rotated_chars.append(new_char)

        return ''.join(rotated_chars)

    result = rotate_string(input_string)
    return result

if __name__ == "__main__":
    input_str = "Non-Euclidean String Manipulator"
    output_str = tesseract_string(input_str)
    print(f"Input: {input_str}")
    print(f"Output: {output_str}")

# Test cases
def test_ascii_to_4d():
    assert ascii_to_4d(0) == (0, 0, 0, 0)
    assert ascii_to_4d(1) == (1, 0, 0, 0)
    assert ascii_to_4d(2) == (0, 1, 0, 0)
    assert ascii_to_4d(3) == (1, 1, 0, 0)
    assert ascii_to_4d(6) == (0, 0, 1, 0)

def test_rotate_4d_point():
    assert rotate_4d_point((0, 0, 0, 0)) == (0, 0, 0, 0)
    assert rotate_4d_point((1, 0, 0, 0)) == (0, -1, 0, 1)
    assert rotate_4d_point((0, 1, 0, 0)) == (-1, 0, 1, 0)
    assert rotate_4d_point((0, 0, 1, 0)) == (0, 1, 0, -1)

def test_rotate_string():
    assert rotate_string("A") == chr((0 + 3*0 + 5*0 + 7*0) % 128)
    assert rotate_string("B") == chr((1 + 3*1 + 5*0 + 7*0) % 128)
    assert rotate_string("C") == chr((-1 + 3*(-1) + 5*1 + 7*0) % 128)
    assert rotate_string("D") == chr((0 + 3*0 + 5*1 + 7*0) % 128)

def test_tesseract_string():
    input_str = "Non-Euclidean String Manipulator"
    expected_output = "Svqjw-Phyfzqg Tqjxqyqo"
    assert tesseract_string(input_str) == expected_output

# Add more tests as needed
```