def draw_pattern(size):
    """Draws an abstract pattern using recursion."""
    if size == 0:
        return
    # Draw the top part of the pattern
    for i in range(size):
        print(' ' * (size - i - 1) + '*' * (2*i + 1))
    # Recursively call to draw the next level
    draw_pattern(size-1)

if __name__ == "__main__":
    draw_pattern(5)

# ===== GENERATED TESTS =====
import pytest

# Original script
def draw_pattern(size):
    """Draws an abstract pattern using recursion."""
    if size == 0:
        return
    # Draw the top part of the pattern
    for i in range(size):
        print(' ' * (size - i - 1) + '*' * (2*i + 1))
    # Recursively call to draw the next level
    draw_pattern(size-1)

if __name__ == "__main__":
    draw_pattern(5)

# Test suite
def test_draw_pattern_positive():
    """Test draw_pattern with positive size."""
    from io import StringIO
    import sys

    def capture_print(func, *args):
        old_stdout = sys.stdout
        sys.stdout = new_stdout = StringIO()
        func(*args)
        sys.stdout = old_stdout
        return new_stdout.getvalue()

    output = capture_print(draw_pattern, 3)
    expected_output = """  
   *
  ***
 *****
"""
    assert output == expected_output

def test_draw_pattern_zero():
    """Test draw_pattern with size zero."""
    from io import StringIO
    import sys

    def capture_print(func, *args):
        old_stdout = sys.stdout
        sys.stdout = new_stdout = StringIO()
        func(*args)
        sys.stdout = old_stdout
        return new_stdout.getvalue()

    output = capture_print(draw_pattern, 0)
    expected_output = ""
    assert output == expected_output

def test_draw_pattern_negative():
    """Test draw_pattern with negative size."""
    from io import StringIO
    import sys

    def capture_print(func, *args):
        old_stdout = sys.stdout
        sys.stdout = new_stdout = StringIO()
        func(*args)
        sys.stdout = old_stdout
        return new_stdout.getvalue()

    output = capture_print(draw_pattern, -5)
    expected_output = ""
    assert output == expected_output

def test_draw_pattern_large():
    """Test draw_pattern with large size."""
    from io import StringIO
    import sys

    def capture_print(func, *args):
        old_stdout = sys.stdout
        sys.stdout = new_stdout = StringIO()
        func(*args)
        sys.stdout = old_stdout
        return new_stdout.getvalue()

    output = capture_print(draw_pattern, 10)
    expected_output = """  
         *
        ***
       *****
      *******
     *********
    ***********
   *************
  *****************
 *******************
*********************

"""
    assert output == expected_output

def test_draw_pattern_one():
    """Test draw_pattern with size one."""
    from io import StringIO
    import sys

    def capture_print(func, *args):
        old_stdout = sys.stdout
        sys.stdout = new_stdout = StringIO()
        func(*args)
        sys.stdout = old_stdout
        return new_stdout.getvalue()

    output = capture_print(draw_pattern, 1)
    expected_output = "*\n"
    assert output == expected_output

def test_draw_pattern_two():
    """Test draw_pattern with size two."""
    from io import StringIO
    import sys

    def capture_print(func, *args):
        old_stdout = sys.stdout
        sys.stdout = new_stdout = StringIO()
        func(*args)
        sys.stdout = old_stdout
        return new_stdout.getvalue()

    output = capture_print(draw_pattern, 2)
    expected_output = """  
 *
***
"""
    assert output == expected_output

def test_draw_pattern_three():
    """Test draw_pattern with size three."""
    from io import StringIO
    import sys

    def capture_print(func, *args):
        old_stdout = sys.stdout
        sys.stdout = new_stdout = StringIO()
        func(*args)
        sys.stdout = old_stdout
        return new_stdout.getvalue()

    output = capture_print(draw_pattern, 3)
    expected_output = """  
   *
  ***
 *****
"""
    assert output == expected_output

def test_draw_pattern_four():
    """Test draw_pattern with size four."""
    from io import StringIO
    import sys

    def capture_print(func, *args):
        old_stdout = sys.stdout
        sys.stdout = new_stdout = StringIO()
        func(*args)
        sys.stdout = old_stdout
        return new_stdout.getvalue()

    output = capture_print(draw_pattern, 4)
    expected_output = """  
    *
   ***
  *****
 *******
"""
    assert output == expected_output

def test_draw_pattern_five():
    """Test draw_pattern with size five."""
    from io import StringIO
    import sys

    def capture_print(func, *args):
        old_stdout = sys.stdout
        sys.stdout = new_stdout = StringIO()
        func(*args)
        sys.stdout = old_stdout
        return new_stdout.getvalue()

    output = capture_print(draw_pattern, 5)
    expected_output = """  
     *
    ***
   *****
  *******
 *********
"""
    assert output == expected_output

def test_draw_pattern_six():
    """Test draw_pattern with size six."""
    from io import StringIO
    import sys

    def capture_print(func, *args):
        old_stdout = sys.stdout
        sys.stdout = new_stdout = StringIO()
        func(*args)
        sys.stdout = old_stdout
        return new_stdout.getvalue()

    output = capture_print(draw_pattern, 6)
    expected_output = """  
      *
     ***
    *****
   *******
  *********
 ***********
"""
    assert output == expected_output

def test_draw_pattern_seven():
    """Test draw_pattern with size seven."""
    from io import StringIO
    import sys

    def capture_print(func, *args):
        old_stdout = sys.stdout
        sys.stdout = new_stdout = StringIO()
        func(*args)
        sys.stdout = old_stdout
        return new_stdout.getvalue()

    output = capture_print(draw_pattern, 7)
    expected_output = """  
       *
      ***
     *****
    *******
   *********
  ***********
 *************
"""
    assert output == expected_output

def test_draw_pattern_eight():
    """Test draw_pattern with size eight."""
    from io import StringIO
    import sys

    def capture_print(func, *args):
        old_stdout = sys.stdout
        sys.stdout = new_stdout = StringIO()
        func(*args)
        sys.stdout = old_stdout
        return new_stdout.getvalue()

    output = capture_print(draw_pattern, 8)
    expected_output = """  
        *
       ***
      *****
     *******
    *********
   ***********
  *************
 *****************
"""
    assert output == expected_output

def test_draw_pattern_nine():
    """Test draw_pattern with size nine."""
    from io import StringIO
    import sys

    def capture_print(func, *args):
        old_stdout = sys.stdout
        sys.stdout = new_stdout = StringIO()
        func(*args)
        sys.stdout = old_stdout
        return new_stdout.getvalue()

    output = capture_print(draw_pattern, 9)
    expected_output = """  
         *
        ***
       *****
      *******
     *********
    ***********
   *************
  *****************
 *******************
"""
    assert output == expected_output

def test_draw_pattern_ten():
    """Test draw_pattern with size ten."""
    from io import StringIO
    import sys

    def capture_print(func, *args):
        old_stdout = sys.stdout
        sys.stdout = new_stdout = StringIO()
        func(*args)
        sys.stdout = old_stdout
        return new_stdout.getvalue()

    output = capture_print(draw_pattern, 10)
    expected_output = """  
          *
         ***
        *****
       *******
      *********
     ***********
    *************
   *****************
  *******************
 *********************

"""
    assert output == expected_output

def test_draw_pattern_eleven():
    """Test draw_pattern with size eleven."""
    from io import StringIO
    import sys

    def capture_print(func, *args):
        old_stdout = sys.stdout
        sys.stdout = new_stdout = StringIO()
        func(*args)
        sys.stdout = old_stdout
        return new_stdout.getvalue()

    output = capture_print(draw_pattern, 11)
    expected_output = """  
           *
          ***
         *****
        *******
       *********
      ***********
     *************
    *****************
   *******************
  *********************

"""
    assert output == expected_output

def test_draw_pattern_twelve():
    """Test draw_pattern with size twelve."""
    from io import StringIO
    import sys

    def capture_print(func, *args):
        old_stdout = sys.stdout
        sys.stdout = new_stdout = StringIO()
        func(*args)
        sys.stdout = old_stdout
        return new_stdout.getvalue()

    output = capture_print(draw_pattern, 12)
    expected_output = """  
            *
           ***
          *****
         *******
        *********
       ***********
      *************
     *****************
    *******************
   *********************

"""
    assert output == expected_output

def test_draw_pattern_thirteen():
    """Test draw_pattern with size thirteen."""
    from io import StringIO
    import sys

    def capture_print(func, *args):
        old_stdout = sys.stdout
        sys.stdout = new_stdout = StringIO()
        func(*args)
        sys.stdout = old_stdout
        return new_stdout.getvalue()

    output = capture_print(draw_pattern, 13)
    expected_output = """  
             *
            ***
           *****
          *******
         *********
        ***********
       *************
      *****************
     *******************
    *********************

"""
    assert output == expected_output

def test_draw_pattern_fourteen():
    """Test draw_pattern with size fourteen."""
    from io import StringIO
    import sys

    def capture_print(func, *args):
        old_stdout = sys.stdout
        sys.stdout = new_stdout = StringIO()
        func(*args)
        sys.stdout = old_stdout
        return new_stdout.getvalue()

    output = capture_print(draw_pattern, 14)
    expected_output = """  
              *
             ***
            *****
           *******
          *********
         ***********
        *************
       *****************
      *******************
     *********************

"""
    assert output == expected_output

def test_draw_pattern_fifteen():
    """Test draw_pattern with size fifteen."""
    from io import StringIO
    import sys

    def capture_print(func, *args):
        old_stdout = sys.stdout
        sys.stdout = new_stdout = StringIO()
        func(*args)
        sys.stdout = old_stdout
        return new_stdout.getvalue()

    output = capture_print(draw_pattern, 15)
    expected_output = """  
               *
              ***
             *****
            *******
           *********
          ***********
         *************
        *****************
       *******************
      *********************

"""
    assert output == expected_output

def test_draw_pattern_sixteen():
    """Test draw_pattern with size sixteen."""
    from io import StringIO
    import sys

    def capture_print(func, *args):
        old_stdout = sys.stdout
        sys.stdout = new_stdout = StringIO()
        func(*args)
        sys.stdout = old_stdout
        return new_stdout.getvalue()

    output = capture_print(draw_pattern, 16)
    expected_output = """  
                *
               ***
              *****
             *******
            *********
           ***********
          *************
         *****************
        *******************
       *********************

"""
    assert output == expected_output

def test_draw_pattern_seventeen():
    """Test draw_pattern with size seventeen."""
    from io import StringIO
    import sys

    def capture_print(func, *args):
        old_stdout = sys.stdout
        sys.stdout = new_stdout = StringIO()
        func(*args)
        sys.stdout = old_stdout
        return new_stdout.getvalue()

    output = capture_print(draw_pattern, 17)
    expected_output = """  
                 *
                ***
               *****
              *******
             *********
            ***********
           *************
          *****************
         *******************
        *********************

"""
    assert output == expected_output

def test_draw_pattern_eighteen():
    """Test draw_pattern with size eighteen."""
    from io import StringIO
    import sys

    def capture_print(func, *args):
        old_stdout = sys.stdout
        sys.stdout = new_stdout = StringIO()
        func(*args)
        sys.stdout = old_stdout
        return new_stdout.getvalue()

    output = capture_print(draw_pattern, 18)
    expected_output = """  
                  *
                 ***
                *****
               *******
              *********
             ***********
            *************
           *****************
          *******************
         *********************

"""
    assert output == expected_output

def test_draw_pattern_nineteen():
    """Test draw_pattern with size nineteen."""
    from io import StringIO
    import sys

    def capture_print(func, *args):
        old_stdout = sys.stdout
        sys.stdout = new_stdout = StringIO()
        func(*args)
        sys.stdout = old_stdout
        return new_stdout.getvalue()

    output = capture_print(draw_pattern, 19)
    expected_output = """  
                   *
                  ***
                 *****
                *******
               *********
              ***********
             *************
            *****************
           *******************
          *********************

"""
    assert output == expected_output

def test_draw_pattern_twenty():
    """Test draw_pattern with size twenty."""
    from io import StringIO
    import sys

    def capture_print(func, *args):
        old_stdout = sys.stdout
        sys.stdout = new_stdout = StringIO()
        func(*args)
        sys.stdout = old_stdout
        return new_stdout.getvalue()

    output = capture_print(draw_pattern, 20)
    expected_output = """  
                    *
                   ***
                  *****
                 *******
                *********
               ***********
              *************
             *****************
            *******************
           *********************

"""
    assert output == expected_output

def test_draw_pattern_twenty_one():
    """Test draw_pattern with size twenty-one."""
    from io import StringIO
    import sys

    def capture_print(func, *args):
        old_stdout = sys.stdout
        sys.stdout = new_stdout = StringIO()
        func(*args)
        sys.stdout = old_stdout
        return new_stdout.getvalue()

    output = capture_print(draw_pattern, 21)
    expected_output = """  
                     *
                    ***
                   *****
                  *******
                 *********
                ***********
               *************
              *****************
             *******************
            *********************

"""
    assert output == expected_output

def test_draw_pattern_twenty_two():
    """Test draw_pattern with size twenty-two."""
    from io import StringIO
    import sys

    def capture_print(func, *args):
        old_stdout = sys.stdout
        sys.stdout = new_stdout = StringIO()
        func(*args)
        sys.stdout = old_stdout
        return new_stdout.getvalue()

    output = capture_print(draw_pattern, 22)
    expected_output = """  
                      *
                     ***
                    *****
                   *******
                  *********
                 ***********
                *************
               *****************
              *******************
             *********************

"""
    assert output == expected_output

def test_draw_pattern_twenty_three():
    """Test draw_pattern with size twenty-three."""
    from io import StringIO
    import sys

    def capture_print(func, *args):
        old_stdout = sys.stdout
        sys.stdout = new_stdout = StringIO()
        func(*args)
        sys.stdout = old_stdout
        return new_stdout.getvalue()

    output = capture_print(draw_pattern, 23)
    expected_output = """  
                       *
                      ***
                     *****
                    *******
                   *********
                  ***********
                 *************
                *****************
               *******************
              *********************

"""
    assert output == expected_output

def test_draw_pattern_twenty_four():
    """Test draw_pattern with size twenty-four."""
    from io import StringIO
    import sys

    def capture_print(func, *args):
        old_stdout = sys.stdout
        sys.stdout = new_stdout = StringIO()
        func(*args)
        sys.stdout = old_stdout
        return new_stdout.getvalue()

    output = capture_print(draw_pattern, 24)
    expected_output = """  
                        *
                       ***
                      *****
                     *******
                    *********
                   ***********
                  *************
                 *****************
                *******************
               *********************

"""
    assert output == expected_output

def test_draw_pattern_twenty_five():
    """Test draw_pattern with size twenty-five."""
    from io import StringIO
    import sys

    def capture_print(func, *args):
        old_stdout = sys.stdout
        sys.stdout = new_stdout = StringIO()
        func(*args)
        sys.stdout = old_stdout
        return new_stdout.getvalue()

    output = capture_print(draw_pattern, 25)
    expected_output = """  
                         *
                        ***
                       *****
                      *******
                     *********
                    ***********
                   *************
                  *****************
                 *******************
                *********************

"""
    assert output == expected_output

def test_draw_pattern_twenty_six():
    """Test draw_pattern with size twenty-six."""
    from io import StringIO
    import sys

    def capture_print(func, *args):
        old_stdout = sys.stdout
        sys.stdout = new_stdout = StringIO()
        func(*args)
        sys.stdout = old_stdout
        return new_stdout.getvalue()

    output = capture_print(draw_pattern, 26)
    expected_output = """  
                          *
                         ***
                        *****
                       *******
                      *********
                     ***********
                    *************
                   *****************
                  *******************
                 *********************

"""
    assert output == expected_output

def test_draw_pattern_twenty_seven():
    """Test draw_pattern with size twenty-seven."""
    from io import StringIO
    import sys

    def capture_print(func, *args):
        old_stdout = sys.stdout
        sys.stdout = new_stdout = StringIO()
        func(*args)
        sys.stdout = old_stdout
        return new_stdout.getvalue()

    output = capture_print(draw_pattern, 27)
    expected_output = """  
                           *
                          ***
                         *****
                        *******
                       *********
                      ***********
                     *************
                    *****************
                   *******************
                  *********************

"""
    assert output == expected_output

def test_draw_pattern_twenty_eight():
    """Test draw_pattern with size twenty-eight."""
    from io import StringIO
    import sys

    def capture_print(func, *args):
        old_stdout = sys.stdout
        sys.stdout = new_stdout = StringIO()
        func(*args)
        sys.stdout = old_stdout
        return new_stdout.getvalue()

    output = capture_print(draw_pattern, 28)
    expected_output = """  
                            *
                           ***
                          *****
                         *******
                        *********
                       ***********
                      *************
                     *****************
                    *******************
                   *********************

"""
    assert output == expected_output

def test_draw_pattern_twenty_nine():
    """Test draw_pattern with size twenty-nine."""
    from io import StringIO
    import sys

    def capture_print(func, *args):
        old_stdout = sys.stdout
        sys.stdout = new_stdout = StringIO()
        func(*args)
        sys.stdout = old_stdout
        return new_stdout.getvalue()

    output = capture_print(draw_pattern, 29)
    expected_output = """  
                             *
                            ***
                           *****
                          *******
                         *********
                        ***********
                       *************
                      *****************
                     *******************
                    *********************

"""
    assert output == expected_output

def test_draw_pattern_thirty():
    """Test draw_pattern with size thirty."""
    from io import StringIO
    import sys

    def capture_print(func, *args):
        old_stdout = sys.stdout
        sys.stdout = new_stdout = StringIO()
       